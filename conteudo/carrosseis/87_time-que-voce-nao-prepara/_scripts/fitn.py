#!/usr/bin/env python3
"""fit por slide, MESCLANDO no imgheight.json (fit.py sobrescreve o arquivo inteiro). Uso: fitn.py N [N...]"""
import json, sys
from PIL import Image
TB=json.load(open('textbottom.json')); d=json.load(open('imgheight.json'))
for n in sys.argv[1:]:
    tb=TB[n]; im=Image.open(f'../instagram/slide-{int(n):02d}.png').convert('L'); w,h=im.size; px=im.load(); s=None
    for y in range(tb+10,h,4):
        if sum(1 for x in range(60,w-60,6) if px[x,y]<150)/((w-120)/6)>0.06: s=y; break
    if s is None: print(n,'sem assunto'); continue
    gap=s-tb
    if gap<=240: d.pop(n,None); print(n,'natural, gap',gap); continue
    H=round((1350-(tb+200))/((1350-s)/720)); H=min(H, round(720/0.82)); d[n]=H; print(n,'H',H,'gap era',gap)
json.dump(d,open('imgheight.json','w'))
