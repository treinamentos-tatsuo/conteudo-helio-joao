#!/usr/bin/env python3
"""Checa se a tese de uma semente do banco MBV já foi publicada.

Uso:  python3 scripts/analise/checar_semente.py "vendedor estrela" "feudo"

Cruza as palavras-chave com o caption dos posts em conteudo/analise/desempenho.csv
e devolve o que já foi ao ar, com data e shares, comparado à mediana do feed.
Nasceu da auditoria de 02/09/2026, que achou 6 sementes publicadas sem marcação
no banco de scouting (uma delas 4 vezes).
"""
import csv, re, sys, statistics as st
from pathlib import Path

CSV = Path(__file__).resolve().parents[2] / "conteudo/analise/desempenho.csv"
PISO_ALCANCE = 5000  # base de comparação: posts que de fato circularam


def num(row, key):
    try:
        return float(row.get(key) or 0)
    except ValueError:
        return 0.0


def main(termos):
    if not termos:
        sys.exit('uso: checar_semente.py "termo" ["outro termo" ...]')

    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    base = [r for r in rows if num(r, "reach") > PISO_ALCANCE]
    mediana = st.median([num(r, "shares") for r in base])

    padrao = re.compile("|".join(re.escape(t) for t in termos), re.I)
    achados = [r for r in rows if padrao.search(r.get("caption_preview") or "")]
    achados.sort(key=lambda r: -num(r, "shares"))

    print(f"mediana do feed (alcance >{PISO_ALCANCE:,}): {mediana:.0f} shares")
    print(f'busca: {" | ".join(termos)}\n')

    if not achados:
        print("LIVRE — nenhum post publicado bate com esses termos.")
        return

    print(f"{len(achados)} post(s) já publicado(s):\n")
    for r in achados[:12]:
        sh = num(r, "shares")
        veredito = "validou" if sh >= 2 * mediana else ("morno" if sh >= mediana else "REPROVOU")
        print(f"  {(r.get('timestamp') or '')[:10]} | {sh:7.0f} sh | {sh/mediana:4.1f}x | {veredito}")
        print(f"    {(r.get('caption_preview') or '')[:100].replace(chr(10), ' ')}")
        print(f"    {r.get('permalink') or ''}\n")

    topo = num(achados[0], "shares")
    if topo < mediana * 1.5:
        print("LEITURA: a tese já foi testada e NÃO performou. Não é semente inexplorada.")
    else:
        print("LEITURA: a tese já performou. Refazer só com veículo/ângulo novo, e depois de esfriar.")


if __name__ == "__main__":
    main(sys.argv[1:])
