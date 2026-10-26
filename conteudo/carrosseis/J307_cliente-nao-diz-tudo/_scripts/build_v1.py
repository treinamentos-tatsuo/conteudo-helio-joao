"""Post J307 — o cliente quase nunca diz tudo (modelo handmade, layout do J254). Peça 8 do Playbook Experiência 360°, p. 7. Fundos: C capa e CTA, B no resto."""
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



def miolo(n, titulo, por_tras, faz, script, dy=0):
    body = (f'<div class="T" style="top:130px;font-size:60px"><span class="r">{titulo}</span></div>'
            f'<div class="P" style="top:300px;font-size:38px"><b style="color:#3a3a3a">Pode estar dizendo:</b> {por_tras}</div>'
            f'<div class="P" style="top:1010px;font-size:30px;color:#8a8580">o que fazer:</div>'
            f'<div class="P2" style="font-size:42px">{faz}</div>')
    return ('B', body, script, dy)


S = {}
# 1 CAPA (C)
S[1] = ('C', """<div class="T" style="top:180px;font-size:58px;white-space:nowrap">O cliente quase nunca</div>
<div class="T" style="top:262px;font-size:118px;white-space:nowrap"><span class="r">DIZ TUDO.</span></div>
<div class="P" style="top:420px;font-size:34px;color:#6a6a6a">Ele mostra. Veja os quatro sinais que o seu time precisa aprender a ler.</div>
<div class="P" style="top:1110px;font-size:40px;color:#A91C20;font-weight:700">veja os sinais &rarr;</div>""",
"""H.boneco(540,720,1.3,'neutro'); H.balao(540,600,150,80,'...',40,'#3a3a3a',[540,668]);
const N=[[230,640,'o tom'],[850,640,'a pressa'],[230,950,'a pergunta 2x'],[850,950,'o sumiço']];
N.forEach(([x,y,t],i)=>{H.rect(x-120,y-42,240,84,{strokeWidth:2.6}); H.text(t,x,y+12,32,'#3a3a3a','middle',700);
  H.circle(x-120,y-42,46,{stroke:H.RED,strokeWidth:3}); H.text(String(i+1),x-120,y-30,30,H.RED,'middle',700);
  H.arrow(x<540?x+130:x-130,y,x<540?470:610,y<800?760:860,{strokeWidth:3},x<540?.12:-.12);});
""")
# 2 tom
S[2] = miolo(2, '1. O tom de voz<br>mudou',
    'algo incomodou, mesmo que ele não tenha dito o quê.',
    'Parar e perguntar se ficou alguma dúvida ou <span class="mk">algo que não agradou.</span>',
"""H.text('ontem',300,560,30,'#6a6a6a','middle'); H.balao(300,650,360,110,'Que ótimo, obrigado!',30,'#3a3a3a',[280,720]);
H.curve([[150,800],[200,780],[250,800],[300,780],[350,800],[400,780],[450,800]],{strokeWidth:3});
H.text('hoje',780,560,30,H.RED,'middle',700); H.balao(780,650,200,110,'Tá.',40,H.RED,[760,720]);
H.poly([[630,800],[660,770],[690,810],[720,760],[750,815],[780,765],[810,812],[840,768],[870,805],[900,780]],{stroke:H.RED,strokeWidth:3});
H.line(540,560,540,900,{strokeWidth:2,strokeLineDash:[10,12]});
""", 20)
# 3 pressa
S[3] = miolo(3, '2. Ele está<br>com pressa',
    'não há espaço para uma explicação longa agora.',
    'Ir direto ao ponto, confirmar o essencial e <span class="mk">combinar o resto por escrito.</span>',
"""H.boneco(260,700,1.25,'corre'); H.relogio(270,560,110);
H.rect(560,520,330,400,{strokeWidth:3}); for(let i=0;i<9;i++) H.line(590,560+i*38,860-(i%3)*40,560+i*38,{strokeWidth:2});
H.xis(725,720,110);
H.text('explicação longa',725,960,30,'#6a6a6a','middle');
""", 20)
# 4 duas vezes
S[4] = miolo(4, '3. Pergunta a mesma<br>coisa duas vezes',
    'a primeira resposta não ficou clara, ou ele não confiou nela.',
    'Explicar de outro jeito e <span class="mk">confirmar se agora ficou claro.</span>',
"""H.boneco(250,720,1.2,'neutro');
H.balao(560,590,300,96,'e o prazo?',36,'#3a3a3a',[330,660]); H.text('às 10h',800,600,28,'#6a6a6a','start');
H.balao(560,800,300,96,'e o prazo?',36,H.RED,[330,790]); H.text('às 16h',800,810,30,H.RED,'start',700);
H.rabisco(560,800,340,130);
""", 30)
# 5 sumiu
S[5] = miolo(5, '4. Sumiu depois<br>de contratar',
    'está perdido, sem tempo ou desanimado.',
    'Procurar o cliente antes que ele esfrie, <span class="mk">com uma ajuda concreta.</span>',
"""H.line(140,760,440,760,{strokeWidth:4}); H.line(440,760,940,760,{strokeWidth:3,strokeLineDash:[14,14]});
H.circle(200,760,22,{fill:'#3a3a3a',fillStyle:'solid'}); H.text('conversou',200,830,28,'#3a3a3a','middle');
H.circle(330,760,22,{fill:'#3a3a3a',fillStyle:'solid'}); H.text('negociou',330,830,28,'#3a3a3a','middle');
H.circle(440,760,30,{stroke:H.RED,strokeWidth:4}); H.poly([[428,760],[438,772],[456,746]],{stroke:H.RED,strokeWidth:4}); H.text('contratou',440,830,30,H.RED,'middle',700);
H.boneco(850,620,1,'neutro',{strokeLineDash:[8,10],stroke:'#9a958e'});
H.text('silêncio',690,720,34,'#6a6a6a','middle',700);
H.text('ninguém procurou',690,900,30,H.RED,'middle',700);
""", 20)
# 6 pergunta (B)
S[6] = ('B', """<div class="T" style="top:330px;font-size:64px">Qual sinal o seu cliente dá</div>
<div class="T" style="top:420px;font-size:72px"><span class="r">que o seu time <span class="u">costuma ignorar?</span></span></div>""",
"""H.boneco(540,830,1.3,'neutro'); H.text('?',600,740,70,H.RED,'middle',700);
""")
# 7 CTA (C)
S[7] = ('C', """<div class="T" style="top:190px;font-size:60px;white-space:nowrap">O seu time escuta</div>
<div class="T" style="top:275px;font-size:70px;white-space:nowrap"><span class="r">O QUE O CLIENTE NÃO DIZ?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')
