#!/usr/bin/env python3
"""Relatorio semanal de desempenho de conteudo, em PDF (formato de artigo).

Regra de forma (decisao do user, 31/08/2026): o documento sai da casa e pode ser lido por
alguem de fora da area. Entao ele se explica sozinho — titulo de tabela descritivo, nome de
coluna por extenso, legenda com a definicao de cada metrica, e um texto de enquadramento
antes dos numeros, na estrutura de artigo:

    Resumo · Objetivo · Metodo · Resultados · Discussao · Conclusao · Limitacoes

O resumo carrega a conclusao logo no comeco — e por isso a estrutura de artigo NAO briga com
a piramide invertida do briefing diario (regra do user, 27/08): o abstract ja e a piramide.

Ordenacao (decisao do user, 31/08): cada tabela ordena pela SUA coluna de resultado, dita na
legenda. Tabela 1 por lead qualificado · Tabela 2 por taxa de interacao · Tabela 3 por alcance.
A frase nao entra na Tabela 1: nao tem CTA por desenho, entao nao ha lead a trackear.

  python3 scripts/analise/briefing_pdf.py --texto conteudo/analise/_briefing_texto.md

Zero chamada de API: le desempenho.json, registro-posts.csv, leads.json, _disparos.json e
_descartados.csv. Renderiza HTML -> PDF com o playwright que ja vive no node_modules.
"""
import argparse, base64, datetime, html, json, os, re, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import tabelas_ritual as T

MESES = ["janeiro","fevereiro","março","abril","maio","junho","julho",
         "agosto","setembro","outubro","novembro","dezembro"]
ORD = {"abaixo": 0, "mediana": 1, "acima": 2, "—": 1}


def num(v, casas=0):
    if v is None: return "—"
    return f"{v:,.{casas}f}".replace(",", " ").replace(".", ",")


# ---------------------------------------------------------------- miniaturas
# A capa da publicacao vive em conteudo/carrosseis/<pasta>/instagram/slide-01.png,
# 1080x1350 e ~1,2 MB. Embutir 39 dessas cruas no PDF daria ~50 MB, entao cada uma e
# reduzida pra 120px de largura em JPEG (~6 KB) e guardada num cache local.
#
# MATCH EXATO em "slide-01.png", nunca glob: 40_colheita tem slide-01-carroca.png e
# slide-01-ceifeiro.png, e 65_feijao-pressao tem um slide-01-v1.png descartado. Um
# glob "slide-01*" pegaria a capa errada nesses dois casos, em silencio.
#
# Os PNGs sao gitignored e vem do Google Drive: numa maquina sem o Drive sincronizado
# eles simplesmente nao existem. Por isso toda falha aqui degrada pra placeholder — o
# relatorio sai sem miniatura, nunca deixa de sair.
CACHE_MIN = os.path.join(RAIZ, "conteudo", "analise", "_miniaturas")
LARGURA_MIN = 120


def _capa_original(pasta):
    p = os.path.join(RAIZ, "conteudo", "carrosseis", pasta, "instagram", "slide-01.png")
    return p if os.path.isfile(p) else None


