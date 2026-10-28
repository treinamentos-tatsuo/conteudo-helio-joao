"""Post J317 — Pepsi x Coca, margem (modelo handmade, layout do J254). Apostila p. 24 e pp. 27-28; números de 2025 conferidos. Fundos: C capa e CTA, B no resto."""
import pathlib
POST = pathlib.Path(__file__).resolve().parents[1]
LIB = (pathlib.Path(__file__).resolve().parents[4] / '.claude/skills/carrossel/modelos/handmade/lib.js').read_text(encoding='utf-8')
RED = '#A91C20'; INK = '#3a3a3a'

FUNDO = {
 'B': "background:#F4F1EA;",
 'A': "background:#F7F5EF;background-image:linear-gradient(#dedad0 1.5px,transparent 1.5px),linear-gradient(90deg,#dedad0 1.5px,transparent 1.5px);background-size:44px 44px;",
 'C': "background:#0f0f0f;",
}
FOLHA = ("<div style='position:absolute;left:70px;top:88px;width:940px;height:1174px;background:#F4F1EA;transform:rotate(-1.1deg);box-shadow:0 18px 40px rgba(0,0,0,.6)'></div>"
         "<div style='position:absolute;left:430px;top:60px;width:220px;height:58px;background:rgba(235,230,215,.88);transform:rotate(-4deg);box-shadow:0 2px 6px rgba(0,0,0,.3)'></div>")
MARGEM = "<div style='position:absolute;left:96px;top:0;bottom:0;width:3px;background:#A91C20;opacity:.55'></div>"

CSS = """*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;%BG%}
.s::after{content:'';position:absolute;inset:0;pointer-events:none;opacity:.35;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .18 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.c{position:absolute;inset:0;z-index:2}
.P{position:absolute;left:130px;width:820px;text-align:center;font-family:'Kalam',cursive;font-size:42px;line-height:1.32;color:#3a3a3a;text-wrap:balance}
.P b{color:#A91C20;font-weight:700}
.P2{position:absolute;left:130px;width:820px;bottom:150px;text-align:center;font-family:'Kalam',cursive;font-size:46px;font-weight:700;line-height:1.28;color:#3a3a3a;text-wrap:balance}
.P2.r{color:#A91C20}
.o{display:inline-block;margin:0 14px}
.T{position:absolute;left:120px;width:840px;text-align:center;font-family:'Kalam',cursive;font-weight:700;line-height:1.05;color:#3a3a3a}
.T .r{color:#A91C20}
.mk{white-space:nowrap;background:linear-gradient(transparent 55%,rgba(169,28,32,.33) 55%,rgba(169,28,32,.33) 92%,transparent 92%);padding:0 4px}
svg{position:absolute;inset:0}
"""


def page(n, fundo, body, script, dy=0):
    dx, dy = dy if isinstance(dy, tuple) else (0, dy)
    extra = FOLHA if fundo == 'C' else (MARGEM if fundo == 'A' else '')
    html = f"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.js"></script>
