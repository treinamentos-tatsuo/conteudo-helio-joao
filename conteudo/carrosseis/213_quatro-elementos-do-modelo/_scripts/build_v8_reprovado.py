"""Post 213 v8 — redesenho editorial (07/10): grade alinhada à esquerda, moldura de página, numerais vazados, destaque com barra lateral.
Texto = o aprovado na v7. A v7 (visual centralizado com pílulas) fica em build_v7.py."""
import pathlib, base64
POST = pathlib.Path(__file__).resolve().parents[1]
LOGO = base64.b64encode(open('/Users/pedrohenrique/Documents/tatsuo-carrossel/.claude/skills/carrossel/modelos/infografico/logo-simbolo.png', 'rb').read()).decode()
TOTAL = 5

CSS = """@import url('https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#0e0e0e;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;background:url('../imagens/fundo.png');color:#fff;font-family:'Source Serif 4',serif}
.s::after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(0,0,0,0) 55%,rgba(0,0,0,.45) 100%);pointer-events:none}
.c{position:absolute;inset:0;z-index:2}
.lbl{font-family:'Montserrat',sans-serif;font-weight:600;font-size:17px;letter-spacing:.28em;text-transform:uppercase;color:#8f8f8f}
.topo{position:absolute;left:110px;right:110px;top:110px;display:flex;justify-content:space-between;align-items:center}
.pe{position:absolute;left:110px;right:110px;top:1196px;display:flex;justify-content:space-between;align-items:center}
.pe .marca{display:flex;align-items:center;gap:14px}
.pe img{width:30px;height:30px}
.fio{position:absolute;left:110px;right:110px;height:1px;background:#353535}
.acento{color:#A91C20}
.h{font-family:'Anton',sans-serif;font-weight:400;letter-spacing:.4px;line-height:1.0;text-transform:uppercase}
.barra{width:72px;height:5px;background:#A91C20}
.num{font-family:'Anton',sans-serif;line-height:.85;color:transparent;-webkit-text-stroke:2px #A91C20}
.def{font-size:31px;line-height:1.42;color:#cfcfcf;text-wrap:pretty}
.dest{text-wrap:pretty;border-left:5px solid #A91C20;padding:4px 0 4px 24px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:25px;line-height:1.38;color:#fff}
.cel{position:absolute;padding:34px 30px 0 0}
.cel .k{font-family:'Montserrat',sans-serif;font-weight:700;font-size:20px;letter-spacing:.2em;color:#A91C20}
.cel .h{margin-top:14px;font-size:46px;line-height:1.04}
.item{position:absolute;left:110px;width:860px;display:flex;gap:26px}
.item .q{flex:0 0 14px;width:14px;height:14px;background:#A91C20;transform:rotate(45deg);margin-top:16px}
.item .h{font-size:40px}
.item p{margin-top:8px;font-size:28px;line-height:1.4;color:#cfcfcf;text-wrap:pretty}
.btn{text-transform:uppercase;display:inline-flex;align-items:center;gap:22px;background:#A91C20;padding:20px 36px;font-family:'Anton',sans-serif;font-size:50px;letter-spacing:1px}
"""

def moldura(n, rotulo='Modelo de negócio', direita=None):
    d = direita or f'{n:02d} / {TOTAL:02d}'
    return (f'<div class="topo"><span class="lbl">{rotulo}</span><span class="lbl">{d}</span></div>'
            f'<div class="fio" style="top:150px"></div><div class="fio" style="top:1176px"></div>'
            f'<div class="pe"><span class="marca"><img src="data:image/png;base64,{LOGO}" alt=""><span class="lbl">Tatsuo Academy</span></span>'
            f'<span class="lbl">{"Arraste &rarr;" if n < TOTAL else ""}</span></div>')

def page(n, body, **kw):
    html = f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s"><div class="c">{moldura(n, **kw)}{body}</div></div></body></html>'
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html)

ITENS = [
    ('01', 'Estrutura de capital baixa', 'Quanto dinheiro a empresa precisa manter investido na operação para funcionar.', 'Quanto menor, menos ela gasta para se manter e crescer.'),
    ('02', 'Margem de contribuição alta', 'É o que sobra de cada venda depois dos custos variáveis.', 'Quanto mais alta, mais sobra para pagar os custos fixos e gerar lucro.'),
    ('03', 'Alta capacidade de crescimento', 'É vender mais sem aumentar custos e estrutura na mesma proporção.', 'Assim, cada venda a mais amplia o lucro.'),
    ('04', 'Recorrência na receita', 'É a parte do faturamento que se repete todo mês sem uma venda nova.', 'Quanto maior, mais previsível fica o caixa.'),
]

