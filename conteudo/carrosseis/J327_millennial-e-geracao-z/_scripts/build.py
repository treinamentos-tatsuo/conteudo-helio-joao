"""Post J327 — millennial x geração Z (modelo handmade, layout do J317). Perfil Tatsuo Academy. Fundos: C capa e CTA, B no resto."""
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
S[1] = ('C', """<div class="T" style="top:165px;font-size:58px;white-space:nowrap">Você lidera millennial</div>
<div class="T" style="top:235px;font-size:58px;white-space:nowrap">e geração Z</div>
<div class="T" style="top:315px;font-size:96px;white-space:nowrap"><span class="r">DO MESMO JEITO?</span></div>
<div class="P" style="top:450px;font-size:32px;color:#6a6a6a">Por isso perde gente boa das duas idades. Veja as três diferenças.</div>
<div class="P" style="top:1110px;font-size:40px;color:#A91C20;font-weight:700">veja as diferenças &rarr;</div>""",
"""H.boneco(540,700,1.2,'segura'); H.rect(575,705,90,110,{strokeWidth:3,fill:H.RED,fillStyle:'hachure',hachureGap:9,stroke:H.RED}); H.text('manual',620,850,26,H.RED,'middle',700);
H.boneco(230,730,1.05,'neutro'); H.arrow(190,700,100,640,{strokeWidth:3},.1); H.text('35 anos',230,1000,32,'#3a3a3a','middle',700);
H.boneco(850,730,1.05,'neutro'); H.arrow(890,700,980,640,{strokeWidth:3},-.1); H.text('22 anos',850,1000,32,'#3a3a3a','middle',700);
""")
# 2 origens
S[2] = slide('Duas gerações,<br>dois começos',
    'O millennial entrou quando emprego era difícil: aguentou chefe ruim e pagou pedágio pra subir. A geração Z entrou com vaga sobrando e, antes de fazer, quer saber <b>por quê.</b>',
    'Nenhum dos dois está errado. <span class="mk">Começaram em mercados diferentes.</span>',
"""const st=[[140,960],[140,900],[210,900],[210,840],[280,840],[280,780],[350,780],[350,720],[420,720],[420,960]]; H.poly(st,{strokeWidth:3});
H.boneco(300,582,.8,'neutro'); H.rect(320,612,44,60,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'hachure',hachureGap:8});
H.text('millennial',280,1010,30,'#3a3a3a','middle',700);
H.line(540,600,540,980,{strokeWidth:2,strokeLineDash:[10,12]});
H.boneco(780,760,1,'neutro'); H.balao(800,650,230,84,'por quê?',36,H.RED,[790,725]);
H.text('geração Z',780,1010,30,H.RED,'middle',700);
""", 30)
# 3 retorno
S[3] = slide('1. O retorno',
    'O millennial espera a avaliação do fim do ano. O&nbsp;Z quer saber <b>nesta semana</b> se está indo bem.',
    'Quem guarda o retorno pra dezembro <span class="mk">perde o Z em agosto.</span>',
"""H.text('millennial',290,560,30,'#3a3a3a','middle',700);
H.rect(150,600,280,300,{strokeWidth:3}); H.line(150,660,430,660,{strokeWidth:3}); H.text('avaliação',290,645,28,'#3a3a3a','middle',700);
H.text('dezembro',290,800,44,'#3a3a3a','middle',700); H.rabisco(290,785,250,110);
H.line(540,560,540,940,{strokeWidth:2,strokeLineDash:[10,12]});
H.text('geração Z',790,560,30,H.RED,'middle',700);
for(let i=0;i<4;i++){const y=600+i*78; H.rect(650,y,280,62,{strokeWidth:2.6}); H.text('semana '+(i+1),720,y+42,26,'#3a3a3a','middle'); H.poly([[850,y+30],[868,y+48],[900,y+12]],{stroke:H.RED,strokeWidth:4});}
""", 20)
# 4 ordem
S[4] = slide('2. A ordem',
    'Pro millennial, a ordem clara basta. Pro Z, ordem sem o porquê parece <b>capricho do chefe.</b>',
    'Explicar o porquê não é mimo. <span class="mk">É o que faz ele acertar</span> <span class="mk">sem você olhando.</span>',
"""H.text('millennial',290,560,30,'#3a3a3a','middle',700);
H.rect(150,600,280,240,{strokeWidth:3}); H.circle(290,612,16,{fill:'#3a3a3a',fillStyle:'solid'}); H.text('faz isso.',290,740,44,'#3a3a3a','middle',700);
H.line(540,560,540,900,{strokeWidth:2,strokeLineDash:[10,12]});
H.text('geração Z',790,560,30,H.RED,'middle',700);
H.rect(650,600,280,240,{strokeWidth:3}); H.circle(790,612,16,{fill:'#3a3a3a',fillStyle:'solid'}); H.text('faz isso,',790,700,40,'#3a3a3a','middle',700);
H.text('porque...',790,770,40,H.RED,'middle',700); H.line(700,790,880,788,{stroke:H.RED,strokeWidth:3});
""", 30)
# 5 crescimento
S[5] = slide('3. O crescimento',
    'O millennial quer ver a escada: o próximo cargo e quando. O Z quer ver o que vai <b>aprender este mês.</b>',
    'Parou de aprender, <span class="mk">ele vai embora.</span>',
"""H.text('millennial',290,560,30,'#3a3a3a','middle',700);
H.poly([[130,930],[230,930],[230,840],[330,840],[330,750],[430,750]],{strokeWidth:3.5});
H.text('assistente',170,968,22,'#3a3a3a','middle'); H.text('analista',280,878,22,'#3a3a3a','middle'); H.text('gerente',380,788,22,'#3a3a3a','middle');
H.arrow(150,860,410,690,{strokeWidth:3,stroke:H.RED},-.1);
H.line(540,560,540,960,{strokeWidth:2,strokeLineDash:[10,12]});
H.text('geração Z',790,560,30,H.RED,'middle',700);
H.rect(650,600,280,330,{strokeWidth:3}); H.text('este mês:',790,660,32,H.RED,'middle',700);
['aprender','praticar','ensinar'].forEach((t,i)=>{const y=720+i*70; H.rect(675,y-26,34,34,{strokeWidth:2.4}); H.poly([[680,y-8],[692,y+4],[712,y-30]],{stroke:H.RED,strokeWidth:3.5}); H.text(t,730,y,30,'#3a3a3a','start');});
""", 20)
# 6 erro do dono
S[6] = slide('O erro do dono',
    'Escolher um jeito só de liderar e aplicar em todo mundo. Quase sempre é o jeito como <b>ele mesmo foi liderado.</b>',
    'E cada líder da empresa <span class="mk">repete o chefe que teve.</span>',
"""H.boneco(190,640,1.15,'aponta'); H.rect(262,690,52,34,{strokeWidth:3}); H.line(288,690,288,655,{strokeWidth:4}); H.text('dono',190,880,30,'#3a3a3a','middle',700);
[470,610,750,890].forEach(x=>{H.boneco(x,680,.85,'neutro'); H.rect(x-38,575,76,40,{stroke:H.RED,strokeWidth:3}); H.text('igual',x,604,24,H.RED,'middle',700);});
""", 30)
# 7 meta
S[7] = slide('A meta é a mesma',
    'Não é sobre agradar geração. <b>A meta é a mesma pros dois.</b>',
    'O que muda é o caminho <span class="mk">que você mostra pra cada um.</span>',
"""H.line(540,560,540,720,{strokeWidth:4}); H.poly([[540,560],[730,597],[540,634],[540,560]],{stroke:H.RED,strokeWidth:3.5});
H.text('META',615,608,28,H.RED,'middle',700);
H.curve([[230,960],[290,900],[250,840],[360,800],[450,760],[530,730]],{strokeWidth:3,strokeLineDash:[12,10]});
H.curve([[850,960],[790,900],[830,840],[720,800],[630,760],[550,730]],{strokeWidth:3,strokeLineDash:[12,10],stroke:H.RED});
H.boneco(120,800,.6,'neutro'); H.text('millennial',150,1010,28,'#3a3a3a','middle',700);
H.boneco(960,800,.6,'neutro'); H.text('geração Z',930,1010,28,H.RED,'middle',700);
""", 10)
# 8 CTA (C)
S[8] = ('C', """<div class="T" style="top:190px;font-size:60px;white-space:nowrap">A sua empresa sabe liderar</div>
<div class="T" style="top:275px;font-size:84px;white-space:nowrap"><span class="r">AS DUAS GERAÇÕES?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')


