#!/usr/bin/env python3
"""fit v2 (04/09, carrossel 88): texto no top da skill; gap alvo 210; recorte lateral ate 35% quando o
sujeito esta no miolo (OBJPOS resolve sujeito nas pontas). Escreve imgheight.json e fade.json (F% = onde o
degrade chega a 100%: no inicio do assunto, pra ramp longo e imperceptivel)."""
import json, sys
from PIL import Image
TB=json.load(open('textbottom.json')); H_=json.load(open('imgheight.json')); FD={}
GAP=210; NAT=720; CROP_MAX=0.35
def subject(n, tb, dark=150, frac=0.06):
    im=Image.open(f'../instagram/slide-{n:02d}.png').convert('L'); w,h=im.size; px=im.load()
    for y in range(tb+10,h,4):
        if sum(1 for x in range(60,w-60,6) if px[x,y]<dark)/((w-120)/6)>frac: return y
for n in [int(a) for a in sys.argv[1:]]:
    tb=TB[str(n)]; s=subject(n,tb)
    if s is None: print(n,'sem assunto'); continue
    f_s=(s-(1350-NAT))/NAT                     # fracao da imagem onde o assunto comeca
    H=round((1350-(tb+GAP))/(1-f_s))
    H=min(H, round(NAT/(1-CROP_MAX)))
    H=max(H, NAT)
    top=1350-H; start=top+f_s*H; gap=start-tb
    F=max(12, min(60, round((start-top)/H*100)))
    H_[str(n)]=H; FD[str(n)]=F
    print(f'[{n:02d}] tb={tb} assunto_nat={s} f_s={f_s:.2f} -> H={H} (recorte {1-NAT/H:.0%}) assunto={start:.0f} gap={gap:.0f} fade={F}%')
json.dump(H_,open('imgheight.json','w')); 
old=json.load(open('fade.json')) if __import__('os').path.exists('fade.json') else {}
old.update(FD); json.dump(old,open('fade.json','w'))
