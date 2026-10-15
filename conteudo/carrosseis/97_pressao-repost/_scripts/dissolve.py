#!/usr/bin/env python3
"""Dissolve imperceptivel (user 04/09, carrossel 88): clareia o topo da foto com uma rampa smoothstep ate a
fracao W (onde o assunto comeca), partindo do _raw. Assim a foto nasce do papel sem banda de cinza visivel.
Uso: dissolve.py N=W [N=W ...]   (ex.: 5=0.30)"""
import sys, numpy as np
from PIL import Image
for arg in sys.argv[1:]:
    n, w = arg.split('='); n = int(n); w = float(w)
    im = Image.open(f'../imagens/_raw/img-{n:02d}.png').convert('L'); a = np.asarray(im).astype(np.float32)
    h = a.shape[0]; y = np.arange(h, dtype=np.float32) / h
    t = np.clip(y / w, 0, 1); k = t * t * (3 - 2 * t)          # smoothstep 0 (topo) -> 1 (assunto)
    k = k[:, None]
    out = 255 - (255 - a) * k
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(f'../imagens/img-{n:02d}.png')
    print(f'img-{n:02d}: topo dissolvido ate {w:.0%}')
