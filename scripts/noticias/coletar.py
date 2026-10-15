#!/usr/bin/env python3
"""
coletar.py — coleta as pautas quentes do dia pros nichos empresarial e médico.

Lê feeds públicos (Google Notícias, Google Trends e os próprios veículos), junta as
matérias que falam do mesmo assunto e ordena cada assunto pelo calor:
- quantos veículos diferentes cobriram
- se está em destaque no Google Notícias (topo, Negócios, Brasil, Saúde)
- se o termo está em alta nas buscas do Google Trends
- quão recente é

Zero chave de API e só biblioteca padrão (roda no python3 do sistema e no launchd).
O ranking é só a peneira: quem escolhe as 10 de cada nicho é a skill /pautas.

Uso:
  python3 scripts/noticias/coletar.py              # janela de 30h, lista 40 assuntos por nicho
  python3 scripts/noticias/coletar.py --horas 36   # janela maior (segunda de manhã, por exemplo)
  python3 scripts/noticias/coletar.py --top 60     # lista mais candidatos por nicho

Saída: conteudo/noticias/_coleta/AAAA-MM-DD.json (tudo) + lista compacta no terminal.
Rodar de novo no mesmo dia substitui o arquivo do dia pela leitura mais fresca.
"""
import argparse, html, json, math, os, re, sys, unicodedata, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SAIDA = os.path.join(RAIZ, "conteudo", "noticias", "_coleta")
BRT = timezone(timedelta(hours=-3))
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
GN = "hl=pt-BR&gl=BR&ceid=BR:pt-419"


def gn_busca(q):
    return "https://news.google.com/rss/search?q=" + urllib.parse.quote(q + " when:1d") + "&" + GN


