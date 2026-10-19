#!/usr/bin/env python3
"""Valida a faixa do topo de cada imagem gerada — o que decide se a transição some no linho.

Calibrado no carrossel 81 (02/09/2026) com o veredito do user:
  APROVADAS (1,3,11): media 177-215, desvio 5-25
  REPROVADAS (2,4,5): media  91-100, desvio 45-71
Media alta = topo claro (no multiply, quase some). Desvio baixo = superficie continua,
sem telhado/viga/prateleira/cabeca atravessando a faixa. As duas coisas, juntas.
"""
import pathlib, statistics as st, sys
from PIL import Image

MEDIA_MIN, DESVIO_MAX = 170, 28
IMG = pathlib.Path(__file__).parent.parent / "imagens"
only = [int(a) for a in sys.argv[1:]]

ruins = []
for f in sorted(IMG.glob("img-*.png")):
    n = int(f.stem.split("-")[1])
    if only and n not in only:
        continue
    im = Image.open(f).convert("L"); w, h = im.size; px = im.load()
    faixa = [px[x, y] for y in range(int(h*0.02), int(h*0.14), 4) for x in range(30, w-30, 12)]
    media, desvio = st.mean(faixa), st.pstdev(faixa)
    falhas = []
    if media < MEDIA_MIN:  falhas.append(f"escuro demais ({media:.0f}<{MEDIA_MIN})")
    if desvio > DESVIO_MAX: falhas.append(f"tem objeto atravessando ({desvio:.0f}>{DESVIO_MAX})")
    st_ = "ok" if not falhas else "REGERAR: " + ", ".join(falhas)
    print(f"  img-{n:02d}: media {media:5.1f} | desvio {desvio:5.1f}  {st_}")
    if falhas: ruins.append(n)

print(f"\n{len(ruins)} pra regerar" + (f": {ruins}" if ruins else ""))
