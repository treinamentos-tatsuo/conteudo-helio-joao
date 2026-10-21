"""Post J276 — o cliente crítico (modelo handmade, layout do J254). Peça 16 do Playbook Experiência 360°, p. 14. Fundos: C capa e CTA, B no resto."""
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


# balao de grito (contorno em zigue-zague)
SPIKY = """function spiky(cx,cy,rx,ry,n,opt){let d='';for(let i=0;i<n;i++){const a=i*2*Math.PI/n,k=i%2?1.22:1;d+=(i?' L':'M')+(cx+Math.cos(a)*rx*k).toFixed(0)+','+(cy+Math.sin(a)*ry*k).toFixed(0);}H.path(d+' Z',opt);}
"""
S = {}
# 1 CAPA (C)
S[1] = ('C', """<div class="T" style="top:180px;font-size:64px;white-space:nowrap">O cliente crítico</div>
<div class="T" style="top:268px;font-size:88px;white-space:nowrap"><span class="r">QUER SER LEVADO</span></div>
<div class="T" style="top:362px;font-size:88px;white-space:nowrap"><span class="r">A SÉRIO.</span></div>
<div class="P" style="top:480px;font-size:32px;color:#6a6a6a">quase sempre existe uma experiência ruim por trás do tom alto</div>""",
SPIKY + """spiky(360,665,200,62,30,{stroke:H.RED,strokeWidth:3});
H.text('VOCÊS SEMPRE...!',360,678,34,H.RED,'middle',700);
H.poly([[330,735],[310,790],[360,742]],{stroke:H.RED,strokeWidth:3});
H.boneco(300,850,1.3,'aponta');
H.boneco(760,900,1.05,'maos_cabeca'); H.text('...',760,820,44,'#3a3a3a','middle',700);
""")
# 2 reconhecer
S[2] = slide('Como reconhecer',
    'Sobe o tom e parte para o ataque, reclama de tudo várias vezes, generaliza e ameaça cancelar ou expor a empresa.',
    'Ele é quem mais mostra <span class="mk">onde a experiência</span> <span class="mk">pode melhorar.</span>',
SPIKY + """H.boneco(540,700,1.25,'aponta');
spiky(300,560,180,52,26,{strokeWidth:2.6}); H.text('vocês nunca cumprem!',300,570,26,'#3a3a3a','middle',700);
spiky(810,600,140,50,24,{strokeWidth:2.6}); H.text('vou cancelar!',810,610,28,H.RED,'middle',700);
spiky(800,880,160,50,24,{strokeWidth:2.6}); H.text('vou postar isso!',800,890,28,H.RED,'middle',700);
""", 30)
# 3 deixar terminar
S[3] = slide('1. Deixar terminar',
    'Não interromper o primeiro desabafo.',
    'Quem é interrompido <span class="mk">sobe o tom</span> para ser ouvido.',
"""H.ellipse(340,540,420,150,{strokeWidth:3}); H.poly([[300,612],[285,680],[350,615]],{strokeWidth:3});
for(let i=0;i<3;i++){const y=505+i*34; H.poly([[190+i*10,y],[230,y-8],[270,y+6],[310,y-6],[350,y+8],[390,y-4],[440,y+4],[480-i*20,y]],{strokeWidth:2.2,roughness:1.8});}
H.boneco(300,720,1.2,'aponta');
const b=H.boneco(760,720,1.2,'segura');
H.rect(b.maoD[0]-4,b.maoD[1]-60,90,110,{strokeWidth:2.6}); [0,1,2,3].forEach(i=>H.line(b.maoD[0]+8,b.maoD[1]-36+i*22,b.maoD[0]+74,b.maoD[1]-36+i*22,{strokeWidth:1.8}));
H.text('ouve e anota',790,1000,32,H.RED,'middle',700);
""", -20)
# 4 reconhecer o que sente
S[4] = slide('2. Reconhecer<br>o que ele sente',
    'Antes de explicar qualquer coisa.',
    'Explicação antes disso <span class="mk">soa como defesa.</span>',
"""const row=(y,a,b,ok)=>{H.rect(150,y,320,96,{strokeWidth:3}); H.text(a,310,y+60,32,'#3a3a3a','middle',700);
  H.arrow(490,y+48,590,y+48,{strokeWidth:4,stroke:ok?H.RED:'#3a3a3a'},0);
  H.rect(610,y,320,96,{strokeWidth:3}); H.text(b,770,y+60,32,'#3a3a3a','middle',700);};
row(560,'1. reconhecer','2. explicar',true);
H.poly([[930,500],[950,525],[990,470]],{stroke:H.RED,strokeWidth:5});
row(780,'1. explicar','2. reconhecer',false);
H.xis(540,828,90);
""", 10)
# 5 fato x emocao
S[5] = slide('3. Separar fato<br>de emoção',
    'Anotar os fatos concretos da reclamação e responder a cada um.',
    'Responder aos fatos, <span class="mk">um por um, com prazo.</span>',
"""H.ellipse(310,700,400,320,{strokeWidth:3});
H.text('vocês nunca cumprem!',310,620,26,'#6a6a6a','middle');
H.text('que absurdo!',310,680,26,'#6a6a6a','middle');
H.text('a tutoria foi',310,748,28,'#3a3a3a','middle',700); H.text('remarcada 2 vezes',310,784,28,'#3a3a3a','middle',700);
H.line(200,798,420,794,{stroke:H.RED,strokeWidth:3.5});
H.arrow(520,720,620,720,{strokeWidth:4},0);
H.rect(640,540,300,330,{strokeWidth:3}); H.text('fato',790,592,34,'#3a3a3a','middle',700);
H.text('tutoria remarcada',790,650,26,'#3a3a3a','middle'); H.text('2 vezes',790,682,26,'#3a3a3a','middle');
H.arrow(790,705,790,765,{strokeWidth:3},0);
H.text('nova data:',790,800,28,'#3a3a3a','middle'); H.text('quinta, 10h',790,840,32,H.RED,'middle',700);
""", 20)
# 6 compromisso
S[6] = slide('4. Fechar com<br>compromisso',
    'Dizer o que vai acontecer, quem faz e quando ele terá notícia.',
    'E cumprir <span class="mk">antes do prazo.</span>',
"""const cx=320,cy=740,r=135; H.circle(cx,cy,r*2,{strokeWidth:3.5});
for(let i=0;i<12;i++){const a=i*Math.PI/6; H.line(cx+Math.cos(a)*r*.84,cy+Math.sin(a)*r*.84,cx+Math.cos(a)*r*.94,cy+Math.sin(a)*r*.94,{strokeWidth:2});}
const ah=(-90+9.67*30)*Math.PI/180, am=(-90+40*6)*Math.PI/180;
H.line(cx,cy,cx+Math.cos(ah)*r*.5,cy+Math.sin(ah)*r*.5,{strokeWidth:5}); H.line(cx,cy,cx+Math.cos(am)*r*.75,cy+Math.sin(am)*r*.75,{strokeWidth:4});
H.text('prometido: 10h',760,680,36,'#3a3a3a','middle',700);
H.text('retorno: 9h40',760,770,42,H.RED,'middle',700);
H.poly([[600,760],[622,786],[660,730]],{stroke:H.RED,strokeWidth:5});
H.line(640,800,880,796,{stroke:H.RED,strokeWidth:3});
""", 10)


