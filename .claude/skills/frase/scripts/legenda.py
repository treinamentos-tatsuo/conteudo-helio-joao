#!/usr/bin/env python3
"""Confere a legenda de um post de frase. Zero API: só lê arquivos locais.

Uso, sempre da raiz do projeto:
  python3 .claude/skills/frase/scripts/legenda.py contar conteudo/carrosseis/<N>_<nome>/legenda.txt
      Conta CARACTERES (não bytes: acento conta 1), confere a parede de 2.200 do Instagram, se termina
      no CTA fixo literal, e aponta construções proibidas e mistura de "te" com "você" pra revisar.
  python3 .claude/skills/frase/scripts/legenda.py publicada conteudo/carrosseis/<N>_<nome>
      Compara o legenda.txt com a legenda que FOI AO AR (caption_full do conteudo/analise/desempenho.json)
      e confere se a publicada saiu inteira, terminando no CTA. Rodar depois que o post aparecer no
      desempenho.json (atualizado todo dia ~9h). Se o arquivo tiver mais de 24 h, rodar SÓ
      `python3 scripts/instagram/pull_insights.py update` (NUNCA o comando `pull`).

Por que existe: o user edita a legenda no arquivo sem avisar e mexe de novo na hora de postar; a
contagem em bytes já deu dois falsos alarmes (166, 168); e duas legendas saíram cortadas no fim sem
ninguém perceber (101, 112).
"""
import csv, difflib, json, pathlib, re, sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[4]
CTA = ("Se você se sentiu provocado a refletir sobre sua vida hoje, me siga. Todo dia pela manhã posto "
       "uma reflexão buscando provocar você em direção ao seu aperfeiçoamento pessoal.")
PAREDE = 2200
PROIBIDAS = [
    (r"n[ãa]o [ée] sobre .{1,80}?[ée] sobre", '"Não é sobre X, é sobre Y"'),
    (r"na empresa,? (?:[ée]|funciona) (?:o mesmo|a mesma|igual)", '"Na empresa é o mesmo X"'),
    (r"(?:quem j[áa]|todo mundo que j[áa]) [^.:!?]{1,80}? sabe\b", '"Quem já X sabe:"'),
    (r"nossa vida funciona igual", '"Com a nossa vida funciona igual"'),
]


def norm(t):
    t = t.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return re.sub(r"\s+", " ", t).strip()


def frases(t):
    return re.split(r"(?<=[.?!:])\s+", norm(t))


def contar(arq):
    p = pathlib.Path(arq)
    t = p.read_text(encoding="utf-8").strip()
    n = len(t)
    print(f"{p}: {n} caracteres ({len(t.encode('utf-8'))} bytes; vale o número de caracteres)")
    print("  parede de 2.200:", "OK" if n <= PAREDE else f"ESTOUROU em {n - PAREDE}: cortar uma ideia, nunca o CTA")
    print("  termina no CTA fixo literal:", "OK" if norm(t).endswith(norm(CTA)) else "NÃO: conferir o fecho")
    for rx, nome in PROIBIDAS:
        for m in re.finditer(rx, t, flags=re.I):
            print(f"  PROIBIDA {nome}: \"...{m.group(0)}...\"")
    nisso = len(re.findall(r"\bisso n[ãa]o [ée]\b", t, flags=re.I))
    if nisso:
        print(f"  \"Isso não é X\" aparece {nisso}x: é permitido, mas não pode virar a fórmula de toda legenda")
    for f in frases(t):
        if re.search(r"\bte\b", f, flags=re.I) and re.search(r"\bvoc[êe]\b|\bseu\b|\bsua\b", f, flags=re.I):
            print(f"  REVISAR te + você na mesma frase: \"{f}\"")


def publicada(pasta):
    post = pathlib.Path(pasta).resolve()
    leg = (post / "legenda.txt").read_text(encoding="utf-8").strip()
    dados = json.loads((ROOT / "conteudo/analise/desempenho.json").read_text(encoding="utf-8"))
    pulled = dados.get("pulled_at", "")
    print(f"desempenho.json atualizado em {pulled}")
    try:
        quando = datetime.fromisoformat(pulled.replace("Z", "+00:00"))
        agora = datetime.now(timezone.utc) if quando.tzinfo else datetime.now()
        if (agora - quando).total_seconds() > 24 * 3600:
            print("  mais de 24 h: rodar SÓ `python3 scripts/instagram/pull_insights.py update` (nunca `pull`)")
    except ValueError:
        pass
    pid = ""
    for r in csv.DictReader(open(ROOT / "conteudo/analise/registro-posts.csv", encoding="utf-8")):
        if r.get("pasta") == post.name:
            pid = (r.get("post_id") or "").strip()
    por_id = {p["id"]: p for p in dados["posts"]}
    alvo = por_id.get(pid)
    if not alvo:  # post_id ainda não casado no registro: procura pelo texto
        alvo = max(dados["posts"], key=lambda p: difflib.SequenceMatcher(
            None, norm(leg)[:400], norm(p.get("caption_full", ""))[:400]).ratio())
        score = difflib.SequenceMatcher(None, norm(leg)[:400], norm(alvo.get("caption_full", ""))[:400]).ratio()
        if score < 0.6:
            sys.exit("Post ainda não aparece no desempenho.json (ou o texto mudou demais). Tentar depois da próxima atualização.")
        print(f"  post_id não está no registro; casado pelo texto: {alvo['id']} ({alvo.get('permalink', '')})")
    pub = alvo.get("caption_full", "")
    print(f"legenda.txt: {len(leg)} caracteres | publicada: {len(pub)} caracteres "
          f"(no desempenho.json cada quebra de linha vira um espaço; a contagem é a do texto postado)")
    print("  publicada termina no CTA:", "OK, saiu inteira" if norm(pub).endswith(norm(CTA))
          else "NÃO: pode ter sido cortada no fim pelo Instagram; avisar o user pra corrigir o post")
    if norm(pub) == norm(leg):
        print("  publicada = legenda.txt (ignorando quebras de linha e aspas curvas)")
        return
    print("  DIFERENTE do legenda.txt. O que foi ao ar vale; registrar no carousel-text.md. Diferenças:")
    for l in difflib.unified_diff(frases(leg), frases(pub), "legenda.txt", "publicada", lineterm="", n=0):
        if not l.startswith("@@"):
            print("   ", l)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("contar", "publicada"):
        sys.exit(__doc__)
    contar(sys.argv[2]) if sys.argv[1] == "contar" else publicada(sys.argv[2])
