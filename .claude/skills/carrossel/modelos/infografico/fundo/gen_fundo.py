"""Fundo escuro da serie de estaticos (1080x1350), recriado a partir dos exemplos do user.

Construcao (medida nos exemplos, escala 1080):
- base quase preta (media ~#0d0d0d) com granulado fino (desvio ~4) e poucos pontos de poeira claros;
- grade de quadrados com cantos arredondados (passo 194 px, vao 2 px, raio 22 px): o vao cinza vira a
  linha e, onde quatro cantos se encontram, sobra a estrela concava cinza;
- a grade so aparece em duas manchas (canto superior esquerdo e inferior direito), sumindo em degrade.
"""
import sys
import numpy as np
from PIL import Image

W, H = 1080, 1350
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 7
OUT = sys.argv[2] if len(sys.argv) > 2 else "fundo-escuro.png"
rng = np.random.default_rng(SEED)

BG = 11.0          # nivel da base (antes do grao)
LINE = 70.0        # nivel da linha/estrela
PITCH, GAP, R = 194.0, 2.0, 22.0

yy, xx = np.mgrid[0:H, 0:W].astype(np.float64)


def grid_alpha(x0, y0):
    """1 no vao entre os quadrados arredondados (linha + estrela), 0 dentro deles; com antialias."""
    lx = np.mod(xx - x0, PITCH) - PITCH / 2       # linhas em x0 + k*PITCH; quadrados entre elas
    ly = np.mod(yy - y0, PITCH) - PITCH / 2
    h = (PITCH - GAP) / 2
    qx = np.abs(lx) - (h - R)
    qy = np.abs(ly) - (h - R)
    outside = np.hypot(np.maximum(qx, 0), np.maximum(qy, 0))
    inside = np.minimum(np.maximum(qx, qy), 0)
    d = outside + inside - R            # distancia assinada ate a borda do quadrado
    return np.clip(d + 0.5, 0, 1)


def smooth(e0, e1, v):
    t = np.clip((v - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


# mascaras das duas manchas (seguem as bordas, como nos exemplos)
tl = np.maximum(
    (1 - smooth(140, 235, xx)) * (1 - smooth(560, 800, yy)),     # faixa da borda esquerda
    (1 - smooth(60, 175, yy)) * (1 - smooth(290, 430, xx)),      # faixa da borda de cima
)
br = np.maximum(
    smooth(925, 1010, xx) * smooth(700, 900, yy),                 # faixa da borda direita
    smooth(1000, 1090, yy) * smooth(640, 820, xx),                # faixa da borda de baixo
)

img = np.full((H, W), BG)
img += (LINE - BG) * grid_alpha(65, 53) * tl
img += (LINE - BG) * grid_alpha(847, 867) * br

# granulado: ruido gaussiano com leve aglomerado (desfoque de ~1 px), aplicado em tudo
noise = rng.normal(0, 1, (H, W))
k = np.array([1, 4, 6, 4, 1], dtype=np.float64); k /= k.sum()
noise = np.apply_along_axis(lambda r: np.convolve(r, k, mode="same"), 1, noise)
noise = np.apply_along_axis(lambda c: np.convolve(c, k, mode="same"), 0, noise)
noise = noise / noise.std() * 4.2
img += noise + 2.0

# poeira: poucos pontos claros e pequenos
n = 190
px = rng.integers(0, W, n); py = rng.integers(0, H, n)
amp = rng.uniform(25, 75, n); rad = rng.uniform(0.5, 1.1, n)
for x, y, a, r in zip(px, py, amp, rad):
    x0, x1 = max(x - 3, 0), min(x + 4, W); y0, y1 = max(y - 3, 0), min(y + 4, H)
    gx, gy = np.meshgrid(np.arange(x0, x1), np.arange(y0, y1))
    img[y0:y1, x0:x1] += a * np.exp(-((gx - x) ** 2 + (gy - y) ** 2) / (2 * r * r))

out = np.clip(np.round(img), 0, 255).astype(np.uint8)
Image.fromarray(np.stack([out] * 3, axis=-1)).save(OUT, optimize=True)
bgzone = out[380:430, 450:650]
print(OUT, "media fundo limpo", round(float(bgzone.mean()), 1), "desvio", round(float(bgzone.std()), 1))
