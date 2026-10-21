#!/usr/bin/env python3
"""Recorta o Hélio das fotos reais (rembg, modelo birefnet-portrait já baixado em ~/.rembg/models) e salva PNG com fundo transparente em imagens/_cut/.
Pedido do João (21/10): o Hélio sozinho, sem nada atrás. Tratar e limpar o fundo de foto real é permitido (modelo fotos-reais, seção 6)."""
import pathlib, sys, time
from rembg import remove, new_session
from PIL import Image, ImageOps
ROOT = pathlib.Path(__file__).parent.parent; OUT = ROOT/"imagens"/"_cut"; OUT.mkdir(parents=True, exist_ok=True)
F = next(p for p in (pathlib.Path.home()/"Desktop").iterdir() if p.name.startswith("fotos para"))
R = next(d for d in F.iterdir() if d.name.startswith("H"))
NAMES = sys.argv[1:] or ["DSCF3122", "0027", "MBV-TATSUOAC-227", "MBV-TATSUOAC-240", "DSCF3116", "MBV-TATSUOAC-247", "0009", "MBV-TATSUOAC-228"]
s = new_session("birefnet-portrait")
for n in NAMES:
    out = OUT/f"{n}.png"
    if out.exists(): print(n, "ja existe", flush=True); continue
    src = next(p for p in R.iterdir() if p.name.startswith(n))
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB"); im.thumbnail((2400, 2400))
    t = time.time(); remove(im, session=s).save(out); print(n, f"ok {time.time()-t:.0f}s", flush=True)
print("FIM", flush=True)
