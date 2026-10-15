#!/usr/bin/env python3
import sys as _sys_trava
_sys_trava.exit("TRAVADO: esta máquina NÃO acessa a API (a Meta bloqueia quando roda em duas máquinas). Os dados chegam pelo pacote diário: python3 scripts/pacote/importar_pacote.py <zip>. Ver CLAUDE.md -> Analytics.")

"""
Puxa o desempenho de todos os posts do Instagram do Hélio via API oficial da Meta
(Instagram API with Instagram Login) e salva em conteudo/analise/.

Zero dependência: usa só a biblioteca padrão do Python 3 (urllib).

Uso:
  1) python3 pull_insights.py exchange    # troca token curto por longo (só na 1ª vez / a cada ~60 dias)
  2) python3 pull_insights.py pull         # puxa mídia + insights -> desempenho.json + desempenho.csv
  3) python3 pull_insights.py refresh      # renova o token de longa duração (opcional, antes de expirar)

O token e o app_secret ficam em ~/.tatsuo/ig-token.json (FORA do Git).
Nunca cole o app_secret no chat: o comando 'exchange' pergunta em modo oculto.
"""

import csv
import datetime
import getpass
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import urllib.error
from collections import Counter

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
GRAPH = "https://graph.instagram.com"
TOKEN_DIR = os.path.expanduser("~/.tatsuo")
TOKEN_PATH = os.path.join(TOKEN_DIR, "ig-token.json")

# Onde salvar o resultado (repo). Resolve relativo a este arquivo pra rodar de qualquer lugar.
_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
OUT_DIR = os.path.join(REPO_ROOT, "conteudo", "analise")
OUT_JSON = os.path.join(OUT_DIR, "desempenho.json")
OUT_CSV = os.path.join(OUT_DIR, "desempenho.csv")
OUT_SNAP = os.path.join(OUT_DIR, "_snapshots.csv")
SNAP_DAYS = 30  # janela do snapshot diario de decaimento

# Métricas por tipo de mídia. A API rejeita a chamada inteira se pedir uma métrica
# não suportada pelo tipo — por isso pedimos um conjunto e, se falhar, degradamos
# métrica a métrica (ver fetch_insights).
METRICS_BY_TYPE = {
    "IMAGE": ["reach", "likes", "comments", "saved", "shares",
              "total_interactions", "views", "follows", "profile_visits"],
    "CAROUSEL_ALBUM": ["reach", "likes", "comments", "saved", "shares",
                       "total_interactions", "views", "follows", "profile_visits"],
    # NÃO acrescentar follows/profile_visits aqui. Testado em 31/08/2026, post a post:
    #   "The Media Insights API does not support the follows metric for this media
    #    product type" — e idem para profile_visits. É limite da API, não falta de pedido.
    # O custo de tentar é alto: a chamada em lote falha e a degradação métrica a métrica
    # dispara 12 requisições por vídeo em vez de 1. Numa janela de update isso são milhares
    # de chamadas extras, que é exatamente o padrão que aciona o anti-abuso da Meta.
    # Consequência conhecida: não existe medida de quanto seguidor o reel traz, embora seja
    # o formato mais publicado da casa. Só dá pra estimar pelo agregado da conta.
    "VIDEO": ["reach", "likes", "comments", "saved", "shares",
              "total_interactions", "views", "ig_reels_avg_watch_time",
              "ig_reels_video_view_total_time"],
    "REELS": ["reach", "likes", "comments", "saved", "shares",
              "total_interactions", "views", "ig_reels_avg_watch_time",
              "ig_reels_video_view_total_time"],
}
DEFAULT_METRICS = ["reach", "likes", "comments", "saved", "shares",
                   "total_interactions", "views"]

# Palavras que NÃO são palavra-chave de CTA (ruído comum de comentário em PT-BR):
# artigos/preposições + reações genéricas. A palavra-chave real é a que se repete
# muito ACIMA desse ruído (todo mundo comenta a mesma).
PT_STOPWORDS = {
    "de", "da", "do", "das", "dos", "que", "com", "sem", "por", "para", "pra",
    "uma", "uns", "umas", "ele", "ela", "eles", "elas", "isso", "essa", "esse",
    "está", "esta", "este", "seu", "sua", "não", "sim", "mais", "muito", "top",
    "bom", "boa", "show", "top", "massa", "demais", "perfeito", "parabéns",
    "obrigado", "obrigada", "amei", "gostei", "curti", "legal", "incrível",
    "the", "and", "you", "for", "são", "tem", "foi", "vai", "aqui", "sobre",
    "como", "quando", "onde", "porque", "também", "então", "cara", "gente",
    "verdade", "certo", "isso", "aí", "lá", "vou", "vocês", "voce", "você",
}


