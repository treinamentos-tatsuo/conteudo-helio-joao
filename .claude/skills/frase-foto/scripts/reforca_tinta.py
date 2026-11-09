"""Reforça a tinta do flip chart depois do corte: preto mais fundo e vermelho carmim vivo, só dentro da folha.
Padrão aprovado pelo João em 09/11/2026 (J343): o motor entrega a letra certa mas com a tinta fraca e o vermelho
puxando pro rosa; este ajuste deixa igual aos flip charts de outubro (J251, J253) sem mexer na letra nem no fundo.

uso (da raiz do projeto):
  python3 .claude/skills/frase-foto/scripts/reforca_tinta.py $P/instagram/flip-v1.png $P/instagram/flip-v1-forte.png
opção: --area x0 x1 y0 y1  (padrão 340 815 500 1100: a folha do flip-mbv.png no corte padrão do corta.py)
"""
import sys
import numpy as np
from PIL import Image

args = sys.argv[1:]
area = (340, 815, 500, 1100)
if '--area' in args:
    i = args.index('--area'); area = tuple(int(v) for v in args[i + 1:i + 5]); del args[i:i + 5]
src, out = args[0], args[1]
x0, x1, y0, y1 = area

a = np.asarray(Image.open(src).convert('RGB')).astype(float)
r = a[y0:y1, x0:x1]
R, G, B = r[..., 0], r[..., 1], r[..., 2]
ink = np.clip((215 - r.mean(axis=2)) / 90, 0, 1)            # 0 no papel, 1 na tinta
red = np.clip((R - (G + B) / 2 - 25) / 40, 0, 1)            # 1 onde a tinta é vermelha
preto = 255 * (r / 255) ** 2.2
verm = np.stack([np.minimum(255, R * 0.92 + 18), 255 * (G / 255) ** 2.6, 255 * (B / 255) ** 2.6], axis=-1)
alvo = preto * (1 - red[..., None]) + verm * red[..., None]
a[y0:y1, x0:x1] = r * (1 - ink[..., None]) + alvo * ink[..., None]
Image.fromarray(np.clip(a, 0, 255).astype('uint8')).save(out)
print('OK', out)
