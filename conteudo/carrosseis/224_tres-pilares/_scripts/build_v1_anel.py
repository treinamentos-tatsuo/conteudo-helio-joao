"""Post 224 — os 3 pilares (apostila p. 1-2), 2 slides no visual do 222 (aprovado). Slide 1: anel dividido em três + três colunas."""
import pathlib, base64, math
POST = pathlib.Path(__file__).resolve().parents[1]
LOGO = base64.b64encode(open('/Users/pedrohenrique/Documents/tatsuo-carrossel/.claude/skills/carrossel/modelos/infografico/logo-simbolo.png','rb').read()).decode()
CSS = """@import url('https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@600;700;800&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#0e0e0e}
.s{position:relative;width:1080px;height:1350px;background:url('../imagens/fundo.png');color:#fff;font-family:'Source Serif 4',serif;overflow:hidden}
.s::after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 40% 40%,rgba(0,0,0,0) 50%,rgba(0,0,0,.5) 100%);pointer-events:none}
.s.verm{background:#A91C20}
.s.verm::after{background:radial-gradient(ellipse at 40% 35%,rgba(255,255,255,.06) 0%,rgba(0,0,0,0) 45%,rgba(0,0,0,.35) 100%)}
.conteudo{position:absolute;inset:0;z-index:2}
.k{position:absolute;left:100px;width:880px;text-align:center;font-family:'Montserrat',sans-serif;font-weight:800;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:#A91C20}
.H{position:absolute;left:100px;width:880px;text-align:center;font-family:'Anton',sans-serif;line-height:1.02;letter-spacing:.5px;text-transform:uppercase}
.m{display:inline-block;background:#A91C20;padding:10px 18px 2px;line-height:1.02;margin-top:14px}
.P{position:absolute;left:130px;width:820px;text-align:center;text-wrap:balance;font-size:36px;line-height:1.38;color:#ededed}
.row{position:absolute;left:100px;width:880px;display:flex;align-items:center;gap:30px}
.row .w{flex:0 0 330px;font-family:'Anton',sans-serif;font-size:60px;line-height:1;letter-spacing:.5px;text-transform:uppercase}
.row .c{font-size:31px;line-height:1.32;color:#d9d9d9;text-wrap:balance}
.eng{position:absolute;left:100px;width:880px;padding-left:34px;border-left:6px solid #A91C20}
.eng .w{font-family:'Anton',sans-serif;font-size:56px;line-height:1;letter-spacing:.5px;text-transform:uppercase}
.eng .c{margin-top:12px;font-size:32px;line-height:1.34;color:#e3e3e3;text-wrap:balance}
.it{position:absolute;left:100px;width:880px;text-align:center}
.it .w{font-family:'Anton',sans-serif;font-size:58px;line-height:1;letter-spacing:.5px;text-transform:uppercase}
.it .c{margin-top:10px;font-size:30px;line-height:1.3;color:#d9d9d9}
.arr{position:absolute;right:100px;top:1190px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:20px;letter-spacing:.2em;color:#9a9a9a}
.pg{position:absolute;left:100px;top:1190px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:20px;letter-spacing:.2em;color:#9a9a9a}
.btn{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;background:#fff;color:#A91C20;font-family:'Anton',sans-serif;font-size:60px;letter-spacing:1px;padding:20px 44px}
"""

TOTAL = 2
EXTRA = """
.col{position:absolute;width:265px;text-align:center}
.col .bar{width:60px;height:6px;margin:0 auto 16px}
.col .w{font-family:'Anton',sans-serif;font-size:38px;letter-spacing:.5px}
.col .c{margin-top:10px;font-size:22px;line-height:1.34;color:#dcdcdc;text-wrap:balance}
.col .d{margin-top:12px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:17.5px;line-height:1.35;color:#fff;text-wrap:balance}
"""
def w(n, body, cls=''):
    foot = f'<div class="pg" style="{"color:rgba(255,255,255,.7)" if cls else ""}">{n:02d}/{TOTAL:02d}</div>' + ('<div class="arr">ARRASTE &rarr;</div>' if n < TOTAL else '')
    html = f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body><div class="s {cls}"><div class="conteudo">{body}{foot}</div></div></body></html>'
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html)

# anel dividido em tres
CX, CY, R1, R0 = 540, 560, 200, 118
def setor(a0, a1):
    p = lambda r, a: (CX + r*math.cos(math.radians(a)), CY + r*math.sin(math.radians(a)))
    x0,y0=p(R1,a0); x1,y1=p(R1,a1); x2,y2=p(R0,a1); x3,y3=p(R0,a0)
    return f'M{x0:.1f},{y0:.1f} A{R1},{R1} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{R0},{R0} 0 0 0 {x3:.1f},{y3:.1f} Z'
