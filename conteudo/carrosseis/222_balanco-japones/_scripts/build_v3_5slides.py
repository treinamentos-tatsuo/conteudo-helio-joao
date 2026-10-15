"""Post 222 v2 visual (10/10): linguagem de post de Instagram, não de apostila.
Tipografia grande alinhada à esquerda, destaque em bloco bordô atrás da palavra, sem círculos/grades/fios/losangos,
CTA com fundo bordô inteiro. Texto = o aprovado (v4). v1 (visual de apostila) em build_v1_apostila.py."""
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

def w(n, body, cls=''):
    foot = f'<div class="pg" style="{"color:rgba(255,255,255,.7)" if cls else ""}">{n:02d}/05</div>' + ('<div class="arr">ARRASTE &rarr;</div>' if n < 5 else '')
    html = f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {cls}"><div class="conteudo">{body}{foot}</div></div></body></html>'
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html)

# 1 capa
w(1, '<div class="H solo" style="top:300px;font-size:136px;line-height:1.0">Estou ficando<br>mais rico<br><span class="m" style="white-space:nowrap">ou mais pobre?</span></div>'
     '<div class="P solo" style="top:800px;left:190px;width:700px">A maioria dos donos não sabe responder, mesmo com a empresa dando lucro.</div>')

# 2 o lucro muda de forma
b = '<div class="k solo" style="top:150px">O lucro não some</div>'
b += '<div class="H solo" style="top:198px;font-size:118px"><span class="m">Muda de forma.</span></div>'
b += '<div class="P solo" style="top:375px;left:130px;width:820px;font-size:33px">O lucro aparece na DRE, mas nem sempre aparece na conta. Antes de virar dinheiro disponível, ele pode ter ido para quatro lugares:</div>'
R = [('Estoque','Comprou mercadoria que ainda não vendeu.'),('Recebível','Vendeu, mas o cliente ainda não pagou.'),
     ('Dívida','O resultado foi usado para abater empréstimo.'),('Retirada','O sócio tirou para si.')]
for i,(a,c) in enumerate(R):
    b += f'<div class="it solo" style="top:{585 + i*140}px"><div class="w">{a}</div><div class="c">{c}</div></div>'
w(2, b)

# 3 a DRE nao responde
b = '<div class="k solo" style="top:150px">A DRE não responde essa pergunta</div>'
b += '<div class="P solo" style="top:215px;left:130px;width:820px">A DRE mostra se a empresa deu lucro no mês. Ela não mostra se esse lucro virou riqueza ou se escorreu pelo caminho. Para isso, o dono precisa olhar para o patrimônio da empresa, e não só para o resultado.</div>'
b += '<div class="H solo" style="top:560px;font-size:112px;line-height:1.08">Lucro é o que<br>a empresa gerou.<br><span class="m">Riqueza é o<br>que ficou.</span></div>'
w(3, b)

# 4 por que o dono se acha mais rico
b = '<div class="H solo" style="top:120px;font-size:90px;line-height:1.24">Por que o dono<br>se acha <span class="m">mais rico</span><br>do que é</div>'
b += '<div class="P solo" style="top:520px;left:130px;width:820px;font-size:32px">Quem tenta responder de cabeça costuma cair em três enganos:</div>'
E = [('O saldo do banco','Conta o saldo inteiro, mas parte dele já tem dono.'),
     ('O recebível','Conta como dinheiro, mas ele tem prazo e inadimplência.'),
     ('O estoque','Conta tudo, mas mercadoria que não vende não vira dinheiro.')]
b += '<div class="solo" style="position:absolute;left:160px;top:650px;width:780px;display:flex;flex-direction:column;gap:40px">'
for i,(a,c) in enumerate(E):
    b += f'<div class="eng" style="position:relative;left:0;width:auto"><div class="w">{a}</div><div class="c">{c}</div></div>'
b += '</div>'
w(4, b)

# 5 CTA (fundo bordo)
b = '<div class="H solo" style="top:175px;font-size:112px;line-height:1.3">Quer a resposta<br>de verdade,<br>todo mês?</div>'
b += '<div class="P solo" style="top:690px;left:120px;width:840px;color:#fff;font-size:35px">O Balanço Japonês mostra, com número, se a empresa está ficando mais rica ou mais pobre. No MBV, o dono de pequena e média empresa aprende a montar e a ler essa ferramenta na própria empresa.</div>'
b += '<div class="btn solo" style="top:960px">LINK NA BIO &rarr;</div>'
b += f'<img class="solo" src="data:image/png;base64,{LOGO}" style="position:absolute;left:508px;top:1150px;width:64px;height:64px;filter:brightness(0) invert(1)" alt="">'
w(5, b, 'verm')
print('ok')
