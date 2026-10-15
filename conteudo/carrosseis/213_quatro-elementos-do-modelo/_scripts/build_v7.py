"""Post 213 — 2 slides no visual do post de referência (grade 2x2 com cruz e losango), texto aprovado em 07/10."""
import pathlib, numpy as np
from PIL import Image
POST = pathlib.Path(__file__).resolve().parents[1]

# fundo: preto liso com leve claridade no centro + granulado (o da referência não tem grade)
H, W = 1350, 1080
rng = np.random.default_rng(7)
yy, xx = np.mgrid[0:H, 0:W]
d = np.hypot((xx - 540) / 700, (yy - 640) / 820)
base = 30 - 20 * np.clip(d, 0, 1)
noise = rng.normal(0, 1, (H, W))
k = np.array([1, 4, 6, 4, 1.]); k /= k.sum()
noise = np.apply_along_axis(lambda r: np.convolve(r, k, 'same'), 1, noise)
noise = np.apply_along_axis(lambda c: np.convolve(c, k, 'same'), 0, noise)
img = np.clip(base + noise / noise.std() * 3.6, 0, 255).astype(np.uint8)
Image.fromarray(np.stack([img] * 3, -1)).save(POST / 'imagens' / 'fundo.png')

CSS = """@import url('https://fonts.googleapis.com/css2?family=Anton&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#111;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;background:url('../imagens/fundo.png');color:#fff;font-family:'Source Serif 4',serif}
.t{position:absolute;left:0;right:0;text-align:center;font-family:'Anton',sans-serif;font-size:92px;line-height:1.02;letter-spacing:.5px}
.t .v{color:#A91C20}
.q{position:absolute;width:440px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;padding-top:30px}
.n{width:78px;height:78px;border-radius:50%;background:#A91C20;display:flex;align-items:center;justify-content:center;font-family:'Anton',sans-serif;font-size:44px}
.q h3{margin-top:16px;font-family:'Anton',sans-serif;font-weight:400;font-size:40px;line-height:1.08;letter-spacing:.3px;text-wrap:balance}
.q p{margin-top:12px;font-size:25px;line-height:1.32;color:#d6d6d6;text-wrap:balance}
.lv{position:absolute;left:539px;width:2px;background:#444}.lh{position:absolute;height:2px;background:#444}
.dia{position:absolute;width:26px;height:26px;background:#A91C20;transform:rotate(45deg)}
.fecho{position:absolute;left:110px;width:860px;text-align:center;font-weight:700;font-size:31px;line-height:1.3;text-wrap:balance}
.intro{position:absolute;left:110px;width:860px;text-align:center;font-size:30px;line-height:1.38;color:#d6d6d6;text-wrap:balance}
.passo{position:absolute;left:110px;width:860px;display:flex;gap:28px;align-items:flex-start}
.passo .n{flex:0 0 78px}
.passo h3{font-family:'Anton',sans-serif;font-weight:400;font-size:40px;line-height:1.1;letter-spacing:.3px}
.passo p{margin-top:6px;font-size:27px;line-height:1.32;color:#d6d6d6;text-wrap:pretty}
.cta{position:absolute;left:90px;width:900px;background:#A91C20;border-radius:14px;padding:30px 44px;text-align:center}
.cta p{font-size:28px;line-height:1.36;font-weight:600;text-wrap:balance}
.cta .bio{margin-top:16px;font-family:'Anton',sans-serif;font-size:54px;letter-spacing:1px}
"""

def page(body):
    return f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s"><div class="conteudo">{body}</div></div></body></html>'