# nicho: empresarial | medico | geral (geral = as palavras do título decidem)
# destaque: vitrine editorial do Google (estar nela já é sinal de calor)
# busca: resultado de busca por palavra; o nicho só vale se o título confirmar
FONTES = [
    # vitrines do Google Notícias
    dict(id="gn_topo", nicho="geral", destaque=True, url="https://news.google.com/rss?" + GN),
    dict(id="gn_negocios", nicho="empresarial", destaque=True,
         url="https://news.google.com/rss/headlines/section/topic/BUSINESS?" + GN),
    dict(id="gn_brasil", nicho="geral", destaque=True,
         url="https://news.google.com/rss/headlines/section/topic/NATION?" + GN),
    dict(id="gn_saude", nicho="medico", destaque=True,
         url="https://news.google.com/rss/headlines/section/topic/HEALTH?" + GN),
    # buscas do Google Notícias no último dia: cobrem os temas que a vitrine não pega
    dict(id="gn_empresas", nicho="empresarial", busca=True, url=gn_busca("empresas OR empresários OR empresário")),
    dict(id="gn_governo", nicho="empresarial", busca=True,
         url=gn_busca('governo federal OR "medida provisória" OR Congresso aprova')),
    dict(id="gn_impostos", nicho="empresarial", busca=True,
         url=gn_busca('imposto OR "Receita Federal" OR "reforma tributária" OR tributação')),
    dict(id="gn_juros", nicho="empresarial", busca=True,
         url=gn_busca("Selic OR juros OR inflação OR crédito OR inadimplência")),
    dict(id="gn_trabalho", nicho="empresarial", busca=True,
         url=gn_busca('CLT OR trabalhista OR "escala 6x1" OR emprego OR demissões')),
    dict(id="gn_quebra", nicho="empresarial", busca=True,
         url=gn_busca('"recuperação judicial" OR falência OR varejo OR "pequenas empresas"')),
    dict(id="gn_medicos", nicho="medico", busca=True, url=gn_busca("médicos OR médico OR medicina")),
    dict(id="gn_cfm", nicho="medico", busca=True,
         url=gn_busca('CFM OR "Conselho Federal de Medicina" OR CRM OR "residência médica"')),
    dict(id="gn_planos", nicho="medico", busca=True,
         url=gn_busca('"planos de saúde" OR "plano de saúde" OR ANS OR operadoras')),
    dict(id="gn_clinicas", nicho="medico", busca=True, url=gn_busca("clínicas OR clínica OR consultório OR hospitais")),
    dict(id="gn_sus", nicho="medico", busca=True, url=gn_busca('SUS OR "Ministério da Saúde" OR Anvisa')),
    # buscas em alta no Brasil
    dict(id="trends", nicho="geral", tipo="trends", url="https://trends.google.com/trending/rss?geo=BR"),
    # veículos (link direto, sem passar pelo Google)
    dict(id="valor", nicho="empresarial", url="https://valor.globo.com/rss/valor"),
    dict(id="folha_mercado", nicho="empresarial", url="https://feeds.folha.uol.com.br/mercado/rss091.xml"),
    dict(id="folha_poder", nicho="geral", url="https://feeds.folha.uol.com.br/poder/rss091.xml"),
    dict(id="g1_economia", nicho="empresarial", url="https://g1.globo.com/rss/g1/economia/"),
    dict(id="estadao_economia", nicho="empresarial",
         url="https://www.estadao.com.br/arc/outboundfeeds/feeds/rss/sections/economia/"),
    dict(id="infomoney", nicho="empresarial", url="https://www.infomoney.com.br/feed/"),
    dict(id="exame", nicho="empresarial", url="https://exame.com/feed/"),
    dict(id="uol_economia", nicho="empresarial", url="https://rss.uol.com.br/feed/economia.xml"),
    dict(id="braziljournal", nicho="empresarial", url="https://braziljournal.com/feed/"),
    dict(id="neofeed", nicho="empresarial", url="https://neofeed.com.br/feed/"),
    dict(id="poder360", nicho="geral", url="https://www.poder360.com.br/feed/"),
    dict(id="metropoles", nicho="geral", url="https://www.metropoles.com/feed"),
    dict(id="jota", nicho="geral", url="https://www.jota.info/feed"),
    dict(id="abr_economia", nicho="empresarial", url="https://agenciabrasil.ebc.com.br/rss/economia/feed.xml"),
    dict(id="abr_politica", nicho="geral", url="https://agenciabrasil.ebc.com.br/rss/politica/feed.xml"),
    dict(id="folha_saude", nicho="medico", url="https://feeds.folha.uol.com.br/equilibrioesaude/rss091.xml"),
    dict(id="veja_saude", nicho="medico", url="https://saude.abril.com.br/feed/"),
    dict(id="drauzio", nicho="medico", url="https://drauziovarella.uol.com.br/feed/"),
    dict(id="medicinasa", nicho="medico", url="https://medicinasa.com.br/feed/"),
    dict(id="futurodasaude", nicho="medico", url="https://futurodasaude.com.br/feed/"),
    dict(id="saudebusiness", nicho="medico", url="https://saudebusiness.com/feed/"),
    dict(id="hospitaisbrasil", nicho="medico", url="https://portalhospitaisbrasil.com.br/feed/"),
    dict(id="abr_saude", nicho="medico", url="https://agenciabrasil.ebc.com.br/rss/saude/feed.xml"),
    dict(id="estadao_saude", nicho="medico",
         url="https://www.estadao.com.br/arc/outboundfeeds/feeds/rss/sections/saude/"),
]

# nome de cada veículo direto (o do Google vem na própria matéria)
VEICULO = {
    "valor": "Valor Econômico", "folha_mercado": "Folha", "folha_poder": "Folha", "g1_economia": "g1",
    "estadao_economia": "Estadão", "infomoney": "InfoMoney", "exame": "Exame", "uol_economia": "UOL",
    "braziljournal": "Brazil Journal", "neofeed": "NeoFeed", "poder360": "Poder360", "metropoles": "Metrópoles",
    "jota": "JOTA", "abr_economia": "Agência Brasil", "abr_politica": "Agência Brasil", "folha_saude": "Folha",
    "veja_saude": "Veja Saúde", "drauzio": "Portal Drauzio Varella", "medicinasa": "Medicina S/A",
    "futurodasaude": "Futuro da Saúde", "saudebusiness": "Saúde Business", "hospitaisbrasil": "Hospitais Brasil",
    "abr_saude": "Agência Brasil", "estadao_saude": "Estadão",
}

