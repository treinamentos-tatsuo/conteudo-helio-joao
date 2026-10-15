#!/usr/bin/env python3
"""Carrossel 220 (6 verdades em 38 anos), modelo fotos-reais. Base: build do 172 (grade, pesos, margens).
v3 do 173 (correção do user, 01/10): diagramação slide a slide, sem molde único.
Composições: lateral (texto à esquerda/direita, degradê lateral), dividida (texto em cima e grito embaixo),
colunas, base centralizada. Anton só onde o slide pede. Slides 2, 8 e 10 seguem da v2 (aprovados)."""
import pathlib, sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
IMG = ROOT/"imagens/v1"; IMG.mkdir(parents=True, exist_ok=True); OUT = ROOT/"instagram"
F = pathlib.Path.home()/"Desktop/fotos para carrosséis"; A = F/"antigas"; R = F/"Hélio"; P = F/"publico"; DT = F/"detalhes"; G = ROOT/"imagens/_src"
def rec(p): return next(R.glob(p+"*"))
BK = "11,11,11"
def lg(d, *stops): return f"linear-gradient({d},{','.join(stops)})"
def c(a, p): return f"rgba({BK},{a}) {p}%"
# n: (fonte, pré-recorte, modo, fx, fy, zoom)
PH = {
 1: (R/"DSCF3122.JPG", None, 'full', .5, .47, 1.1),
 2: (A/"Captura de Tela 2026-10-01 às 19.04.57.png", (0,0,690,380), 'top', .5, .4, 1),
 3: (G/"gen-03-v2.png", None, 'full', .5, .4, 1),
 4: (G/"gen-04-v2.png", None, 'full', .5, .4, 1),
 5: (G/"gen-05-v2.png", None, 'full', .5, .4, 1),
 6: (G/"gen-06-v2.png", None, 'full', .5, .4, 1),
 7: (R/"MBV-TATSUOAC-241.jpg", None, 'full', .55, .5, 1.0),
 8: (G/"gen-08-v2.png", None, 'full', .5, .4, 1),
 9: (R/"DSCF3116.JPG", None, 'full', .5, .3, 1.0),
 10: (P/"DSCF3088.JPG", None, 'full', .52, .385, 1.3),
 11: (P/"MBV-TATSUOAC-217.jpg", None, 'full', .69, .45, 1.35),
 12: (R/"MBV-TATSUOAC-207.jpg", None, 'full', .53, .45, 1.15),
}
import numpy as np
def grade(g, n):
    """Tratamento profissional P&B: autocontraste, curva em S, nitidez local (clareza), vinheta e grão fino."""
    g = ImageOps.autocontrast(g, cutoff=0.5)
    a = np.asarray(g).astype(np.float32)/255
    k = 2.4; a = 0.5 + 0.5*np.tanh(k*(a-0.5))/np.tanh(k/2)
    g = Image.fromarray((a*255).clip(0,255).astype(np.uint8))
    g = g.filter(ImageFilter.UnsharpMask(radius=40, percent=22, threshold=0))
    g = g.filter(ImageFilter.UnsharpMask(radius=2, percent=45, threshold=2))
    a = np.asarray(g).astype(np.float32)
    h, w = a.shape; yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx-w/2)/(w/2))**2 + ((yy-h/2)/(h/2))**2)
    a *= 1 - 0.22*np.clip(r-0.55, 0, 1)**1.5
    rng = np.random.default_rng(n); a += rng.normal(0, 5.5, a.shape)
    return Image.fromarray(a.clip(0,255).astype(np.uint8))
COLOR = {1, 10, 11, 12}
SHRINK = {6: .8}
OFF = {2: 170}
def grade_color(im, n):
    im = ImageOps.autocontrast(im, cutoff=0.4)
    im = ImageEnhance.Contrast(im).enhance(1.08); im = ImageEnhance.Color(im).enhance(0.92)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=40, threshold=2))
    a = np.asarray(im).astype(np.float32); h, w = a.shape[:2]; yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx-w/2)/(w/2))**2 + ((yy-h/2)/(h/2))**2)
    a *= (1 - 0.25*np.clip(r-0.5, 0, 1)**1.5)[..., None]
    a += np.random.default_rng(n).normal(0, 4, a.shape)
    return Image.fromarray(a.clip(0,255).astype(np.uint8))