ITENS = [
    ('1', 'ESTRUTURA DE CAPITAL BAIXA', 'ESTRUTURA DE<br>CAPITAL BAIXA', 'Quanto dinheiro a empresa precisa manter investido na operação para funcionar.', 'Quanto menor, menos ela gasta para se manter e crescer.'),
    ('2', 'MARGEM DE CONTRIBUIÇÃO ALTA', 'MARGEM DE<br>CONTRIBUIÇÃO ALTA', 'É o que sobra de cada venda depois dos custos variáveis.', 'Quanto mais alta, mais sobra para pagar os custos fixos e gerar lucro.'),
    ('3', 'ALTA CAPACIDADE DE CRESCIMENTO', 'ALTA CAPACIDADE<br>DE CRESCIMENTO', 'É vender mais sem aumentar custos e estrutura na mesma proporção.', 'Assim, cada venda a mais amplia o lucro.'),
    ('4', 'RECORRÊNCIA NA RECEITA', 'RECORRÊNCIA<br>NA RECEITA', 'É a parte do faturamento que se repete todo mês sem uma venda nova.', 'Quanto maior, mais previsível fica o caixa.'),
]
EXTRA = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
.passo p{text-wrap:balance}
.q{padding-top:0}
.q .n{width:96px;height:96px;font-size:54px}
.q h3{margin-top:22px;font-size:48px;line-height:1.08}
.bloco{position:absolute;left:130px;width:820px;text-align:center;display:flex;flex-direction:column;align-items:center}
.bloco .n{width:96px;height:96px;font-size:54px}
.bloco h3{margin-top:22px;font-family:'Anton',sans-serif;font-weight:400;font-size:56px;line-height:1.08;letter-spacing:.3px}
.bloco p{margin-top:16px;font-size:33px;line-height:1.38;color:#d6d6d6;text-wrap:balance}
.dest{margin-top:22px;background:#A91C20;border-radius:10px;padding:12px 28px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:27px;line-height:1.3;color:#fff;width:fit-content;max-width:820px}
.bola{flex:0 0 22px;width:22px;height:22px;border-radius:50%;background:#A91C20;margin-top:14px}
"""

def pg(body):
    return page(body).replace('<style>', '<style>' + EXTRA.split(chr(10),2)[1] + chr(10)).replace('</style>', EXTRA + '</style>')

# slide 1: capa
b = '<div class="t solo" style="top:280px;font-size:84px">OS 4 ELEMENTOS DE UM<br><span class="v">BOM MODELO DE NEGÓCIO</span></div>'
b += '<div class="lv" style="top:540px;height:560px"></div><div class="lh" style="top:819px;left:150px;width:780px"></div><div class="dia" style="left:527px;top:807px"></div>'
for (x, y), it in zip([(100, 555), (540, 555), (100, 870), (540, 870)], ITENS):
    b += f'<div class="q solo" style="left:{x}px;top:{y}px;width:440px;height:210px"><div class="n">{it[0]}</div><h3>{it[2]}</h3></div>'
(POST / 'instagram' / 'slide-01.html').write_text(pg(b))

# slides 2 e 3: definicao em serifa + a consequencia destacada na faixa bordo
def dois(a, c):
    s = f'<div class="bloco solo" style="top:180px"><div class="n">{a[0]}</div><h3>{a[1]}</h3><p>{a[3]}</p><div class="dest">{a[4]}</div></div>'
    s += '<div class="lh" style="top:674px;left:250px;width:580px"></div><div class="dia" style="left:527px;top:662px"></div>'
    s += f'<div class="bloco solo" style="top:735px"><div class="n">{c[0]}</div><h3>{c[1]}</h3><p>{c[3]}</p><div class="dest">{c[4]}</div></div>'
    return pg(s)
(POST / 'instagram' / 'slide-02.html').write_text(dois(ITENS[0], ITENS[1]))
(POST / 'instagram' / 'slide-03.html').write_text(dois(ITENS[2], ITENS[3]))

# slide 4: como analisar, topicos com bolinha (sem numero), centralizado na vertical
PASSOS = [
    ('OLHE PARA O SEU MODELO', 'Avalie os quatro elementos na sua empresa, com número, não com impressão.'),
    ('SEJA HONESTO', 'Pergunte se o problema está na gestão ou no próprio modelo, porque cada um pede uma correção diferente.'),
    ('REINVENTE QUANDO PRECISAR', 'Se as deficiências superam as virtudes, é hora de mudar o modelo.'),
]
b4 = '<div class="t solo" style="top:250px;font-size:84px">COMO ANALISAR<br><span class="v">O SEU MODELO</span></div>'
b4 += '<div class="intro solo" style="top:460px;left:130px;width:820px;font-size:30px">Todo negócio tem virtudes e deficiências.<br>O que muda o resultado é conhecer as da sua empresa antes de tomar qualquer decisão.</div>'
y = 645
for i, (tt, p) in enumerate(PASSOS):
    b4 += f'<div class="passo solo" style="top:{y}px;left:150px;width:780px;gap:24px"><div class="bola"></div><div><h3>{tt}</h3><p>{p}</p></div></div>'
    if i < 2:
        b4 += f'<div class="lh" style="top:{y + 150}px;left:150px;width:780px"></div>'
    y += 172
(POST / 'instagram' / 'slide-04.html').write_text(pg(b4))

# slide 5: so o CTA
b5 = '<div class="intro solo" style="top:360px;left:150px;width:780px;font-size:40px;line-height:1.36;color:#fff">No MBV, o dono de pequena e média empresa aprende a ler o próprio negócio e a decidir com base nele:</div>'
b5 += '<div class="t solo" style="top:610px;font-size:64px;line-height:1.15">LUCRATIVIDADE<br>CRESCIMENTO<br>CULTURA</div>'
b5 += '<div class="cta solo" style="top:880px;left:290px;width:500px;padding:22px 30px"><div class="bio" style="margin-top:0;font-size:56px">LINK NA BIO</div></div>'
import base64
logo = base64.b64encode(open('/Users/pedrohenrique/Documents/tatsuo-carrossel/.claude/skills/carrossel/modelos/infografico/logo-simbolo.png','rb').read()).decode()
b5 += f'<img class="solo" src="data:image/png;base64,{logo}" style="position:absolute;left:504px;top:1120px;width:72px;height:72px" alt="">'
(POST / 'instagram' / 'slide-05.html').write_text(pg(b5))
print('ok')
