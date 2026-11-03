#!/usr/bin/env python3
"""Checagem automatica de vao morto e invasao texto x imagem, por slide renderizado.

Para cada slide: pega o bottom do bloco de texto (textbottom.json, medido via Playwright)
e o inicio do CONTEUDO da imagem no slide (primeira linha do render, abaixo do texto,
em que >6% dos pixels sao escuros o bastante pra "ler como assunto").
  INVASAO  = conteudo comeca antes de texto_bottom + 30px
  VAO MORTO = conteudo comeca mais de 220px depois do fim do texto
Roda depois do render: python3 check.py [N...]
"""
import json, pathlib, sys
from PIL import Image

SCR = pathlib.Path(__file__).parent
IG = SCR.parent / "instagram"
TB = json.loads((SCR / "textbottom.json").read_text(encoding='utf-8'))
only = [int(a) for a in sys.argv[1:]] or sorted(int(k) for k in TB)

DARK = 150      # luminancia que conta como "assunto"
FRAC = 0.06     # fracao da linha que precisa ser escura
GAP_MAX = 260   # user 02/09: acima disso le como "imagem muito para baixo"
GAP_MIN = 30    # folga minima antes do assunto

for n in only:
    f = IG / f"slide-{n:02d}.png"
    if not f.exists():
        continue
    im = Image.open(f).convert("L")
    w, h = im.size
    px = im.load()
    tb = TB[str(n)]
    start = None
    # varre da linha abaixo do texto ate o rodape, faixa central (evita bordas)
    for y in range(tb + 10, h, 4):
        dark = sum(1 for x in range(60, w - 60, 6) if px[x, y] < DARK)
        if dark / ((w - 120) / 6) > FRAC:
            start = y
            break
    if start is None:
        print(f"[{n:02d}] texto ate {tb} | SEM conteudo detectavel — imagem ausente/apagada? CONFERIR")
        continue
    gap = start - tb
    verdict = "ok"
    if gap < GAP_MIN:
        verdict = f"INVASAO (assunto a {gap}px do texto)"
    elif gap > GAP_MAX:
        verdict = f"VAO MORTO ({gap}px de deserto)"
    print(f"[{n:02d}] texto ate y={tb} | assunto comeca y={start} | gap={gap}px | {verdict}")