def miniatura(pasta):
    """Data URI da capa reduzida, ou None se nao houver capa no disco (reel, ou maquina
    sem o Drive). Regenera o cache so quando a origem e mais nova que o derivado."""
    origem = _capa_original(pasta)
    if not origem:
        return None
    destino = os.path.join(CACHE_MIN, f"{pasta}.jpg")
    try:
        if not os.path.isfile(destino) or os.path.getmtime(destino) < os.path.getmtime(origem):
            os.makedirs(CACHE_MIN, exist_ok=True)
            # Windows: sem o sips do Mac, a miniatura sai pelo Pillow
            from PIL import Image
            im = Image.open(origem).convert("RGB")
            im.thumbnail((int(LARGURA_MIN * 1.25), int(LARGURA_MIN * 1.25)))
            im.save(destino, "JPEG", quality=72)
        with open(destino, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
    except Exception:
        return None  # sips ausente, PNG corrompido, disco cheio: segue sem miniatura


def celula_capa(pasta, permalink, formato):
    """Miniatura clicavel. Sem capa, um bloco cinza dizendo o formato — a linha nunca some."""
    src = miniatura(pasta)
    if src:
        interno = f"<img class='mini' src='{src}' alt='capa de {html.escape(pasta)}'>"
    else:
        interno = f"<span class='semcapa'>{html.escape(formato)}<br>sem capa</span>"
    if permalink:
        return f"<td class='capa'><a href='{html.escape(permalink)}'>{interno}</a></td>"
    return f"<td class='capa'>{interno}</td>"


def qual_contagem(contatos):
    q = {"MQL": 0, "Q-MQL": 0, "N-MQL": 0, "sem classif.": 0}
    for c in contatos:
        q[T.qualificacao(c["tags"])] = q.get(T.qualificacao(c["tags"]), 0) + 1
    return q


ORIGEM_ORGANICA = {"Manychat", "Instagram DM", "Linkbio", "Youtube"}
ORIGEM_PAGA = {"Formulário Meta", "Tráfego"}


def painel_conta():
    """Metricas de CONTA, transcritas do painel de Insights do Instagram.
    A API oficial nao devolve contagem de conta (nem seguidores), entao esta camada
    entra a mao, por captura de tela, e fica auditavel em _painel-instagram.csv."""
    p = os.path.join(T.ANALISE, "_painel-instagram.csv")
    if not os.path.exists(p): return []
    import csv as _csv
    with open(p, encoding="utf-8") as f:
        return sorted(_csv.DictReader(f), key=lambda r: r["janela_ini"])


def _classe_origem(c):
    """Orgânico x pago pela FONTE DA OPORTUNIDADE (o que chega ao comercial),
    nao pelo source do contato — o source do contato nao conhece o canal Instagram DM."""
    fs = {(o.get("fonte") or "") for o in (c.get("oportunidades") or [])}
    if fs & ORIGEM_ORGANICA: return "organico"
    if fs & ORIGEM_PAGA: return "pago"
    return "sem oportunidade"


def _qual(tags):
    t = " ".join(tags or []).lower()
    return "Q-MQL" if "q-mql" in t else ("N-MQL" if "n-mql" in t else ("MQL" if "mql" in t else None))


def painel_leads(janelas):
    """Contatos criados em cada janela, separados por origem e qualificacao do comercial."""
    try: contatos = T.carregar("leads.json")["contatos"]
    except Exception: return {}
    out = {}
    for ini, fim in janelas:
        acc = {k: {"n": 0, "MQL": 0, "Q-MQL": 0, "N-MQL": 0, "utm": 0}
               for k in ("organico", "pago", "sem oportunidade")}
        for c in contatos:
            dc = (c.get("dt_criacao_brt") or "")[:10]
            if not dc or not (ini <= dc <= fim): continue
            k = _classe_origem(c); r = acc[k]; r["n"] += 1
            q = _qual(c.get("tags"))
            if q: r[q] += 1
            atr = (c.get("ultima_atribuicao") if c.get("reimpactado")
                   else c.get("primeira_atribuicao")) or {}
            if atr.get("campaign"): r["utm"] += 1
        out[(ini, fim)] = acc
    return out


def coletar(dias=7):
    posts = T.carregar("desempenho.json")["posts"]
    fichas = T.carregar("registro-posts.csv")
    fora = T.descartados()
    dp = os.path.join(T.ANALISE, "_disparos.json")
    disparos = json.load(open(dp, encoding="utf-8")) if os.path.exists(dp) else {}
    try: contatos = T.carregar("leads.json")["contatos"]
    except Exception: contatos = []

    por_campanha = {}
    for c in contatos:
        atr = (c["ultima_atribuicao"] if c["reimpactado"] else c["primeira_atribuicao"]) or {}
        camp = T.palavra_da_campanha(atr.get("campaign"))
        if camp: por_campanha.setdefault(camp, []).append(c)

    def idade_de(f):
        return (T.HOJE - datetime.date.fromisoformat(f["data_publicacao"])).days

    def linhas_de(formatos, limite=14):
        vistos, saida = set(), []
        for f in fichas:
            if f.get("formato") not in formatos or not f.get("data_publicacao"): continue
            if idade_de(f) > limite or f["pasta"] in vistos: continue
            vistos.add(f["pasta"])
            p = T.casar(f, posts, fora)
            if p and (p["metrics"].get("reach") or 0) >= T.REACH_MINIMO:
                saida.append((f, p))
        return saida

    def estado(f):
        i = idade_de(f)
        st = ("fechado" if f.get("resultado_vs_previsao") else "fecha hoje") if i >= 7 \
             else f"maturando (D+{i})"
        return i, datetime.date.fromisoformat(f["data_publicacao"]).strftime("%d/%m"), st

    # --- Tabela 1: so quem tem CTA (carrossel e reel com palavra-chave) ---
    t1 = []
    for f, p in linhas_de(("carrossel", "reel"), limite=dias):
        pal = (f.get("palavra_chave") or "").strip().upper()
        if not pal: continue
        d = disparos.get(pal, {}); cs = por_campanha.get(pal, [])
        temutm = bool(cs) or d.get("utm")
        q = qual_contagem(cs)
        i, dia, st = estado(f)
        rc = p["metrics"].get("reach") or 0
        com = p["metrics"].get("comments") or 0
        t1.append(dict(pasta=f["pasta"], palavra=pal, dia=dia, idade=i,
                       pilar=f.get("pilar") or "—", objetivo=f.get("objetivo") or "—",
                       formato=f["formato"], permalink=p.get("permalink"),
                       com=com, com1k=(1000 * com / rc) if rc else 0,
                       disp=d.get("disparos"), ctr=d.get("ctr"),
                       novos=len([c for c in cs if not c["reimpactado"]]),
                       reimp=len([c for c in cs if c["reimpactado"]]),
                       mql=q["MQL"], qmql=q["Q-MQL"], nmql=q["N-MQL"],
                       rastro=bool(temutm)))
    t1.sort(key=lambda r: (r["mql"] + r["qmql"], r["novos"], r["disp"] or -1), reverse=True)

    # --- Tabela 2: carrossel e reel, ordenada por taxa ---
    t2 = []
    for f, p in linhas_de(("carrossel", "reel")):
        m = p["metrics"]; rc = m["reach"]; t = T.taxa_de(p, "carrossel")
        pal = (f.get("palavra_chave") or "").strip().upper()
        d = disparos.get(pal, {}); cs = por_campanha.get(pal, [])
        i, dia, st = estado(f)
        q = qual_contagem(cs)
        t2.append(dict(pasta=f["pasta"], palavra=pal, formato=f["formato"], dia=dia, idade=i,
                       pilar=f.get("pilar") or "—", objetivo=f.get("objetivo") or "—",
                       permalink=p.get("permalink"),
                       alcance=rc, taxa=t, banda=T.banda_de(t, f["formato"]),
                       prev=f.get("previsao") or "—", com=m.get("comments") or 0,
                       com1k=1000*(m.get("comments") or 0)/rc,
                       views=m.get("views") or 0,
                       shr=1000*m.get("shares",0)/rc, sav=1000*m.get("saved",0)/rc,
                       disp=d.get("disparos") if pal else None,
                       leads=len(cs) if (cs or d.get("utm")) else None,
                       mql=q["MQL"] + q["Q-MQL"], status=st))
    # 1a metrica do objetivo LEAD, decisao do user em 31/08: comentario e o degrau que vira
    # disparo de automacao (rho +0,94). A taxa de interacao continua na tabela e continua
    # sendo o que pontua no placar — o que mudou foi a ORDEM de leitura.
    t2.sort(key=lambda r: r["com1k"], reverse=True)

    # --- Tabela 3: frase, ordenada por alcance ---
    t3 = []
    for f, p in linhas_de(("frase",)):
        m = p["metrics"]; rc = m["reach"]; t = T.taxa_de(p, "frase")
        i, dia, st = estado(f)
        t3.append(dict(pasta=f["pasta"], dia=dia, idade=i, alcance=rc,
                       pilar=f.get("pilar") or "—", objetivo=f.get("objetivo") or "—",
                       permalink=p.get("permalink"), formato="frase",
                       shares=m.get("shares") or 0, taxa=t, banda=T.banda_de(t, "frase"),
                       # follows/profile_visits ja vinham da API pra IMAGE e CAROUSEL desde
                       # sempre, e nunca tinham sido reportados. Sao o ativo que a frase
                       # constroi: publico novo no perfil.
                       follows=m.get("follows"), visitas=m.get("profile_visits"),
                       sav=1000*m.get("saved",0)/rc, prev=f.get("previsao") or "—", status=st))
    t3.sort(key=lambda r: r["alcance"], reverse=True)
    return t1, t2, t3


def secoes(caminho):
    """Le o markdown de enquadramento. '# Titulo' abre secao; '- ' vira item; resto e paragrafo."""
    if not caminho or not os.path.exists(caminho): return {}
    out, chave = {}, None
    for ln in open(caminho, encoding="utf-8").read().split("\n"):
        if ln.startswith("# "):
            chave = ln[2:].strip().lower(); out[chave] = []
        elif ln.strip() and chave:
            out[chave].append(ln.strip())
    return out


def inline(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(s))


def bloco(secs, chave, titulo=None, numero=None):
    linhas = secs.get(chave.lower())
    if not linhas: return ""
    b = []
    if titulo:
        n = f"<span class='n'>{numero}</span>" if numero else ""
        b.append(f"<h2>{n}{html.escape(titulo)}</h2>")
    for ln in linhas:
        if ln.startswith("- "):
            b.append("<li>" + inline(ln[2:]) + "</li>")
        else:
            b.append("<p>" + inline(ln) + "</p>")
    txt = "".join(b)
    return re.sub(r"(<li>.*</li>)", r"<ul>\1</ul>", txt, flags=re.S) if "<li>" in txt else txt


CSS = """
@page { size:A4 landscape; margin:13mm 12mm 11mm; }
*{box-sizing:border-box}
body{font-family:"Instrument Sans","Helvetica Neue",Helvetica,Arial,sans-serif;color:#111;
     font-size:8.6pt;line-height:1.5;margin:0}
.capa{margin-bottom:7mm}
h1{font-size:20pt;letter-spacing:-.5pt;margin:0 0 1.5mm;font-weight:800;max-width:210mm}
.rule{height:3px;background:#A91C20;width:40mm;margin:2mm 0 3mm}
.sub{color:#555;font-size:8.6pt}
h2{font-size:10pt;margin:6.5mm 0 2mm;font-weight:800;letter-spacing:.3pt;text-transform:uppercase;
   border-bottom:1.5px solid #111;padding-bottom:1.2mm}
h2 .n{color:#A91C20;margin-right:2.5mm}
h3{font-size:8.8pt;margin:4mm 0 1.5mm;font-weight:800}
h3 .cap{color:#A91C20}
p{margin:0 0 2mm;max-width:245mm;text-align:justify}
ul{margin:0 0 2mm;padding-left:5mm;max-width:245mm}
li{margin-bottom:1.3mm}
.resumo{background:#f5f5f5;border-left:3px solid #A91C20;padding:3mm 4mm 2mm;margin-bottom:2mm}
.resumo p{max-width:none}
table{width:100%;border-collapse:collapse;font-size:7.5pt;font-variant-numeric:tabular-nums;
      margin-top:1mm}
th{text-align:right;font-weight:700;border-bottom:1.2px solid #111;padding:1.4mm 1.3mm;
   font-size:6.8pt;text-transform:uppercase;letter-spacing:.25pt;vertical-align:bottom;
   line-height:1.25}
th.l,td.l{text-align:left}
td{padding:1.3mm;border-bottom:.5px solid #ddd;text-align:right;white-space:nowrap;
   vertical-align:middle}
td.l{white-space:normal}
td.capa{padding:1.1mm 2mm 1.1mm 0;width:15mm}
td.capa a{display:block;text-decoration:none}
img.mini{width:13mm;height:auto;display:block;border:.5px solid #ddd}
.semcapa{display:flex;align-items:center;justify-content:center;width:13mm;height:16.2mm;
         background:#eee;border:.5px solid #ddd;color:#999;font-size:5.4pt;line-height:1.25;
         text-align:center;text-transform:uppercase;letter-spacing:.2pt}
.pilar{display:inline-block;font-size:6.3pt;letter-spacing:.3pt;text-transform:uppercase;
       padding:.5mm 1.4mm;border:.5px solid #bbb;border-radius:1mm;color:#444;white-space:nowrap}
.pilar.Cultura{border-color:#A91C20;color:#A91C20}
.chave{display:block;color:#999;font-size:6.4pt;letter-spacing:.4pt;text-transform:uppercase}
tr.destaque td{background:#fbf1f1}
tr.imaturo td{color:#777}
.acima{color:#A91C20;font-weight:700}
.abaixo{color:#999}
.errou{color:#A91C20;font-weight:700}
.leg{color:#555;font-size:6.9pt;margin-top:1.8mm;line-height:1.5;max-width:245mm}
.leg b{color:#111}
.pg{page-break-before:always}
.rod{margin-top:6mm;padding-top:2mm;border-top:.5px solid #ccc;color:#888;font-size:6.5pt}
"""


def tabela(numero, titulo, legenda, cabs, linhas):
    b = [f"<h3><span class='cap'>Tabela {numero}.</span> {titulo}</h3><table><tr>"]
    for c, cls in cabs: b.append(f"<th class='{cls}'>{c}</th>")
    b.append("</tr>")
    b.extend(linhas)
    b.append("</table>")
    b.append(f"<div class='leg'>{legenda}</div>")
    return "".join(b)


def render(t1, t2, t3, secs, hoje, dias):
    fim = hoje
    ini = hoje - datetime.timedelta(days=dias)
    b = ["<div class='capa'><h1>Relatório semanal de desempenho de conteúdo</h1><div class='rule'></div>"
         f"<div class='sub'>Instagram &amp; TikTok — Tatsuo Academy &nbsp;·&nbsp; semana de "
         f"{ini.strftime('%d')} a {fim.strftime('%d')} de {MESES[hoje.month-1]} de {hoje.year} "
         f"&nbsp;·&nbsp; emitido em {hoje.strftime('%d/%m/%Y')}</div></div>"]

    if secs.get("resumo"):
        b.append("<h2><span class='n'>1</span>Resumo</h2><div class='resumo'>")
        b.append(bloco(secs, "resumo")); b.append("</div>")
    b.append(bloco(secs, "objetivo", "Objetivo", 2))
    b.append(bloco(secs, "método", "Método", 3))

    b.append("<div class='pg'></div><h2><span class='n'>4</span>Resultados</h2>")

    # ---------- Tabela 1: painel da conta (fonte: painel do Instagram) ----------
    pc = painel_conta()
    if len(pc) >= 2:
        ant, atu = pc[-2], pc[-1]
        def _rot(r):
            i = datetime.date.fromisoformat(r["janela_ini"]); f = datetime.date.fromisoformat(r["janela_fim"])
            return f"{i.strftime('%d/%m')} a {f.strftime('%d/%m')}"
        LINHAS = [("Visualizações", "visualizacoes"), ("Pessoas alcançadas", "visualizadores"),
                  ("Interações", "interacoes"), ("Seguidores líquidos ganhos", "seguidores_liquidos"),
                  ("Visitas ao perfil", "visitas_perfil"), ("Toques no link da bio", "toques_bio")]
        L = []
        for rot, k in LINHAS:
            va, vb = int(ant.get(k) or 0), int(atu.get(k) or 0)
            var = (vb - va) / va * 100 if va else None
            cls = "" if var is None else (" class='acima'" if var >= 0 else " class='abaixo'")
            txt = "—" if var is None else f"{var:+.0f}%"
            L.append(f"<tr><td class='l'>{rot}</td><td>{num(va)}</td><td>{num(vb)}</td>"
                     f"<td><span{cls}>{txt}</span></td></tr>")
        b.append(tabela(1,
            f"Desempenho da conta no Instagram: semana de {_rot(atu)} contra a de {_rot(ant)}",
            "<b>Coluna de resultado, que ordena a tabela: variação.</b> Esta tabela mede a CONTA, não as "
            "publicações da semana: ela conta o que aconteceu na janela em todo o acervo do perfil, "
            "incluindo visualizações de publicações antigas. <b>Visualizações</b> conta exibições, com "
            "repetição; <b>pessoas alcançadas</b> conta gente distinta. <b>Seguidores líquidos</b> é o "
            "ganho menos as saídas. Os números vêm do painel de Insights do próprio Instagram, "
            "transcritos de captura de tela — <b>a API oficial da Meta não devolve métrica de conta, "
            "nem contagem de seguidores</b>. Por isso esta tabela e as seguintes não se somam: elas "
            "respondem perguntas diferentes e vêm de fontes diferentes.",
            [("métrica da conta", "l"), (_rot(ant), ""), (_rot(atu), ""), ("variação", "")], L))
        b.append(bloco(secs, "leitura conta"))

        # ---------- Tabela 2: leads por origem ----------
        jan = [(ant["janela_ini"], ant["janela_fim"]), (atu["janela_ini"], atu["janela_fim"])]
        pl = painel_leads(jan)
        if pl:
            ROT = {"organico": "Orgânico (Manychat · Instagram DM · Linkbio)",
                   "pago": "Pago (Formulário Meta · Tráfego)",
                   "sem oportunidade": "Sem oportunidade no funil"}
            L = []
            for k in ("organico", "pago", "sem oportunidade"):
                for (i, f), rot in zip(jan, (_rot(ant), _rot(atu))):
                    r = pl[(i, f)][k]
                    pct = (f"{100*r['MQL']/r['n']:.1f}".replace(".", ",") + "%") if r["n"] else "—"
                    cls = " class='destaque'" if k == "organico" else ""
                    L.append(f"<tr{cls}><td class='l'>{ROT[k]}</td><td class='l'>{rot}</td>"
                             f"<td><b>{num(r['n'])}</b></td><td>{num(r['MQL'])}</td>"
                             f"<td>{num(r['Q-MQL'])}</td><td>{num(r['N-MQL'])}</td>"
                             f"<td>{pct}</td><td>{num(r['utm'])}</td></tr>")
            b.append(tabela(2,
                "Contatos novos entrados no CRM por origem e qualificação do comercial, "
                "nas duas mesmas semanas",
                "<b>Coluna de resultado, que ordena a tabela: contatos.</b> <b>Orgânico</b> é o contato "
                "que chegou por conteúdo do perfil; <b>pago</b>, por anúncio. A separação usa a "
                "<b>fonte registrada na oportunidade</b> — o que de fato chega ao time comercial — e não "
                "o campo de origem do contato, que desconhece o canal Instagram DM e por isso subestima "
                "o orgânico. <b>MQL</b> é o contato que o comercial classificou como qualificado, "
                "<b>Q-MQL</b> como quase qualificado e <b>N-MQL</b> como não qualificado; a etiqueta é "
                "posta à mão pelo time de vendas e leva alguns dias, então a semana mais recente tende a "
                "aparecer subqualificada. <b>Sem oportunidade no funil</b> é o contato que entrou no CRM e "
                "nunca virou negócio — não tem origem registrada e não chega ao comercial. "
                "<b>Com identificação no link</b> conta quantos carregavam etiqueta de campanha, que é o "
                "que permite dizer de QUAL publicação o contato veio: é a instrumentação, e hoje ela "
                "cobre uma fração pequena do orgânico.",
                [("origem", "l"), ("período", "l"), ("contatos", ""), ("MQL", ""), ("Q-MQL", ""),
                 ("N-MQL", ""), ("% MQL", ""), ("com identifi-<br>cação no link", "")], L))
            b.append(bloco(secs, "leitura leads"))
        b.append("<div class='pg'></div>")

    # ---------- Tabela 1 ----------
    L = []
    for r in t1:
        cls = " class='destaque'" if (r["mql"] + r["qmql"]) else ""
        rastro = "" if r["rastro"] else "<span class='abaixo'> (link sem etiqueta)</span>"
        L.append(f"<tr{cls}>" + celula_capa(r['pasta'], r['permalink'], r['formato']) +
                 f"<td class='l'>{html.escape(r['pasta'])}"
                 f"<span class='chave'>{html.escape(r['formato'])} · objetivo {html.escape(r['objetivo'])}"
                 f" · palavra do CTA: {html.escape(r['palavra'])}</span></td>"
                 f"<td class='l'><span class='pilar {html.escape(r['pilar'])}'>{html.escape(r['pilar'])}</span></td>"
                 f"<td>{r['dia']}</td><td>{num(r['com'])}</td><td>{num(r['com1k'],2)}</td>"
                 f"<td>{r['disp'] if r['disp'] is not None else '—'}</td>"
                 f"<td>{r['ctr'] or '—'}</td><td>{r['novos']}{rastro}</td><td>{r['reimp']}</td>"
                 f"<td><b>{r['mql']}</b></td><td>{r['qmql']}</td><td>{r['nmql']}</td></tr>")
    b.append(tabela(3,
        "Conversão de audiência em contato comercial, por publicação com chamada para ação "
        f"(carrosséis e reels publicados entre {ini.strftime('%d/%m')} e {fim.strftime('%d/%m')})",
        "<b>Coluna de resultado, que ordena a tabela: leads qualificados (MQL + Q-MQL).</b> "
        "Só entram carrosséis e reels: a publicação de frase não leva chamada para ação por decisão "
        "editorial, portanto não há lead a rastrear nela. <b>Comentários</b> é o total de comentários "
        "na publicação. <b>Disparos</b> é quantas vezes a automação de mensagem direta foi acionada "
        "por alguém que escreveu a palavra do CTA no comentário. <b>Cliques</b> é a proporção desses "
        "disparos em que a pessoa clicou no link enviado. <b>Contatos novos</b> são cadastros inéditos "
        "no CRM atribuídos a esta publicação; <b>reimpactados</b> são contatos que já existiam e "
        "voltaram por ela. <b>MQL</b> (lead qualificado para marketing), <b>Q-MQL</b> (qualificado com "
        "ressalva) e <b>N-MQL</b> (não qualificado) são a classificação dada pelo time comercial. "
        "<b>Comentários por mil</b> é o total de comentários dividido pelo alcance e multiplicado por "
        "mil — é a primeira métrica de leitura do carrossel, porque é o degrau que vira disparo de "
        "automação: medido em 31 de agosto sobre as 19 publicações com automação, a correlação entre "
        "comentário e disparo é de 0,94, contra 0,70 da taxa de interação e 0,51 do alcance. "
        "<b>Pilar</b> é o eixo da metodologia MBV a que a publicação pertence. "
        "A <b>capa</b> é clicável e abre a publicação no Instagram. "
        "<i>Link sem etiqueta</i> significa que a automação funcionou e a pessoa clicou, mas o link não "
        "carregava identificação de origem — o lead existe e o CRM não sabe de onde veio.",
        [("capa", "l"), ("publicação", "l"), ("pilar", "l"), ("publicada em", ""),
         ("comen-<br>tários", ""), ("comen-<br>tários<br>por mil", ""), ("disparos da<br>automação", ""),
         ("cliques no<br>link", ""), ("contatos<br>novos", ""), ("reimpac-<br>tados", ""),
         ("MQL", ""), ("Q-MQL", ""), ("N-MQL", "")], L))
    b.append(bloco(secs, "leitura 1"))

    # ---------- Tabela 2 ----------
    L = []
    for r in t2:
        cls = " class='imaturo'" if r["idade"] < 7 else ""
        errou = r["prev"] != "—" and r["prev"] != r["banda"]
        bc = f" class='{r['banda']}'" if r["banda"] in ("acima", "abaixo") else ""
        L.append(f"<tr{cls}>" + celula_capa(r['pasta'], r['permalink'], r['formato']) +
                 f"<td class='l'>{html.escape(r['pasta'])}"
                 f"<span class='chave'>{r['formato']} · objetivo {html.escape(r['objetivo'])}"
                 f"{' · palavra: ' + html.escape(r['palavra']) if r['palavra'] else ''}</span></td>"
                 f"<td class='l'><span class='pilar {html.escape(r['pilar'])}'>{html.escape(r['pilar'])}</span></td>"
                 f"<td>{r['dia']}</td><td>D+{r['idade']}</td>"
                 f"<td><b>{num(r['com1k'],2)}</b></td><td>{num(r['views'])}</td><td>{num(r['shr'],2)}</td>"
                 f"<td>{num(r['alcance'])}</td>"
                 f"<td>{num(r['taxa'],1)}</td><td class='l'><span{bc}>{r['banda']}</span></td>"
                 f"<td class='l'>{'<span class=errou>'+r['prev']+'</span>' if errou else r['prev']}</td>"
                 f"<td>{num(r['com'])}</td>"
                 f"<td>{r['disp'] if r['disp'] is not None else '—'}</td>"
                 f"<td>{r['leads'] if r['leads'] is not None else '—'}</td>"
                 f"<td class='l'>{r['status']}</td></tr>")
    b.append("<div class='pg'></div>")
    b.append(tabela(4,
        "Desempenho dos carrosséis e reels na ordem de prioridade do objetivo LEAD: "
        "comentário, visualização e compartilhamento, com a taxa de interação e a previsão ao lado "
        "(últimos 14 dias)",
        "<b>Coluna de resultado, que ordena a tabela: comentários por mil.</b> Carrossel e reel com "
        "chamada para ação existem para gerar contato comercial, e o comentário é o degrau que leva até "
        "lá — quem escreve a palavra do CTA aciona a automação. Por isso as três primeiras colunas de "
        "número são, nesta ordem, as métricas que importam para esse objetivo. "
        "<b>Comentários por mil</b> e <b>compartilhamentos por mil</b> são a contagem dividida pelo "
        "alcance e multiplicada por mil, o que põe na mesma escala uma publicação vista por 2 mil "
        "pessoas e outra vista por 200 mil. <b>Visualizações</b> é quantas vezes a publicação foi "
        "exibida, contando repetições — diferente de alcance, que conta pessoas distintas. "
        "<b>Taxa de interação</b> soma curtidas, comentários, salvamentos e compartilhamentos por mil "
        "alcançados: é a nota de qualidade editorial da peça, e continua sendo <b>a única métrica que "
        "conta no placar de previsão</b>. <b>Faixa</b> classifica essa taxa contra os últimos 90 dias "
        "do próprio perfil, em três terços de igual tamanho — e a régua é diferente para cada formato: "
        f"carrossel <i>abaixo</i> de {T.BANDAS['carrossel'][0]:.1f} e <i>acima</i> de {T.BANDAS['carrossel'][1]:.1f}; "
        f"reel <i>abaixo</i> de {T.BANDAS['reel'][0]:.1f} e <i>acima</i> de {T.BANDAS['reel'][1]:.1f}. "
        "<b>Previsto</b> é a faixa que a máquina apostou antes de publicar; em vermelho quando não "
        "bateu com a que saiu. <b>Pilar</b> é o eixo da metodologia MBV. A <b>capa</b> é clicável e "
        "abre a publicação no Instagram. <b>Situação</b>: o número só vira oficial em D+7 — antes "
        "disso a publicação ainda está crescendo e aparece em cinza.",
        [("capa", "l"), ("publicação", "l"), ("pilar", "l"), ("publicada em", ""), ("idade", ""),
         ("1ª · comen-<br>tários<br>por mil", ""), ("2ª · visua-<br>lizações", ""),
         ("3ª · compart.<br>por mil", ""),
         ("alcance", ""), ("taxa de<br>interação<br>(por mil)", ""), ("faixa", "l"),
         ("previsto", "l"), ("comen-<br>tários", ""),
         ("disparos", ""), ("leads", ""), ("situação", "l")], L))
    b.append(bloco(secs, "leitura 2"))

    # ---------- Tabela 3 ----------
    L = []
    for r in t3:
        cls = " class='imaturo'" if r["idade"] < 7 else ""
        errou = r["prev"] != "—" and r["prev"] != r["banda"]
        bc = f" class='{r['banda']}'" if r["banda"] in ("acima", "abaixo") else ""
        L.append(f"<tr{cls}>" + celula_capa(r['pasta'], r['permalink'], 'frase') +
                 f"<td class='l'>{html.escape(r['pasta'])}"
                 f"<span class='chave'>frase · objetivo {html.escape(r['objetivo'])}</span></td>"
                 f"<td class='l'><span class='pilar {html.escape(r['pilar'])}'>{html.escape(r['pilar'])}</span></td>"
                 f"<td>{r['dia']}</td><td>D+{r['idade']}</td>"
                 f"<td><b>{num(r['alcance'])}</b></td><td>{num(r['taxa'],2)}</td>"
                 f"<td>{num(r['follows'])}</td><td>{num(r['visitas'])}</td>"
                 f"<td>{num(r['shares'])}</td>"
                 f"<td class='l'><span{bc}>{r['banda']}</span></td>"
                 f"<td class='l'>{'<span class=errou>'+r['prev']+'</span>' if errou else r['prev']}</td>"
                 f"<td class='l'>{r['status']}</td></tr>")
    b.append(tabela(5,
        "Desempenho das publicações de frase na ordem de prioridade do objetivo ALCANCE: "
        "alcance, intensidade de compartilhamento e seguidores ganhos (últimos 14 dias)",
        "<b>Coluna de resultado, que ordena a tabela: alcance.</b> A frase não leva chamada para ação "
        "por decisão editorial — a função dela é sair da audiência já conquistada e ser vista por gente "
        "nova, não captar contato. Por isso ela é avaliada primeiro pelo tamanho do público que atingiu. "
        "<b>Compartilhamentos por mil</b> é o número de compartilhamentos dividido pelo alcance e "
        "multiplicado por mil: mede a intensidade com que quem viu decidiu repassar, independentemente "
        "de quantas pessoas viram. É essa taxa, e não o alcance, que a máquina tenta prever — o alcance "
        "depende da distribuição do algoritmo e não é previsível com as variáveis conhecidas antes de "
        "publicar. <b>Seguidores ganhos</b> e <b>visitas ao perfil</b> são contabilizados pelo próprio "
        "Instagram como decorrentes daquela publicação, e medem o ativo que a frase constrói: público "
        "novo dentro do perfil. São reportados aqui pela primeira vez. "
        f"<b>Faixa</b>: <i>abaixo</i> de {T.BANDAS['frase'][0]:.2f}, <i>mediana</i> até "
        f"{T.BANDAS['frase'][1]:.2f}, <i>acima</i> disso. "
        "Comentário não entra: publicação de frase quase não gera. A <b>capa</b> é clicável e abre a "
        "publicação no Instagram.",
        [("capa", "l"), ("publicação", "l"), ("pilar", "l"), ("publicada em", ""), ("idade", ""),
         ("1ª ·<br>alcance", ""), ("2ª · compart.<br>por mil", ""), ("3ª · seguidores<br>ganhos", ""),
         ("visitas ao<br>perfil", ""), ("compartilha-<br>mentos", ""),
         ("faixa", "l"), ("previsto", "l"), ("situação", "l")], L))
    b.append(bloco(secs, "leitura 3"))

    b.append("<div class='pg'></div>")
    b.append(bloco(secs, "discussão", "Discussão", 5))
    b.append(bloco(secs, "conclusão", "Conclusão — o que muda a partir de hoje", 6))
    b.append(bloco(secs, "limitações", "Limitações", 7))

    pull = T.carregar("desempenho.json").get("pulled_at", "?")
    b.append(f"<div class='rod'>Gerado por <b>scripts/analise/briefing_pdf.py</b>. Fontes: base de "
             f"métricas do Instagram (<i>desempenho.json</i>, extraída em {pull}), registro de fichas "
             f"editoriais (<i>registro-posts.csv</i>), base de contatos do CRM GoHighLevel "
             f"(<i>leads.json</i>), leitura do painel Manychat (<i>_disparos.json</i>) e lista de "
             f"publicações descartadas (<i>_descartados.csv</i>). Nenhuma chamada de API na geração "
             f"do documento.</div>")
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style><body>" + "".join(b) + "</body>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--texto"); ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--saida", default=None)
    ap.add_argument("--ate", default=None,
                    help="Data de FIM da janela (YYYY-MM-DD). Sem isso, o relatorio fecha hoje — "
                         "e prosa e tabela podem acabar em periodos diferentes.")
    a = ap.parse_args()
    if a.ate:
        T.HOJE = datetime.date.fromisoformat(a.ate)   # alinha TODAS as janelas do documento
    t1, t2, t3 = coletar(a.dias)
    doc = render(t1, t2, t3, secoes(a.texto), T.HOJE, a.dias)
    saida = a.saida or os.path.join(RAIZ, "conteudo", "analise",
                                    f"relatorio-semanal-{T.HOJE.isoformat()}.pdf")
    tmp = saida.replace(".pdf", ".html")
    open(tmp, "w", encoding="utf-8").write(doc)
    js = """
const {chromium} = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2], {waitUntil:'networkidle'});
  await p.pdf({path: process.argv[3], format:'A4', landscape:true, printBackground:true,
               displayHeaderFooter:true, headerTemplate:'<span></span>',
               footerTemplate:'<div style="width:100%;font-size:7px;color:#999;padding:0 12mm;'
                 + 'font-family:Helvetica;display:flex;justify-content:space-between">'
                 + '<span>Tatsuo Academy — relatório semanal de desempenho de conteúdo</span>'
                 + '<span><span class="pageNumber"></span> de <span class="totalPages"></span></span></div>',
               margin:{top:'13mm',bottom:'14mm',left:'12mm',right:'12mm'}});
  await b.close();
})();
"""
    jsf = os.path.join(RAIZ, ".briefing_pdf.js")
    open(jsf, "w").write(js)
    subprocess.run(["node", jsf, tmp, saida], cwd=RAIZ, check=True)
    os.remove(jsf); os.remove(tmp)
    print(saida)


if __name__ == "__main__":
    main()
