"""Post J278 — isso não é comigo (modelo handmade, layout do J254). Peça 10 do Playbook Experiência 360°, p. 8. Fundos: C capa e CTA, B no resto."""
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
S[1] = ('C', """<div class="T" style="top:185px;font-size:60px;white-space:nowrap">A frase que mais destrói</div>
<div class="T" style="top:272px;font-size:100px;white-space:nowrap"><span class="r">O ATENDIMENTO</span></div>
<div class="P" style="top:1090px;font-size:40px;color:#A91C20;font-weight:700">entenda o que fazer no lugar &rarr;</div>""",
"""H.ellipse(560,560,560,150,{strokeWidth:3.5}); H.poly([[600,630],[650,720],[660,632]],{strokeWidth:3.5});
H.text('“Isso não é comigo.”',560,578,54,'#3a3a3a','middle',700);
H.rabisco(560,560,600,180);
H.boneco(700,790,1.3,'bracos');
H.boneco(300,830,1.1,'maos_cabeca'); H.text('?',300,745,54,'#3a3a3a','middle',700);
""")
# 2 organograma
S[2] = slide('O cliente não conhece<br>o seu organograma',
    'Para ele, a empresa é uma só. Quando o problema é de outra área e ninguém assume, ele sente que foi empurrado de um lado para o outro.',
    None,
"""const B=[[200,640,'vendas'],[700,640,'financeiro'],[450,980,'entrega']];
B.forEach(([x,y,t])=>{H.rect(x,y,200,84,{strokeWidth:3}); H.text(t,x+100,y+54,32,'#3a3a3a','middle',700);});
H.arrow(410,670,690,670,{strokeWidth:4},.18); H.arrow(790,735,640,975,{strokeWidth:4},.18); H.arrow(440,1010,290,735,{strokeWidth:4},.18);
H.boneco(550,780,.95,'maos_cabeca'); H.text('?',550,712,48,'#3a3a3a','middle',700);
H.text('“não é aqui...”',300,615,28,'#6a6a6a','middle'); H.text('“fala com o outro setor”',820,615,28,'#6a6a6a','middle');
""", -30)


# 3 escada
def passo(i, nome, desc, y):
    return (f'<div style="position:absolute;left:260px;top:{y}px;width:700px;text-align:left;font-family:Kalam,cursive">'
            f'<div style="font-size:44px;font-weight:700;color:#A91C20;line-height:1.1">{nome}</div>'
            f'<div style="font-size:33px;color:#3a3a3a;line-height:1.25;margin-top:6px">{desc}</div></div>')


PASSOS = [('RECEBI', 'O cliente sabe que o pedido chegou em alguém, e em quem.'),
          ('ASSUMI', 'Essa pessoa leva o assunto até o fim, mesmo que outra área execute.'),
          ('ACOMPANHEI', 'Segue o andamento sem esperar o cliente cobrar.'),
          ('AVISEI', 'Fecha a volta com o cliente.')]
YS = [330, 520, 710, 900]
S[3] = ('B', '<div class="T" style="top:130px;font-size:60px"><span class="r">Ser dono do problema<br>até o fim</span></div>'
        + ''.join(passo(i, n, d, y) for i, ((n, d), y) in enumerate(zip(PASSOS, YS))),
"""[330,520,710,900].forEach((y,i)=>{H.circle(185,y+30,78,{stroke:H.RED,strokeWidth:3.5}); H.text(String(i+1),185,y+46,44,H.RED,'middle',700);
  if(i<3) H.line(185,y+72,185,y+178,{strokeWidth:2.5,strokeLineDash:[10,10]});});
""")
# 4 o passo esquecido
S[4] = slide('O passo que quase<br>todo mundo esquece',
    'A solução foi aplicada, o caso foi encerrado e ninguém avisou o cliente. Para ele, o problema continua aberto.',
    'O problema só sai da mão de quem assumiu quando chega <span class="mk">resolvido na mão do cliente.</span>',
"""['recebi','assumi','acompanhei','avisei'].forEach((t,i)=>{const y=560+i*92;
  H.rect(320,y,56,56,{strokeWidth:3}); H.text(t,410,y+42,38,'#3a3a3a','start',700);
  if(i<3) H.poly([[330,y+28],[346,y+46],[372,y+8]],{stroke:H.RED,strokeWidth:4});});
H.rabisco(348,864,120,110); H.text('?',348,880,46,H.RED,'middle',700);
H.arrow(700,880,590,880,{strokeWidth:4},.0); H.text('o cliente',790,870,32,H.RED,'middle',700); H.text('não sabe',790,906,32,H.RED,'middle',700);
""", 20)
# 5 quem e o dono
S[5] = slide('Na sua empresa, quem é<br>dono do problema?',
    'Se a resposta é “depende de quem atendeu”, ninguém é. Quem assume o problema do cliente se define antes de ele aparecer, não no meio da confusão.',
    None,
"""H.rect(430,800,220,96,{strokeWidth:3}); H.text('o problema',540,858,32,'#3a3a3a','middle',700);
H.boneco(260,700,1,'aponta'); H.boneco(820,700,1,'aponta'); H.boneco(540,1000,1,'aponta');
H.arrow(330,740,770,760,{strokeWidth:3,stroke:'#3a3a3a'},-.12); H.arrow(840,850,600,1010,{strokeWidth:3,stroke:'#3a3a3a'},.15); H.arrow(480,1040,250,850,{strokeWidth:3,stroke:'#3a3a3a'},.15);
H.text('ninguém é',540,1200,46,H.RED,'middle',700);
""", -60)
# 6 CTA (C)
S[6] = ('C', """<div class="T" style="top:190px;font-size:60px;white-space:nowrap">O problema do seu cliente</div>
<div class="T" style="top:275px;font-size:100px;white-space:nowrap"><span class="r">TEM DONO?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')
