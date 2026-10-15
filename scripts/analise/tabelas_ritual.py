#!/usr/bin/env python3
"""Gera as duas tabelas fixas do briefing do /ritual (pedido do user, 28/08/2026).

  1. TRACKEAMENTO — post x disparos x leads x qualificacao MQL (o que vira negocio)
  2. PERFORMANCE  — carrosseis maturados x taxa x banda da regua viva (o que vira audiencia)

Regra do user: post que ainda nao fechou em D+7 NAO se esconde — aparece com aviso
de maturacao ("D+5, ainda maturando"), porque ajuda a decidir o dia mesmo sem valer placar.
Zero chamada de API: le desempenho.json, registro-posts.csv, leads.json e _descartados.csv.
Disparos do Manychat vem do painel (nao tem API aqui) — passar via disparos.json se existir.
"""
import csv, json, os, re, datetime, difflib, sys

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "conteudo")
ANALISE = os.path.join(BASE, "analise")
HOJE = datetime.date.today()
_REGUA_CACHE = {}


def _regua():
    """Régua viva, calculada uma vez por execução. Sem desempenho.json, devolve vazio."""
    if not _REGUA_CACHE:
        _REGUA_CACHE["_lido"] = True
        try:
            sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))), "instagram"))
            import reguas
            _REGUA_CACHE.update(reguas.calcular()["formatos"])
        except Exception:
            pass
    return _REGUA_CACHE


def _reguas_formato(nome):
    return _regua().get(nome)


_BANDAS_CACHE = {}
# Bandas vêm da RÉGUA VIVA, nunca de número fixo aqui. Até 31/08 este arquivo hardcodava
# (42.49/76.98 e 6.35/9.03) enquanto validar_registro.py já importava reguas ao vivo — as duas
# fontes tinham divergido em silêncio, que é exatamente o apodrecimento que o docstring da
# reguas.py diz querer evitar. Se a régua muda, a tabela muda junto.
FALLBACK = {"carrossel": (42.49, 76.98, "interacoes/1k"), "frase": (6.35, 9.03, "shares/1k"),
            "reel": (26.14, 40.82, "interacoes/1k")}


# DADO FINAL (14/09, decisao do user): o placar fecha no ABSOLUTO em D+7 — comentarios no
# carrossel e no reel, compartilhamentos na frase. A taxa continua na tabela como ESTIMATIVA
# (norte de D+1 a D+4 e leitura descontando alcance), nunca como atestado. Ultimo valor
# conhecido (14/09, 90d, maturados): carrossel 8/35 com · reel 1/6 com · frase ver reguas.
FALLBACK_FINAL = {"carrossel": (8.0, 35.0, "comentarios"), "reel": (1.0, 6.0, "comentarios"),
                  "frase": (66.0, 438.0, "compartilhamentos")}


def _bandas():
    if not _BANDAS_CACHE:
        for nome, f in _regua().items():
            if isinstance(f, dict) and "taxa_p33" in f:
                _BANDAS_CACHE[nome] = (f["taxa_p33"], f["taxa_p67"], f["rotulo_taxa"])
            if isinstance(f, dict) and "final_p33" in f:
                _BANDAS_CACHE[nome + "/final"] = (f["final_p33"], f["final_p67"], f["final_rotulo"])
        for nome, v in FALLBACK.items():  # último valor conhecido, se a régua não rodou
            _BANDAS_CACHE.setdefault(nome, v)
        for nome, v in FALLBACK_FINAL.items():
            _BANDAS_CACHE.setdefault(nome + "/final", v)
    return _BANDAS_CACHE


class _Bandas(dict):
    """Mantém a leitura `BANDAS[formato]` que o resto do arquivo já usa, mas resolvendo
    pela régua viva na primeira consulta em vez de por constante."""
    def __getitem__(self, k): return _bandas()[k]
    def get(self, k, default=None): return _bandas().get(k, default)


BANDAS = _Bandas()
# Banda do ALVO DE LEAD do carrossel (com/1k). Nao substitui a taxa oficial do placar:
# entra AO LADO dela (decisao do user, 28/08 — "nao trocar, agregar").
# Comentario e o unico degrau que leva ao LEAD: rho +0,94 com disparo real do Manychat
# (remedido em 31/08 sobre 19 posts com automacao), contra +0,70 da taxa composta e +0,51
# do alcance. Desde 31/08 e a 1a metrica de leitura do carrossel na reguas.py, entao a banda
# vem de la tambem — nada de terco calculado a mao em dois lugares.
def _banda_com():
    for pr in (_reguas_formato("carrossel") or {}).get("prioridades", []):
        if pr["metrica"] == "comments" and not pr.get("indisponivel"):
            return (pr["p33"], pr["p67"])
    return (1.31, 3.99)