STOP = set("""
a o as os um uma uns umas de da do das dos em na no nas nos por para pra pelo pela pelos pelas com sem sob sobre
entre ate apos e ou que se ao aos esta estao ser foi sao tem vai vao diz dizem afirma afirmam segundo como mais menos
muito ja nao sim seu sua seus suas ele ela eles elas isso esse essa este quem qual quais quando onde porque contra
depois antes ano anos dia dias hoje ontem amanha semana mes novo nova novos novas pode podem deve devem fazer faz
veja saiba entenda video fotos vivo brasil brasileiro brasileira brasileiros vez vezes ter sera
nesta neste nessa nesse feira segunda terca quarta quinta sexta sabado domingo
""".split())


def raiz(t):
    """Plural pro singular, o bastante pra 'canetas' e 'caneta' virarem a mesma palavra."""
    if len(t) <= 3:
        return t
    for suf, rep in (("oes", "ao"), ("aes", "ao"), ("ais", "al"), ("eis", "el"), ("res", "r"), ("zes", "z"),
                     ("ns", "m")):
        if t.endswith(suf) and len(t) > len(suf) + 2:
            return t[: -len(suf)] + rep
    return t[:-1] if t.endswith("s") and not t.endswith("ss") else t


def sem_acento(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def tokens(s):
    return {raiz(t) for t in re.findall(r"[a-z0-9]{3,}", sem_acento(s)) if t not in STOP}


# o que puxa pro nicho médico (prefixo) e o que puxa pro empresarial: economia, empresa e governo
MEDICO_PREF = ("medic", "saude", "hospita", "clinic", "pacient", "vacin", "doenc", "cancer", "dengue", "remedi",
               "farmac", "enferm", "cirurg", "consultori", "odont", "dentist", "psiquiatr", "obesid", "epidem",
               "surto", "virus", "infecc", "diabet", "cardio", "oncolog", "pediatr", "gestant", "tratament",
               "terapi", "diagnos", "sanitari", "telemedic", "ozempic", "mounjaro", "semaglut", "tirzepat")
MEDICO_TOKEN = {raiz(t) for t in ("sus", "ans", "cfm", "crm", "cremesp", "anvisa", "hapvida", "unimed", "amil", "dasa",
                                  "fleury", "sulamerica", "fiocruz", "butantan", "oms", "gripe", "covid", "sarampo")}
NAO_MEDICO = {raiz(t) for t in ("pet", "pets", "veterinario", "veterinaria", "cachorro", "gato", "animais")}
EMPRESA_PREF = ("empres", "negoci", "econom", "mercad", "financ", "banc", "credit", "juro", "selic", "copom",
                "inflac", "ipca", "impost", "tribut", "receita", "fiscal", "arrecad", "orcament", "divida",
                "deficit", "governo", "ministr", "planalto", "congress", "senad", "camara", "deputad", "stf",
                "supremo", "decret", "sancion", "regulament", "proib", "restric", "fiscaliz", "multa", "tarifa",
                "subsidi", "salari", "empreg", "desempreg", "trabalh", "pib", "dolar", "cambio", "bolsa",
                "ibovespa", "lucr", "prejuiz", "fatur", "vend", "varej", "industr", "comerci", "servic", "consum",
                "preco", "combust", "gasolin", "diesel", "petrol", "energia", "eletric", "privatiz", "falenc",
                "recuperac", "invest", "startup", "aquisic", "apost", "aposentad", "previdenc", "taxa", "agro",
                "export", "import", "frete", "logist", "imobil", "aluguel", "constru", "franquia", "sebrae",
                "executiv", "demiss", "greve", "sindic", "escala", "jornada", "inteligenc", "tecnolog", "chatgpt",
                "openai", "abono", "pasep", "cnpj", "acionist", "dividend", "banco")
EMPRESA_TOKEN = {raiz(t) for t in ("lei", "pix", "mei", "ipo", "pib", "clt", "inss", "fgts", "pis", "6x1", "bets",
                                   "ceo", "bndes", "cvm", "copom", "fed")}

# sinais de pauta fora do perfil: rebaixam no ranking, não excluem (a curadoria decide)
SINAIS = {k: {raiz(t) for t in v.split()} for k, v in {
    "esporte": "futebol brasileirao libertadores sulamericana gol gols flamengo corinthians palmeiras vasco botafogo "
               "fluminense gremio neymar ancelotti selecao escalacao campeonato rodada placar ufc nba formula tenista",
    "celebridade": "bbb novela reality cantor cantora atriz ator famosos fofoca namoro namorada namorado separacao "
                   "influenciadora affair",
    "crime": "preso presa assassinato homicidio tiroteio sequestro estupro feminicidio chacina baleado esfaqueado "
             "latrocinio",
    "loteria": "lotofacil mega sena quina lotomania timemania loteria dupla",
    "eleicao": "quaest datafolha atlasintel ipec nexus eleitor eleitores eleicao eleicoes candidato candidata "
               "candidatos candidatura chapa turno debate urna urnas tse votos voto campanha palanque comicio "
               "presidencial presidenciavel presidenciaveis intencao pleito",
}.items()}

# palavras que aparecem em muito assunto todo santo dia: não contam como tema do dia
PERENE = {raiz(t) for t in """governo lula trump presidente mercado empresa empresas preco precos milhoes milhao
bilhoes bilhao mil reais estado estados sao paulo rio janeiro federal nacional caso casos pessoa pessoas morte morre
saude medico medicos brasil mundo pais cidade prefeitura policia justica anuncia aponta revela mostra alta queda
sobe cai partir outubro setembro segunda terca quarta quinta sexta sabado domingo primeiro primeira 2026 2027 100
nesta neste nessa feira publica publico abre tipo rede adulto perda pesquisa eua tratamento doenca paciente hora
agora entrevista afirma apos contra
""".split()}

# preferência de link: veículo grande com link direto primeiro
PRIORIDADE = ["g1", "Folha", "Valor Econômico", "Estadão", "UOL", "InfoMoney", "Exame", "Poder360", "Agência Brasil",
              "JOTA", "CNN Brasil", "O Globo", "Brazil Journal", "NeoFeed", "Metrópoles", "Veja Saúde",
              "Futuro da Saúde", "Medicina S/A", "Saúde Business", "Portal Drauzio Varella", "Hospitais Brasil"]

MESES_PT = {"fev": "Feb", "abr": "Apr", "mai": "May", "ago": "Aug", "set": "Sep", "out": "Oct", "dez": "Dec"}
DIAS_PT = {"seg": "Mon", "ter": "Tue", "qua": "Wed", "qui": "Thu", "sex": "Fri", "sab": "Sat", "sáb": "Sat",
           "dom": "Sun"}


def limpa(s):
    s = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", s or "", flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", " ", html.unescape(s)))
    return re.sub(r"\s+", " ", s).strip()


