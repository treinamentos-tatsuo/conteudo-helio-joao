#!/usr/bin/env python3
"""Sincroniza o status das frases em conteudo/banco-frases.md com o registro-posts.csv.

Zero API. Lê o registro (fichas) e reescreve só o status entre crases no cabeçalho
`### N. Frase — \`status\`` de cada frase cuja ficha tem semente `banco-N`.

Regras:
- ficha com data_publicacao e status ainda não `publicada` → `publicada (post P, DATA)`
- ficha fechada (resultado_taxa preenchido) e status sem "FECHADA" → acrescenta
  ` — FECHADA D+7: X shares/1k · alcance R · vs previsão`
- status que já contém "FECHADA" nunca é tocado (pode ter leitura manual mais rica)
- `--dry-run` só mostra o que mudaria.

Criado 2026-09-08: o ritual atualizava registro e base, mas o banco ficava com
"produzida — aguardando publicação" semanas depois do post no ar.
"""
import csv, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
BANCO = ROOT / "conteudo/banco-frases.md"
REG = ROOT / "conteudo/analise/registro-posts.csv"
DRY = "--dry-run" in sys.argv

HEAD = re.compile(r"^(### (\d+)\. .+? — `)([^`]*)(`.*)$")

fichas = {}
for r in csv.DictReader(open(REG, encoding="utf-8")):
    if r.get("formato") != "frase":
        continue
    m = re.fullmatch(r"banco-(\d+)", (r.get("semente") or "").strip())
    if not m:
        continue
    fichas[int(m.group(1))] = r

lines = BANCO.read_text(encoding="utf-8").split("\n")
changes = []
for i, line in enumerate(lines):
    m = HEAD.match(line)
    if not m:
        continue
    n = int(m.group(2))
    r = fichas.get(n)
    if not r:
        continue
    status = m.group(3)
    pasta = r["pasta"]
    post = pasta.split("_", 1)[0]
    data = r.get("data_publicacao") or ""
    taxa = (r.get("resultado_taxa") or "").strip()
    new = status
    if data and not status.startswith("publicada"):
        new = f"publicada (post {post}, {data})"
    if taxa and "FECHADA" not in new:
        alc = (r.get("resultado_alcance") or "").strip()
        vs = (r.get("resultado_vs_previsao") or "").strip()
        extra = f"FECHADA D+7: {taxa} shares/1k"
        if alc:
            extra += f" · alcance {alc}"
        if vs:
            extra += f" · {vs}"
        new = new.rstrip(")") + f" — {extra})" if new.endswith(")") else new + f" — {extra}"
    if new != status:
        changes.append((n, status, new))
        lines[i] = m.group(1) + new + m.group(4)

for n, old, new in changes:
    print(f"[{n:02d}] {old}\n     -> {new}")
if not changes:
    print("banco-frases.md já sincronizado (0 mudanças).")
elif DRY:
    print(f"(dry-run: {len(changes)} mudança(s) não gravadas)")
else:
    BANCO.write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(changes)} mudança(s) gravadas em {BANCO.relative_to(ROOT)}")
