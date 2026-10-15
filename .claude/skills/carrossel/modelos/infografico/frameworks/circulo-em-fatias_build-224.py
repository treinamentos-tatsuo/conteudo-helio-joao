"""Post 224 — os 3 pilares (apostila p. 1-2), 2 slides no visual do 222 (aprovado). Slide 1: anel dividido em três + três colunas."""
import pathlib, base64, math
POST = pathlib.Path(__file__).resolve().parents[1]
# pasta do modelo infografico: sobe a partir deste arquivo ate a raiz do projeto (ou usa a pasta atual), sem caminho fixo de usuario
RAIZ = next((p for p in pathlib.Path(__file__).resolve().parents if (p / '.claude/skills/carrossel').is_dir()), pathlib.Path.cwd())
INFO = RAIZ / '.claude/skills/carrossel/modelos/infografico'
LOGO = base64.b64encode((INFO / 'logo-simbolo.png').read_bytes()).decode()
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
    foot = '<div class="arr">ARRASTE &rarr;</div>' if n < TOTAL else ''   # sem paginacao (pedido do user, 11/10)
    html = f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body><div class="s {cls}"><div class="conteudo">{body}{foot}</div></div></body></html>'
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html)

# slide 1 v2 (11/10): padrao da referencia do Alfredo — circulo grande dividido em tres, conteudo dentro de cada fatia,
# badges vermelhos com icone na borda, centro com anel vermelho e icone; titulo sans pesado em duas cores.
import re as _re
ICO = INFO / 'icones'
def icon(nome, px, cor='#ffffff', traco=2.0):
    s = (ICO / f'{nome}.svg').read_text()
    s = _re.sub(r'width="24"', f'width="{px}"', s, count=1); s = _re.sub(r'height="24"', f'height="{px}"', s, count=1)
    s = s.replace('stroke="currentColor"', f'stroke="{cor}"', 1).replace('stroke-width="2"', f'stroke-width="{traco}"', 1)
    return _re.sub(r'class="[^"]*"', '', s, count=1)

EXTRA += """
.T1{position:absolute;left:90px;width:900px;text-align:center;font-family:'Montserrat',sans-serif;font-weight:800;line-height:1.08;letter-spacing:-1.5px;text-transform:uppercase;white-space:nowrap}
.sub{position:absolute;left:90px;width:900px;text-align:center;font-family:'Montserrat',sans-serif;font-weight:600;font-size:30px}
.sub u{color:#A91C20;text-decoration-thickness:3px;text-underline-offset:6px}
.fat{position:absolute}
.fat .t{display:inline-block;background:#A91C20;color:#fff;border-radius:6px;padding:6px 16px 5px;box-shadow:0 6px 16px rgba(0,0,0,.35);font-family:'Montserrat',sans-serif;font-weight:800;font-size:27px;line-height:1.15;text-transform:uppercase;letter-spacing:-.2px}
.fat .d{margin-top:14px;font-family:'Montserrat',sans-serif;font-weight:500;font-size:21px;line-height:1.4;color:#e4e4e4;text-wrap:pretty}
.fat .l{margin-top:14px;font-family:'Montserrat',sans-serif;font-weight:800;font-size:18px}
.fat .a{margin-top:4px;font-family:'Montserrat',sans-serif;font-weight:500;font-size:19px;line-height:1.36;color:#fff}
.fat .a b{color:#A91C20;font-weight:800;margin-right:6px}
.badge{position:absolute;border-radius:50%;background:#A91C20;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 10px #0d0d0d}
"""
CX, CY, R = 540, 770, 430
RI_RED, RI_BLK = 105, 68
def pt(r, a): return (CX + r*math.cos(math.radians(a)), CY + r*math.sin(math.radians(a)))
def fatia(a0, a1, r0=RI_RED):
    x0,y0=pt(R,a0); x1,y1=pt(R,a1); x2,y2=pt(r0,a1); x3,y3=pt(r0,a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r0},{r0} 0 0 0 {x3:.1f},{y3:.1f} Z'
SECT = [(150, 270), (270, 390), (30, 150)]   # sup-esq, sup-dir, baixo
svg = '<svg width="1080" height="1350" style="position:absolute;inset:0" viewBox="0 0 1080 1350"><defs>'
svg += '<radialGradient id="gf" cx="540" cy="770" r="430" gradientUnits="userSpaceOnUse"><stop offset="0.3" stop-color="#1f1f1f"/><stop offset="1" stop-color="#121212"/></radialGradient></defs>'
for a0, a1 in SECT:
    svg += f'<path d="{fatia(a0, a1)}" fill="url(#gf)"/>'
    x0,y0=pt(R,a0+3); x1,y1=pt(R,a1-3)
    svg += f'<path d="M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="#A91C20" stroke-width="3"/>'
for a in (270, 30, 150):   # vaos pretos grossos entre as fatias
    x0,y0=pt(RI_BLK,a); x1,y1=pt(R+6,a)
    svg += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#0d0d0d" stroke-width="16"/>'
svg += f'<circle cx="{CX}" cy="{CY}" r="{RI_RED}" fill="#A91C20"/><circle cx="{CX}" cy="{CY}" r="{RI_BLK}" fill="#0d0d0d"/>'
for a in (270, 30, 150):
    x0,y0=pt(RI_BLK-2,a); x1,y1=pt(RI_RED+2,a)
    svg += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#0d0d0d" stroke-width="16"/>'