<style>{CSS.replace('%BG%', FUNDO[fundo])}</style></head><body><div class="s">{extra}
<svg id="d" width="1080" height="1350"><defs><filter id="pencil"><feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="2" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/><feGaussianBlur stdDeviation=".35"/></filter></defs><g id="g" filter="url(#pencil)" transform="translate({dx},{dy})"></g><g id="gt" transform="translate({dx},{dy})"></g><g id="gd" filter="url(#pencil)"></g></svg>
<div class="c">{body}</div></div>
<script>{LIB}
document.fonts.ready.then(()=>{{H.init('{INK}'); {script} H.decorar(); document.body.setAttribute('data-ok','1');}});
</script></body></html>"""
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html, encoding='utf-8')


def slide(titulo, texto, fecho, script, dy=0):
    body = (f'<div class="T" style="top:130px;font-size:60px"><span class="r">{titulo}</span></div>'
            + (f'<div class="P" style="top:300px;font-size:38px">{texto}</div>' if texto else '')
            + (f'<div class="P2" style="font-size:42px">{fecho}</div>' if fecho else ''))
    return ('B', body, script, dy)


S = {}
# 1 CAPA (C)
S[1] = ('C', """<div class="T" style="top:170px;font-size:58px;white-space:nowrap">A Pepsi fatura o dobro</div>
<div class="T" style="top:240px;font-size:58px;white-space:nowrap">da Coca-Cola.</div>
<div class="T" style="top:325px;font-size:100px;white-space:nowrap"><span class="r">E LUCRA MENOS.</span></div>
<div class="P" style="top:460px;font-size:32px;color:#6a6a6a">o motivo vale para qualquer empresa, inclusive a sua</div>""",
"""const base=1030;
H.line(150,base,500,base,{strokeWidth:3}); H.line(580,base,930,base,{strokeWidth:3});
H.rect(190,base-400,120,400,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'hachure',hachureGap:12,fillWeight:1.2});
H.rect(340,base-200,120,200,{stroke:H.RED,strokeWidth:3,fill:H.RED,fillStyle:'hachure',hachureGap:12,fillWeight:1.2});
H.text('Pepsi',250,base+42,30,'#3a3a3a','middle',700); H.text('Coca',400,base+42,30,H.RED,'middle',700);
H.text('faturamento',325,base+90,34,'#3a3a3a','middle',700);
H.rect(620,base-150,120,150,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'hachure',hachureGap:12,fillWeight:1.2});
H.rect(770,base-180,120,180,{stroke:H.RED,strokeWidth:3,fill:H.RED,fillStyle:'hachure',hachureGap:12,fillWeight:1.2});
H.text('Pepsi',680,base+42,30,'#3a3a3a','middle',700); H.text('Coca',830,base+42,30,H.RED,'middle',700);
H.text('lucro',755,base+90,34,'#3a3a3a','middle',700);
H.rabisco(830,base-100,180,200);
""")
# 2 numeros
S[2] = slide('Os números de 2025',
    'A Pepsi faturou <b>US$ 93,9 bilhões</b>. A Coca, <b>US$ 47,9 bilhões</b>.',
    'Vendendo a metade, a Coca <span class="mk">ficou com mais dinheiro.</span>',
"""H.text('lucro operacional',540,500,36,'#3a3a3a','middle',700);
H.text('o que sobra depois de fabricar, entregar e manter a estrutura',540,545,26,'#6a6a6a','middle');
const pie=(cx,cy,r,f,cor)=>{H.circle(cx,cy,r*2,{strokeWidth:3});
  const a0=-Math.PI/2,a1=a0+f*2*Math.PI; const x1=cx+r*Math.cos(a1),y1=cy+r*Math.sin(a1);
  H.path(`M${cx},${cy} L${cx},${cy-r} A${r},${r} 0 ${f>.5?1:0},1 ${x1.toFixed(0)},${y1.toFixed(0)} Z`,{stroke:cor,strokeWidth:3,fill:cor,fillStyle:'hachure',hachureGap:8,fillWeight:1.6});};