G = 1.8
cores = ['#A91C20', '#6e1418', '#2c2c2c']
setores = [(-90+G, 30-G), (30+G, 150-G), (150+G, 270-G)]   # topo-direita, baixo, esquerda
nomes = ['LUCRATIVIDADE', 'CRESCIMENTO', 'CULTURA']
svg = '<svg width="1080" height="1350" style="position:absolute;inset:0" viewBox="0 0 1080 1350"><defs>'
for i,(a0,a1) in enumerate(setores):
    rm = (R0+R1)/2
    s, e = a0+4, a1-4
    meio = ((s + e) / 2) % 360
    if 0 < meio < 180:   # arco de baixo: desenha ao contrario pro texto nao ficar de cabeca pra baixo
        s, e, sweep = e, s, 0
    else:
        sweep = 1
    svg += f'<path id="arc{i}" d="M{CX+rm*math.cos(math.radians(s)):.1f},{CY+rm*math.sin(math.radians(s)):.1f} A{rm},{rm} 0 0 {sweep} {CX+rm*math.cos(math.radians(e)):.1f},{CY+rm*math.sin(math.radians(e)):.1f}" fill="none"/>'
svg += '</defs>'
for (a0,a1),c in zip(setores,cores):
    svg += f'<path d="{setor(a0,a1)}" fill="{c}"/>'
for i,nm in enumerate(nomes):
    dy = 22 if i == 1 else 10
    svg += f'<text font-family="Anton" font-size="30" letter-spacing="1.5" fill="#fff" dy="{dy}"><textPath href="#arc{i}" startOffset="50%" text-anchor="middle">{nm}</textPath></text>'
svg += f'<circle cx="{CX}" cy="{CY}" r="{R0-12}" fill="#0f0f0f" stroke="#A91C20" stroke-width="3"/></svg>'

b = svg
b += '<div class="H solo" style="top:130px;font-size:74px;line-height:1.08">Os 3 pilares que sustentam<br><span class="m">qualquer negócio</span></div>'
b += f'<div style="position:absolute;left:{CX-90}px;top:{CY-46}px;width:180px;text-align:center;font-family:Anton,sans-serif;font-size:34px;line-height:1.3">SEU<br>NEGÓCIO</div>'
C = [('Lucratividade','Saber se a empresa dá lucro de verdade e para onde vai o dinheiro.','É o que garante que o esforço vire resultado.', cores[0]),
     ('Crescimento','Um processo comercial que vende com método, não com sorte.','É o que sustenta a expansão.', cores[1]),
     ('Cultura','Líderes e um time que fazem a empresa andar sem depender do dono.','É o que permite crescer sem quebrar.', '#5a5a5a')]
for i,(t,c,d,cor) in enumerate(C):
    x = 100 + i*(265+42)
    b += f'<div class="col solo" style="left:{x}px;top:810px"><div class="bar" style="background:{cor}"></div><div class="w">{t.upper()}</div><div class="c">{c}</div><div class="d">{d}</div></div>'
w(1, b)

# 2 pergunta + sintomas + oferta + botao (fundo bordo)
EXTRA += """
.sint{position:absolute;left:190px;width:700px}
.sint div{font-family:'Montserrat',sans-serif;font-weight:700;font-size:28px;line-height:1.2;padding:16px 0;border-bottom:1px solid rgba(255,255,255,.35);text-align:center}
.sint div:last-child{border-bottom:0}
.btn2{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;background:#fff;color:#A91C20;font-family:'Anton',sans-serif;font-size:50px;letter-spacing:1px;padding:20px 42px;box-shadow:0 10px 30px rgba(0,0,0,.3)}
.apoio{position:absolute;left:0;right:0;text-align:center;font-family:'Montserrat',sans-serif;font-weight:700;font-size:20px;letter-spacing:.22em;color:rgba(255,255,255,.85)}
"""
b = '<div class="H solo" style="top:130px;font-size:84px;line-height:1.16">Qual desses pilares<br>está mais fraco<br>na sua empresa?</div>'
b += '<div class="sint solo" style="top:470px"><div>Lucro que não aparece na conta.</div><div>Venda que depende de sorte.</div><div>Empresa que não anda sem o dono.</div></div>'
b += '<div class="P solo" style="top:715px;left:150px;width:780px;color:#fff;font-size:30px">Cada um desses sintomas nasce em um pilar. No MBV, imersão de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três: Lucratividade, Crescimento e Cultura.</div>'
b += '<div class="btn2 solo" style="top:960px">QUERO PARTICIPAR DO MBV</div>'
b += '<div class="apoio solo" style="top:1112px">LINK NA BIO &rarr;</div>'
w(2, b, 'verm')
print('ok')