# 7 frases
def col(x, itens):
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:360px;text-align:left;font-family:Kalam,cursive;'
                   f'font-size:33px;line-height:1.25;color:#3a3a3a">{t}</div>' for t, y in itens)


S[7] = ('B', '<div class="T" style="top:130px;font-size:60px"><span class="r">Frases que ajudam<br>e frases que afastam</span></div>'
        '<div class="T" style="top:340px;left:150px;width:380px;font-size:40px;text-align:left">AJUDAM</div>'
        '<div class="T" style="top:340px;left:610px;width:340px;font-size:40px;text-align:left"><span class="r">AFASTAM</span></div>'
        + col(190, [('“Você tem razão de estar chateado com isso.”', 430), ('“Deixa eu entender exatamente o que aconteceu.”', 640),
                    ('“Até amanhã às 10h eu retorno com a solução.”', 850)])
        + col(650, [('“Calma.”', 430), ('“Não é bem assim.”', 640), ('“Isso não é comigo.”', 850)]),
"""[455,665,875].forEach(y=>{H.poly([[150,y],[164,y+16],[186,y-14]],{stroke:'#3a3a3a',strokeWidth:4}); H.xis(625,y,14,{strokeWidth:4});});
H.line(560,350,560,1060,{strokeWidth:2,strokeLineDash:[10,12]});
""")
# 8 CTA (C)
S[8] = ('C', """<div class="T" style="top:190px;font-size:64px;white-space:nowrap">O seu time ouve</div>
<div class="T" style="top:275px;font-size:92px;white-space:nowrap"><span class="r">OU SE DEFENDE?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')

