"""Post 222 v2 visual (10/10): linguagem de post de Instagram, não de apostila.
Tipografia grande alinhada à esquerda, destaque em bloco bordô atrás da palavra, sem círculos/grades/fios/losangos,
CTA com fundo bordô inteiro. Texto = o aprovado (v4). v4 visual (10/10): 8 slides — framework circular no 2; slides 3, 4 e 5 da v3 divididos em dois. v1 (visual de apostila) em build_v1_apostila.py."""
import pathlib, base64
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

TOTAL = 8
EXTRA = """
.cmp{position:absolute;width:380px;height:300px;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.cmp .w{font-family:'Anton',sans-serif;font-size:66px;letter-spacing:.5px}
.cmp .l{margin-top:14px;font-family:'Montserrat',sans-serif;font-weight:800;font-size:20px;letter-spacing:.18em}
.cmp .ic{font-family:'Anton',sans-serif;font-size:90px;line-height:1;margin-bottom:6px}
.q4{position:absolute;width:210px;text-align:center}
.q4 .w{font-family:'Anton',sans-serif;font-size:36px;letter-spacing:.5px}
.q4 .c{margin-top:6px;font-size:19.5px;line-height:1.28;color:#f1f1f1;text-wrap:balance}
"""

def w(n, body, cls=''):
    foot = f'<div class="pg" style="{"color:rgba(255,255,255,.7)" if cls else ""}">{n:02d}/{TOTAL:02d}</div>' + ('<div class="arr">ARRASTE &rarr;</div>' if n < TOTAL else '')
    html = f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body><div class="s {cls}"><div class="conteudo">{body}{foot}</div></div></body></html>'
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html)

# 1 capa
w(1, '<div class="H solo" style="top:300px;font-size:136px;line-height:1.0">Estou ficando<br>mais rico<br><span class="m" style="white-space:nowrap">ou mais pobre?</span></div>'
     '<div class="P solo" style="top:800px;left:190px;width:700px">A maioria dos donos não sabe responder, mesmo com a empresa dando lucro.</div>')

# 2 framework: circulo em quatro quadrantes, lucro no centro
import math
CX, CY, R1, R0 = 540, 838, 338, 88
def setor(a0, a1):
    p = lambda r, a: (CX + r*math.cos(math.radians(a)), CY + r*math.sin(math.radians(a)))
    x0,y0 = p(R1,a0); x1,y1 = p(R1,a1); x2,y2 = p(R0,a1); x3,y3 = p(R0,a0)
    return f'M{x0:.1f},{y0:.1f} A{R1},{R1} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{R0},{R0} 0 0 0 {x3:.1f},{y3:.1f} Z'
G = 1.6  # folga angular entre os quadrantes
cores = ['#A91C20', '#2a2a2a', '#A91C20', '#2a2a2a']
quads = [(180+G, 270-G), (270+G, 360-G), (0+G, 90-G), (90+G, 180-G)]   # sup-esq, sup-dir, inf-dir, inf-esq
svg = '<svg width="1080" height="1350" style="position:absolute;inset:0" viewBox="0 0 1080 1350">'
for (a0, a1), c in zip(quads, cores):
    svg += f'<path d="{setor(a0, a1)}" fill="{c}"/>'
svg += f'<circle cx="{CX}" cy="{CY}" r="{R0-10}" fill="#0f0f0f" stroke="#A91C20" stroke-width="3"/></svg>'
b = svg
b += '<div class="k solo" style="top:140px">O lucro não some</div>'
b += '<div class="H solo" style="top:188px;font-size:112px"><span class="m">Muda de forma.</span></div>'
b += '<div class="P solo" style="top:345px;left:130px;width:820px;font-size:31px">O lucro aparece na DRE, mas nem sempre aparece na conta. Antes de virar dinheiro disponível, ele pode ter ido para quatro lugares:</div>'
b += f'<div style="position:absolute;left:{CX-90}px;top:{CY-34}px;width:180px;text-align:center;font-family:Anton,sans-serif;font-size:46px;line-height:1">LUCRO<div style="font-family:Montserrat,sans-serif;font-weight:700;font-size:15px;letter-spacing:.2em;color:#bdbdbd;margin-top:6px">DA DRE</div></div>'
Q = [('Estoque','Comprou mercadoria que ainda não vendeu.', 225),('Recebível','Vendeu, mas o cliente ainda não pagou.', 315),
     ('Dívida','Usou o resultado para abater empréstimo.', 45),('Retirada','O sócio tirou para si.', 135)]