svg += '</svg>'
b = svg
b += '<div class="T1 solo" style="top:112px;left:110px;width:860px;font-size:50px;background:#fff;color:#0d0d0d;border-radius:6px;padding:18px 0 16px;box-shadow:0 12px 30px rgba(0,0,0,.5)">Os 3 pilares que sustentam<br><span style="color:#A91C20;font-size:64px">qualquer negócio</span></div>'
b += '<div class="sub solo" style="top:284px;font-size:26px">Entenda o papel de cada um <u>na sua empresa</u></div>'
b += f'<div style="position:absolute;left:{CX-46}px;top:{CY-46}px">{icon("building-store", 92, "#ffffff", 1.7)}</div>'
P = [('Lucratividade', 'Saber se a empresa dá lucro de verdade e para onde vai o dinheiro.', 'É o que garante que o esforço vire resultado.', 'coin', 240),
     ('Crescimento', 'Um processo comercial que vende com método, não com sorte.', 'É o que sustenta a expansão.', 'trending-up', 300),
     ('Cultura', 'Líderes e um time que fazem a empresa andar sem depender do dono.', 'É o que permite crescer sem quebrar.', 'hierarchy-2', 90)]
POS = [(192, 594, 220), (708, 594, 220), (340, 936, 400)]
POS3 = [(176, 568, 250), (654, 568, 250), (354, 954, 480)]   # (v5) bloco unico: titulo + paragrafo; ajustado por busca
POS2 = [((276, 480, 270), (172, 630, 310)), ((580, 480, 258), (684, 630, 290)), ((340, 936, 400), (340, 1050, 400))]   # busca fit224e.js; mesmas alturas nas duas fatias de cima   # medidas por busca (fit224.js): texto inteiro dentro da fatia, longe do centro, dos divisores, da borda e dos badges
for (nome, d, a, ic, ang), (x, y, wd) in zip(P, POS):
    bx, by = pt(R - (12 if ang == 90 else 0), ang)
    b += f'<div class="badge solo" style="left:{bx-50:.0f}px;top:{by-50:.0f}px;width:100px;height:100px">{icon(ic, 54, "#ffffff", 2.0)}</div>'
    k = P.index((nome, d, a, ic, ang))
    x, y, wd = POS3[k]
    alin = 'center'
    wfit = '' if k < 2 else 'width:fit-content;'
    pos = 'left:50%;transform:translateX(-50%);' if k == 2 else f'left:{x}px;width:{wd}px;'
    b += f'<div class="fat solo" data-sec="{k}" style="{pos}top:{y}px;{wfit}max-width:{wd}px;text-align:{alin}"><div class="t">{nome}</div><div class="d">{d} {a}</div></div>'
w(1, b)

# 2 v3 (11/10): mesma linguagem do slide 1 — fundo escuro, sintoma em cartao com badge do pilar, botao branco mantido
EXTRA += """
.row3{position:absolute;left:110px;width:860px;height:120px;border-radius:14px;background:linear-gradient(100deg,#1f1f1f,#141414);border:2px solid #A91C20;display:flex;align-items:center;gap:26px;padding:0 30px 0 22px}
.row3 .bd{flex:0 0 84px;height:84px;border-radius:50%;background:#A91C20;display:flex;align-items:center;justify-content:center}
.row3 .sx{font-family:'Montserrat',sans-serif;font-weight:800;font-size:28px;line-height:1.2;color:#fff}
.row3 .pl{margin-top:8px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:21px;letter-spacing:.06em;color:#d0d0d0}
.row3 .pl b{color:#A91C20;font-weight:800}
.ponte{position:absolute;left:110px;width:860px;text-align:center;font-family:'Montserrat',sans-serif;font-weight:500;font-size:26px;line-height:1.45;color:#e6e6e6;text-wrap:balance}
.ponte b{color:#fff;font-weight:800}
.btn3{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;background:#fff;color:#A91C20;font-family:'Montserrat',sans-serif;font-weight:800;font-size:38px;letter-spacing:-.5px;padding:24px 44px;border-radius:6px;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)}
.bio{position:absolute;left:0;right:0;text-align:center;font-family:'Montserrat',sans-serif;font-weight:800;font-size:26px;letter-spacing:.2em;color:#fff}
"""
b = '<div class="T1 solo" style="top:118px;font-size:56px;line-height:1.12">Qual desses pilares<br><span style="color:#A91C20">está mais fraco</span><br>na sua empresa?</div>'
S = [('Lucro que não aparece na conta.', 'Lucratividade', 'coin'),
     ('Venda que depende de sorte.', 'Crescimento', 'trending-up'),
     ('Empresa que não anda sem o dono.', 'Cultura', 'hierarchy-2')]
for i, (s, pl, ic) in enumerate(S):
    b += f'<div class="row3 solo" style="top:{360 + i*146}px"><div class="bd">{icon(ic, 46, "#ffffff", 2.0)}</div><div><div class="sx">{s}</div><div class="pl"><b>&rarr;</b> Pilar {pl}</div></div></div>'
b += '<div class="ponte solo" style="top:820px">Cada um desses sintomas nasce em um pilar. No <b>MBV</b>, imersão de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três.</div>'
b += '<div class="btn3 solo" style="top:1000px">QUERO PARTICIPAR DO MBV</div>'
b += '<div class="bio solo" style="top:1130px">LINK NA BIO &rarr;</div>'
w(2, b)
print('ok')
