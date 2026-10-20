"""Post J267 — o cliente que não volta (modelo handmade, layout do J254). Texto v2 com os números conferidos (Zendesk 82%, Accenture 3x). Fundos: C capa e CTA, B no resto."""
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



def slide(titulo, texto, fonte, fecho, script, dy=0):
    body = (f'<div class="T" style="top:130px;font-size:60px"><span class="r">{titulo}</span></div>'
            + (f'<div class="P" style="top:300px;font-size:38px">{texto}</div>' if texto else '')
            + (f'<div class="P" style="top:{fonte[1]}px;font-size:26px;color:#8a8580">{fonte[0]}</div>' if fonte else '')
            + f'<div class="P2" style="font-size:42px">{fecho}</div>')
    return ('B', body, script, dy)


S = {}
# 1 CAPA (C)
S[1] = ('C', """<div class="T" style="top:185px;font-size:56px;white-space:nowrap">A maioria dos clientes não reclama.</div>
<div class="T" style="top:280px;font-size:104px;white-space:nowrap"><span class="r">SÓ NÃO VOLTA.</span></div>""",
"""H.rect(170,560,420,420,{strokeWidth:3}); H.path('M150,560 L380,470 L610,560',{strokeWidth:3});
H.text('LOJA',380,535,30,'#3a3a3a','middle',700);
H.rect(200,850,360,70,{strokeWidth:3,fill:'#3a3a3a',fillStyle:'hachure',hachureGap:14,fillWeight:1});
H.boneco(300,700,1,'neutro'); H.balao(300,610,170,70,'próximo!',26,'#3a3a3a',[300,660]);
H.rect(470,700,80,150,{strokeWidth:2.5});
H.boneco(790,720,1.25,'corre'); H.arrow(860,900,960,900,{strokeWidth:4},0);
H.rabisco(795,800,200,330);
H.text('ninguém ficou sabendo...',560,1130,44,H.RED,'middle',700);
""")
# 2 82%
S[2] = slide('O atendimento decide<br>a próxima compra',
    '<b>82%</b> dos brasileiros tomam decisões de compra pela qualidade do atendimento.',
    ('(Zendesk, CX Trends 2022)', 410),
    'A primeira venda o produto faz. <span class="mk">A segunda depende</span> de como o cliente foi tratado.',
"""H.rect(170,640,740,120,{strokeWidth:3.5});
H.rect(176,646,601,108,{stroke:H.RED,strokeWidth:2,fill:H.RED,fillStyle:'hachure',hachureGap:10,fillWeight:2});
H.text('82%',477,722,64,'#ffffff','middle',700);
H.line(777,620,777,790,{strokeWidth:2.5,strokeLineDash:[10,8]});
H.text('0',170,820,30,'#6a6a6a','middle'); H.text('100%',910,820,30,'#6a6a6a','middle');
H.text('decidem pelo atendimento',477,880,34,H.RED,'middle',700);
""")
# 3 3x
S[3] = slide('O cliente frustrado<br>vai embora',
    'Quem se frustra numa compra tem até <b>3 vezes mais chance</b> de não voltar para a marca.',
    ('(Accenture, mais de 20 mil consumidores em 19 países)', 410),
    'E ele quase nunca volta para contar <span class="mk">o que deu errado.</span>',
"""H.boneco(250,640,1,'corre'); H.text('sem frustração',250,880,30,'#6a6a6a','middle');
H.line(400,560,400,900,{strokeWidth:2,strokeLineDash:[10,12]});
H.boneco(540,640,1,'corre'); H.boneco(680,640,1,'corre'); H.boneco(820,640,1,'corre');
H.rabisco(680,720,470,300);
H.text('3x',680,560,64,H.RED,'middle',700); H.text('com frustração',680,920,30,H.RED,'middle',700);
""")
# 4 reclama x some
S[4] = ('B', """<div class="T" style="top:130px;font-size:60px"><span class="r">Quem reclama ainda está<br>dando uma chance</span></div>
<div class="P2" style="font-size:44px">O risco de verdade é <span class="mk">o cliente que sai</span> <span class="mk">em silêncio.</span></div>""",
"""H.boneco(290,560,1.2,'aponta'); H.balao(250,420,280,96,'isso está errado!',30,'#3a3a3a',[280,505]);
H.text('RECLAMA',290,830,44,'#3a3a3a','middle',700);
H.text('a empresa fica sabendo',290,885,30,'#3a3a3a','middle'); H.text('e pode corrigir',290,925,30,'#3a3a3a','middle');
H.line(540,400,540,960,{strokeWidth:2,strokeLineDash:[10,12]});
H.boneco(790,560,1.2,'neutro',{strokeLineDash:[8,10],stroke:'#9a958e'});
H.arrow(860,640,960,640,{strokeWidth:4},0);
H.text('SOME',790,830,44,H.RED,'middle',700);
H.text('ninguém descobre',790,885,30,'#3a3a3a','middle'); H.text('e o erro continua',790,925,30,'#3a3a3a','middle');
""")
# 5 iceberg
S[5] = slide('Quantos clientes saíram<br>sem dizer por quê?',
    'A empresa que só olha para quem reclama enxerga a menor parte do problema.',
    None,
    'Procurar quem sumiu é a única forma de descobrir <span class="mk">o que ele não disse.</span>',
"""H.path('M470,640 L540,520 L610,640',{strokeWidth:3.5});
H.line(130,640,950,640,{strokeWidth:2.5});
[[150,660],[260,668],[820,668],[930,660]].forEach(([x,y])=>H.line(x,y,x+60,y,{strokeWidth:2}));
H.path('M470,640 L330,760 L380,900 L540,980 L720,900 L760,760 L610,640',{stroke:H.RED,strokeWidth:3.5,fill:H.RED,fillStyle:'hachure',hachureGap:12,fillWeight:1.2});
H.text('reclamou',690,560,32,'#3a3a3a','start',700); H.arrow(680,566,615,590,{stroke:'#3a3a3a',strokeWidth:3},.2);
H.text('sumiu calado',840,880,34,H.RED,'start',700);
""", 30)
# 6 CTA (C)
S[6] = ('C', """<div class="T" style="top:190px;font-size:60px;white-space:nowrap">Quanto custa o cliente</div>
<div class="T" style="top:275px;font-size:86px;white-space:nowrap"><span class="r">QUE SAI CALADO?</span></div>
<div class="P" style="top:460px;font-size:42px">No MBV, treinamento de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: <b>Lucratividade, Crescimento e Cultura.</b></div>""",
"""H.rect(220,820,640,130,{stroke:H.RED,strokeWidth:5,roughness:1.8}); H.rect(228,826,628,118,{stroke:H.RED,strokeWidth:3,roughness:2.4});
H.text('QUERO PARTICIPAR DO MBV',540,902,46,H.RED,'middle',700);
H.arrow(540,1100,540,975,{strokeWidth:4},.0); H.text('link na bio',540,1155,44,'#3a3a3a','middle',700);
""")

for n, (fundo, body, script, *dy) in S.items():
    page(n, fundo, body, script, *(dy or [0]))
print('ok')
