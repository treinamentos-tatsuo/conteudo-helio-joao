#!/usr/bin/env python3
"""Carrossel 172 (As 3 regras da liderança), modelo fotos-reais. Base: build3 do 173.
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
 1: (R/"DSCF3076.JPG", None, 'full', .5, .3, 1.0),
 2: (R/"DSCF3323.JPG", (0,560,4160,5600), 'full', .52, 0, 1.0),
 3: (DT/"MBV-TATSUOAC-175.jpg", None, 'full', .6, .5, 1),
 4: (G/"gen-04-v2.png", None, 'full', .5, .4, 1),
 5: (G/"gen-05-v2.png", None, 'full', .5, .4, 1),
 6: (R/"DSCF3105.JPG", None, 'full', .5, .3, 1.05),
 7: (R/"MBV-TATSUOAC-337.jpg", None, 'full', .45, .5, 1),
 8: (DT/"MBV-TATSUOAC-18.jpg", None, 'full', .55, .5, 1),
 9: (G/"gen-09-v2.png", None, 'full', .5, .5, 1),
 10: (R/"DSCF3115.JPG", None, 'full', .5, .3, 1.05),
 11: (R/"DSCF3327.JPG", (0,1180,4160,6240), 'full', .5, 0, 1),
 12: (R/"MBV-TATSUOAC-230.jpg", (0,900,3448,5168), 'full', .48, 0, 1.0),
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
def photo(n):
    src, pre, mode, fx, fy, z = PH[n]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if pre: im = im.crop(pre)
    W = 1080; H = 1350 if mode == 'full' else int(mode[1:]) if mode.startswith('h') else round(im.height*W/im.width)
    sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    g = ImageOps.grayscale(im.crop((l, t, l+W, t+H))); g = grade(g, n)
    g.save(IMG/f"img-{n:02d}.png"); return H
TOPFADE = lambda h: lg("to bottom", c(0,0), c(0, round(h*0.62/13.5)), c(.92, round(h*0.93/13.5)), c(1, round(h/13.5)))
S = {
 1: (lg("to bottom", c(0,0), c(0,40), c(.9,58), c(1,68)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="big" style="font-size:58px"><span class="ul">Liderança tem 3 regras.</span></div>'
     '<div class="a" style="font-size:132px;line-height:.96;margin-top:30px">SEJA EXEMPLO.<br>SEJA EXEMPLO.<br>SEJA EXEMPLO.</div></div>'),
 2: (lg("to bottom", c(0,0), c(0,48), c(.9,62), c(1,70)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="big" style="font-size:52px">Eu repito isso na minha imersão,<br>e repito de propósito.</div>'
     '<div class="rule" style="margin:34px auto 26px"></div>'
     '<div class="s">Porque é a regra</div>'
     '<div class="s r" style="font-size:56px;line-height:1.12">que o dono mais quebra.</div></div>'),
 3: (lg("to bottom", c(.55,0), c(.55,30), c(.9,52), c(1,62)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="s" style="font-size:44px">Um empresário que estava na sala<br>cobrava qualidade e prazo da fábrica dele.</div>'
     '<div class="rule" style="margin:34px auto 26px"></div>'
     '<div class="s">E o time respondia sempre igual:</div>'
     '<div class="s r" style="font-size:58px;line-height:1.12;margin-top:8px">impossível fazer<br>essa peça em 1 hora.</div></div>'),
 4: (lg("to bottom", c(0,0), c(0,40), c(.9,54), c(1,62)),
     '<div class="b" style="bottom:165px;left:170px;right:170px;text-align:center">'
     '<div class="big" style="font-size:58px">Ele não discutiu.</div>'
     '<div class="s" style="margin-top:22px">Juntou a produção inteira,<br>pediu a peça mais difícil</div>'
     '<div class="s" style="margin-top:18px">e fez na frente de todo mundo,<br>parando pra explicar.</div>'
     '<div class="rule" style="margin:34px auto 26px"></div>'
     '<div class="s r" style="font-size:92px;line-height:1">45 minutos.</div>'
     '<div class="s r" style="font-size:38px;margin-top:14px">Foi o tempo que ele levou pra fazer a peça.</div></div>'),
 5: (lg("to bottom", c(0,0), c(0,38), c(.9,53), c(1,61)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="big" style="font-size:52px">No dia seguinte,<br>a fábrica estava parada.</div>'
     '<div class="s fit" style="margin-top:14px">Todo mundo procurando defeito na peça dele.</div>'
     '<div class="rule" style="margin:34px auto 26px"></div>'
     '<div class="s"><b>Ninguém mais falava em impossível.</b></div>'
     '<div class="s r" style="font-size:52px;line-height:1.12;margin-top:6px">Agora precisavam<br>de outra desculpa.</div></div>'),
 6: (lg("to bottom", c(0,0), c(0,44), c(.9,58), c(1,66)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="big" style="font-size:58px"><span class="ul">Agora pensa na sua empresa.</span></div>'
     '<div class="s fit" style="margin-top:26px">Você cobra prazo, qualidade, atendimento, venda.</div>'
     '<div class="rule" style="margin:32px auto 26px"></div>'
     '<div class="s">Mas quando foi a última vez</div>'
     '<div class="s r" style="font-size:54px;line-height:1.12">que o seu time viu você fazendo?</div></div>'),
 7: (lg("to bottom", c(.95,0), c(.7,22), c(0,36), c(0,50), c(.92,66), c(1,78)),
     '<div class="b" style="top:130px;left:140px;right:140px;text-align:center">'
     '<div class="big" style="font-size:52px">O time não gosta do general<br>escondido na trincheira.</div></div>'
     '<div class="b" style="bottom:165px;left:110px;right:110px;text-align:center">'
     '<div class="a" style="font-size:118px;line-height:.98">GOSTA DO QUE LEVA<br>O PRIMEIRO TIRO.</div></div>'),
 8: (lg("to bottom", c(.95,0), c(.75,34), c(.35,44), c(.35,56), c(.8,66), c(1,82)),
     '<div class="b" style="top:300px;left:140px;right:140px;text-align:center">'
     '<div class="big" style="font-size:50px">Dono que cobra da sala<br>com ar-condicionado<br>e nunca pisa na operação</div></div>'
     '<div class="b" style="bottom:330px;left:120px;right:120px;text-align:center">'
     '<div class="s" style="font-size:46px">pode até ser obedecido.</div>'
     '<div class="s r" style="font-size:80px;line-height:1.05;margin-top:8px">Mas não é seguido.</div></div>'),
 9: (lg("to right", c(1,0), c(.85,42), c(.3,64), c(0,78)) + "," + lg("to bottom", c(0,70), c(.7,100)),
     '<div class="b" style="top:0;bottom:0;left:110px;width:620px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="big" style="font-size:58px">Ninguém gosta<br>de líder covarde.</div>'
     '<div class="rule" style="margin:38px 0 30px"></div>'
     '<div class="s">Do que some na hora<br>da decisão difícil,</div>'
     '<div class="s" style="margin-top:20px">do que manda o gerente demitir</div>'
     '<div class="s r" style="margin-top:20px">e do que só aparece quando<br>a meta já furou.</div></div>'),
 10: (lg("to bottom", c(0,0), c(0,44), c(.9,58), c(1,66)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="s">E ninguém vira outro líder do dia pra noite.</div>'
     '<div class="big" style="font-size:64px;margin-top:8px">Eu mesmo não virei.</div>'
     '<div class="rule" style="margin:34px auto 26px"></div>'
     '<div class="s"><b>Hoje um pouco melhor que ontem.</b></div>'
     '<div class="s r" style="font-size:48px;margin-top:6px">E o time vem junto, no mesmo passo.</div></div>'),
 11: (lg("to bottom", c(0,0), c(0,46), c(.9,60), c(1,68)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="big" style="font-size:50px">No meu treinamento<br>eu ensino o dono<br>a liderar pelo exemplo:</div>'
     '<div class="rule" style="margin:34px auto 26px"></div>'
     '<div class="s">onde estar, o que fazer na frente do time</div>'
     '<div class="s r" style="margin-top:6px">e como transformar isso<br>numa rotina que o time copia.</div></div>'),
 12: (lg("to bottom", c(0,0), c(0,34), c(.96,50), c(1,58)),
     '<div class="b" style="bottom:165px;left:120px;right:120px;text-align:center">'
     '<div class="big" style="font-size:56px">Fatos convencem.</div>'
     '<div class="s r" style="font-size:66px;line-height:1.08;margin-top:6px">Exemplos arrastam multidões.</div>'
     '<div class="rule" style="margin:36px auto 30px"></div>'
     '<div style="color:#F3F3F3;font-size:60px;font-weight:600;line-height:1.1">Comenta <span class="a" style="font-size:80px">EXEMPLO</span></div>'
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
    html = HEAD + f'<div class="slide"><img class="ph" src="../imagens/v1/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div>' + JS + '</body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html); print(f"[{n:02d}] ok")
