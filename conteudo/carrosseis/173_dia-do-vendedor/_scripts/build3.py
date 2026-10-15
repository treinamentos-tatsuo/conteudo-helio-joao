#!/usr/bin/env python3
"""v3 do 173 (correção do user, 01/10): diagramação slide a slide, sem molde único.
Composições: lateral (texto à esquerda/direita, degradê lateral), dividida (texto em cima e grito embaixo),
colunas, base centralizada. Anton só onde o slide pede. Slides 2, 8 e 10 seguem da v2 (aprovados)."""
import pathlib, sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
IMG = ROOT/"imagens/v3"; IMG.mkdir(parents=True, exist_ok=True); OUT = ROOT/"instagram"
A = pathlib.Path.home()/"Desktop/fotos_album_2621284"; R = A/"recentes"; G = ROOT/"imagens/_src"
def rec(p): return next(R.glob(p+"*"))
BK = "11,11,11"
def lg(d, *stops): return f"linear-gradient({d},{','.join(stops)})"
def c(a, p): return f"rgba({BK},{a}) {p}%"
# n: (fonte, pré-recorte, modo, fx, fy, zoom)
PH = {
 1: (rec("0018"), None, 'full', .42, 0, 1.08),
 3: (A/"noticia_100388.jpg", None, 'top', .5, .4, 1),
 4: (A/"images.jpeg", None, 'top', .5, .45, 1),
 5: (G/"gen-05-v2.png", None, 'full', .5, .3, 1),
 6: (A/"helio-tatsuo-yotsui-fundador-da-franquia-hoken-1423773939609_615x300.jpg", None, 'h930', .5, .4, 1),
 10: (rec("0028"), None, 'full', .74, .85, 1.25),
 7: (rec("ARB0"), None, 'full', .56, .55, 1.1),
 9: (rec("0009"), None, 'full', .66, .46, 1.45),
 11: (rec("0024"), None, 'full', .5, .35, 1),
 12: (rec("0022"), None, 'full', .5, .5, 1),
 13: (A/"acqua.jpg", (0,40,1080,1350), 'full', .5, .5, 1),
 14: (A/"file38168_3738c2c29540.jpeg", None, 'full', .45, .55, 1),
 15: (rec("0003"), None, 'full', .5, .5, 1.25),
 16: (rec("0011"), None, 'full', .5, .2, 1.05),
}
def photo(n):
    src, pre, mode, fx, fy, z = PH[n]
    im = Image.open(src).convert("RGB")
    if pre: im = im.crop(pre)
    W = 1080; H = 1350 if mode == 'full' else int(mode[1:]) if mode.startswith('h') else round(im.height*W/im.width)
    sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    g = ImageOps.grayscale(im.crop((l, t, l+W, t+H))); g = ImageOps.autocontrast(g, cutoff=1); g = ImageEnhance.Contrast(g).enhance(1.1)
    if sc > 1.3: g = g.filter(ImageFilter.UnsharpMask(radius=2, percent=50, threshold=3))
    g.save(IMG/f"img-{n:02d}.png"); return H