def photo(n):
    src, pre, mode, fx, fy, z = PH[n]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if pre: im = im.crop(pre)
    W = 1080; H = 1350 if mode == 'full' else int(mode[1:]) if mode.startswith('h') else round(im.height*W/im.width)
    sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    g = grade_color(im.crop((l, t, l+W, t+H)), n) if n in COLOR else grade(ImageOps.grayscale(im.crop((l, t, l+W, t+H))), n)
    if n in SHRINK:
        f = SHRINK[n]; sm = g.resize((round(W*f), round(H*f)), Image.LANCZOS)
        mask = Image.new("L", sm.size, 0); mk = Image.new("L", (sm.width-80, sm.height-80), 255)
        mask.paste(mk, (40, 40)); mask = mask.filter(ImageFilter.GaussianBlur(30))
        canvas = Image.new(g.mode, (W, H), 0 if g.mode == "L" else (11, 11, 11))
        canvas.paste(sm, ((W-sm.width)//2, (H-sm.height)//2), mask); g = canvas
    g.save(IMG/f"img-{n:02d}.png"); return H
TOPFADE = lambda h: lg("to bottom", c(0,0), c(0, round(h*0.62/13.5)), c(.92, round(h*0.93/13.5)), c(1, round(h/13.5)))
S = {
 1: (lg("to bottom", c(0,0), c(0,46), c(.9,60), c(1,68)),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="big" style="font-size:52px">Em 38 anos de empresa, eu aprendi</div>'
     '<div style="margin-top:18px"><span class="hla" style="font-size:150px;line-height:1.08">6 VERDADES</span></div>'
     '<div class="big" style="font-size:52px;margin-top:18px">que ninguém me contou.</div></div>'),
 2: (lg("to bottom", c(1,0), c(1,12.6), c(0,20), c(0,36), c(.93,52), c(1,58)),
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:44px">Eu saí de limpador de peixe na feira<br>e construí uma empresa que vendeu</div>'
     '<div class="s r" style="font-size:52px;line-height:1.15;margin-top:6px">mais de 9 bilhões em 4 continentes.</div>'
     '<div class="s" style="font-size:44px;margin-top:40px"><span class="hl">E quase tudo o que eu sei,</span><br><span class="hl">eu aprendi errando.</span></div></div>'),
 3: (lg("to bottom", c(0,0), c(0,34), c(.93,50), c(1,58)),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="lab">Verdade 1</div>'
     '<div class="big" style="font-size:54px">Empresa foi feita para botar<br>dinheiro no bolso do dono.</div>'
     '<div class="s" style="margin-top:26px">Pró-labore não é remuneração de dono.</div>'
     '<div class="s r" style="margin-top:14px">Portanto se a sua empresa só paga<br>o seu pró-labore, você tem um emprego<br>com todo o risco de um negócio.</div></div>'),
 4: (lg("to bottom", c(0,0), c(0,34), c(.93,50), c(1,58)),
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="lab">Verdade 2</div>'
     '<div class="big" style="font-size:56px">O gerente do banco<br>não é seu parceiro.</div>'
     '<div class="s" style="margin-top:26px;text-wrap:balance;padding:0 20px">Ele só está esperando aparecer um analfabeto empresarial <span class="r">pra emprestar dinheiro a mais de 60% ao ano e pegar uma grande fatia do seu bolo.</span></div></div>'),
 5: (lg("to right", c(1,0), c(.95,50), c(.4,70), c(0,84)) + "," + lg("to bottom", c(0,70), c(.6,100)),
     '<div class="b" style="top:0;bottom:0;left:90px;width:640px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="lab">Verdade 3</div>'
     '<div class="big" style="font-size:54px">Modelo de negócio<br>vale mais que talento.</div>'
     '<div class="s" style="margin-top:28px;font-size:40px">Um empresário mediano<br>num modelo bom vai mais longe<br>que um gênio num modelo ruim.</div>'
     '<div class="s" style="margin-top:24px;font-size:40px"><span class="hl">E o gênio sofre a vida inteira</span><br><span class="hl">sem saber o que está errado.</span></div></div>'),
 6: (lg("to bottom", c(.96,0), c(.7,18), c(0,28), c(0,58), c(.92,70), c(1,80)),
     '<div class="b" style="top:170px;left:110px;right:110px;text-align:center">'
     '<div class="lab">Verdade 4</div>'
     '<div class="big" style="font-size:58px">A empresa carrega<br>o DNA do dono.</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s">Quando o dono diz que só tem<br>gente fraca trabalhando com ele,</div>'
     '<div class="s r" style="font-size:54px;line-height:1.14;margin-top:10px">adivinha quem é o espelho<br>dessa gente.</div></div>'),
 7: (lg("to right", c(1,0), c(.85,42), c(.3,64), c(0,78)) + "," + lg("to bottom", c(0,70), c(.7,100)),
     '<div class="b" style="top:0;bottom:0;left:110px;width:600px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="lab">Verdade 5</div>'
     '<div class="big" style="font-size:50px">Na feira, eu nunca<br>perdi uma noite<br>de sono.</div>'
     '<div class="s r" style="font-size:54px;line-height:1.12;margin-top:10px">Como empresário,<br>perdi muitas.</div>'
     '<div class="s" style="margin-top:34px">Ninguém avisa do peso<br>e da solidão que é ser dono.</div></div>'),
 8: (lg("to bottom", c(0,0), c(0,34), c(.93,50), c(1,58)),
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="lab">Verdade 6</div>'
     '<div class="big" style="font-size:60px">Faturamento é vaidade.</div>'
     '<div class="s" style="margin-top:26px;text-wrap:balance;padding:0 20px">A minha empresa vendeu mais de 9 bilhões. Sabe o que esse número significa sozinho? <span class="hl">Nada.</span> <span class="r">O que vale verdadeiramente é o dinheiro que sobra no seu bolso.</span></div></div>'),
 9: (lg("to bottom", c(0,0), c(0,40), c(.93,55), c(1,63)),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Eu aprendi tudo isso apanhando,<br>pagando caro por cada erro.</div>'
     '<div class="big" style="font-size:58px;margin-top:20px">Eu era um verdadeiro<br>analfabeto empresarial.</div>'
     '<div class="s" style="font-size:46px;margin-top:30px"><span class="hl">Mas você não precisa levar 38 anos.</span></div></div>'),
 10: (lg("to bottom", c(0,0), c(0,42), c(.9,56), c(1,64)),
     '<div class="b" style="bottom:250px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:52px">Eu juntei tudo o que aprendi<br>em 38 anos num treinamento<br>de 3 dias:</div>'
     '<div class="s r" style="font-size:84px;line-height:1.05;margin-top:16px">a Imersão MBV.</div></div>'),
 11: (lg("to bottom", c(1,0), c(.9,28), c(.35,38), c(0,46), c(0,100)),
     '<div class="b" style="top:110px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:54px">Lá eu ensino gestão<br>pra donos de PME:</div>'
     '<div class="s" style="font-size:46px;margin-top:22px"><b>Lucratividade, Crescimento e Cultura.</b></div>'
     '<div class="s" style="font-size:44px;margin-top:20px"><span class="hl">Pra você ter clareza</span><br><span class="hl">de onde está o seu dinheiro.</span></div></div>'),
 12: (lg("to bottom", c(0,0), c(0,42), c(.92,56), c(1,64)),
     '<div class="b" style="bottom:250px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:54px">Quer começar a enxergar<br>a sua empresa de verdade?</div>'
     '<div style="color:#F3F3F3;font-size:60px;font-weight:600;line-height:1.1;margin-top:36px">Comenta <span class="hla" style="font-size:86px;line-height:1.15;vertical-align:middle">CLAREZA</span></div>'
     '<div class="s" style="font-size:40px;margin-top:8px">que eu mando o link no seu direct.</div></div>'),
}
HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,600;1,700&family=Anton&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0B0B0B;font-family:'Source Serif Pro',serif}
.ph{position:absolute;left:0;top:0;width:1080px}.shade{position:absolute;inset:0}.b{position:absolute;z-index:2}
.s{font-size:42px;line-height:1.32;font-weight:400;color:#F3F3F3}.s b{font-weight:600}
.big{font-size:64px;line-height:1.12;font-weight:600;color:#F3F3F3}
.r{color:#A91C20;font-weight:600}
.a{font-family:'Anton',sans-serif;color:#A91C20;text-transform:uppercase;letter-spacing:.5px}
.rule{width:84px;height:6px;background:#A91C20}
.hla{font-family:'Anton',sans-serif;text-transform:uppercase;background:#A91C20;color:#F3F3F3;padding:0 22px;display:inline-block;letter-spacing:.5px}
.hl{background:#A91C20;color:#F3F3F3;padding:2px 14px;-webkit-box-decoration-break:clone;box-decoration-break:clone;line-height:1.62}
.lab{font-size:30px;letter-spacing:8px;text-transform:uppercase;color:#A91C20;font-weight:700;margin-bottom:16px}
</style></head><body>'''
JS = r'''<script>
const NS='http://www.w3.org/2000/svg';
function svg(){const s=document.createElementNS(NS,'svg');s.setAttribute('width','1080');s.setAttribute('height','1350');s.style.cssText='position:absolute;left:0;top:0;z-index:3;overflow:visible;pointer-events:none';document.querySelector('.slide').appendChild(s);return s;}
function brush(el){const r=el.getBoundingClientRect(),s=svg(),x0=r.left-10,x1=r.right+10,y=r.bottom-2,w=x1-x0;
 s.innerHTML=`<path d="M${x0} ${y+4} C ${x0+w*.3} ${y-3}, ${x0+w*.62} ${y+9}, ${x1} ${y-1}" stroke="#A91C20" stroke-width="10" fill="none" stroke-linecap="round" opacity=".95"/>`+
 `<path d="M${x0+18} ${y+12} C ${x0+w*.38} ${y+6}, ${x0+w*.7} ${y+15}, ${x1-26} ${y+7}" stroke="#A91C20" stroke-width="4.5" fill="none" stroke-linecap="round" opacity=".85"/>`;}
function arrow(a,b){const ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect(),s=svg();
 const x0=ra.left+ra.width*.5,y0=ra.bottom+10,x1=rb.right+16,y1=rb.top+rb.height*.45;
 const c1x=x0+150,c1y=y0+260,c2x=x1+170,c2y=y1-230;
 const ang=Math.atan2(y1-c2y,x1-c2x),L=34,sp=.5;
 const h1=[x1-L*Math.cos(ang-sp),y1-L*Math.sin(ang-sp)],h2=[x1-L*Math.cos(ang+sp),y1-L*Math.sin(ang+sp)];
 s.innerHTML=`<path d="M${x0} ${y0} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${x1} ${y1}" stroke="#A91C20" stroke-width="7" fill="none" stroke-linecap="round"/>`+
 `<path d="M${h1[0]} ${h1[1]} L${x1} ${y1} L${h2[0]} ${h2[1]}" stroke="#A91C20" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;}
document.fonts.ready.then(()=>{document.querySelectorAll('.fit').forEach(e=>{e.style.whiteSpace='nowrap';let f=parseFloat(getComputedStyle(e).fontSize);const W=e.parentElement.clientWidth;while(e.scrollWidth>W&&f>28){f-=1;e.style.fontSize=f+'px';}});const g=[...document.querySelectorAll('.big.fit')];if(g.length){const m=Math.min(...g.map(e=>parseFloat(e.style.fontSize||getComputedStyle(e).fontSize)));g.forEach(e=>e.style.fontSize=m+'px');}document.querySelectorAll('.ul').forEach(brush);const a=document.getElementById('af'),b=document.getElementById('at');if(a&&b)arrow(a,b);});
</script>'''
for n in ([int(x) for x in sys.argv[1:]] or S):
    h = photo(n); grad, body = S[n]
    if grad is None: grad = TOPFADE(h)
    html = HEAD + f'<div class="slide"><img class="ph" style="top:{OFF.get(n,0)}px" src="../imagens/v1/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div>' + JS + '</body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html); print(f"[{n:02d}] ok")
