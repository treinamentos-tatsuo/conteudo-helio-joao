#!/usr/bin/env python3
"""Pos-processa: desatura (P&B garantido) e foto -> quadrado ancorado no rodape."""
import json, pathlib, sys
from PIL import Image

SCR = pathlib.Path(__file__).parent
IMG = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/28_vender-tomate-e-casa/imagens")
RAW = IMG / "_raw"
RAW.mkdir(exist_ok=True)
CFG = json.loads((SCR / "prompts.json").read_text())
only = [int(a) for a in sys.argv[1:]] or None

# cortes extras no topo, por slide (quando conteudo escuro invade a faixa de texto)
EXTRA_TOP = {}

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
    im = Image.open(keep).convert("L").convert("RGB")  # P&B garantido
    w, h = im.size
    if kind == "cutout":
        g = im.convert("L").point(lambda p: 0 if p < 243 else 255)
        box = g.point(lambda p: 255 - p).getbbox()
        if box:
            m = 12
            box = (max(0, box[0] - m), max(0, box[1] - m), min(w, box[2] + m), min(h, box[3] + m))
            im = im.crop(box)
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
