#!/usr/bin/env python3
"""Pos-processa as imagens: foto -> quadrado ancorado no rodape; cutout -> crop na caixa.

O gpt-image-2 ignora o parametro `size` e quase sempre devolve retrato (1024x1536).
A composicao pedida no prompt (sujeito no terco inferior, metade de cima palida)
garante que o quadrado de baixo pega o sujeito e mantem o topo pro texto.
"""
import json, pathlib, sys
from PIL import Image

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
RAW = IMG / "_raw"
RAW.mkdir(exist_ok=True)
CFG = json.loads((SCR / "prompts.json").read_text())
only = [int(a) for a in sys.argv[1:]] or None

# cortes extras no topo do quadrado, quando o conteudo escuro sobe e come o texto
EXTRA_TOP = {6: 120, 10: 230}
# cutout que fica pequeno demais no slide: guardar so a fracao de cima da caixa
KEEP_TOP = {17: 0.60}

for item in CFG["images"]:
    n, kind = item["n"], item["kind"]
    if only and n not in only:
        continue
    src = IMG / f"img-{n:02d}.png"
    if not src.exists():
        print(f"[{n:02d}] AUSENTE")
        continue
    keep = RAW / f"img-{n:02d}.png"
    if not keep.exists():
        keep.write_bytes(src.read_bytes())
    im = Image.open(keep).convert("L").convert("RGB")  # mata qualquer desvio de cor
    w, h = im.size
    if kind == "cutout":
        g = im.convert("L").point(lambda p: 0 if p < 243 else 255)
        box = g.point(lambda p: 255 - p).getbbox()
        if box:
            m = 12
            box = (max(0, box[0] - m), max(0, box[1] - m), min(w, box[2] + m), min(h, box[3] + m))
            im = im.crop(box)
        frac = KEEP_TOP.get(n)
        if frac:
            im = im.crop((0, 0, im.size[0], int(im.size[1] * frac)))
        out = im
    else:
        side = min(w, h)
        x0 = max(0, (w - side) // 2)
        out = im.crop((x0, h - side, x0 + side, h))
        extra = EXTRA_TOP.get(n, 0)
        if extra:
            out = out.crop((0, extra, side, side))
    out.save(src)
    print(f"[{n:02d}] {kind}: {w}x{h} -> {out.size[0]}x{out.size[1]}")
