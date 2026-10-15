#!/usr/bin/env python3
"""Degrau horizontal no topo da foto: maior salto de luminancia media entre linhas vizinhas (janela de 3px)
na metade de cima. Salto > 12 = faixa branca com linha dura (user, 12/09, carrossel 114: slides 3, 7, 12)."""
import pathlib, sys, numpy as np
from PIL import Image
IMG = pathlib.Path(__file__).parent.parent / "imagens"
only = [int(a) for a in sys.argv[1:]]
for f in sorted(IMG.glob("img-*.png")):
    n = int(f.stem.split("-")[1])
    if only and n not in only: continue
    a = np.asarray(Image.open(f).convert("L")).astype(float); h = a.shape[0]
    rows = a[: int(h*0.55), 40:-40].mean(axis=1)
    d = np.abs(rows[3:] - rows[:-3]); y = int(d.argmax())
    print(f"  img-{n:02d}: degrau {d.max():5.1f} em y={y} ({y/h:.0%})  {'LINHA DURA' if d.max() > 12 else 'ok'}")