def carregar(nome):
    with open(os.path.join(ANALISE, nome), encoding="utf-8") as f:
        return json.load(f) if nome.endswith(".json") else list(csv.DictReader(f))

def descartados():
    p = os.path.join(ANALISE, "_descartados.csv")
    if not os.path.exists(p): return set()
    with open(p, encoding="utf-8") as f:
        return {l["post_id"].strip() for l in csv.DictReader(f) if l.get("post_id", "").strip()}

def ressalvas():
    """Ressalva de leitura por post: o numero existe e esta certo, mas UMA dimensao dele
    nao pode ser comparada com a dos outros posts (ex.: o CTA ficou 17h sem automacao).
    Diferente do _descartados.csv, que joga o post inteiro fora.
    Fonte: conteudo/analise/_ressalvas.csv — post_id,data_publicacao,escopo,motivo,marcado_em,marcado_por."""
    p = os.path.join(ANALISE, "_ressalvas.csv")
    if not os.path.exists(p): return {}
    out = {}
    with open(p, encoding="utf-8") as f:
        for l in csv.DictReader(f):
            pid = (l.get("post_id") or "").strip()
            esc = (l.get("escopo") or "").strip().lower()
            if pid and esc:
                out.setdefault(pid, []).append((esc, (l.get("motivo") or "").strip()))
    return out

def marca(ficha, resv, *escopos):
    """' !' quando o post tem ressalva em algum dos escopos pedidos (sem escopo = qualquer)."""
    rs = resv.get((ficha.get("post_id") or "").strip(), [])
    if not rs: return ""
    return " !" if (not escopos or any(e in escopos for e, _ in rs)) else ""

def norm(s):
    return re.sub(r"[^a-z0-9áàâãéêíóôõúç ]", "", re.sub(r"\s+", " ", (s or "")).strip().lower())

def legenda(pasta):
    f = os.path.join(BASE, "carrosseis", pasta, "carousel-text.md")
    if not os.path.exists(f): return None
    m = re.search(r"^##+ Legenda.*?$(.*)", open(f, encoding="utf-8").read(), re.M | re.S)
    if not m: return None
    for ln in m.group(1).split("\n"):
        ln = ln.strip()
        if ln and not ln.startswith((">", "#", "-", "*", "|")): return ln

# formato da ficha -> media_type da API. Sem isso, frase casa com carrossel
# publicado no mesmo dia e reel casa com qualquer coisa (bug visto em 28/08).
TIPO = {"frase": "IMAGE", "carrossel": "CAROUSEL_ALBUM", "reel": "VIDEO"}
REACH_MINIMO = 50  # abaixo disso o post acabou de sair e nao ha taxa que signifique nada


def casar(ficha, posts, fora):
    """Casa a ficha com o post da API. Devolve None se nao houver casamento CONFIAVEL —
    e melhor a linha faltar no briefing do que aparecer com o numero de outro post."""
    pid = (ficha.get("post_id") or "").strip()
    if pid:
        for p in posts:
            if str(p.get("id")) == pid: return p
        return None
    dp = ficha.get("data_publicacao")
    if not dp: return None
    tipo = TIPO.get(ficha.get("formato"))
    cand = [p for p in posts
            if p["timestamp"][:10] == dp
            and str(p.get("id")) not in fora
            and (tipo is None or p.get("media_type") == tipo)]
    if not cand: return None
    if len(cand) == 1:
        return cand[0]
    leg = legenda(ficha["pasta"])
    if not leg:
        return None  # varios candidatos e nada pra desempatar: nao chutar
    ln = norm(leg)[:80]
    melhor = max(cand, key=lambda p: difflib.SequenceMatcher(None, ln, norm(p["caption_full"])[:80]).ratio())
    score = difflib.SequenceMatcher(None, ln, norm(melhor["caption_full"])[:80]).ratio()
    return melhor if score >= 0.45 else None

def taxa_de(post, formato):
    m = post["metrics"]; r = m.get("reach") or 0
    if not r: return None
    alvo = m.get("shares", 0) if formato == "frase" else m.get("total_interactions", 0)
    return 1000 * alvo / r

def banda_de(taxa, formato):
    """Banda da ESTIMATIVA (taxa). Nao fecha placar desde 14/09."""
    lo, hi, _ = BANDAS.get(formato, BANDAS["carrossel"])
    return "abaixo" if taxa < lo else ("acima" if taxa > hi else "mediana")