def tag(bloco, nome):
    m = re.search(r"<%s(?:\s[^>]*)?>(.*?)</%s>" % (nome, nome), bloco, re.S)
    return m.group(1) if m else ""


def data(s):
    s = limpa(s)
    if not s:
        return None
    try:
        return parsedate_to_datetime(s).astimezone(timezone.utc)
    except (TypeError, ValueError, IndexError):
        pass
    # feed com dia e mês em português (UOL: "Seg, 28 Set 2026 17:31:54 -0300")
    partes = s.replace(",", "").split()
    if len(partes) >= 5:
        partes = [DIAS_PT.get(p.lower(), MESES_PT.get(p.lower(), p)) for p in partes]
        try:
            return parsedate_to_datetime(" ".join(partes)).astimezone(timezone.utc)
        except (TypeError, ValueError, IndexError):
            pass
    m = re.match(r"(\d{4}-\d{2}-\d{2})[T ](\d{2}:\d{2}:\d{2})(?:\.\d+)?(Z|[+-]\d{2}:?\d{2})?", s)
    if m:
        dt = datetime.fromisoformat(m.group(1) + "T" + m.group(2))
        tz = m.group(3)
        if not tz:
            dt = dt.replace(tzinfo=BRT)  # veículo brasileiro sem fuso = horário de Brasília
        elif tz == "Z":
            dt = dt.replace(tzinfo=timezone.utc)
        else:
            tz = tz.replace(":", "")
            dt = dt.replace(tzinfo=timezone(timedelta(hours=int(tz[:3]), minutes=int(tz[0] + tz[3:]))))
        return dt.astimezone(timezone.utc)
    return None


