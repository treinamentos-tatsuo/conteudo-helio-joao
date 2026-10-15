#!/usr/bin/env python3
"""P&B garantido no pos (erros-frequentes 2026-07-24): guarda o raw em imagens/_raw/ e desatura imagens/img-NN.png.
Uso: post.py [N ...]. Antes de regerar uma imagem, RENOMEAR o raw (img-NN-v1.png), nunca rm."""
import pathlib, sys
from PIL import Image
IMG = pathlib.Path(__file__).parent.parent / "imagens"; RAW = IMG / "_raw"; RAW.mkdir(exist_ok=True)
only = [int(a) for a in sys.argv[1:]]
for f in sorted(IMG.glob("img-*.png")):
    n = int(f.stem.split("-")[1])
    if only and n not in only: continue
    keep = RAW / f.name
    if not keep.exists(): keep.write_bytes(f.read_bytes())
    Image.open(keep).convert("L").convert("RGB").save(f)
    print(f"img-{n:02d}: P&B ok")