def final_de(post, formato):
    """O dado final em absoluto: comentarios (carrossel/reel) ou compartilhamentos (frase)."""
    m = post["metrics"]
    return m.get("shares", 0) if formato == "frase" else m.get("comments", 0)

def banda_final(valor, formato):
    """Banda do DADO FINAL (absoluto em D+7). E esta que fecha o placar desde 14/09."""
    lo, hi, _ = BANDAS.get(formato + "/final", BANDAS["carrossel/final"])
    return "abaixo" if valor < lo else ("acima" if valor > hi else "mediana")

# O utm_campaign mudou de formato em 29/08: era a palavra crua (SONHO, CULTURA) e virou
# datada (2026-08-30-FOME). Sem tirar o prefixo, todo post novo aparece como "sem rastro"
# mesmo tendo lead — foi o erro do ritual de 31/08. Normaliza os dois formatos.
def palavra_da_campanha(camp):
    c = (camp or "").strip()
    m = re.match(r"^\d{4}-\d{2}-\d{2}[-_](.+)$", c)
    return (m.group(1) if m else c).strip().upper()

# Campanha datada (2026-09-06-DONO) -> (PALAVRA, date); campanha antiga (SONHO) -> (PALAVRA, None).
def chave_da_campanha(camp):
    c = (camp or "").strip()
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[-_](.+)$", c)
    if m:
        try: return m.group(2).strip().upper(), datetime.date.fromisoformat(m.group(1))
        except ValueError: pass
    return c.upper(), None

# A palavra do CTA pode repetir entre posts (DONO em 27/08 e em 06/09; regra de 27/08 na
# /etiqueta). Quem identifica o post e o utm_campaign DATADO, entao o casamento e por
# palavra + data (ate 1 dia de folga: a automacao pode nascer na vespera da publicacao).
# Campanha antiga sem data (SONHO, CULTURA, PATRAO...) so casa com ficha publicada ate
# 28/08, antes do padrao datado. Corrigido 06/09: a tabela creditava ao carrossel 91 os
# 6 disparos e o lead da automacao DONO do carrossel 64.
DATA_UTM_DATADO = datetime.date(2026, 8, 29)

def contatos_de(f, por_campanha):
    pal = (f.get("palavra_chave") or "").strip().upper()
    if not pal or not f.get("data_publicacao"): return []
    pub = datetime.date.fromisoformat(f["data_publicacao"])
    out = []
    for (p, d), cs in por_campanha.items():
        if p != pal: continue
        if d is None:
            if pub < DATA_UTM_DATADO: out.extend(cs)
        elif abs((d - pub).days) <= 1:
            out.extend(cs)
    return out

# _disparos.json e leitura manual do painel; cada entrada diz de que post e (campo "post").
# Entrada com "post" so serve pra aquele post; entrada sem "post" (legado) casa pela palavra.
def disparos_de(f, disparos):
    pal = (f.get("palavra_chave") or "").strip().upper()
    if not pal: return None
    d = disparos.get(pal)
    if not isinstance(d, dict): return None
    if d.get("post") and d["post"] != f.get("pasta"): return None
    return d


def qualificacao(tags):
    t = " ".join(tags).lower()
    if "q-mql" in t: return "Q-MQL"
    if "n-mql" in t: return "N-MQL"
    if re.search(r"(^|[^qn-])mql", t): return "MQL"
    return "sem classif."