TOPFADE = lambda h: lg("to bottom", c(0,0), c(0, round(h*0.62/13.5)), c(.92, round(h*0.93/13.5)), c(1, round(h/13.5)))
S = {
 1: (lg("to bottom", c(.95,0), c(.55,22), c(0,36), c(0,56), c(.92,74), c(1,86)),
     '<div class="b" style="top:96px;left:70px;right:70px;text-align:center">'
     '<div class="big"><span class="ul">Hoje é o Dia do Vendedor,</span></div>'
     '<div class="s" style="margin-top:22px">e isso faz passar um filme na minha cabeça,<br>porque foi através das vendas que eu saí da feira<br>e me tornei um empresário que <span id="af">vendeu</span></div></div>'
     '<div class="b" style="bottom:96px;left:0;right:0;text-align:center"><div class="a" style="font-size:132px;line-height:.98"><span id="at">MAIS DE 7 BILHÕES</span><br>DE REAIS.</div></div>'),
 3: (None,
     '<div class="b" style="bottom:84px;left:50px;right:50px;text-align:center">'
     '<div class="s" style="font-size:38px">Fiz mais de</div>'
     '<div class="a" style="font-size:168px;line-height:.95;margin-top:4px">10 MIL</div>'
     '<div class="a" style="font-size:82px;line-height:1">DEMONSTRAÇÕES,</div>'
     '<div class="s" style="margin-top:12px"><i>anotadas cliente por cliente.</i></div>'
     '<div class="rule" style="margin:28px auto"></div>'
     '<div class="s" style="font-size:35px;white-space:nowrap">Chegou um ponto em que, só no aperto de mão do bom dia,</div>'
     '<div class="s r" style="font-size:50px;margin-top:6px">eu já sabia se ia vender ou não.</div></div>'),
 4: (None,
     '<div class="b" style="bottom:100px;left:60px;right:60px;text-align:center">'
     '<div class="s" style="font-size:39px">Tudo o que eu aprendi nessas portas virou livro:</div>'
     '<div class="s r" style="font-size:70px;line-height:1.08;font-style:italic;margin-top:22px">Você Nasceu Para<br>Vender Muito,</div>'
     '<div class="s r" style="font-size:44px;margin-top:10px">best-seller da Veja e da PublishNews.</div>'
     '<div class="rule" style="margin:40px auto 34px"></div>'
     '<div class="s">Escrevi pra mostrar que venda não é dom.</div>'
     '<div class="s" style="font-size:50px;font-weight:700;margin-top:6px">É técnica, e técnica se aprende.</div></div>'),
 5: (lg("to bottom", c(0,0), c(0,36), c(.9,54), c(1,62)),
     '<div class="b" style="bottom:108px;left:70px;width:300px;text-align:left">'
     '<div class="s" style="font-size:40px">Em</div><div class="a" style="font-size:168px;line-height:.92">1997</div></div>'
     '<div class="b" style="bottom:100px;left:400px;right:60px;text-align:left;border-left:4px solid #A91C20;padding-left:34px">'
     '<div class="s" style="font-size:36px">eu abri o meu escritório<br>em São José do Rio Preto<br>pra vender purificador de água.</div>'
     '<div class="s r" style="font-size:40px;margin-top:16px">600 reais de aluguel.</div>'
     '<div class="s" style="font-size:36px;margin-top:22px"><b>Quem vendia era eu.</b><br>Quem atendia o telefone<br>e cuidava de todo o resto<br><span class="ul">era a Regina, minha esposa.</span></div></div>'),
 6: (lg("to bottom", c(0,0), c(0,50), c(.9,64), c(1,70)),
     '<div class="b" style="bottom:90px;left:70px;right:70px;text-align:center">'
     '<div class="s">E por muito tempo eu achei<br>que era isso que fazia a empresa crescer:</div>'
     '<div class="rule" style="margin:30px auto"></div>'
     '<div class="s" style="font-size:62px;line-height:1.12;font-weight:700">vender cada vez mais,</div>'
     '<div class="s r" style="font-size:62px;line-height:1.12">aumentar o faturamento.</div></div>'),
 7: (lg("to right", c(1,0), c(.9,34), c(.35,58), c(0,72)) + "," + lg("to bottom", c(0,70), c(.6,100)),
     '<div class="b" style="top:0;bottom:0;left:76px;width:560px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="big" style="font-size:58px;line-height:1.1">Eu era um vendedor<br>excepcional.</div>'
     '<div class="s" style="margin-top:22px">Por isso a minha empresa<br>sempre faturou muito.</div>'
     '<div class="rule" style="margin:40px 0 30px"></div>'
     '<div class="s">E por isso mesmo</div>'
     '<div class="a" style="font-size:118px;line-height:1;margin-top:10px">SEMPRE<br>PERDI MUITO<br>DINHEIRO.</div></div>'),
 9: (lg("to left", c(1,0), c(.9,36), c(.35,58), c(0,70)) + "," + lg("to bottom", c(0,72), c(.6,100)),
     '<div class="b" style="top:0;bottom:0;right:76px;width:520px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="s">Todo problema de gestão<br>eu resolvia do mesmo jeito:</div>'
     '<div class="a" style="font-size:132px;line-height:.98;margin-top:16px">VENDENDO<br>MAIS.</div>'
     '<div class="rule" style="margin:40px 0 30px"></div>'
     '<div class="s" style="font-size:48px;font-weight:700">Tomava dois gols?</div>'
     '<div class="s r" style="font-size:48px">Saía pra fazer dois.</div></div>'),
 11: (lg("to bottom", c(.95,0), c(.6,20), c(0,34), c(0,58), c(.9,76), c(1,88)),
     '<div class="b" style="top:100px;left:70px;right:70px;text-align:center">'
     '<div class="big" style="font-size:56px">Se eu soubesse lá atrás<br>o que eu ensino hoje,</div>'
     '<div class="s" style="margin-top:14px">eu teria acumulado</div></div>'
     '<div class="b" style="bottom:96px;left:0;right:0;text-align:center">'
     '<div class="a" style="font-size:140px;line-height:1">10, TALVEZ<br>100 VEZES MAIS</div>'
     '<div class="s" style="margin-top:14px">do que eu acumulei.</div></div>'),
 12: (lg("to bottom", c(0,0), c(0,36), c(.9,52), c(1,60)),
     '<div class="b" style="bottom:100px;left:70px;right:70px;text-align:center">'
     '<div class="big fit" style="font-size:52px">Levei anos pra entender que vendedor</div><div class="big fit" style="font-size:52px">e empresário são profissões diferentes.</div>'
     '<div class="rule" style="margin:36px auto 30px"></div>'
     '<div class="s">O vendedor resolve tudo vendendo.</div>'
     '<div class="s r" style="margin-top:8px">O empresário cuida do lucro,<br>do crescimento e da cultura.</div></div>'),
 13: (lg("to bottom", c(.95,0), c(.75,22), c(0,36), c(0,56), c(.94,72), c(1,84)),
     '<div class="b" style="top:92px;left:76px;right:76px;text-align:left">'
     '<div class="s">Quando eu aprendi, a empresa que começou<br>num escritório de 600 reais<br><b>passou a vender sem depender de mim.</b></div></div>'
     '<div class="b" style="bottom:100px;left:76px;right:76px;text-align:left">'
     '<div class="s">Eu deixei de ser o melhor vendedor da empresa</div>'
     '<div class="a fit" style="font-size:138px;line-height:1;margin-top:10px">E VIREI O DONO DELA.</div></div>'),
 14: (lg("to bottom", c(0,0), c(0,38), c(.9,52), c(1,60)),
     '<div class="b" style="bottom:92px;left:70px;right:70px;text-align:center">'
     '<div class="s">O moleque que saiu da feira e estudou até os 15<br>fez MBA na FGV e hoje ensina dono de empresa.</div>'
     '<div class="rule" style="margin:34px auto 30px"></div>'
     '<div class="s" style="font-size:52px;font-weight:700">E eu continuo vendedor.</div>'
     '<div class="s" style="margin-top:6px">Só que hoje eu vendo</div>'
     '<div class="a" style="font-size:106px;line-height:1;margin-top:6px">PENSANDO COMO<br>EMPRESÁRIO.</div></div>'),
 15: (lg("to bottom", c(0,0), c(0,46), c(.9,60), c(1,68)),
     '<div class="b" style="bottom:100px;left:40px;right:40px;text-align:center">'
     '<div class="big fit" style="font-size:52px">Tudo o que eu levei 29 anos pra aprender</div><div class="big fit" style="font-size:52px">está no MBV, o meu treinamento pra dono de PME:</div>'
     '<div class="rule" style="margin:36px auto 30px"></div>'
     '<div class="s" style="font-size:44px;font-weight:700">Lucratividade, Crescimento e Cultura.</div>'
     '<div class="s r" style="margin-top:10px">A parte que a venda não resolve.</div></div>'),
 16: (lg("to bottom", c(0,0), c(0,46), c(.9,60), c(1,68)),
     '<div class="b" style="bottom:88px;left:70px;right:70px;text-align:center">'
     '<div class="big" style="font-size:58px">Feliz Dia do Vendedor.</div>'
     '<div class="s r" style="margin-top:8px">Principalmente pra você, dono,<br>que ainda resolve tudo vendendo mais.</div>'
     '<div class="rule" style="margin:28px auto 24px"></div>'
     '<div class="s">Quer aprender a parte que a venda não resolve?</div>'
     '<div class="a" style="font-size:140px;line-height:1;margin-top:8px">COMENTA MBV</div>'
     '<div class="s" style="font-size:36px;margin-top:8px">que eu te mando no direct o link da próxima turma.</div></div>'),
 10: (lg("to bottom", c(0,0), c(0,42), c(.9,56), c(1,64)),
     '<div class="b" style="bottom:92px;left:70px;right:70px;text-align:center">'
     '<div class="big" style="font-size:54px">E é o que a maioria dos donos<br>faz até hoje.</div>'
     '<div class="s" style="margin-top:14px">Em vez de aprender gestão,<br>pensa em vender mais.</div>'
     '<div class="rule" style="margin:32px auto 26px"></div>'
     '<div class="s">Só que venda em cima de empresa desarrumada<br>não resolve o problema.</div>'
     '<div class="a" style="font-size:170px;line-height:1;margin-top:8px">ACELERA.</div></div>'),
}
HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,600;1,700&family=Anton&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0B0B0B;font-family:'Source Serif Pro',serif}
.ph{position:absolute;left:0;top:0;width:1080px}.shade{position:absolute;inset:0}.b{position:absolute;z-index:2}
.s{font-size:42px;line-height:1.3;font-weight:600;color:#F3F3F3}.s b{font-weight:700}
.big{font-size:64px;line-height:1.12;font-weight:700;color:#F3F3F3}
.r{color:#A91C20;font-weight:700}
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
    html = HEAD + f'<div class="slide"><img class="ph" src="../imagens/v3/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div>' + JS + '</body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html); print(f"[{n:02d}] ok")