def baixa(fonte):
    r = urllib.request.Request(fonte["url"], headers={
        "User-Agent": UA, "Accept": "application/rss+xml, application/xml, text/xml, */*"})
    with urllib.request.urlopen(r, timeout=25) as resp:
        bruto = resp.read()
        # a Folha manda ISO-8859-1: sem isso o "Saúde" vira "Sa�de"
        cs = resp.headers.get_content_charset()
    m = re.search(rb'encoding=["\']([\w-]+)["\']', bruto[:200])
    cs = (m.group(1).decode() if m else None) or cs or "utf-8"
    try:
        return bruto.decode(cs, "replace")
    except LookupError:
        return bruto.decode("utf-8", "replace")


def titulo_limpo(t, veiculo):
    if veiculo and t.endswith(" - " + veiculo):
        t = t[: -len(veiculo) - 3]
    # padrão Folha no Google: "Título - 28/09/2026 - Equilíbrio e Saúde"
    return re.sub(r"\s-\s\d{2}/\d{2}/\d{4}\s-\s.*$", "", t).strip()


def le_feed(fonte, corpo):
    """Devolve (matérias, tendências). Parser por regex: feed com XML torto não derruba a coleta."""
    materias, tendencias = [], []
    blocos = re.findall(r"<item[\s>].*?</item>", corpo, re.S) or re.findall(r"<entry[\s>].*?</entry>", corpo, re.S)
    base = dict(fonte=fonte["id"], nicho=fonte["nicho"], busca=bool(fonte.get("busca")),
                destaque=bool(fonte.get("destaque")))
    if fonte.get("tipo") == "trends":
        for b in blocos:
            termo = limpa(tag(b, "title"))
            buscas = int(re.sub(r"\D", "", tag(b, "ht:approx_traffic")) or 0)
            quando = data(tag(b, "pubDate"))
            tendencias.append(dict(termo=termo, buscas=buscas))
            for n in re.findall(r"<ht:news_item>(.*?)</ht:news_item>", b, re.S):
                materias.append(dict(base, titulo=limpa(tag(n, "ht:news_item_title")),
                                     link=limpa(tag(n, "ht:news_item_url")), veiculo=limpa(tag(n, "ht:news_item_source")),
                                     quando=quando, resumo="", relacionadas=1, outros_veiculos=[],
                                     tendencia=dict(termo=termo, buscas=buscas)))
        return materias, tendencias
    for b in blocos:
        titulo = limpa(tag(b, "title"))
        link = limpa(tag(b, "link")) or (re.search(r'<link[^>]*href="([^"]+)"', b) or [None, ""])[1]
        quando = data(tag(b, "pubDate") or tag(b, "dc:date") or tag(b, "updated") or tag(b, "published"))
        desc = tag(b, "description") or tag(b, "summary") or tag(b, "content:encoded")
        veiculo, relacionadas, outros, resumo = VEICULO.get(fonte["id"], ""), 1, [], ""
        if fonte["id"].startswith("gn_"):
            veiculo = limpa(tag(b, "source"))
            lista = html.unescape(desc)
            relacionadas = max(1, len(re.findall(r"<li>", lista)))
            outros = [limpa(v) for v in re.findall(r"<font[^>]*>(.*?)</font>", lista)]
        else:
            resumo = limpa(desc)[:320]
        titulo = titulo_limpo(titulo, veiculo)
        if "redir.folha.com.br" in link and "*http" in link:
            link = link.split("*", 1)[1]  # a Folha embrulha o link num redirecionador
        if titulo and link:
            materias.append(dict(base, titulo=titulo, link=link, veiculo=veiculo, quando=quando, resumo=resumo,
                                 relacionadas=relacionadas, outros_veiculos=outros, tendencia=None))
    return materias, tendencias


def nichos_de(tk, materias):
    medico = (bool(tk & MEDICO_TOKEN) or any(t.startswith(MEDICO_PREF) for t in tk)) and not (tk & NAO_MEDICO)
    empresa = bool(tk & EMPRESA_TOKEN) or any(t.startswith(EMPRESA_PREF) for t in tk)
    ns = {m["nicho"] for m in materias if m["nicho"] != "geral" and not m["busca"]}
    if medico:
        ns.add("medico")
    if empresa:
        ns.add("empresarial")
    return sorted(ns) or ["geral"]


