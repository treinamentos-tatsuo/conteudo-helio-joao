"""Post 254 — o cliente tem as suas razões (modelo handmade, layout do post "3 contas" da Tatsuo Academy). Texto v1 do Playbook Experiência 360°, p. 3. Fundos: C capa e CTA, B no resto."""
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



def miolo(n, titulo, por_tras, faz, script, dy=0):
    body = (f'<div class="T" style="top:130px;font-size:60px"><span class="r">{titulo}</span></div>'
            f'<div class="P" style="top:300px;font-size:38px"><b style="color:#3a3a3a">Por trás:</b> {por_tras}</div>'
            f'<div class="P" style="top:1010px;font-size:30px;color:#8a8580">o que a empresa faz:</div>'
            f'<div class="P2" style="font-size:42px">{faz}</div>')
    return ('B', body, script, dy)


S = {}
# 1 CAPA (C)
S[1] = ('C', """<div class="T" style="top:185px;font-size:56px;white-space:nowrap">O cliente não tem sempre razão.</div>
<div class="T" style="top:280px;font-size:90px;white-space:nowrap"><span class="r">MAS SEMPRE TEM</span></div>
<div class="T" style="top:375px;font-size:90px;white-space:nowrap"><span class="r">AS SUAS RAZÕES.</span></div>
<div class="T" style="top:492px;font-size:30px;font-weight:400;letter-spacing:.06em">4 COMPORTAMENTOS E O QUE ESTÁ POR TRÁS</div>""",
"""H.boneco(360,760,1.4,'aponta');
H.balao(300,630,170,96,'!!!',46,H.RED,[330,700]);
H.rabisco(365,860,240,390);
H.boneco(700,790,1.3,'maos_cabeca');
H.text('?',700,700,60,'#3a3a3a','middle',700); H.text('?',600,760,44,'#3a3a3a','middle',700); H.text('?',810,740,44,'#3a3a3a','middle',700);
H.text('ele erra...',780,1105,40,'#6a6a6a','middle');
H.text('mas por quê?',800,1160,46,H.RED,'middle',700);
""")
# 2 cobra varias vezes
S[2] = miolo(2, '1. Cobra a mesma resposta<br>várias vezes',
    'pressa, ou a sensação de que ninguém está cuidando do pedido dele.',
    'Dar um prazo claro e <span class="mk">avisar antes</span> de ele precisar perguntar de novo.',
"""H.rect(330,520,330,440,{strokeWidth:3.5}); H.rect(350,550,290,340,{strokeWidth:2});
H.circle(495,925,22,{strokeWidth:2});
H.rect(365,570,230,58,{strokeWidth:2.2}); H.text('e o meu pedido?',480,608,26,'#3a3a3a','middle');
H.rect(395,650,230,58,{strokeWidth:2.2}); H.text('alguém viu?',510,688,26,'#3a3a3a','middle');
H.rect(365,730,260,64,{stroke:H.RED,strokeWidth:3}); H.text('3ª vez que pergunto!',495,771,26,H.RED,'middle',700);
H.relogio(820,690,150); H.line(760,780,880,600,{stroke:H.RED,strokeWidth:4});
H.text('sem prazo',820,830,34,H.RED,'middle',700);
""")
# 3 reclama do combinado
S[3] = miolo(3, '2. Reclama do que<br>estava combinado',
    'uma expectativa diferente do que foi dito, criada na venda ou numa conversa anterior.',
    'Retomar o combinado com calma, <span class="mk">sem tom de quem ganhou</span> a discussão.',
"""H.boneco(250,710,1.1,'aponta');
H.balao(300,570,330,96,'fica pronto rapidinho!',27,'#3a3a3a',[265,650]);
H.text('o que ele ouviu',260,960,30,'#6a6a6a','middle');
H.text('≠',540,800,120,H.RED,'middle',700);
H.rect(660,560,250,330,{strokeWidth:3}); H.text('contrato',785,612,32,'#3a3a3a','middle',700);
[660,700,740].forEach(y=>H.line(690,y,880,y,{strokeWidth:2}));
H.text('prazo: 30 dias',785,820,32,H.RED,'middle',700); H.line(690,836,880,832,{stroke:H.RED,strokeWidth:3});
H.text('o que estava escrito',785,960,30,'#6a6a6a','middle');
""")
# 4 desconfiado
S[4] = miolo(4, '3. Chega desconfiado<br>e testando',
    'uma experiência ruim que ele já teve, com a sua empresa ou com outra.',
    'Mostrar com <span class="mk">fato e prazo</span>, não com promessa.',
"""H.boneco(270,780,1.3,'neutro');
H.circle(340,700,22,{strokeWidth:2.2}); H.circle(375,655,32,{strokeWidth:2.2});
H.ellipse(640,575,470,140,{strokeWidth:3}); H.text('da última vez, me enrolaram...',640,585,31,'#3a3a3a','middle',700);
H.rect(620,740,230,170,{strokeWidth:3}); H.path('M610,740 L735,680 L860,740',{strokeWidth:3});
H.rect(705,820,60,90,{strokeWidth:2.5}); H.xis(735,820,70);
H.text('outra empresa',735,955,28,'#6a6a6a','middle');
""")
# 5 pede o que nao contratou
S[5] = miolo(5, '4. Pede o que<br>não contratou',
    'não entendeu o que comprou, ou tem uma necessidade que ninguém perguntou.',
    'Explicar o que está incluído e <span class="mk">perguntar o que ele precisa</span> resolver.',
"""H.rect(200,560,380,360,{strokeWidth:3}); H.text('contratado',390,612,32,'#3a3a3a','middle',700);
[0,1,2].forEach(i=>{const y=690+i*80; H.poly([[235,y],[250,y+16],[276,y-16]],{stroke:H.RED,strokeWidth:3.5}); H.line(300,y,545,y,{strokeWidth:2.2});});
const b=H.boneco(770,770,1.2,'segura');
H.rect(b.maoD[0]-6,b.maoD[1]-46,100,82,{strokeWidth:3,strokeLineDash:[12,9]}); H.text('?',b.maoD[0]+44,b.maoD[1]+12,54,H.RED,'middle',700);
H.balao(760,600,260,92,'e isso aqui?',32,'#3a3a3a',[760,690]);
""")
# 6 fecho
S[6] = ('B', """<div class="T" style="top:150px;font-size:56px">Quem enxerga a razão do cliente</div>
<div class="T" style="top:225px;font-size:56px">para de discutir com ele</div>
<div class="T" style="top:310px;font-size:70px"><span class="r">e começa a <span class="u">resolver com ele.</span></span></div>""",
"""H.boneco(200,700,1.05,'aponta'); H.boneco(420,700,1.05,'maos_cabeca');
H.xis(310,610,42);
H.text('discutir',310,960,36,'#6a6a6a','middle',700);
H.line(540,600,540,980,{strokeWidth:2,strokeLineDash:[10,12]});
H.boneco(640,700,1.05,'aponta'); H.boneco(740,700,1.05,'aponta');
H.rect(825,690,150,100,{strokeWidth:3}); H.text('o',900,730,28,'#3a3a3a','middle',700); H.text('problema',900,764,28,'#3a3a3a','middle',700);
H.text('resolver junto',740,960,36,H.RED,'middle',700);
""")
# 7 CTA (C)
S[7] = ('C', """<div class="T" style="top:190px;font-size:62px;white-space:nowrap">O seu time discute</div>
<div class="T" style="top:275px;font-size:92px;white-space:nowrap"><span class="r">OU RESOLVE?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')