def main(dias=7):
    posts = carregar("desempenho.json")["posts"]
    fichas = carregar("registro-posts.csv")
    fora = descartados()
    resv = ressalvas()
    disp_path = os.path.join(ANALISE, "_disparos.json")
    disparos = json.load(open(disp_path, encoding="utf-8")) if os.path.exists(disp_path) else {}
    try: contatos = carregar("leads.json")["contatos"]
    except Exception: contatos = []

    por_campanha = {}
    for c in contatos:
        atr = (c["ultima_atribuicao"] if c["reimpactado"] else c["primeira_atribuicao"]) or {}
        chave = chave_da_campanha(atr.get("campaign"))
        if chave[0]:
            por_campanha.setdefault(chave, []).append(c)

    janela = [f for f in fichas if f.get("data_publicacao")
              and (HOJE - datetime.date.fromisoformat(f["data_publicacao"])).days <= dias]
    janela.sort(key=lambda f: f["data_publicacao"])

    print(f"\n=== TABELA 1 — TRACKEAMENTO (leads e qualificacao) · ultimos {dias} dias ===")
    print(f"{'post':30} {'publicado':10} {'palavra':10} {'disp':>5} {'CTR':>6} {'novos':>6} {'reimp':>6}  qualificacao")
    for f in janela:
        pal = (f.get("palavra_chave") or "").strip().upper()
        d = disparos_de(f, disparos) or {}
        cs = contatos_de(f, por_campanha)
        novos = [c for c in cs if not c["reimpactado"]]; reimp = [c for c in cs if c["reimpactado"]]
        if not pal:
            dd, ctr, nn, rr, q = "—", "—", "—", "—", "sem CTA por desenho"
        else:
            # TRES estados, nao dois (corrigido 01/09 — o bug que inventou um alarme falso):
            #   sem entrada no painel  -> "?"  ainda nao li o Manychat, nao sei nada
            #   entrada com utm=False  -> "*"  li o painel e o link REALMENTE nao tinha UTM
            #   entrada com utm=True   -> numero (mesmo que seja zero lead ainda)
            # Antes, "?" e "*" eram a mesma coisa: post de ontem, sem leitura e sem lead,
            # aparecia como "sem UTM" e ia pro briefing como falha de automacao que nao existiu.
            lido = disparos_de(f, disparos) is not None
            dd = str(d.get("disparos", "?")); ctr = d.get("ctr", "?")
            if not lido and not cs:
                nn = rr = "?"
            elif cs or d.get("utm"):
                nn = str(len(novos)); rr = str(len(reimp))
            else:
                nn = rr = "*"
            qs = {}
            for c in cs: qs[qualificacao(c["tags"])] = qs.get(qualificacao(c["tags"]), 0) + 1
            q = " · ".join(f"{v} {k}" for k, v in sorted(qs.items())) or "—"
        dia = datetime.date.fromisoformat(f["data_publicacao"]).strftime("%d/%m")
        print(f"{f['pasta'][:30]:30} {dia:10} {pal or '—':10} {dd:>5} {ctr:>6} {nn:>6} {rr:>6}  {q}"
              f"{marca(f, resv, 'lead')}")
    print("  * = painel LIDO e o link nao tinha UTM: o lead clicou e chegou, mas sem etiqueta de campanha.")
    print("  ? = painel AINDA NAO LIDO pra essa automacao (palavra + post). Nao afirma nada sobre a automacao.")

    def linhas_de(formato):
        vistos = set(); saida = []
        for f in fichas:
            if f.get("formato") != formato or not f.get("data_publicacao"): continue
            if (HOJE - datetime.date.fromisoformat(f["data_publicacao"])).days > 14: continue
            if f["pasta"] in vistos: continue
            vistos.add(f["pasta"])
            post = casar(f, posts, fora)
            if not post: continue
            saida.append((f, post))
        return sorted(saida, key=lambda x: x[0]["data_publicacao"], reverse=True)

    def cab(f, post):
        idade = (HOJE - datetime.date.fromisoformat(f["data_publicacao"])).days
        dia = datetime.date.fromisoformat(f["data_publicacao"]).strftime("%d/%m")
        if idade >= 7:
            v = f.get("resultado_vs_previsao")
            # ficha retroativa (sem previsao escrita ANTES) fecha, mas nao entra no placar
            st = "FECHADO (nao pontua)" if v == "nao-pontua" else ("FECHADO (D+7)" if v else "fecha hoje")
        else:
            st = f"D+{idade} — maturando"
        return idade, dia, st

    print(f"\n=== TABELA 2 — CARROSSEL E REEL (o funil ate o lead) ===")
    print(f"{'post':28} {'publ':6} {'idade':>5} {'alcance':>8} {'curt/1k':>8} {'shr/1k':>7} {'sav/1k':>7} {'COM':>5} {'BANDA':>7} {'taxa':>6} {'est.':>7} {'prev':>7} {'disp':>5} {'LEADS':>6}  status")
    for formato in ("carrossel", "reel"):
        for f, post in linhas_de(formato):
            idade, dia, st = cab(f, post)
            m = post["metrics"]; rc = m["reach"]
            if rc < REACH_MINIMO:
                print(f"{f['pasta'][:28]:28} {dia:6} {'D+'+str(idade):>5}   acabou de sair, sem dado ainda")
                continue
            t = taxa_de(post, "carrossel")
            pal = (f.get("palavra_chave") or "").strip().upper()
            dd = disparos_de(f, disparos) or {}
            cs = contatos_de(f, por_campanha)
            if not pal:
                sdisp, sleads = "—", "—"
            else:
                sdisp = str(dd.get("disparos", "?"))
                # lead SO conta quando o link levava UTM; sem isso o rastro nao existe.
                # Mas "nao li o painel" NAO e "nao tinha UTM" — ver comentario na tabela 1.
                if cs or dd.get("utm"): sleads = str(len(cs))
                elif disparos_de(f, disparos) is None: sleads = "?"
                else: sleads = "s/UTM"
            fv = final_de(post, formato)
            print(f"{f['pasta'][:28]:28} {dia:6} {'D+'+str(idade):>5} {rc:8,} {1000*m.get('likes',0)/rc:8.1f} "
                  f"{1000*m.get('shares',0)/rc:7.2f} {1000*m.get('saved',0)/rc:7.2f} {fv:5} {banda_final(fv, formato):>7} "
                  f"{t:6.1f} {banda_de(t,'carrossel'):>7} {f.get('previsao') or '—':>7} {sdisp:>5} {sleads:>6}  {st}"
                  f"{marca(f, resv)}")
    _lo, _hi, _rot = BANDAS["carrossel/final"]
    print(f"  COM = {_rot} em absoluto, o DADO FINAL que fecha o placar em D+7: <{_lo:.0f} abaixo · {_lo:.0f}-{_hi:.0f} mediana · >{_hi:.0f} acima (regua viva, carrossel).")
    _lo, _hi, _rot = BANDAS["reel/final"]
    print(f"        reel: <{_lo:.0f} abaixo · {_lo:.0f}-{_hi:.0f} mediana · >{_hi:.0f} acima.")
    _lo, _hi, _rot = BANDAS["carrossel"]
    print(f"  taxa = {_rot}, ESTIMATIVA (norte ate D+4; nao atesta): <{_lo} abaixo · {_lo}-{_hi} mediana · >{_hi} acima. 'est.' e a banda dela.")
    print("  disp = disparos do Manychat (a palavra digitada) · LEADS = contatos com rastro no CRM.")
    print("  's/UTM' = painel lido, link sem etiqueta: sem rastro, nao sem lead. '?' = painel ainda nao lido.")

    print(f"\n=== TABELA 3 — FRASE (nao tem CTA: o alvo e espalhar) ===")
    print(f"{'post':28} {'publ':6} {'idade':>5} {'alcance':>8} {'curt/1k':>8} {'sav/1k':>7} {'SHARES':>7} {'BANDA':>7} {'shr/1k':>7} {'est.':>7} {'prev':>7}  status")
    for f, post in linhas_de("frase"):
        idade, dia, st = cab(f, post)
        m = post["metrics"]; rc = m["reach"]
        if rc < REACH_MINIMO:
            print(f"{f['pasta'][:28]:28} {dia:6} {'D+'+str(idade):>5}   acabou de sair, sem dado ainda")
            continue
        t = taxa_de(post, "frase")
        fv = final_de(post, "frase")
        print(f"{f['pasta'][:28]:28} {dia:6} {'D+'+str(idade):>5} {rc:8,} {1000*m.get('likes',0)/rc:8.1f} "
              f"{1000*m.get('saved',0)/rc:7.2f} {fv:7,} {banda_final(fv,'frase'):>7} {t:7.2f} {banda_de(t,'frase'):>7} {f.get('previsao') or '—':>7}  {st}"
              f"{marca(f, resv)}")
    _lo, _hi, _rot = BANDAS["frase/final"]
    print(f"  SHARES = {_rot} em absoluto, o DADO FINAL da frase em D+7: <{_lo:.0f} abaixo · {_lo:.0f}-{_hi:.0f} mediana · >{_hi:.0f} acima (regua viva).")
    _lo, _hi, _rot = BANDAS["frase"]
    print(f"  shr/1k = {_rot}, ESTIMATIVA (norte ate D+4): <{_lo} abaixo · {_lo}-{_hi} mediana · >{_hi} acima.")
    print("  Comentario nao entra: frase quase nao gera.")

    vistas = set(); ativas = []
    for f in fichas:
        pid = (f.get("post_id") or "").strip()
        dp = f.get("data_publicacao")
        if not pid or not dp or pid in vistas or pid not in resv: continue
        if (HOJE - datetime.date.fromisoformat(dp)).days > 14: continue
        vistas.add(pid); ativas.append(f)
    if ativas:
        print("\n=== RESSALVAS DE LEITURA (as linhas marcadas com ! nas tabelas) ===")
        for f in ativas:
            for esc, mot in resv[(f.get("post_id") or "").strip()]:
                print(f"  {f['pasta'][:28]:28} [{esc}] {mot}")
        print("  O numero do post esta certo; o que NAO vale e comparar o escopo marcado com o")
        print("  dos outros posts. Diferente do _descartados.csv, que descarta o post inteiro.")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
