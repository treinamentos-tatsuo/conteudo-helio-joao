"""Testes do modelo 'handmade' (Tatsuo Academy): 3 direcoes x 2 slides, desenho a lapis com rough.js + letra manuscrita.
Tema provisorio: o time que so se encontra no dia do jogo."""
import pathlib
OUT = pathlib.Path(__file__).parent
RED = '#A91C20'

DIRS = {
 'A-caderno': dict(
    bg="background:#F7F5EF;background-image:linear-gradient(#dedad0 1.5px,transparent 1.5px),linear-gradient(90deg,#dedad0 1.5px,transparent 1.5px);background-size:44px 44px;",
    extra="<div style='position:absolute;left:96px;top:0;bottom:0;width:3px;background:#A91C20;opacity:.55'></div>",
    ink='#262626', fill='#262626', fontT="'Caveat',cursive", fontB="'Patrick Hand',cursive", tw=700, ts=104, bs=40, hl='pen'),
 'B-folha-lisa': dict(
    bg="background:#F4F1EA;",
    extra="",
    ink='#3a3a3a', fill='#5a5a5a', fontT="'Kalam',cursive", fontB="'Kalam',cursive", tw=700, ts=86, bs=36, hl='marker'),
 'C-papel-na-mesa': dict(
    bg="background:#0f0f0f;",
    extra="<div class='folha' style='position:absolute;left:70px;top:90px;width:940px;height:1170px;background:#F6F3EC;transform:rotate(-1.2deg);box-shadow:0 18px 40px rgba(0,0,0,.6)'></div>"
          "<div style='position:absolute;left:430px;top:62px;width:220px;height:58px;background:rgba(235,230,215,.85);transform:rotate(-4deg);box-shadow:0 2px 6px rgba(0,0,0,.3)'></div>",
    ink='#2a2a2a', fill='#2a2a2a', fontT="'Gochi Hand',cursive", fontB="'Gochi Hand',cursive", tw=400, ts=80, bs=34, hl='pen'),
}

HEAD = """<!doctype html><html lang="pt-br"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Patrick+Hand&family=Kalam:wght@400;700&family=Gochi+Hand&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;%BG%}
.s::after{content:'';position:absolute;inset:0;pointer-events:none;opacity:.35;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .18 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.t{position:absolute;left:110px;width:860px;text-align:center;font-family:%FT%;font-weight:%TW%;font-size:%TS%px;line-height:1.02;color:%INK%}
.b{position:absolute;font-family:%FB%;font-size:%BS%px;line-height:1.25;color:%INK%}
.r{color:#A91C20}
.mk{background:linear-gradient(transparent 55%,rgba(169,28,32,.35) 55%,rgba(169,28,32,.35) 92%,transparent 92%);padding:0 6px}
svg{position:absolute;inset:0}
</style></head><body><div class="s">%EXTRA%<svg id="d" width="1080" height="1350">
<defs><filter id="pencil"><feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="2" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/><feGaussianBlur stdDeviation=".35"/></filter></defs><g id="g" filter="url(#pencil)"></g></svg>
%BODY%</div>
<script>
const svg=document.getElementById('d'), G=document.getElementById('g'), rc=rough.svg(svg);
const INK='%INK%', FILL='%FILL%', RED='#A91C20';
const o=(x={})=>Object.assign({stroke:INK,strokeWidth:3,roughness:1.6,bowing:1.6},x);
const add=n=>G.appendChild(n);
const line=(a,b,c,d,x)=>add(rc.line(a,b,c,d,o(x)));
const circ=(x,y,d,opt)=>add(rc.circle(x,y,d,o(opt)));
function arrow(x1,y1,x2,y2,opt){opt=Object.assign({stroke:RED,strokeWidth:4},opt||{});
  const mx=(x1+x2)/2+(y2-y1)*.18, my=(y1+y2)/2-(x2-x1)*.18;
  add(rc.curve([[x1,y1],[mx,my],[x2,y2]],o(opt)));
  const a=Math.atan2(y2-(my+y2)/2*0-my+ (y2-my)*0, x2-mx); const ang=Math.atan2(y2-my,x2-mx);
  for(const s of [-1,1]){const k=ang+Math.PI+s*.45; line(x2,y2,x2+30*Math.cos(k),y2+30*Math.sin(k),opt)}}
function boneco(x,y,s,pose){s=s||1;const h=34*s;circ(x,y,h*2,{fill:'none'});
  const ny=y+h, hy=y+h+70*s; line(x,ny,x,hy);
  const arms={neutro:[[-40,40],[40,40]],acena:[[-40,40],[38,-30]],perdido:[[-30,10],[30,10]],corre:[[-45,20],[40,55]],bracos:[[-50,-10],[50,-10]]}[pose||'neutro'];
  line(x,ny+22*s,x+arms[0][0]*s,ny+22*s+arms[0][1]*s); line(x,ny+22*s,x+arms[1][0]*s,ny+22*s+arms[1][1]*s);
  const legs=pose==='corre'?[[-40,55],[35,60]]:[[-25,70],[25,70]];
  line(x,hy,x+legs[0][0]*s,hy+legs[0][1]*s); line(x,hy,x+legs[1][0]*s,hy+legs[1][1]*s);}
function bola(x,y,d){circ(x,y,d,{fill:FILL,fillStyle:'hachure',hachureGap:7,fillWeight:1.5});}
function scribbleCircle(x,y,w,h){add(rc.ellipse(x,y,w,h,o({stroke:RED,strokeWidth:4,roughness:2.2})));add(rc.ellipse(x+4,y-3,w+10,h+6,o({stroke:RED,strokeWidth:3,roughness:2.6})));}
%SCRIPT%
</script></body></html>"""

