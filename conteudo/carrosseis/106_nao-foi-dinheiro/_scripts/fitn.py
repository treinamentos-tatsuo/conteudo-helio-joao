#!/usr/bin/env python3
"""fit.py para slides específicos: mede o render em altura natural e MESCLA no imgheight.json (não apaga os outros).
Uso: fitn.py N [N...]   (render os N sem altura antes)"""
import json, pathlib, sys
from PIL import Image
SCR=pathlib.Path(__file__).parent; IG=SCR.parent/"instagram"
TB=json.loads((SCR/"textbottom.json").read_text()); GAP=200; NATURAL=720; DARK,FRAC=150,0.06
try: H=json.loads((SCR/"imgheight.json").read_text())
except FileNotFoundError: H={}
for n in [int(a) for a in sys.argv[1:]]:
    im=Image.open(IG/f"slide-{n:02d}.png").convert("L"); w,h=im.size; px=im.load(); tb=TB[str(n)]; s=None
    for y in range(tb+10,h,4):
        if sum(1 for x in range(60,w-60,6) if px[x,y]<DARK)/((w-120)/6)>FRAC: s=y; break
    if s is None: print(f"[{n:02d}] sem assunto"); continue
    gap=s-tb
    if gap<=240: print(f"[{n:02d}] gap {gap} ok natural"); H.pop(str(n),None); continue
    omf=(1350-s)/NATURAL; hh=round((1350-(tb+GAP))/omf); H[str(n)]=hh
    print(f"[{n:02d}] gap {gap} -> H={hh} (recorte {100*(1-NATURAL/hh):.0f}%)")
json.dump(H,open(SCR/"imgheight.json","w"),indent=1)