def agrupa(materias):
    """Junta matérias do mesmo assunto: palavras em comum pesadas pela raridade no dia (IDF)."""
    for m in materias:
        m["tk"] = tokens(m["titulo"])
    n = len(materias) or 1
    df = {}
    for m in materias:
        for t in m["tk"]:
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log(n / c) for t, c in df.items()}

    def peso(ts):
        return sum(idf.get(t, 0) for t in ts)

    def sim(a, b):
        comum = a & b
        if len(comum) < 2:
            return 0.0
        return peso(comum) / max(1e-9, min(peso(a), peso(b)))

    # vitrine do Google primeiro: o título do assunto sai de quem deu destaque
    grupos = []
    for m in sorted(materias, key=lambda m: (not m["destaque"], m["busca"])):
        if not m["tk"]:
            continue
        melhor, melhor_sim = None, 0.0
        for g in grupos:
            s = max(sim(m["tk"], o["tk"]) for o in g["materias"][:3])
            if s > melhor_sim:
                melhor, melhor_sim = g, s
        if melhor is not None and melhor_sim >= 0.45:
            melhor["materias"].append(m)
        else:
            grupos.append(dict(materias=[m]))
    return grupos


def resume_grupo(g, tendencias, agora):
    ms = g["materias"]
    veiculos = set()
    for m in ms:
        if m["veiculo"]:
            veiculos.add(m["veiculo"])
        veiculos.update(v for v in m["outros_veiculos"] if v)
    todos_tk = set().union(*(m["tk"] for m in ms))
    # tendência: todas as palavras do termo buscado aparecem no assunto
    tend = next((m["tendencia"] for m in ms if m["tendencia"]), None)
    if not tend:
        for t in tendencias:
            tt = tokens(t["termo"])
            if tt and tt <= todos_tk:
                tend = t
                break
    datas = [m["quando"] for m in ms if m["quando"]]
    horas = max(0.0, (agora - max(datas)).total_seconds() / 3600) if datas else 99.0
    destaque = any(m["destaque"] for m in ms)
    relacionadas = max(m["relacionadas"] for m in ms)
    sinais = sorted(k for k, pal in SINAIS.items() if todos_tk & pal)
    calor = 3.0 * math.log2(1 + len(veiculos)) + 1.0 * math.log2(1 + relacionadas) + (2.0 if destaque else 0.0)
    if tend:
        calor += 1.5 * (1 + math.log10(max(tend["buscas"], 1000) / 1000))
    calor += 1.5 * math.exp(-horas / 12)
    calor -= sum(2.0 if s == "eleicao" else 3.0 for s in sinais)

    def rank(m):
        direto = not m["link"].startswith("https://news.google.com")
        pos = PRIORIDADE.index(m["veiculo"]) if m["veiculo"] in PRIORIDADE else len(PRIORIDADE)
        return (not direto, pos, -(m["quando"] or agora).timestamp())
    ordenadas = sorted(ms, key=rank)
    return dict(
        tk=sorted(todos_tk),
        titulo=sorted(ms, key=lambda m: (not m["destaque"], rank(m)))[0]["titulo"],
        link=ordenadas[0]["link"], veiculo=ordenadas[0]["veiculo"],
        nichos=nichos_de(todos_tk, ms), calor=round(calor, 2), n_veiculos=len(veiculos),
        veiculos=sorted(veiculos), destaque_google=destaque, google_relacionadas=relacionadas,
        tendencia=tend, horas=round(horas, 1), sinais=sinais,
        resumo=next((m["resumo"] for m in ordenadas if m["resumo"]), ""),
        materias=[dict(titulo=m["titulo"], link=m["link"], veiculo=m["veiculo"],
                       hora=m["quando"].astimezone(BRT).strftime("%d/%m %H:%M") if m["quando"] else "")
                  for m in ordenadas[:6]],
    )


def linha_sinais(p):
    s = ["%d veículo%s" % (p["n_veiculos"], "" if p["n_veiculos"] == 1 else "s")]
    if p["destaque_google"]:
        s.append("destaque Google")
    if p["tendencia"]:
        buscas = "{:,}".format(p["tendencia"]["buscas"]).replace(",", ".")
        s.append('Trends "%s" %s+ buscas' % (p["tendencia"]["termo"], buscas))
    s.append("sem data" if p["horas"] >= 99 else ("agora" if p["horas"] < 1 else "há %.0fh" % p["horas"]))
    if p["sinais"]:
        s.append("[" + ", ".join(p["sinais"]) + "]")
    return " · ".join(s)


