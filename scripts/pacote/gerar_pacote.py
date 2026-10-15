#!/usr/bin/env python3
"""
gerar_pacote.py — empacota os dados BRUTOS do analytics pra máquina do João.

Roda só na máquina principal (a única que fala com a API da Meta, o CRM e o painel
do Manychat). NÃO chama API nenhuma: só lê o que os coletores já gravaram em
conteudo/analise/ e monta um zip. Nada é interpretado: o pacote leva o dado como
ele está no disco, mais um MANIFESTO que descreve cada arquivo.

Uso:
  python3 scripts/pacote/gerar_pacote.py              # ~/Desktop/pacote-analytics-joao/pacote-AAAA-MM-DD.zip
  python3 scripts/pacote/gerar_pacote.py --saida DIR  # outra pasta de saída
  python3 scripts/pacote/gerar_pacote.py --dias 14    # janela dos textos de post (padrão 14 dias)

A data do nome é a de Brasília. Rodar de novo no mesmo dia substitui o zip do dia.

Dentro do zip (pasta pacote-AAAA-MM-DD/):
  MANIFESTO.md       o que é cada arquivo, de onde vem, quando foi coletado, nº de registros, colunas
  checksums.txt      sha256 de cada arquivo (confere com: shasum -a 256 -c checksums.txt)
  pacote.json        metadados lidos pelo importar_pacote.py
  analise/...        dados brutos (Instagram, CRM, Manychat, logs, registro factual)
  posts/<pasta>/     carousel-text.md (sem a linha "Etiqueta:" da previsão) e legenda.txt
                     dos posts publicados na janela
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import socket
import sys
import tempfile
import zipfile

try:
    from zoneinfo import ZoneInfo
    BRT = ZoneInfo("America/Sao_Paulo")
except Exception:  # sem base de fusos: Brasília não tem horário de verão desde 2019
    BRT = dt.timezone(dt.timedelta(hours=-3))

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(AQUI, "..", ".."))
ANALISE = os.path.join(REPO, "conteudo", "analise")
CARROSSEIS = os.path.join(REPO, "conteudo", "carrosseis")
SAIDA_PADRAO = os.path.expanduser("~/Desktop/pacote-analytics-joao")

FORMATO_PACOTE = 1

# Colunas do registro-posts.csv que são FATO (o que o post é). O resto do registro
# (previsão, justificativa, resultado, nervo, mecanismo, roupa, consciência da dor)
# é análise desta máquina e não sai.
REGISTRO_COLS = ["data", "data_publicacao", "post_id", "pasta", "formato",
                 "semente", "pilar", "funil", "objetivo", "palavra_chave"]
TEXTOS_POST = ["carousel-text.md", "legenda.txt"]
PASTA_OK = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
# Linha do carousel-text.md com a previsão da /etiqueta (ex. "- Etiqueta: mediana, 10-38
# comentários em D+7"). Previsão é análise desta máquina: a linha sai, o resto vai literal.
LINHA_PREVISAO = re.compile(r"^\s*(?:[-*]\s+)?(?:\*\*)?etiqueta(?:\*\*)?\s*:", re.IGNORECASE)

# Tudo que os coletores escrevem em conteudo/analise/ (lido nos próprios scripts):
#   pull_insights.py update -> desempenho.json, desempenho.csv, _snapshots.csv
#   agendamento com.tatsuo.ig-update (stdout+stderr do update) -> _update.log
#   pull_insights.py pull (rodado uma vez, 06/08/2026) -> _pull.log
#   pull_leads.py update -> leads.json
#   leitura do painel do Manychat (ritual, à mão) -> _disparos.json
#   captura do painel do Instagram (à mão) -> _painel-instagram.csv
# O token (~/.tatsuo/ig-token.json) e o ghl.env nunca entram.
ARQUIVOS = [
    {"nome": "desempenho.json", "obrigatorio": True,
     "origem": "`scripts/instagram/pull_insights.py update` (API do Instagram, Graph API com login do Instagram)"},
    {"nome": "desempenho.csv", "obrigatorio": True,
     "origem": "`scripts/instagram/pull_insights.py update` (mesma coleta do desempenho.json, em tabela)"},
    {"nome": "_snapshots.csv", "obrigatorio": True,
     "origem": "`scripts/instagram/pull_insights.py update` (gravado no fim de todo update, sem chamada extra)"},
    {"nome": "leads.json", "obrigatorio": False,
     "origem": "`scripts/ghl/pull_leads.py update` (API do GoHighLevel v2, CRM)"},
    {"nome": "_disparos.json", "obrigatorio": False,
     "origem": "leitura manual do painel do Manychat no navegador (só leitura; o Manychat não tem API), feita no ritual"},
    {"nome": "_painel-instagram.csv", "obrigatorio": False,
     "origem": "digitado à mão a partir de captura de tela do painel do Instagram (dado da conta, não vem da API)"},
    {"nome": "_update.log", "obrigatorio": False,
     "origem": "saída do agendamento do macOS `com.tatsuo.ig-update`, que roda `pull_insights.py update` às 9h, 14h, 20h e no boot"},
    {"nome": "_pull.log", "obrigatorio": False,
     "origem": "saída do único `pull_insights.py pull` completo (06/08/2026), que montou a base"},
]

# Padrões de segredo: se aparecer qualquer um num arquivo do pacote, nada é gerado.
SEGREDOS = [
    re.compile(r"IGAA[A-Za-z0-9_-]{20,}"),          # token do Instagram
    re.compile(r"EAA[A-Za-z0-9]{40,}"),              # token da Meta/Facebook
    re.compile(r"access_token="),
    re.compile(r"client_secret|app_secret"),
    re.compile(r"\bpit-[0-9a-f]{8}-[0-9a-f]{4}"),     # token de integração privada do GoHighLevel
    re.compile(r"Bearer [A-Za-z0-9._-]{20,}"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
]


# ---------------------------------------------------------------------------
# utilidades
# ---------------------------------------------------------------------------
def agora():
    return dt.datetime.now(BRT)


def fmt_bytes(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024 or u == "GB":
            return f"{n:.0f} {u}" if u == "B" else f"{n:.1f} {u}"
        n /= 1024.0


def mtime(path):
    return dt.datetime.fromtimestamp(os.path.getmtime(path), BRT).strftime("%Y-%m-%d %H:%M")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def origem_maquina():
    return hashlib.sha256(("tatsuo-pacote|" + socket.gethostname()).encode()).hexdigest()[:16]


def origem_repo():
    return hashlib.sha256(("tatsuo-pacote|" + os.path.realpath(REPO)).encode()).hexdigest()[:16]


def ler_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return r.fieldnames or [], list(r)


def contar_linhas(path):
    n = 0
    with open(path, "rb") as f:
        for _ in f:
            n += 1
    return n


def cols_md(cols):
    return ", ".join(f"`{c}`" for c in cols)


# ---------------------------------------------------------------------------
# descrição de cada arquivo (só fato: o que é, quando, quanto, quais campos)
# ---------------------------------------------------------------------------
def resumo_desempenho_json(path):
    d = json.load(open(path, encoding="utf-8"))
    posts = d.get("posts", [])
    campos, metricas = set(), set()
    tipos = {}
    for p in posts:
        campos |= set(p.keys())
        metricas |= set((p.get("metrics") or {}).keys())
        k = f"{p.get('media_type','')}/{p.get('media_product_type','')}"
        tipos[k] = tipos.get(k, 0) + 1
    ts = sorted(p.get("timestamp", "") for p in posts if p.get("timestamp"))
    det = [
        f"- `pulled_at`: {d.get('pulled_at','?')} (horário local da máquina principal, Brasília). `count`: {d.get('count','?')}.",
        f"- Posts publicados de {ts[0][:10] if ts else '?'} a {ts[-1][:10] if ts else '?'}. Por tipo: "
        + ", ".join(f"{k} {v}" for k, v in sorted(tipos.items())) + ".",
        f"- Campos de cada post: {cols_md(sorted(campos))}.",
        f"- Métricas em `metrics`: {cols_md(sorted(metricas))}.",
        "- `timestamp` é o horário de publicação como a API devolve (UTC, ex. `2026-10-13T15:36:50+0000`).",
        "- `caption_full` é a legenda inteira com as quebras de linha trocadas por espaço; `caption_preview`, os primeiros 140 caracteres.",
        "- Métricas pedidas por tipo: IMAGE e CAROUSEL_ALBUM = reach, likes, comments, saved, shares, total_interactions, views, follows, profile_visits. "
        "VIDEO/REELS = reach, likes, comments, saved, shares, total_interactions, views, ig_reels_avg_watch_time, ig_reels_video_view_total_time "
        "(a API não entrega follows nem profile_visits para vídeo). Os dois tempos de reel vêm em milissegundos, como a API devolve.",
        "- Todo valor de métrica é o acumulado de vida do post no momento em que ele foi lido.",
        "- O `update` relê só os posts publicados nos últimos 30 dias (e acrescenta os novos). Post mais velho que isso guarda o número da última vez que foi lido.",
        "- `comments_read`, `cta_keyword`, `cta_keyword_count`, `cta_share`, `cta_top_tokens` foram calculados só pelo `pull` completo de 06/08/2026, lendo os comentários. "
        "O `update` não lê comentário: guarda o valor antigo, e post novo vem com 0 ou vazio nesses campos.",
    ]
    return {"coleta": d.get("pulled_at", "?"), "registros": f"{len(posts)} posts", "detalhes": det}


def resumo_desempenho_csv(path):
    cols, rows = ler_csv(path)
    det = [
        f"- {len(rows)} linhas, uma por post. Mesma coleta do `desempenho.json` (é reescrito junto com ele).",
        f"- Colunas: {cols_md(cols)}.",
        "- Não tem `caption_full` nem `cta_top_tokens` (só no JSON). Célula vazia = a API não devolveu aquela métrica para aquele tipo de post.",
    ]
    return {"coleta": f"mesma do desempenho.json (arquivo gravado em {mtime(path)})",
            "registros": f"{len(rows)} posts", "detalhes": det}


def resumo_snapshots(path):
    cols, rows = ler_csv(path)
    dias = sorted({r["data_snapshot"] for r in rows if r.get("data_snapshot")})
    faltam = []
    if dias:
        d0, d1 = dt.date.fromisoformat(dias[0]), dt.date.fromisoformat(dias[-1])
        tem = set(dias)
        faltam = [(d0 + dt.timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)
                  if (d0 + dt.timedelta(days=i)).isoformat() not in tem]
    ultimo = [r for r in rows if dias and r.get("data_snapshot") == dias[-1]]
    det = [
        f"- {len(rows)} linhas; {len(dias)} dias fotografados, de {dias[0] if dias else '?'} a {dias[-1] if dias else '?'}; "
        f"{len(ultimo)} posts na foto do último dia.",
        f"- Colunas: {cols_md(cols)}.",
        "- Uma linha por post por dia, para todo post com 0 a 30 dias de idade na data da foto. `idade_dias` = `data_snapshot` menos a data do `timestamp` de publicação.",
        "- `comments`, `reach`, `saved`, `shares` são o acumulado de vida naquele dia (a API não dá série diária; ela só existe porque o update fotografa todo dia).",
        "- Rodar o update mais de uma vez no mesmo dia substitui as linhas daquele dia pela leitura mais recente; nunca duplica.",
        "- Dia sem foto não se recupera pela API. Dias sem foto entre o primeiro e o último: "
        + (", ".join(faltam) if faltam else "nenhum") + ".",
    ]
    return {"coleta": f"último dia fotografado {dias[-1] if dias else '?'} (arquivo gravado em {mtime(path)})",
            "registros": f"{len(rows)} linhas", "detalhes": det}


def resumo_leads(path):
    d = json.load(open(path, encoding="utf-8"))
    cont = d.get("contatos", [])
    ck, ok, ak = set(), set(), set()
    for c in cont:
        ck |= set(c.keys())
        for o in c.get("oportunidades") or []:
            ok |= set(o.keys())
        for a in (c.get("primeira_atribuicao"), c.get("ultima_atribuicao")):
            if a:
                ak |= set(a.keys())
    det = [
        f"- `pulled_at`: {d.get('pulled_at','?')} (Brasília). `janela_dias`: {d.get('janela_dias','?')} (contatos de 00h de {d.get('janela_dias','?')} dias atrás até a hora da coleta).",
        f"- `total_contatos`: {d.get('total_contatos','?')}; `total_reimpactados`: {d.get('total_reimpactados','?')}; `total_oportunidades`: {d.get('total_oportunidades','?')}.",
        "- Duas buscas no CRM: contatos CRIADOS na janela (`reimpactado=false`) e contatos ATUALIZADOS na janela que não foram criados nela (`reimpactado=true`). "
        "O GoHighLevel junta contato pelo e-mail: lead antigo que volta não cria contato novo, só atualiza o existente.",
        f"- Campos de cada contato: {cols_md(sorted(ck))}.",
        "- `dt_criacao_brt` e `dt_atualizacao_brt` estão em horário de Brasília. `tags` são as etiquetas do contato no CRM (é onde o comercial marca `mql`, `q-mql`, `n-mql`). "
        "`customFields` vem como a API entrega.",
        f"- `primeira_atribuicao` (attributionSource do CRM) e `ultima_atribuicao` (lastAttributionSource): {cols_md(sorted(ak))}; `null` quando o CRM não tem rastro.",
        f"- `oportunidades` (só as do período, ligadas a contatos da lista): {cols_md(sorted(ok))}. "
        "`funil_valido=true` = um dos 5 \"Funil de Vendas\" listados no `pull_leads.py`; os demais funis da conta vêm com `false`.",
        "- **Dados pessoais** (nome, e-mail, telefone): manter em canal privado.",
    ]
    return {"coleta": d.get("pulled_at", "?"),
            "registros": f"{len(cont)} contatos, {d.get('total_oportunidades','?')} oportunidades", "detalhes": det}


def resumo_disparos(path):
    d = json.load(open(path, encoding="utf-8"))
    chaves = {k: v for k, v in d.items() if not k.startswith("_")}
    campos = set()
    lidas = {}
    for v in chaves.values():
        if isinstance(v, dict):
            campos |= set(v.keys())
            le = v.get("lido_em") or "(sem lido_em)"
            lidas[le] = lidas.get(le, 0) + 1
    det = [
        f"- `_lido_em`: {d.get('_lido_em','?')} (última leitura do painel). `_fonte`: {d.get('_fonte','')}",
        f"- {len(chaves)} palavras-chave. Chave = palavra do CTA em caixa alta. Campos: {cols_md(sorted(campos))}.",
        "- `disparos` = execuções da automação no painel; `ctr` = porcentagem de clique no botão do DM como o painel mostra; "
        "`post` = pasta do post no registro desta máquina; `utm` = se o link do DM leva UTM; `lido_em` = data em que aquela chave foi lida pela última vez.",
        "- Campos que só algumas chaves têm: `cliques` (cliques no botão, quando o painel mostrava o número), `campanha` (o utm_campaign do link), "
        "`estado` (situação da automação anotada na leitura), `palavra` (a palavra real, quando a chave leva sufixo de data para não colidir com outra).",
        "- Chaves que começam com `_` são notas do arquivo: " + ", ".join(f"`{k}`" for k in sorted(d) if k.startswith("_")) + ".",
        "- Quando a mesma palavra foi usada em mais de um post, a chave guarda a automação do post mais recente.",
        "- Chaves por data de leitura: " + ", ".join(f"{k}: {v}" for k, v in sorted(lidas.items())) + ".",
    ]
    return {"coleta": d.get("_lido_em", "?"), "registros": f"{len(chaves)} palavras", "detalhes": det}


def resumo_painel(path):
    cols, rows = ler_csv(path)
    cap = sorted(r.get("capturado_em", "") for r in rows if r.get("capturado_em"))
    jan = [f"{r.get('janela_ini','?')} a {r.get('janela_fim','?')}" for r in rows]
    det = [
        f"- {len(rows)} linhas, uma por janela semanal da conta: {'; '.join(jan) if jan else 'nenhuma'}.",
        f"- Colunas: {cols_md(cols)}.",
        "- Digitado à mão a partir de captura de tela do painel do Instagram (são números da conta inteira, que a API por post não dá).",
    ]
    return {"coleta": cap[-1] if cap else mtime(path), "registros": f"{len(rows)} linhas", "detalhes": det}


def resumo_log(path, nome):
    det = [f"- {contar_linhas(path)} linhas, {fmt_bytes(os.path.getsize(path))}. Última escrita: {mtime(path)}."]
    if nome == "_update.log":
        det += [
            "- Acumula a saída de todas as rodadas do agendamento, sem data por rodada. Cada rodada lista os posts da janela de 30 dias "
            "(data, tipo, reach, comentários, novo/atualizado), fecha com \"Base atualizada: N posts\" e a linha do snapshot do dia.",
            "- Erros de rede e de API aparecem aqui como o Python imprime (ex. falha de DNS quando o Mac está sem internet).",
        ]
    else:
        det += ["- Saída do `pull` completo de 06/08/2026 (lista de mídia desde 2025-01-01, insights e comentários de cada post). Não muda mais."]
    return {"coleta": f"última escrita {mtime(path)}", "registros": f"{contar_linhas(path)} linhas", "detalhes": det}


RESUMOS = {
    "desempenho.json": resumo_desempenho_json,
    "desempenho.csv": resumo_desempenho_csv,
    "_snapshots.csv": resumo_snapshots,
    "leads.json": resumo_leads,
    "_disparos.json": resumo_disparos,
    "_painel-instagram.csv": resumo_painel,
}

DESTINO = {  # para onde o importar_pacote.py copia cada arquivo
    "registro-posts-factual.csv": "conteudo/analise/_registro-maquina-user.csv",
}


# ---------------------------------------------------------------------------
# montagem
# ---------------------------------------------------------------------------
def montar_registro(dest):
    src = os.path.join(ANALISE, "registro-posts.csv")
    cols, rows = ler_csv(src)
    faltam = [c for c in REGISTRO_COLS if c not in cols]
    if faltam:
        sys.exit(f"registro-posts.csv sem as colunas {faltam}; nada foi gerado.")
    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=REGISTRO_COLS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in REGISTRO_COLS})
    pubs = sorted(r["data_publicacao"] for r in rows if r.get("data_publicacao"))
    det = [
        f"- {len(rows)} fichas (uma por post produzido na máquina principal, gravadas pela skill /etiqueta). "
        f"{sum(1 for r in rows if r.get('post_id'))} com `post_id`; {len(pubs)} com `data_publicacao` "
        f"(de {pubs[0] if pubs else '?'} a {pubs[-1] if pubs else '?'}).",
        f"- Colunas (só as factuais do registro-posts.csv): {cols_md(REGISTRO_COLS)}.",
        "- `data` = dia da ficha; `data_publicacao` = dia em que foi ao ar; `post_id` = id da mídia na API (vazio enquanto não foi casado com o post); "
        "`pasta` = conteudo/carrosseis/<pasta> na máquina principal; `formato` = carrossel, frase ou reel; `semente` = de onde veio a ideia; "
        "`pilar` = Lucratividade, Crescimento ou Cultura; `funil` = campo aposentado em 31/08/2026 (vazio desde então); "
        "`objetivo` = lead, seguidor ou alcance, declarado na criação; `palavra_chave` = palavra do CTA de comentário (vazio quando o post não tem).",
        "- As outras colunas do registro original (previsão, faixa, justificativa, resultados, nervo, consciência da dor, mecanismo, roupa) ficaram de fora: são análise da máquina principal.",
    ]
    return rows, {"coleta": f"arquivo gravado em {mtime(src)}", "registros": f"{len(rows)} fichas", "detalhes": det}


def achar_pasta(pasta):
    if not PASTA_OK.match(pasta or ""):
        return None
    cand = [os.path.join(CARROSSEIS, pasta)]
    base = os.path.join(REPO, "conteudo")
    for sub in sorted(os.listdir(base)):
        cand.append(os.path.join(base, sub, pasta))
    for c in cand:
        if os.path.isdir(c):
            return c
    return None


def montar_posts(rows, hoje, dias, raiz_posts):
    ini = (hoje - dt.timedelta(days=dias)).isoformat()
    fim = hoje.isoformat()
    vistos, lista = set(), []
    for r in rows:
        dp, pasta = (r.get("data_publicacao") or "").strip(), (r.get("pasta") or "").strip()
        if not dp or not (ini <= dp <= fim) or not pasta or pasta in vistos:
            continue
        vistos.add(pasta)
        item = {"pasta": pasta, "data_publicacao": dp, "formato": r.get("formato", ""),
                "post_id": r.get("post_id", ""), "arquivos": [], "linhas_previsao_retiradas": 0}
        src = achar_pasta(pasta)
        if src:
            for nome in TEXTOS_POST:
                p = os.path.join(src, nome)
                if not os.path.isfile(p):
                    continue
                os.makedirs(os.path.join(raiz_posts, pasta), exist_ok=True)
                dst = os.path.join(raiz_posts, pasta, nome)
                if nome == "carousel-text.md":
                    linhas = open(p, encoding="utf-8").read().split("\n")
                    fica = [ln for ln in linhas if not LINHA_PREVISAO.match(ln)]
                    item["linhas_previsao_retiradas"] = len(linhas) - len(fica)
                    open(dst, "w", encoding="utf-8").write("\n".join(fica))
                    shutil.copystat(p, dst)
                else:
                    shutil.copy2(p, dst)
                item["arquivos"].append(nome)
        item["origem"] = os.path.relpath(src, REPO) if src else None
        lista.append(item)
    lista.sort(key=lambda x: (x["data_publicacao"], x["pasta"]))
    return ini, fim, lista


def checar_segredos(raiz):
    achados = []
    for base, _, files in os.walk(raiz):
        for fn in files:
            p = os.path.join(base, fn)
            try:
                txt = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for rx in SEGREDOS:
                if rx.search(txt):
                    achados.append((os.path.relpath(p, raiz), rx.pattern))
    return achados


def escrever_manifesto(path, info):
    L = []
    L.append(f"# Pacote de dados brutos do analytics — {info['data']}")
    L.append("")
    L.append(f"Gerado em {info['gerado_em']} (horário de Brasília) por `scripts/pacote/gerar_pacote.py`, na máquina principal "
             "(a única que coleta: API do Instagram, CRM GoHighLevel e painel do Manychat).")
    L.append("")
    L.append("> **Aviso:** dados brutos, sem interpretação; leads.json contém dados pessoais de leads, manter em canal privado.")
    L.append("")
    L.append("Este manifesto só descreve os arquivos: o que é, de onde vem, quando foi coletado, quantos registros e quais colunas. "
             "Nenhum número aqui foi analisado ou comparado.")
    L.append("")
    L.append("## Como importar")
    L.append("")
    L.append("Na máquina que recebe: `python3 scripts/pacote/importar_pacote.py <caminho do zip>`. O importador confere o `checksums.txt` antes de copiar qualquer coisa. "
             "Conferência manual, dentro da pasta extraída: `shasum -a 256 -c checksums.txt`.")
    L.append("")
    L.append("## Arquivos")
    L.append("")
    L.append("| Arquivo no pacote | Vai para (na importação) | Origem | Coleta | Registros | Tamanho |")
    L.append("|---|---|---|---|---|---|")
    for a in info["arquivos"]:
        L.append(f"| `{a['caminho']}` | `{a['destino']}` | {a['origem']} | {a['coleta']} | {a['registros']} | {fmt_bytes(a['bytes'])} |")
    if info["ausentes"]:
        L.append("")
        L.append("Não estavam no disco na hora do pacote (não vieram): " + ", ".join(f"`{x}`" for x in info["ausentes"]) + ".")
    L.append("")
    L.append("## Detalhe por arquivo")
    for a in info["arquivos"]:
        L.append("")
        L.append(f"### `{a['caminho']}`")
        L.append("")
        L.append(f"Origem: {a['origem']}.")
        L.append("")
        L.extend(a["detalhes"])
    L.append("")
    L.append(f"## Textos dos posts publicados de {info['posts_ini']} a {info['posts_fim']}")
    L.append("")
    L.append("Para cada ficha do registro com `data_publicacao` nessa janela, vêm os arquivos `carousel-text.md` (texto dos slides, legenda e as notas de produção, "
             "como estão na pasta do post) e `legenda.txt` (quando a pasta tem esse arquivo). Na importação vão para `conteudo/carrosseis/_da-maquina-do-user/<pasta>/`.")
    L.append("")
    L.append("Única alteração: no `carousel-text.md`, a linha que começa com \"Etiqueta:\" (a previsão de desempenho gravada pela /etiqueta) é retirada, "
             "porque previsão é análise da máquina principal. A última coluna diz quantas linhas saíram de cada arquivo. O resto vai literal.")
    L.append("")
    L.append("| Pasta | Publicado em | Formato | post_id | Arquivos | Linhas retiradas |")
    L.append("|---|---|---|---|---|---|")
    for p in info["posts"]:
        arq = ", ".join(p["arquivos"]) if p["arquivos"] else ("pasta não encontrada" if not p["origem"] else "pasta sem esses arquivos")
        L.append(f"| `{p['pasta']}` | {p['data_publicacao']} | {p['formato']} | {p['post_id'] or '(vazio)'} | {arq} | {p['linhas_previsao_retiradas']} |")
    L.append("")
    L.append("## O que não vem no pacote")
    L.append("")
    L.append("- Token, chave e credencial de qualquer API (ficam só na máquina principal).")
    L.append("- A análise da máquina principal: as colunas de previsão e resultado do registro, `hipoteses.md`, os briefings do ritual, "
             "as listas de exceção (`_descartados.csv`, `_ressalvas.csv`, `_cauda-longa.csv`), `manychat-baseline.md` e relatórios.")
    L.append("- Imagens (os PNGs dos posts ficam no Google Drive).")
    L.append("")
    L.append("## Integridade")
    L.append("")
    L.append("`checksums.txt` tem o sha256 de todos os arquivos do pacote, inclusive este manifesto e o `pacote.json` (só não de si mesmo).")
    L.append("")
    open(path, "w", encoding="utf-8").write("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description="Gera o pacote diário de dados brutos do analytics (zero API).")
    ap.add_argument("--saida", default=SAIDA_PADRAO, help="pasta onde o zip é gravado")
    ap.add_argument("--dias", type=int, default=14, help="janela, em dias, dos textos de posts publicados (padrão 14)")
    args = ap.parse_args()

    t = agora()
    hoje = t.date()
    data = hoje.isoformat()
    raiz_nome = f"pacote-{data}"
    tmp = tempfile.mkdtemp(prefix="pacote-")
    try:
        raiz = os.path.join(tmp, raiz_nome)
        os.makedirs(os.path.join(raiz, "analise"))

        arquivos, ausentes = [], []
        for a in ARQUIVOS:
            src = os.path.join(ANALISE, a["nome"])
            if not os.path.isfile(src):
                if a["obrigatorio"]:
                    sys.exit(f"Falta {src}; nada foi gerado.")
                ausentes.append(a["nome"])
                continue
            dst = os.path.join(raiz, "analise", a["nome"])
            shutil.copy2(src, dst)
            if a["nome"] in RESUMOS:
                r = RESUMOS[a["nome"]](dst)
            else:
                r = resumo_log(dst, a["nome"])
            arquivos.append({"caminho": f"analise/{a['nome']}",
                             "destino": DESTINO.get(a["nome"], f"conteudo/analise/{a['nome']}"),
                             "origem": a["origem"], "bytes": os.path.getsize(dst), **r})

        reg_dst = os.path.join(raiz, "analise", "registro-posts-factual.csv")
        rows, r = montar_registro(reg_dst)
        arquivos.append({"caminho": "analise/registro-posts-factual.csv",
                         "destino": DESTINO["registro-posts-factual.csv"],
                         "origem": "recorte de `conteudo/analise/registro-posts.csv` (fichas da skill /etiqueta), só colunas factuais",
                         "bytes": os.path.getsize(reg_dst), **r})

        ini, fim, posts = montar_posts(rows, hoje, args.dias, os.path.join(raiz, "posts"))

        info = {"data": data, "gerado_em": t.strftime("%Y-%m-%d %H:%M"), "arquivos": arquivos,
                "ausentes": ausentes, "posts_ini": ini, "posts_fim": fim, "posts": posts}
        escrever_manifesto(os.path.join(raiz, "MANIFESTO.md"), info)

        meta = {
            "formato_pacote": FORMATO_PACOTE,
            "data": data,
            "gerado_em": info["gerado_em"],
            "fuso": "America/Sao_Paulo",
            "origem_maquina": origem_maquina(),
            "origem_repo": origem_repo(),
            "janela_posts_dias": args.dias,
            "arquivos": {a["caminho"]: {"coleta": a["coleta"], "registros": a["registros"], "bytes": a["bytes"]}
                         for a in arquivos},
            "posts": posts,
        }
        json.dump(meta, open(os.path.join(raiz, "pacote.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

        achados = checar_segredos(raiz)
        if achados:
            for rel, pat in achados:
                print(f"SEGREDO? {rel} casa com o padrão {pat}", file=sys.stderr)
            sys.exit("Padrão de token/credencial encontrado; nada foi gerado. Conferir os arquivos acima.")

        todos = []
        for base, _, files in os.walk(raiz):
            for fn in files:
                rel = os.path.relpath(os.path.join(base, fn), raiz).replace(os.sep, "/")
                todos.append(rel)
        todos.sort()
        with open(os.path.join(raiz, "checksums.txt"), "w", encoding="utf-8") as f:
            for rel in todos:
                f.write(f"{sha256(os.path.join(raiz, rel))}  {rel}\n")
        todos.append("checksums.txt")

        os.makedirs(args.saida, exist_ok=True)
        final = os.path.join(args.saida, f"{raiz_nome}.zip")
        parcial = final + ".parcial"
        with zipfile.ZipFile(parcial, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for rel in sorted(todos):
                z.write(os.path.join(raiz, rel), f"{raiz_nome}/{rel}")
        os.replace(parcial, final)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"Pacote: {final} ({fmt_bytes(os.path.getsize(final))})")
    for a in arquivos:
        print(f"  {a['caminho']:42} coleta {a['coleta']:>22}  {a['registros']}")
    if ausentes:
        print(f"  ausentes (não vieram): {', '.join(ausentes)}")
    com_texto = sum(1 for p in posts if p["arquivos"])
    print(f"  posts publicados de {ini} a {fim}: {len(posts)} fichas, {com_texto} com texto")


if __name__ == "__main__":
    main()
