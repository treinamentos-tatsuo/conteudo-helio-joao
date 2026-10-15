#!/usr/bin/env python3
"""Calcula imgheight.json a partir do render em altura natural.

Fórmula (erros-frequentes 2026-09-01, carrossel 77):
    (1 - f) = (1350 - assunto_medido) / 720
    H       = (1350 - (texto_bottom + GAP)) / (1 - f)
Roda: render em altura natural -> fit.py -> build.py -> render de novo -> check.py
"""
import json, pathlib, sys
from PIL import Image

SCR = pathlib.Path(__file__).parent
IG = SCR.parent / "instagram"
TB = json.loads((SCR / "textbottom.json").read_text())
GAP = 200          # alvo (user 02/09: 320 ainda le como "imagem muito para baixo")
CROP_MAX = 0.18    # recorte lateral maximo; acima disso decepa gente nas pontas da cena
DARK, FRAC = 150, 0.06
NATURAL = 720      # altura da 1536x1024 com width:100%

def subject_start(n, tb):
    f = IG / f"slide-{n:02d}.png"
    if not f.exists(): return None
    im = Image.open(f).convert("L"); w, h = im.size; px = im.load()
    for y in range(tb + 10, h, 4):
        dark = sum(1 for x in range(60, w - 60, 6) if px[x, y] < DARK)
        if dark / ((w - 120) / 6) > FRAC:
            return y
    return None

try: out = {int(k): v for k, v in json.loads((SCR / "imgheight.json").read_text()).items()}
except FileNotFoundError: out = {}
for k in sorted(TB, key=int):
    n, tb = int(k), TB[k]
    if n in out:
        print(f"[{n:02d}] ja tem H={out[n]} (render nao esta em altura natural) — mantido"); continue
    s = subject_start(n, tb)
    if s is None:
        print(f"[{n:02d}] sem assunto detectavel — pulando"); continue
    gap = s - tb
    if gap <= 240:
        print(f"[{n:02d}] gap {gap}px ja OK, altura natural"); continue
    one_minus_f = (1350 - s) / NATURAL
    H = round((1350 - (tb + GAP)) / one_minus_f)
    perda = 1 - NATURAL / H
    if perda > CROP_MAX:
        H = round(NATURAL / (1 - CROP_MAX)); perda = CROP_MAX
        nota = f" [travado no teto de recorte; gap final ~{round(tb+ (1350-tb) - (H*one_minus_f))}px]"
    else:
        nota = ""
    out[n] = H
    print(f"[{n:02d}] gap {gap}px -> H={H}px (recorte lateral {perda*100:.0f}%){nota}")

(SCR / "imgheight.json").write_text(json.dumps(out, indent=1))
print(f"\nimgheight.json: {len(out)} slides ajustados")
