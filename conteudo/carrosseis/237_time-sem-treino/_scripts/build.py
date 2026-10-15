"""Post 237 — time sem treino (modelo handmade). Copy v4 aprovada em 14/10. Fundos: C capa e CTA, A no grafico (slide 7), B no resto."""
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
.mk{background:linear-gradient(transparent 55%,rgba(169,28,32,.33) 55%,rgba(169,28,32,.33) 92%,transparent 92%);padding:0 4px}
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


S = {}
# 1 CAPA (C)
S[1] = ('C', """<div class="T" style="top:170px;left:110px;width:860px;font-size:64px;white-space:nowrap">Você cobra gol de um time</div>
<div class="T" style="top:262px;font-size:86px;white-space:nowrap"><span class="r">QUE NUNCA TREINOU.</span></div>""",
"""H.rect(340,450,600,680,{strokeWidth:3});
H.rect(810,650,130,280,{strokeWidth:2.5}); H.rect(940,720,34,140,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'cross-hatch',hachureGap:12,fillWeight:.8});
H.boneco(220,720,1.45,'aponta');
H.balao(250,560,220,110,'CHUTA!',44,H.RED,[225,650]);
H.rabisco(222,820,200,340);
H.boneco(470,600,1,'maos_cabeca'); H.text('?',470,535,56,'#3a3a3a','middle',700);
H.boneco(660,800,1,'neutro'); H.text('?',660,735,56,'#3a3a3a','middle',700);
H.boneco(480,920,1,'acena'); H.text('?',480,855,56,'#3a3a3a','middle',700);
H.boneco(740,560,1,'neutro');
H.bola(600,1070,44);
""")
# 2 vestiario (B)
S[2] = ('B', """<div class="P" style="top:150px">Imagina um time de futebol que só se encontra no vestiário, <span class="u">dez minutos antes do jogo</span>.</div>
<div class="P2">Ninguém treinou passe, ninguém combinou jogada.</div>""",
"""H.relogio(540,640,150);
H.line(140,1110,940,1110,{strokeWidth:3});
[200,330,460,620,750,880].forEach((x,i)=>H.boneco(x,960,.9,['neutro','acena','neutro','maos_cabeca','neutro','acena'][i]));
H.text('quem é você?',330,885,32,'#3a3a3a','middle'); H.text('eu jogo onde?',750,885,32,'#3a3a3a','middle');
""", -150)
# 3 goleada (B)
S[3] = ('B', """<div class="P" style="top:140px">O técnico manda entrar em campo e cada um corre pra um lado. O time toma de goleada e a <span class="u">culpa cai no jogador</span>.</div>
<div class="P2">E a sua empresa joga assim <span class="mk">todo santo dia.</span></div>""",
"""H.campo(140,600,800,440);
const P=[[300,760],[420,900],[560,700],[680,880],[820,760]];
const D=[[-90,-60],[-80,70],[30,-90],[90,60],[80,-70]];
P.forEach(([x,y],i)=>{H.boneco(x,y-40,.55,'corre'); H.arrow(x,y+30,x+D[i][0],y+30+D[i][1],{strokeWidth:3},.3);});
H.bola(540,980,34);
H.rect(380,1080,320,90,{strokeWidth:3}); H.text('0  x  7',540,1142,56,H.RED,'middle',700);
""", -170)
# 4 balcao (B)
S[4] = ('B', """<div class="P" style="top:140px">O funcionário entra, alguém explica <span class="u">em meia hora</span> e ele já vai atender. Promete o que não pode, erra o pedido.</div>
<div class="P2">E quem paga é o cliente que você levou <span class="mk">anos pra conquistar.</span></div>""",
"""H.balcao(160,960,760);
H.boneco(360,760,1.15,'segura'); H.boneco(760,760,1.15,'neutro');
H.balao(330,610,320,110,'entrego amanhã!',30,'#3a3a3a',[350,690]);
H.rect(470,880,110,80,{strokeWidth:3}); H.text('pedido',525,932,24,'#3a3a3a','middle'); H.xis(525,920,52);
H.rabisco(760,830,190,260); H.text('cliente há 15 anos',760,1110,34,H.RED,'middle',700);
""", -150)
# 5 incendio (B)
S[5] = ('B', """<div class="P" style="top:140px">Aí o telefone toca e quem entra em campo é <span class="o">você.</span> Você refaz o orçamento, liga pro cliente, pede desculpa e resolve.</div>
<div class="P2 r"><span class="u2">Toda semana, o mesmo incêndio.</span></div>""",
"""H.celular(170,620,120,210); H.text('cliente',230,712,24,'#3a3a3a','middle',700); H.text('chamando',230,742,20,'#3a3a3a','middle');
H.boneco(470,690,1.1,'corre');
H.arrow(310,700,400,720,{strokeWidth:3},.2);
['sem 1','sem 2','sem 3','sem 4'].forEach((s,i)=>{const x=615+i*115; H.chama(x,880,1.1); H.line(x-36,884,x+36,884,{strokeWidth:2.5}); H.text(s,x,925,28,'#3a3a3a','middle');});
""", (-30, -56))
# 6 ciclo (B)
S[6] = ('B', """<div class="P" style="top:140px">E o pior: <span class="u">ele está aprendendo</span>. Cada vez que você resolve no lugar dele, ele aprende que não precisa resolver.</div>
<div class="P2">O time aprende exatamente o que você <span class="mk">deixa acontecer.</span></div>""",
"""H.line(130,1060,950,1060,{strokeWidth:3});
// funcionario folgado na cadeira
H.line(250,820,250,1060,{strokeWidth:3}); H.line(250,920,360,920,{strokeWidth:3}); H.line(355,920,355,1060,{strokeWidth:3});
H.boneco(300,800,1.2,'relax');
H.circle(380,740,14,{strokeWidth:2}); H.circle(405,705,20,{strokeWidth:2});
H.ellipse(500,630,260,104,{strokeWidth:3}); H.text('o chefe resolve',500,641,32,'#3a3a3a','middle',700);
// dono carregando tudo
H.boneco(760,830,1.2,'carrega');
[['orçamento',670,742,180],['pedido',685,692,150],['cliente bravo',660,642,200]].forEach(([t,x,y,w])=>{H.rect(x,y,w,48,{strokeWidth:2.5}); H.text(t,x+w/2,y+34,28,'#3a3a3a','middle',700);});
H.line(830,800,846,786,{stroke:H.RED,strokeWidth:3}); H.line(836,826,856,820,{stroke:H.RED,strokeWidth:3}); H.line(684,800,668,786,{stroke:H.RED,strokeWidth:3});
""", -127)
# 7 grito + grafico (A)
S[7] = ('A', """<div class="P" style="top:140px;font-size:38px">E você deixa, porque treinar dá trabalho e tempo é a coisa que você menos tem</div>
<div class="T" style="top:300px;font-size:66px"><span class="r">MAS NÃO TREINAR DÁ MUITO MAIS</span></div>""",
"""H.line(170,1110,720,1110,{strokeWidth:3}); H.line(170,1110,170,560,{strokeWidth:3});
H.text('trabalho',160,545,28,'#3a3a3a','start'); H.text('semanas →',650,1150,28,'#3a3a3a','middle');
H.poly([[180,1060],[240,800],[290,1020],[350,740],[400,1030],[460,680],[520,1040],[580,700],[640,1050],[710,620]],{stroke:H.RED,strokeWidth:5,roughness:1.2});
H.poly([[180,950],[710,950]],{strokeWidth:4,strokeLineDash:[18,14]});
H.arrow(760,700,712,640,{stroke:'#3a3a3a',strokeWidth:3}); H.text('sem treino:',770,730,32,'#3a3a3a','start'); H.text('incêndio',770,772,32,H.RED,'start',700); H.text('toda semana',770,814,32,'#3a3a3a','start');
H.arrow(760,1000,712,958,{stroke:'#3a3a3a',strokeWidth:3}); H.text('com treino:',770,1030,32,'#3a3a3a','start'); H.text('esforço',770,1072,32,'#3a3a3a','start'); H.text('constante',770,1114,32,'#3a3a3a','start');
""")
# 8 senior (B)
S[8] = ('B', """<div class="P" style="top:150px">E amigão, empresa pequena não tem dinheiro pra pagar <span class="u">funcionário sênior</span>, não.</div>
<div class="P2">Quem chega aqui chega cru, e o que deixa ele bom é o <span class="mk">treino.</span></div>""",
"""H.path('M380,580 L660,580 L710,640 L660,700 L380,700 Z',{strokeWidth:3}); H.circle(680,640,16,{strokeWidth:2.5});
H.text('sênior',520,656,48,'#3a3a3a','middle',700); H.line(370,668,700,612,{stroke:H.RED,strokeWidth:6,roughness:1.8});
H.text('não cabe no seu caixa',540,770,32,H.RED,'middle',700);
H.boneco(250,900,1,'neutro'); H.text('dia 1',250,1110,32,'#3a3a3a','middle',700);
H.arrow(360,980,720,980,{strokeWidth:5},.08);
[420,480,540,600,660].forEach(x=>H.line(x,955,x,1000,{strokeWidth:2.5}));
H.boneco(830,880,1.15,'bracos'); H.text('dia 180',830,1110,32,'#3a3a3a','middle',700);
H.path('M830,730 L840,758 L870,758 L846,776 L855,804 L830,787 L805,804 L814,776 L790,758 L820,758 Z',{stroke:H.RED,strokeWidth:3,fill:H.RED,fillStyle:'hachure',hachureGap:6});
""", -170)
# 9 formula (B)
S[9] = ('B', """<div class="P" style="top:150px">É ensinar, repetir, <span class="u">repetir de novo</span> e reconhecer quando ele acerta,</div>
<div class="P2">acompanhando <span class="u">todo dia</span> até aquilo virar <span class="mk">o jeito da sua empresa trabalhar.</span></div>""",
"""const D=['S','T','Q','Q','S'];
D.forEach((d,i)=>H.text(d,230+i*85,600,28,'#3a3a3a','middle',700));
for(let r=0;r<4;r++){ H.text('sem '+(r+1),150,666+r*80,22,'#3a3a3a','middle');
  D.forEach((d,i)=>{const x=230+i*85,y=620+r*80; H.rect(x-32,y,64,64,{strokeWidth:2.2}); H.poly([[x-16,y+34],[x-4,y+48],[x+20,y+14]],{stroke:H.RED,strokeWidth:3.5});});}
H.line(640,960,960,960,{strokeWidth:3});
H.boneco(720,780,1.05,'acena'); H.boneco(880,790,1,'bracos');
H.balao(700,640,180,92,'isso!',40,H.RED,[715,700]);
""", -96)
# 10 dono com apito (B)
S[10] = ('B', """<div class="P" style="top:140px">E numa empresa de dono, quem marca esse treino é <span class="o">você,</span> porque se o dono não marcar, ninguém marca por ele.</div>
<div class="P2">O seu time vai evoluir exatamente <span class="mk">pra onde você treinar.</span></div>""",
"""H.rect(130,560,820,600,{strokeWidth:3});
H.rect(790,700,160,320,{strokeWidth:2.5}); H.rect(890,790,60,140,{strokeWidth:2.5});
H.rect(950,800,36,120,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'cross-hatch',hachureGap:12,fillWeight:.8});
const b=H.boneco(240,700,1.1,'apito'); H.circle(b.maoD[0]+4,b.maoD[1]-10,18,{strokeWidth:2.5});
H.text('priii!',310,660,32,H.RED,'start',700); H.rabisco(240,770,190,280);
[[420,1100],[500,1100],[580,1100],[660,1100]].forEach(([x,y])=>H.cone(x,y,1));
const J=[[430,820],[580,920],[700,790]];
J.forEach(([x,y])=>H.boneco(x,y,.8,'corre'));
H.poly([[460,920],[560,990]],{strokeWidth:2.5,strokeLineDash:[10,10]}); H.poly([[610,990],[690,890]],{strokeWidth:2.5,strokeLineDash:[10,10]});
H.bola(470,935,28);
H.arrow(740,880,900,860,{strokeWidth:5},.15);
""", -170)
# 11 CTA (C)
S[11] = ('C', """<div class="P" style="top:250px;font-size:44px">No MBV, imersão de três dias para donos de pequenas e médias empresas, você aprende gestão, inclusive gestão de pessoas, nos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,780,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,786,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,862,46,H.RED,'middle',700);
H.arrow(540,1080,540,940,{strokeWidth:4},.0); H.text('link na bio',540,1130,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')