# 1 — capa: titulo grande alinhado à esquerda + tabela 2x2 com fios
b = '<div class="h solo" style="position:absolute;left:110px;top:230px;font-size:112px">Os 4 elementos<br>de um bom<br><span class="acento">modelo de negócio</span></div>'
b += '<div class="barra" style="position:absolute;left:110px;top:600px"></div>'
b += '<div class="fio" style="top:690px"></div><div class="fio" style="top:930px"></div>'
b += '<div style="position:absolute;left:540px;top:690px;width:1px;height:480px;background:#353535"></div>'
for (x, y), (k, nome, _, _) in zip([(110, 690), (570, 690), (110, 930), (570, 930)], ITENS):
    b += f'<div class="cel solo" style="left:{x}px;top:{y}px;width:400px"><div class="k">{k}</div><div class="h">{nome}</div></div>'
page(1, b)

# 2 e 3 — dois elementos por slide: numeral vazado à esquerda, texto na coluna da direita
def dois(n, a, c):
    s = ''
    for (k, nome, de, ds), top in ((a, 255), (c, 740)):
        s += f'<div class="num" style="position:absolute;left:104px;top:{top + 6}px;font-size:190px">{k}</div>'
        s += (f'<div class="solo" style="position:absolute;left:360px;top:{top}px;width:610px">'
              f'<div class="h" style="font-size:52px;line-height:1.04;text-wrap:balance">{nome}</div>'
              f'<p class="def" style="margin-top:18px">{de}</p><div class="dest" style="margin-top:22px">{ds}</div></div>')
    s += '<div class="fio" style="top:660px"></div>'
    page(n, s)
dois(2, ITENS[0], ITENS[1])
dois(3, ITENS[2], ITENS[3])

# 4 — como analisar
PASSOS = [
    ('Olhe para o seu modelo', 'Avalie os quatro elementos na sua empresa, com número, não com impressão.'),
    ('Seja honesto', 'Pergunte se o problema está na gestão ou no próprio modelo, porque cada um pede uma correção diferente.'),
    ('Reinvente quando precisar', 'Se as deficiências superam as virtudes, é hora de mudar o modelo.'),
]
b4 = '<div class="h solo" style="position:absolute;left:110px;top:210px;font-size:96px">Como analisar<br><span class="acento">o seu modelo</span></div>'
b4 += '<p class="def solo" style="position:absolute;left:110px;top:440px;width:800px;font-size:30px">Todo negócio tem virtudes e deficiências. O que muda o resultado é conhecer as da sua empresa antes de tomar qualquer decisão.</p>'
y = 640
for i, (t, p) in enumerate(PASSOS):
    b4 += f'<div class="fio" style="top:{y - 34}px"></div>'
    b4 += f'<div class="item solo" style="top:{y}px"><div class="q"></div><div><div class="h">{t}</div><p>{p}</p></div></div>'
    y += 176
page(4, b4)

# 5 — CTA
b5 = '<div class="lbl solo" style="position:absolute;left:110px;top:300px;color:#A91C20;font-weight:700">Imersão MBV</div>'
b5 += '<p class="solo" style="position:absolute;left:110px;top:350px;width:840px;font-size:46px;line-height:1.3">No MBV, o dono de pequena e média empresa aprende a ler o próprio negócio e a decidir com base nele:</p>'
b5 += '<div class="fio" style="top:660px"></div><div class="fio" style="top:800px"></div>'
for i, p in enumerate(['Lucratividade', 'Crescimento', 'Cultura']):
    x = 110 + i * 287
    if i:
        b5 += f'<div style="position:absolute;left:{x}px;top:660px;width:1px;height:140px;background:#353535"></div>'
    b5 += f'<div class="h solo" style="position:absolute;left:{x + (24 if i else 0)}px;top:705px;font-size:42px">{p}</div>'
b5 += '<div class="btn solo" style="position:absolute;left:110px;top:900px">Link na bio <span style="font-family:Montserrat;font-weight:600;font-size:44px">&rarr;</span></div>'
page(5, b5)
print('ok')