for nome, cap, ang in Q:
    r = (R0 + R1) / 2 - 4
    x = CX + r*math.cos(math.radians(ang)); y = CY + r*math.sin(math.radians(ang))
    sx = 1 if ang in (45, 315) else -1; sy = 1 if ang in (45, 135) else -1
    L = (CX + sx*120 - 100, CY + sy*172 - 55, 200)   # posicao espelhada medida: todo o texto dentro do quadrante, folga minima de 13 px
    b += f'<div class="q4" style="left:{L[0]}px;top:{L[1]}px;width:{L[2]}px"><div class="w">{nome.upper()}</div><div class="c">{cap}</div></div>'
w(2, b)

# 3 a DRE nao responde (comparacao lucro x riqueza)
b = '<div class="H solo" style="top:170px;font-size:100px;line-height:1.14">A DRE não responde<br><span class="m">essa pergunta</span></div>'
b += '<div class="P solo" style="top:450px">A DRE mostra se a empresa deu lucro no mês. Ela não mostra se esse lucro virou riqueza ou se escorreu pelo caminho.</div>'
b += '<div class="cmp solo" style="left:130px;top:700px;background:#1c1c1c;border:2px solid #3a3a3a"><div class="ic" style="color:#fff">&check;</div><div class="w">LUCRO</div><div class="l" style="color:#bdbdbd">A DRE MOSTRA</div></div>'
b += '<div class="cmp solo" style="left:570px;top:700px;background:#A91C20"><div class="ic">?</div><div class="w">RIQUEZA</div><div class="l" style="color:#fff">A DRE NÃO MOSTRA</div></div>'
w(3, b)

# 4 lucro x riqueza (frase heroica)
b = '<div class="P solo" style="top:230px;left:150px;width:780px">Para isso, o dono precisa olhar para o patrimônio da empresa, e não só para o resultado.</div>'
b += '<div class="H solo" style="top:470px;font-size:116px;line-height:1.12">Lucro é o que<br>a empresa gerou.<br><span class="m">Riqueza é o<br>que ficou.</span></div>'
w(4, b)

# 5 por que o dono se acha mais rico (abertura)
b = '<div class="H solo" style="top:300px;font-size:116px;line-height:1.24">Por que o dono<br>se acha <span class="m">mais rico</span><br>do que é</div>'
b += '<div class="P solo" style="top:800px;left:190px;width:700px">Quem tenta responder de cabeça costuma cair em três enganos:</div>'
w(5, b)

# 6 os tres enganos
E = [('O saldo do banco','Conta o saldo inteiro, mas parte dele já tem dono.'),
     ('O recebível','Conta como dinheiro, mas ele tem prazo e inadimplência.'),
     ('O estoque','Conta tudo, mas mercadoria que não vende não vira dinheiro.')]
b = '<div class="solo" style="position:absolute;left:170px;top:330px;width:780px;display:flex;flex-direction:column;gap:70px">'
for i,(a,c) in enumerate(E):
    b += f'<div style="display:flex;gap:34px;align-items:flex-start"><div style="font-family:Anton,sans-serif;font-size:120px;line-height:.86;color:transparent;-webkit-text-stroke:2px #A91C20;flex:0 0 110px">{i+1}</div>'
    b += f'<div><div style="font-family:Anton,sans-serif;font-size:62px;line-height:1;letter-spacing:.5px;text-transform:uppercase">{a}</div><div style="margin-top:12px;font-size:33px;line-height:1.34;color:#e3e3e3;text-wrap:balance">{c}</div></div></div>'
b += '</div>'
w(6, b)

# 7 a resposta de verdade
b = '<div class="H solo" style="top:250px;font-size:116px;line-height:1.3">Quer a resposta<br>de verdade,<br><span class="m">todo mês?</span></div>'
b += '<div class="P solo" style="top:800px;left:150px;width:780px">O Balanço Japonês mostra, com número, se a empresa está ficando mais rica ou mais pobre.</div>'
w(7, b)

# 8 CTA (fundo bordo)
b = '<div class="k solo" style="top:380px;color:#fff;opacity:.85">Imersão MBV</div>'
b += '<div class="P solo" style="top:450px;left:130px;width:820px;color:#fff;font-size:46px;line-height:1.32">No MBV, o dono de pequena e média empresa aprende a montar e a ler essa ferramenta na própria empresa.</div>'
b += '<div class="btn solo" style="top:820px">LINK NA BIO &rarr;</div>'
b += f'<img class="solo" src="data:image/png;base64,{LOGO}" style="position:absolute;left:508px;top:1030px;width:64px;height:64px;filter:brightness(0) invert(1)" alt="">'
w(8, b, 'verm')
print('ok')