pie(300,720,120,.122,'#3a3a3a'); pie(780,720,120,.287,H.RED);
H.text('Pepsi',300,895,36,'#3a3a3a','middle',700); H.text('US$ 11,5 bi',300,940,32,'#3a3a3a','middle');
H.text('12 centavos de cada dólar',300,980,26,'#6a6a6a','middle');
H.text('Coca',780,895,36,H.RED,'middle',700); H.text('cerca de US$ 13,7 bi',780,940,32,H.RED,'middle',700);
H.text('29 centavos de cada dólar',780,980,26,H.RED,'middle');
""")
# 3 Coca
S[3] = slide('O jeito da Coca',
    'A Coca vende principalmente o xarope concentrado. Quem engarrafa e distribui, na maior parte, são parceiros independentes, donos das fábricas e dos caminhões.',
    'A estrutura pesada <span class="mk">fica com os parceiros.</span>',
"""H.rect(150,640,220,240,{stroke:H.RED,strokeWidth:3}); H.text('Coca',260,690,34,H.RED,'middle',700);
H.rect(220,730,80,120,{strokeWidth:3}); H.rect(240,710,40,24,{strokeWidth:2.5}); H.text('xarope',260,800,22,'#3a3a3a','middle',700);
H.arrow(390,760,520,760,{strokeWidth:4},0);
H.rect(540,600,390,330,{strokeWidth:2.5,strokeLineDash:[10,10]});
H.text('parceiro independente',735,640,28,'#3a3a3a','middle',700);
H.rect(570,720,160,120,{strokeWidth:3}); H.rect(600,670,30,50,{strokeWidth:2.5}); H.text('fábrica',650,790,24,'#3a3a3a','middle',700);
H.rect(760,760,110,70,{strokeWidth:3}); H.rect(870,780,40,50,{strokeWidth:3}); H.circle(790,840,30,{strokeWidth:2.5}); H.circle(890,840,30,{strokeWidth:2.5});
H.text('caminhão',830,900,24,'#3a3a3a','middle',700);
""", 20)
# 4 Pepsi
S[4] = slide('O jeito da Pepsi',
    'A Pepsi é, em boa parte, uma empresa de salgadinhos, e engarrafa boa parte das próprias bebidas. Isso exige mais fábricas, mais caminhões e mais armazéns.',
    'E toda essa estrutura <span class="mk">custa caro para manter.</span>',
"""H.boneco(540,820,1.25,'carrega');
[['armazém',420,727,240],['caminhão',440,669,200],['fábrica',430,611,220]].forEach(([t,x,y,w])=>{H.rect(x,y,w,58,{strokeWidth:2.8}); H.text(t,x+w/2,y+40,30,'#3a3a3a','middle',700);});
H.text('Pepsi',650,960,34,'#3a3a3a','start',700);
H.line(610,800,632,782,{stroke:H.RED,strokeWidth:3}); H.line(616,830,642,822,{stroke:H.RED,strokeWidth:3}); H.line(470,800,448,782,{stroke:H.RED,strokeWidth:3}); H.line(464,830,438,822,{stroke:H.RED,strokeWidth:3});
""", 0)
# 5 dois produtos
S[5] = slide('Na sua empresa,<br>acontece o mesmo',
    'Dois produtos vendidos a R$ 100 podem ter margens completamente diferentes.',
    'O faturamento é igual. <span class="mk">O resultado não.</span>',
"""const tag=(x,y,t)=>{H.path(`M${x-90},${y-40} L${x+60},${y-40} L${x+100},${y} L${x+60},${y+40} L${x-90},${y+40} Z`,{strokeWidth:3}); H.circle(x+60,y,14,{strokeWidth:2}); H.text(t,x-15,y+14,36,'#3a3a3a','middle',700);};
tag(300,560,'R$ 100'); tag(780,560,'R$ 100');
H.text('produto A',300,640,28,'#6a6a6a','middle'); H.text('produto B',780,640,28,'#6a6a6a','middle');
H.arrow(300,665,300,725,{strokeWidth:3,stroke:'#3a3a3a'},0); H.arrow(780,665,780,725,{strokeWidth:3,stroke:'#3a3a3a'},0);
H.rect(230,960-220,140,220,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'hachure',hachureGap:12,fillWeight:1.2});
H.rect(710,960-55,140,55,{stroke:H.RED,strokeWidth:3,fill:H.RED,fillStyle:'hachure',hachureGap:10,fillWeight:1.4});
H.line(150,960,930,960,{strokeWidth:2.5});
H.text('sobram R$ 60',300,1000,32,'#3a3a3a','middle',700); H.text('sobram R$ 15',780,1000,32,H.RED,'middle',700);
""", -20)
# 6 balanca
S[6] = slide('Vender mais não é<br>lucrar mais',
    'O lucro depende de quanto sobra de cada venda e do tamanho da estrutura que a empresa carrega para vender.',
    'Não é o preço na etiqueta que diz se a venda foi boa, <span class="mk">é quanto sobrou dela.</span>',
"""H.path('M500,900 L540,820 L580,900 Z',{strokeWidth:3}); H.line(420,900,660,900,{strokeWidth:3});
H.line(240,600,840,660,{strokeWidth:4}); H.line(540,630,540,820,{strokeWidth:3.5});
H.line(240,600,180,700,{strokeWidth:2}); H.line(240,600,300,700,{strokeWidth:2}); H.path('M170,700 Q240,750 310,700',{strokeWidth:3});
[[215,690],[245,690],[230,668]].forEach(([x,y])=>H.circle(x,y,28,{strokeWidth:2.4}));
H.line(840,660,780,760,{strokeWidth:2}); H.line(840,660,900,760,{strokeWidth:2}); H.path('M770,760 Q840,810 910,760',{strokeWidth:3});
H.rect(785,700,110,50,{stroke:H.RED,strokeWidth:2.6,fill:H.RED,fillStyle:'hachure',hachureGap:9}); H.rect(800,655,80,45,{stroke:H.RED,strokeWidth:2.6,fill:H.RED,fillStyle:'hachure',hachureGap:9});
H.text('o que sobra',240,800,30,'#3a3a3a','middle',700); H.text('de cada venda',240,836,30,'#3a3a3a','middle',700);
H.text('a estrutura',840,860,30,H.RED,'middle',700);
""", -40)
# 7 CTA (C)
S[7] = ('C', """<div class="T" style="top:190px;font-size:60px;white-space:nowrap">Você sabe quanto sobra</div>
<div class="T" style="top:275px;font-size:90px;white-space:nowrap"><span class="r">DE CADA VENDA?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')