def temas_do_dia(pautas, minimo=3):
    """Tema quente se espalha em vários assuntos (a MP das bets, o influenciador, a pesquisa):
    conta em quantos assuntos com 2+ veículos cada palavra aparece, por nicho."""
    temas = {}
    for nicho in ("empresarial", "medico"):
        cont = {}
        for p in pautas:
            if nicho in p["nichos"] and p["n_veiculos"] >= 2:
                for t in p["tk"]:
                    if t not in PERENE and not t.isdigit():
                        cont.setdefault(t, []).append(p["id"])
        temas[nicho] = sorted(([t, ids] for t, ids in cont.items() if len(ids) >= minimo),
                              key=lambda x: -len(x[1]))[:15]
    return temas


def _tenta(fn, arg):
    try:
        return fn(arg), None
    except Exception as e:  # uma fonte fora do ar não derruba as outras
        return None, str(e)[:80]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--horas", type=float, default=30, help="janela de recência (padrão 30h)")
    ap.add_argument("--top", type=int, default=40, help="assuntos listados por nicho (padrão 40)")
    args = ap.parse_args()

    agora = datetime.now(timezone.utc)
    corte = agora - timedelta(hours=args.horas)
    materias, tendencias, ok, erro = [], [], [], {}
    with ThreadPoolExecutor(12) as ex:
        baixados = list(ex.map(lambda f: (f, _tenta(baixa, f)), FONTES))
    for f, (corpo, err) in baixados:
        if err:
            erro[f["id"]] = err
            continue
        ms, ts = le_feed(f, corpo)
        if not ms and not ts:
            erro[f["id"]] = "feed sem itens"
            continue
        ok.append(f["id"])
        tendencias.extend(ts)
        materias.extend(m for m in ms if m["quando"] and m["quando"] >= corte)

    pautas = sorted((resume_grupo(g, tendencias, agora) for g in agrupa(materias)), key=lambda p: -p["calor"])
    for i, p in enumerate(pautas, 1):
        p["id"] = i
    temas = temas_do_dia(pautas)
    for p in pautas:
        del p["tk"]

    os.makedirs(SAIDA, exist_ok=True)
    caminho = os.path.join(SAIDA, agora.astimezone(BRT).strftime("%Y-%m-%d") + ".json")
    with open(caminho, "w", encoding="utf-8") as fh:
        json.dump(dict(gerado_em=agora.astimezone(BRT).strftime("%Y-%m-%d %H:%M"), janela_horas=args.horas,
                       fontes_ok=ok, fontes_erro=erro, n_materias=len(materias), tendencias=tendencias,
                       temas=temas, pautas=pautas), fh, ensure_ascii=False, indent=1)

    print("Coleta %s · %d matérias em %d assuntos · %d/%d fontes ok" % (
        agora.astimezone(BRT).strftime("%d/%m %H:%M"), len(materias), len(pautas), len(ok), len(FONTES)))
    if erro:
        print("Fontes com falha: " + ", ".join("%s (%s)" % (k, v) for k, v in erro.items()))
    if tendencias:
        print("Em alta no Google: " + " · ".join("%s (%s+)" % (t["termo"], t["buscas"]) for t in tendencias))
    for nicho, nome, top in (("empresarial", "EMPRESARIAL", args.top), ("medico", "MÉDICO", args.top),
                             ("geral", "GERAL (fora dos dois nichos, só o que estourou)", 15)):
        lista = [p for p in pautas if nicho in p["nichos"]]
        print("\n== %s · %d assuntos (mostrando %d) ==" % (nome, len(lista), min(top, len(lista))))
        if temas.get(nicho):
            print("Temas espalhados em vários assuntos: " + " · ".join(
                "%s (%d: %s)" % (t, len(ids), " ".join("#%d" % i for i in ids[:8])) for t, ids in temas[nicho]))
        for p in lista[:top]:
            print("#%d  calor %.1f · %s" % (p["id"], p["calor"], linha_sinais(p)))
            print("    %s (%s)" % (p["titulo"], p["veiculo"] or "Google Notícias"))
    print("\nArquivo: " + os.path.relpath(caminho, RAIZ))


if __name__ == "__main__":
    sys.exit(main())