def _strip_accents(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")


def _tokenize(text):
    """Extrai tokens de palavra (>=3 letras), sem @menções, urls, acento ou caixa."""
    text = re.sub(r"@\w+", " ", text)          # tira marcações de amigo
    text = re.sub(r"https?://\S+", " ", text)  # tira links
    words = re.findall(r"[A-Za-zÀ-ÿ]{3,}", text)
    return [_strip_accents(w).lower() for w in words]


def analyze_keyword(comments):
    """
    Detecta a palavra-chave de CTA de um post: como todo mundo comenta a MESMA
    palavra, ela é o token que aparece no maior número de comentários (frequência
    de documento, não de termo). Retorna também o top-5 pra eu conferir depois.
    """
    texts = [(c.get("text") or "") for c in comments]
    n = len(texts)
    empty = {"comments_read": n, "cta_keyword": "", "cta_keyword_count": 0,
             "cta_share": 0.0, "cta_top_tokens": []}
    if n == 0:
        return empty
    doc_freq = Counter()
    for t in texts:
        for tok in set(_tokenize(t)):          # set => conta 1 vez por comentário
            if tok not in PT_STOPWORDS:
                doc_freq[tok] += 1
    if not doc_freq:
        return empty
    top = doc_freq.most_common(5)
    kw, kwc = top[0]
    return {
        "comments_read": n,
        "cta_keyword": kw,
        "cta_keyword_count": kwc,
        "cta_share": round(kwc / n, 3),        # fração dos comentários com a palavra
        "cta_top_tokens": [f"{w}:{c}" for w, c in top],
    }


# ---------------------------------------------------------------------------
# HTTP helpers (stdlib only)
# ---------------------------------------------------------------------------
def _get(url, params):
    qs = urllib.parse.urlencode(params)
    full = f"{url}?{qs}"
    req = urllib.request.Request(full, headers={"User-Agent": "tatsuo-ig/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise ApiError(e.code, body)


class ApiError(Exception):
    def __init__(self, code, body):
        self.code = code
        self.body = body
        try:
            self.payload = json.loads(body)
        except Exception:
            self.payload = {}
        msg = self.payload.get("error", {}).get("message", body)
        super().__init__(f"HTTP {code}: {msg}")


# ---------------------------------------------------------------------------
# Token store
# ---------------------------------------------------------------------------
def load_token():
    if not os.path.exists(TOKEN_PATH):
        sys.exit(f"Token não encontrado em {TOKEN_PATH}.\n"
                 f"Rode primeiro:  python3 {os.path.basename(__file__)} exchange")
    with open(TOKEN_PATH) as f:
        return json.load(f)


def save_token(data):
    os.makedirs(TOKEN_DIR, exist_ok=True)
    with open(TOKEN_PATH, "w") as f:
        json.dump(data, f, indent=2)
    os.chmod(TOKEN_PATH, 0o600)
    print(f"Token salvo em {TOKEN_PATH} (permissão 600).")


def _stamp_expiry(tok, expires_in):
    # Sem Date.now no ambiente do agente, mas aqui é execução real: time.time() ok.
    tok["expires_in"] = expires_in
    tok["obtained_at"] = int(time.time())
    tok["expires_at_human"] = time.strftime(
        "%Y-%m-%d %H:%M", time.localtime(time.time() + expires_in))
    return tok


# ---------------------------------------------------------------------------
# Comandos
# ---------------------------------------------------------------------------
def cmd_exchange():
    """Valida o token do painel e, se der, troca por um de longa duração (~60 dias)."""
    print("== Configurar token (Instagram API with Instagram Login) ==")
    print("Use as credenciais DO INSTAGRAM (painel do app > Configuração da API com")
    print("login do Instagram), NÃO as do Facebook.\n")
    app_id = input("ID do app do Instagram: ").strip()
    app_secret = getpass.getpass("Chave secreta do app do Instagram (oculto): ").strip()
    short = getpass.getpass("Token gerado no painel (oculto): ").strip()

    if not short:
        sys.exit("Nenhum token informado. Rode de novo e cole o token.")
    print(f"\n(recebido: token de {len(short)} caracteres, "
          f"chave secreta de {len(app_secret)} caracteres)")

    # 1) O token é válido? Testa em /me ANTES de qualquer coisa — isola o problema.
    try:
        me = _get(f"{GRAPH}/me", {"fields": "id,username", "access_token": short})
        print(f"Token válido. Conta: @{me.get('username', '?')} (id {me.get('id', '?')}).")
    except ApiError as e:
        sys.exit(
            "\nO TOKEN não passou no teste (/me): " + str(e) +
            "\n> Provável colagem incompleta. Gere o token de novo no painel "
            "('Gerar token'), copie inteiro e cole sem espaços.\n"
            "> Confira também que não trocou a ordem (secret x token) nos campos."
        )

    tok = {"app_id": app_id, "app_secret": app_secret,
           "access_token": short, "token_type": "bearer"}

    # 2) Tenta trocar por longa duração. Se o token do painel já for longo, a troca
    #    falha e a gente simplesmente usa o token que já funciona.
    try:
        data = _get(f"{GRAPH}/access_token", {
            "grant_type": "ig_exchange_token",
            "client_secret": app_secret,
            "access_token": short,
        })
        tok["access_token"] = data["access_token"]
        _stamp_expiry(tok, data.get("expires_in", 0))
        print(f"Trocado por token de longa duração. Expira ~{tok['expires_at_human']}.")
    except ApiError as e:
        _stamp_expiry(tok, 60 * 24 * 3600)
        print("Não deu pra trocar por longa duração (" + str(e) + ").")
        print("Mas o token JÁ funciona, então vou salvar e usar ele mesmo.")
        print("(Se a troca falhou por chave secreta errada, o 'refresh' futuro não "
              "vai funcionar — mas o pull de agora funciona normal.)")

    save_token(tok)
    print("\nPronto. Agora rode:  python3 scripts/instagram/pull_insights.py pull")


def cmd_refresh():
    """Renova o token de longa duração (só funciona se ele tiver >24h de vida)."""
    tok = load_token()
    data = _get(f"{GRAPH}/refresh_access_token", {
        "grant_type": "ig_refresh_token",
        "access_token": tok["access_token"],
    })
    tok["access_token"] = data["access_token"]
    _stamp_expiry(tok, data.get("expires_in", 0))
    save_token(tok)
    print(f"Token renovado. Expira ~{tok['expires_at_human']}.")


def fetch_all_media(token, since=None):
    """
    Pagina /me/media (mais novos primeiro). Se 'since' (YYYY-MM-DD) for informado,
    para de paginar assim que aparecem posts mais antigos que a data — bem mais rápido.
    """
    media = []
    params = {
        "fields": "id,caption,media_type,media_product_type,timestamp,permalink,comments_count",
        "access_token": token,
        "limit": 100,
    }
    url = f"{GRAPH}/me/media"
    page = 1
    stop = False
    while True:
        data = _get(url, params)
        batch = data.get("data", [])
        kept = 0
        for m in batch:
            ts = (m.get("timestamp") or "")[:10]
            if since and ts and ts < since:
                stop = True
                continue
            media.append(m)
            kept += 1
        print(f"  página {page}: +{kept} posts (total {len(media)})")
        if stop:
            break
        nxt = data.get("paging", {}).get("next")
        if not nxt:
            break
        # 'next' já vem com querystring completa; separa pra reusar o _get.
        parsed = urllib.parse.urlparse(nxt)
        url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        params = dict(urllib.parse.parse_qsl(parsed.query))
        page += 1
    return media


def fetch_insights(media_id, media_type, token):
    """
    Puxa insights de uma mídia. Se o conjunto de métricas falhar (tipo não suporta
    alguma), degrada e tenta métrica a métrica, coletando o que der.
    """
    candidates = METRICS_BY_TYPE.get(media_type, DEFAULT_METRICS)

    def _call(metrics):
        data = _get(f"{GRAPH}/{media_id}/insights", {
            "metric": ",".join(metrics),
            "access_token": token,
        })
        out = {}
        for item in data.get("data", []):
            vals = item.get("values", [])
            out[item["name"]] = vals[0].get("value") if vals else None
        return out

    try:
        return _call(candidates)
    except ApiError:
        # Degrada: uma métrica a menos por vez.
        result = {}
        for m in candidates:
            try:
                result.update(_call([m]))
            except ApiError:
                pass  # métrica não suportada por esse post; segue
        return result


def fetch_comments(media_id, token, max_pages=60):
    """Pagina os comentários de nível superior de uma mídia."""
    comments = []
    params = {"fields": "text,timestamp,username,like_count",
              "access_token": token, "limit": 50}
    url = f"{GRAPH}/{media_id}/comments"
    pages = 0
    while pages < max_pages:
        try:
            data = _get(url, params)
        except ApiError:
            break  # sem permissão de comentários nesse post, ou indisponível
        comments.extend(data.get("data", []))
        nxt = data.get("paging", {}).get("next")
        if not nxt:
            break
        parsed = urllib.parse.urlparse(nxt)
        url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        params = dict(urllib.parse.parse_qsl(parsed.query))
        pages += 1
    return comments


def cmd_update():
    """
    Pull INCREMENTAL e educado (anti-bloqueio):
    - só busca posts novos + re-atualiza os últimos REFRESH_DAYS (números maturando)
    - NÃO chama /comments (voltam vazios sem App Review; era metade do volume)
    - pausa entre chamadas pra não disparar o anti-abuso da Meta
    Mescla no desempenho.json/csv existente sem tocar no histórico antigo.
    """
    REFRESH_DAYS = 30  # cobre ate D+30 (medido 27/08: ~227 chamadas/dia, 6,6% do burst que bloqueou)
    PACE = 0.7  # segundos entre posts

    if not os.path.exists(OUT_JSON):
        sys.exit("Sem desempenho.json existente — rode 'pull' uma vez primeiro.")
    existing = json.load(open(OUT_JSON))
    by_id = {p["id"]: p for p in existing["posts"]}

    cutoff = time.strftime("%Y-%m-%d", time.localtime(time.time() - REFRESH_DAYS * 86400))
    tok = load_token()
    token = tok["access_token"]
    print(f"Update incremental: buscando posts desde {cutoff} "
          f"(base atual: {len(by_id)} posts)...")
    media = fetch_all_media(token, cutoff)
    novos = sum(1 for m in media if m["id"] not in by_id)
    print(f"{len(media)} posts na janela ({novos} novos, "
          f"{len(media)-novos} pra re-atualizar). Ritmo: {PACE}s/post.\n")

    for i, m in enumerate(media, 1):
        mtype = m.get("media_type", "")
        try:
            ins = fetch_insights(m["id"], mtype, token)
        except ApiError as e:
            print(f"  [{i}/{len(media)}] {m['id']} insights indisponíveis: {e}")
            ins = {}
        caption = (m.get("caption") or "").replace("\n", " ").strip()
        old = by_id.get(m["id"], {})
        by_id[m["id"]] = {
            "id": m["id"],
            "media_type": mtype,
            "media_product_type": m.get("media_product_type", ""),
            "timestamp": m.get("timestamp", ""),
            "permalink": m.get("permalink", ""),
            "caption_preview": caption[:140],
            "caption_full": caption,
            "comments_count": m.get("comments_count", ""),
            "comments_read": old.get("comments_read", 0),
            "cta_keyword": old.get("cta_keyword", ""),
            "cta_keyword_count": old.get("cta_keyword_count", 0),
            "cta_share": old.get("cta_share", 0.0),
            "cta_top_tokens": old.get("cta_top_tokens", []),
            "metrics": ins,
        }
        tag = "novo" if not old else "atualizado"
        print(f"  [{i}/{len(media)}] {m['timestamp'][:10]} {mtype:15} "
              f"reach={ins.get('reach','-'):>7} com={ins.get('comments','-'):>5}  ({tag})")
        time.sleep(PACE)

    rows = sorted(by_id.values(), key=lambda p: p["timestamp"], reverse=True)
    _write_outputs(rows)
    print(f"\nBase atualizada: {len(rows)} posts.")
    write_snapshot(rows)
    report_snapshot_gaps()


def _write_outputs(rows):
    all_metric_keys = set()
    for r in rows:
        all_metric_keys.update(r["metrics"].keys())
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump({"pulled_at": time.strftime("%Y-%m-%d %H:%M"),
                   "count": len(rows), "posts": rows}, f, ensure_ascii=False, indent=2)
    metric_cols = sorted(all_metric_keys)
    base_cols = ["timestamp", "media_type", "media_product_type",
                 "id", "permalink", "caption_preview", "comments_count",
                 "comments_read", "cta_keyword", "cta_keyword_count", "cta_share"]
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(base_cols + metric_cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in base_cols] +
                       [r["metrics"].get(k, "") for k in metric_cols])


def cmd_pull():
    since = sys.argv[2] if len(sys.argv) > 2 else "2025-01-01"
    tok = load_token()
    token = tok["access_token"]
    print(f"Puxando lista de mídia (desde {since})...")
    media = fetch_all_media(token, since)
    print(f"\n{len(media)} posts desde {since}. Puxando insights de cada um...\n")

    rows = []
    all_metric_keys = set()
    for i, m in enumerate(media, 1):
        mtype = m.get("media_type", "")
        print(f"  [{i}/{len(media)}] {m['id']} ({mtype})")
        try:
            ins = fetch_insights(m["id"], mtype, token)
        except ApiError as e:
            print(f"      insights indisponíveis: {e}")
            ins = {}
        all_metric_keys.update(ins.keys())

        comments = fetch_comments(m["id"], token)
        kw = analyze_keyword(comments)
        if kw["cta_keyword"]:
            print(f"      {kw['comments_read']} comentários | palavra-chave provável: "
                  f"'{kw['cta_keyword']}' em {kw['cta_keyword_count']} "
                  f"({int(kw['cta_share']*100)}%)")
        else:
            print(f"      {kw['comments_read']} comentários lidos")

        caption = (m.get("caption") or "").replace("\n", " ").strip()
        rows.append({
            "id": m["id"],
            "media_type": mtype,
            "media_product_type": m.get("media_product_type", ""),
            "timestamp": m.get("timestamp", ""),
            "permalink": m.get("permalink", ""),
            "caption_preview": caption[:140],
            "caption_full": caption,
            "comments_count": m.get("comments_count", ""),
            "comments_read": kw["comments_read"],
            "cta_keyword": kw["cta_keyword"],
            "cta_keyword_count": kw["cta_keyword_count"],
            "cta_share": kw["cta_share"],
            "cta_top_tokens": kw["cta_top_tokens"],
            "metrics": ins,
        })

    os.makedirs(OUT_DIR, exist_ok=True)

    with open(OUT_JSON, "w") as f:
        json.dump({
            "pulled_at": time.strftime("%Y-%m-%d %H:%M"),
            "count": len(rows),
            "posts": rows,
        }, f, ensure_ascii=False, indent=2)

    metric_cols = sorted(all_metric_keys)
    base_cols = ["timestamp", "media_type", "media_product_type",
                 "id", "permalink", "caption_preview", "comments_count",
                 "comments_read", "cta_keyword", "cta_keyword_count", "cta_share"]
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(base_cols + metric_cols)
        for r in rows:
            w.writerow([r[c] for c in base_cols] +
                       [r["metrics"].get(k, "") for k in metric_cols])

    print(f"\nPronto:\n  {OUT_JSON}\n  {OUT_CSV}")
    print("Peça ao Claude:  'varre o conteudo/analise/desempenho.csv e monta o o-que-funciona.md'")


SNAP_COLS = ["data_snapshot", "post_id", "idade_dias", "comments", "reach", "saved", "shares"]


def _snap_rows_from(posts, dia):
    """Uma linha por post dentro da janela SNAP_DAYS. Zero chamada de API: só lê o
    que já veio do disco/memória. A API devolve valor ACUMULADO DE VIDA, não série
    diária — dia não fotografado é dia perdido pra sempre, não dá backfill."""
    d0 = datetime.date.fromisoformat(dia)
    out = []
    for post in posts:
        pub = datetime.date.fromisoformat(post["timestamp"][:10])
        idade = (d0 - pub).days
        if idade < 0 or idade > SNAP_DAYS:
            continue
        m = post.get("metrics") or {}
        out.append({
            "data_snapshot": dia, "post_id": post["id"], "idade_dias": idade,
            "comments": m.get("comments", 0), "reach": m.get("reach", 0),
            "saved": m.get("saved", 0), "shares": m.get("shares", 0),
        })
    return out


def write_snapshot(posts, dia=None, quiet=False):
    """Grava/atualiza o snapshot do dia. Idempotente: rodar 2x no mesmo dia
    SUBSTITUI as linhas daquele dia (fica a leitura mais fresca), nunca duplica.
    Nunca deixa o arquivo pela metade — escreve em tmp e troca no fim."""
    dia = dia or time.strftime("%Y-%m-%d")
    novos = _snap_rows_from(posts, dia)
    if not novos:
        if not quiet:
            print(f"[snapshot] {dia}: nenhum post na janela de {SNAP_DAYS}d — nada gravado.")
        return 0

    antigos = []
    if os.path.exists(OUT_SNAP):
        with open(OUT_SNAP, newline="") as f:
            antigos = [r for r in csv.DictReader(f) if r.get("data_snapshot") != dia]

    tmp = OUT_SNAP + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=SNAP_COLS)
        w.writeheader()
        for r in sorted(antigos + novos, key=lambda r: (r["data_snapshot"], str(r["post_id"]))):
            w.writerow({c: r.get(c, "") for c in SNAP_COLS})
    os.replace(tmp, OUT_SNAP)
    if not quiet:
        print(f"[snapshot] {dia}: {len(novos)} posts gravados (janela {SNAP_DAYS}d).")
    return len(novos)


def report_snapshot_gaps(desde=None):
    """Falha em silêncio é o pior tipo de falha: se um dia não foi fotografado,
    ele precisa aparecer na cara de quem rodar. Não conserta nada — só denuncia."""
    if not os.path.exists(OUT_SNAP):
        print("[snapshot] AVISO: _snapshots.csv não existe.")
        return []
    with open(OUT_SNAP, newline="") as f:
        tem = {r["data_snapshot"] for r in csv.DictReader(f) if r.get("data_snapshot")}
    if not tem:
        return []
    ini = datetime.date.fromisoformat(desde or min(tem))
    hoje = datetime.date.today()
    faltam = [d.isoformat() for d in
              (ini + datetime.timedelta(days=i) for i in range((hoje - ini).days + 1))
              if d.isoformat() not in tem]
    if faltam:
        print(f"[snapshot] BURACOS ({len(faltam)}): {', '.join(faltam)}")
        print("[snapshot] dia sem foto NÃO é recuperável pela API (valores são acumulados de vida);")
        print("[snapshot] só dá pra recuperar de um desempenho.json commitado naquele dia.")
    else:
        print(f"[snapshot] sem buracos de {ini} até hoje.")
    return faltam


def cmd_snapshot():
    """Regrava o snapshot de hoje a partir do desempenho.json em disco. ZERO API.
    Serve de rede de segurança: pode rodar quantas vezes quiser, é idempotente."""
    if not os.path.exists(OUT_JSON):
        print("desempenho.json não existe — rode 'update' antes.")
        sys.exit(1)
    with open(OUT_JSON) as f:
        data = json.load(f)
    dia = sys.argv[2] if len(sys.argv) > 2 else None

    # Guarda contra o pior erro possível: gravar a data de HOJE com números VELHOS.
    # Isso não seria um buraco — seria uma linha reta falsa, que mente dizendo que o
    # post parou de crescer. Buraco é honesto; dado errado contamina a análise.
    if dia is None:
        hoje = time.strftime("%Y-%m-%d")
        pulled = (data.get("pulled_at") or "")[:10]
        if pulled != hoje:
            print(f"[snapshot] ABORTADO: desempenho.json é de {pulled or '?'}, não de {hoje}.")
            print("[snapshot] gravar hoje com número velho vira linha reta falsa. Rode 'update' antes,")
            print(f"[snapshot] ou force a data real do dado: snapshot {pulled or 'AAAA-MM-DD'}")
            sys.exit(1)

    write_snapshot(data.get("posts", []), dia=dia)
    report_snapshot_gaps()


def main():
    cmds = {"exchange": cmd_exchange, "refresh": cmd_refresh,
            "pull": cmd_pull, "update": cmd_update,
            "snapshot": cmd_snapshot}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]]()


if __name__ == "__main__":
    main()