SLIDES = {
 1: dict(body="""<div class="t" style="top:150px">Seu time só se<br>encontra no <span class="r">dia do jogo</span></div>
<div class="b" style="left:150px;top:1120px;width:780px;text-align:center">E depois ninguém entende por que a gente perde.</div>""",
 script="""
// calendario
add(rc.rectangle(150,430,780,150,o({strokeWidth:3})));
const dias=['SEG','TER','QUA','QUI','SEX','SÁB'];
dias.forEach((d,i)=>{const x=150+i*130; if(i) line(x,430,x,580,{strokeWidth:2});
  const t=document.createElementNS('http://www.w3.org/2000/svg','text');t.setAttribute('x',x+65);t.setAttribute('y',470);t.setAttribute('text-anchor','middle');
  t.setAttribute('font-family','Patrick Hand');t.setAttribute('font-size','30');t.setAttribute('fill',INK);t.textContent=d;svg.appendChild(t);
  if(i<5){line(x+40,505,x+90,555,{stroke:'#9a9a9a',strokeWidth:2});line(x+90,505,x+40,555,{stroke:'#9a9a9a',strokeWidth:2});}});
scribbleCircle(150+5*130+65,520,140,120);
// bonecos chegando de todo lado no sabado
boneco(260,720,1,'perdido'); boneco(430,700,1,'acena'); boneco(650,720,1,'neutro'); boneco(840,700,1,'corre');
bola(545,950,70);
arrow(260,860,470,940,{}); arrow(840,860,610,940,{});
"""),
 2: dict(body="""<div class="t" style="top:130px;font-size:%TS2%px">Treinar dá trabalho.<br><span class="r">Não treinar dá mais.</span></div>
<div class="b" style="left:740px;top:520px;width:240px">sem treino:<br><span class="mk">apaga incêndio</span><br>toda semana</div>
<div class="b" style="left:740px;top:900px;width:240px">com treino:<br>esforço<br>constante</div>
<div class="b" style="left:160px;top:1145px;width:760px;text-align:center">Quem puxa o treino é o <span class="r">dono</span>.</div>""",
 script="""
// eixos
line(150,1060,700,1060,{strokeWidth:3}); line(150,1060,150,430,{strokeWidth:3});
const tx=(s,x,y,sz,c,anc)=>{const t=document.createElementNS('http://www.w3.org/2000/svg','text');t.setAttribute('x',x);t.setAttribute('y',y);t.setAttribute('text-anchor',anc||'middle');t.setAttribute('font-family','Patrick Hand');t.setAttribute('font-size',sz||26);t.setAttribute('fill',c||INK);t.textContent=s;svg.appendChild(t)};
tx('trabalho',140,410,28,INK,'start'); tx('semanas →',620,1100,28);
// linha sem treino (picos)
add(rc.linearPath([[160,1000],[220,700],[270,960],[330,600],[380,980],[440,520],[500,990],[560,560],[620,1000],[690,480]],o({stroke:RED,strokeWidth:5,roughness:1.2})));
// linha com treino (constante)
add(rc.linearPath([[160,880],[690,880]],o({strokeWidth:4,strokeLineDash:[18,14]})));
arrow(735,600,690,520,{stroke:INK,strokeWidth:3}); arrow(735,935,690,890,{stroke:INK,strokeWidth:3});
"""),
}

for name, d in DIRS.items():
    for n, sl in SLIDES.items():
        html = HEAD
        for k, v in {'%BG%': d['bg'], '%EXTRA%': d['extra'], '%INK%': d['ink'], '%FILL%': d['fill'], '%FT%': d['fontT'], '%FB%': d['fontB'],
                     '%TW%': str(d['tw']), '%TS%': str(d['ts']), '%BS%': str(d['bs'])}.items():
            html = html.replace(k, v)
        body = sl['body'].replace('%TS2%', str(int(d['ts'] * .85)))
        if d['hl'] == 'pen':
            body = body.replace('class="mk"', 'class="r" style="text-decoration:underline wavy #A91C20;text-underline-offset:8px"')
        html = html.replace('%BODY%', body).replace('%SCRIPT%', sl['script'])
        (OUT / f'{name}_slide-{n}.html').write_text(html)
print('ok')
