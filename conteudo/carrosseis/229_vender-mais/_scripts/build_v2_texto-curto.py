"""Post 229 — vender mais (apostila p. 44), 6 slides no padrao visual do 224 (fundo escuro, Montserrat, vermelho so #A91C20,
titulo da capa em bloco branco, sem paginacao). Cada slide tem um recurso visual que guia o olhar: grafico, linha do tempo,
barras, grafico mes a mes e diagrama de caminhos. Texto = o aprovado (v2 mastigada)."""
import pathlib, re

POST = pathlib.Path(__file__).resolve().parents[1]
ICO = pathlib.Path('/Users/pedrohenrique/Documents/tatsuo-carrossel/.claude/skills/carrossel/modelos/infografico/icones')
RED = '#A91C20'


def icon(nome, px, cor='#ffffff', traco=2.0):
    s = (ICO / f'{nome}.svg').read_text()
    s = re.sub(r'width="24"', f'width="{px}"', s, count=1)
    s = re.sub(r'height="24"', f'height="{px}"', s, count=1)
    s = s.replace('stroke="currentColor"', f'stroke="{cor}"', 1).replace('stroke-width="2"', f'stroke-width="{traco}"', 1)
    return re.sub(r'class="[^"]*"', '', s, count=1)


CSS = f"""@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#0e0e0e}}
.s{{position:relative;width:1080px;height:1350px;background:url('../imagens/fundo.png');color:#fff;font-family:'Montserrat',sans-serif;overflow:hidden}}
.s::after{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.45) 100%);pointer-events:none}}
.conteudo{{position:absolute;inset:0;z-index:2}}
.tb{{position:absolute;left:110px;width:860px;text-align:center;background:#fff;color:#0d0d0d;border-radius:6px;padding:20px 0 18px;
  font-weight:800;text-transform:uppercase;letter-spacing:-1.2px;line-height:1.08;box-shadow:0 12px 30px rgba(0,0,0,.5)}}
.tb .v{{color:{RED}}}
.T{{position:absolute;left:100px;width:880px;text-align:center;font-weight:800;text-transform:uppercase;letter-spacing:-1.2px;line-height:1.08;font-size:58px}}
.T .v{{color:{RED}}}
.sub{{position:absolute;left:100px;width:880px;text-align:center;font-weight:600;font-size:26px}}
.sub u{{color:{RED};text-decoration-thickness:3px;text-underline-offset:6px}}
.P{{position:absolute;left:130px;width:820px;text-align:center;font-weight:500;font-size:28px;line-height:1.45;color:#e8e8e8;text-wrap:balance}}
.P b{{color:#fff;font-weight:800}}
.badge{{border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 9px #0d0d0d}}
.tag{{display:inline-block;background:{RED};color:#fff;border-radius:6px;padding:6px 14px 5px;font-weight:800;font-size:22px;text-transform:uppercase;letter-spacing:.02em}}
.cap{{font-weight:700;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#bdbdbd}}
.dest{{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;background:#fff;color:{RED};font-weight:800;font-size:34px;
  padding:18px 34px;border-radius:6px;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)}}
.card{{position:absolute;border-radius:14px;background:linear-gradient(160deg,#1f1f1f,#141414);border:2px solid {RED}}}
.arr{{position:absolute;right:110px;top:1200px;font-weight:700;font-size:20px;letter-spacing:.2em;color:#9a9a9a}}
"""

TOTAL = 6


def w(n, body):
    foot = '<div class="arr">ARRASTE &rarr;</div>' if n < TOTAL else ''
    html = (f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="s"><div class="conteudo">{body}{foot}</div></div></body></html>')
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html)


def svg(inner, h=1350):
    return f'<svg width="1080" height="{h}" viewBox="0 0 1080 {h}" style="position:absolute;inset:0;overflow:visible">{inner}</svg>'


ARROW_DEFS = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
              f'<path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
              f'<marker id="aw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
              f'<path d="M0,0 L10,5 L0,10 z" fill="#ffffff"/></marker></defs>')

# ---------------- 1 CAPA: grafico vendas sobem x caixa cai ----------------
b = ('<div class="tb solo" style="top:112px;font-size:42px;white-space:nowrap">Sua empresa pode quebrar<br>'
     '<span class="v" style="font-size:42px">justamente quando vende mais</span></div>')
b += '<div class="sub solo" style="top:292px">Entenda por que crescer <u>pede dinheiro antes de dar lucro</u></div>'
# grafico: area 160..920 x 430..1080
X0, X1, Y0, Y1 = 170, 910, 470, 1110
g = ARROW_DEFS
g += f'<line x1="{X0}" y1="{Y1}" x2="{X1+20}" y2="{Y1}" stroke="#4a4a4a" stroke-width="2"/>'
g += f'<line x1="{X0}" y1="{Y1}" x2="{X0}" y2="{Y0-10}" stroke="#4a4a4a" stroke-width="2"/>'
n = 6
bw = 70
for i in range(n):
    h = 120 + i * 80
    x = X0 + 50 + i * 118
    g += f'<rect x="{x}" y="{Y1-h}" width="{bw}" height="{h}" rx="6" fill="{RED}" opacity="{0.55 + i*0.09:.2f}"/>'
# linha do caixa caindo
pts = [(X0 + 50 + i * 118 + bw / 2, Y0 + 70 + i * i * 14 + i * 40) for i in range(n)]
d = 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)
g += f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" marker-end="url(#aw)"/>'
for x, y in pts[:-1]:
    g += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#0d0d0d" stroke="#fff" stroke-width="4"/>'
b += svg(g)
b += f'<div class="solo" style="position:absolute;left:{X0+30}px;top:{Y0-10}px;display:flex;gap:30px;align-items:center">' \
     f'<span class="tag">&#9650; vendas</span><span class="tag" style="background:#fff;color:#0d0d0d">&#9660; caixa</span></div>'
w(1, b)

# ---------------- 2 LINHA DO TEMPO: o dinheiro sai antes de voltar ----------------
b = '<div class="T solo" style="top:120px">O dinheiro sai<br><span class="v">antes de voltar</span></div>'
b += ('<div class="P solo" style="top:330px">Você paga o fornecedor, a mercadoria e os salários hoje. '
      'O cliente só paga daqui a algumas semanas.</div>')
LY = 720
g = ARROW_DEFS
g += f'<line x1="210" y1="{LY}" x2="870" y2="{LY}" stroke="#4a4a4a" stroke-width="4" stroke-dasharray="2 14" stroke-linecap="round"/>'
# faixa do dinheiro preso
g += f'<rect x="290" y="{LY-34}" width="500" height="68" rx="34" fill="{RED}" opacity=".18"/>'
g += f'<line x1="300" y1="{LY}" x2="780" y2="{LY}" stroke="{RED}" stroke-width="10" stroke-linecap="round" marker-end="url(#ah)"/>'
b += svg(g)
b += f'<div class="badge solo" style="position:absolute;left:150px;top:{LY-70}px;width:140px;height:140px">{icon("cash-banknote", 72)}</div>'
b += f'<div class="badge solo" style="position:absolute;left:790px;top:{LY-70}px;width:140px;height:140px;background:#fff">{icon("receipt", 70, RED)}</div>'
b += f'<div class="solo" style="position:absolute;left:110px;top:{LY+92}px;width:220px;text-align:center"><div class="cap" style="color:#fff">Hoje</div><div style="margin-top:6px;font-weight:800;font-size:26px">Você paga</div></div>'
b += f'<div class="solo" style="position:absolute;left:750px;top:{LY+92}px;width:220px;text-align:center"><div class="cap" style="color:#fff">Semanas depois</div><div style="margin-top:6px;font-weight:800;font-size:26px">O cliente paga</div></div>'
b += f'<div class="solo" style="position:absolute;left:340px;top:{LY-150}px;width:400px;text-align:center">{icon("lock", 56, "#ffffff", 2.0)}<div style="margin-top:6px;font-weight:800;font-size:27px">Dinheiro preso</div><div class="cap" style="margin-top:4px">dentro da empresa</div></div>'
b += '<div class="P solo" style="top:990px">Enquanto isso, <b>esse dinheiro fica preso dentro da empresa</b>.</div>'
w(2, b)

# ---------------- 3 BARRAS: vender mais prende mais dinheiro ----------------
b = '<div class="T solo" style="top:120px">Vender mais prende<br><span class="v">mais dinheiro</span></div>'
b += ('<div class="P solo" style="top:290px;font-size:26px">Para vender 50% a mais, você compra 50% a mais e paga 50% a mais, tudo antes de receber. '
      'Numa empresa que fatura R$ 300 mil por mês:</div>')
BASE = 1120
U = 0.95  # px por mil
g = ARROW_DEFS
g += f'<line x1="170" y1="{BASE}" x2="910" y2="{BASE}" stroke="#4a4a4a" stroke-width="2"/>'
h400, h600 = 400 * U, 600 * U
g += f'<rect x="240" y="{BASE-h400}" width="220" height="{h400}" rx="8" fill="#2c2c2c" stroke="#5a5a5a" stroke-width="2"/>'
g += f'<rect x="620" y="{BASE-h400}" width="220" height="{h400}" rx="8" fill="#2c2c2c" stroke="#5a5a5a" stroke-width="2"/>'
g += f'<rect x="620" y="{BASE-h600}" width="220" height="{h600-h400+6}" rx="8" fill="{RED}"/>'
# seta de crescimento entre as barras
g += f'<path d="M480,{BASE-h400+60} Q520,{BASE-h600-20} 606,{BASE-h600+40}" fill="none" stroke="#fff" stroke-width="5" marker-end="url(#aw)"/>'
b += svg(g)
b += f'<div class="solo" style="position:absolute;left:240px;top:{BASE-h400+18}px;width:220px;text-align:center;font-weight:900;font-size:34px;white-space:nowrap">R$ 400 mil</div>'
b += f'<div class="solo" style="position:absolute;left:620px;top:{BASE-h600+16}px;width:220px;text-align:center;font-weight:900;font-size:30px;white-space:nowrap">+ R$ 200 mil</div>'
b += f'<div class="solo" style="position:absolute;left:560px;top:{BASE-h600-66}px;width:340px;text-align:center"><span class="tag" style="background:#fff;color:#0d0d0d;font-size:24px">= R$ 600 mil presos</span></div>'
b += f'<div class="solo" style="position:absolute;left:620px;top:{BASE-h400+18}px;width:220px;text-align:center;font-weight:900;font-size:34px;white-space:nowrap">R$ 400 mil</div>'
b += f'<div class="solo" style="position:absolute;left:200px;top:{BASE+16}px;width:300px;text-align:center"><div class="cap" style="color:#fff">Hoje</div></div>'
b += f'<div class="solo" style="position:absolute;left:530px;top:{BASE+16}px;width:400px;text-align:center"><div class="cap" style="color:#fff">Vendendo 50% a mais</div></div>'
b += f'<div class="solo" style="position:absolute;left:150px;top:{BASE-h400-150}px;width:400px;text-align:center">{icon("lock", 44)}<div class="cap" style="margin-top:4px;color:#fff">presos esperando<br>o cliente pagar</div></div>'
w(3, b)

# ---------------- 4 GRAFICO MES A MES: a conta de quem cresce ----------------
b = '<div class="T solo" style="top:120px">A conta de<br><span class="v">quem cresce</span></div>'
b += ('<div class="solo" style="position:absolute;left:110px;top:300px;width:860px;display:flex;gap:28px">'
      f'<div class="card" style="position:relative;flex:1;padding:22px 20px;text-align:center;border-color:#5a5a5a"><div style="font-weight:900;font-size:46px">+ R$ 25 mil</div><div style="margin-top:6px;font-weight:600;font-size:22px;color:#dcdcdc">de lucro a mais por mês,<br>que entra aos poucos</div></div>'
      f'<div class="card" style="position:relative;flex:1;padding:22px 20px;text-align:center;background:{RED};border-color:{RED}"><div style="font-weight:900;font-size:46px">&minus; R$ 200 mil</div><div style="margin-top:6px;font-weight:600;font-size:22px;color:#fff">que saem do caixa agora, antes<br>da primeira venda nova</div></div></div>')
# grafico: saldo acumulado da decisao de crescer, mes 0..8
GX0, GX1, GY0, GY1 = 190, 900, 560, 1040
zero_y = GY0 + 60
scale = (GY1 - zero_y) / 200
g = ARROW_DEFS
g += f'<line x1="{GX0}" y1="{zero_y}" x2="{GX1+10}" y2="{zero_y}" stroke="#6a6a6a" stroke-width="2"/>'
step = (GX1 - GX0) / 9
for m in range(9):
    val = -200 + 25 * m
    x = GX0 + step * (m + 0.5) - 26
    if val < 0:
        h = -val * scale
        g += f'<rect x="{x:.0f}" y="{zero_y}" width="52" height="{h:.0f}" rx="5" fill="{RED}" opacity="{1 - m*0.07:.2f}"/>'
    g += f'<text x="{x+26:.0f}" y="{GY1+44}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="18" fill="#bdbdbd">{"HOJE" if m == 0 else f"MÊS {m}"}</text>'
# seta mostrando a volta
xm8 = GX0 + step * 8.5
g += f'<path d="M{GX0+step*0.5+30:.0f},{GY1-20} Q{(GX0+xm8)/2:.0f},{GY1+0} {xm8-20:.0f},{zero_y+24}" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="10 9" marker-end="url(#aw)"/>'
g += f'<circle cx="{xm8:.0f}" cy="{zero_y}" r="13" fill="#fff"/>'
b += svg(g)
b += f'<div class="solo" style="position:absolute;left:{GX0-80}px;top:{zero_y-34}px;width:70px;text-align:right" ><span class="cap" style="color:#fff">R$ 0</span></div>'
b += f'<div class="solo" style="position:absolute;left:{xm8-190:.0f}px;top:{zero_y-118}px;width:300px;text-align:center"><span class="tag" style="background:#fff;color:{RED}">só no mês 8</span><div style="margin-top:8px;font-weight:700;font-size:20px;color:#e6e6e6">o lucro extra cobre a conta</div></div>'
b += '<div class="dest solo" style="top:1115px;font-size:30px;padding:14px 30px">O lucro vem depois. A conta vem antes.</div>'
w(4, b)

# ---------------- 5 CAMINHOS: de onde sai esse dinheiro ----------------
b = '<div class="T solo" style="top:120px">De onde sai<br><span class="v">esse dinheiro?</span></div>'
b += '<div class="P solo" style="top:290px">Só existem três lugares:</div>'
HX, HY = 540, 470
g = ARROW_DEFS
for tx in (230, 540, 850):
    g += f'<path d="M{HX},{HY+95} C{HX},{HY+180} {tx},{HY+150} {tx},{HY+240}" fill="none" stroke="{RED}" stroke-width="6" marker-end="url(#ah)"/>'
b += svg(g)
b += (f'<div class="solo" style="position:absolute;left:{HX-120}px;top:{HY-50}px;width:240px;height:150px;border-radius:12px;background:#fff;color:#0d0d0d;'
      f'display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-weight:900;font-size:40px">R$ 200 mil</div>'
      f'<div class="cap" style="color:{RED};margin-top:4px">para crescer</div></div>')
F = [('coin', 'Do lucro que você deixou na empresa', 230, ''),
     ('wallet', 'Do seu próprio bolso', 540, ''),
     ('building-bank', 'Do banco', 850, 'que cobra juros todo mês')]
for ic, t, x, extra in F:
    b += (f'<div class="solo" style="position:absolute;left:{x-140}px;top:{HY+250}px;width:280px;text-align:center;display:flex;flex-direction:column;align-items:center">'
          f'<div class="badge" style="width:116px;height:116px">{icon(ic, 60)}</div>'
          f'<div style="margin-top:22px;font-weight:800;font-size:26px;line-height:1.25;text-wrap:balance">{t}</div>'
          + (f'<div style="margin-top:10px"><span class="tag" style="font-size:18px">{extra}</span></div>' if extra else '') + '</div>')
b += ('<div class="card solo" style="left:130px;top:1035px;width:820px;padding:24px 34px;text-align:center;font-weight:700;font-size:26px;line-height:1.4">'
      'Quem acelera sem saber de onde vai sair o dinheiro pode <span style="color:#fff;background:' + RED + ';padding:0 8px;border-radius:4px">crescer e quebrar ao mesmo tempo</span>.</div>')
w(5, b)

# ---------------- 6 CTA ----------------
b = '<div class="T solo" style="top:150px;font-size:60px">Sua empresa está<br><span class="v">pronta para crescer?</span></div>'
pil = [('coin', 'Lucratividade'), ('trending-up', 'Crescimento'), ('hierarchy-2', 'Cultura')]
b += '<div class="solo" style="position:absolute;left:130px;top:380px;width:820px;display:flex;justify-content:space-between">'
for ic, nm in pil:
    b += (f'<div style="width:240px;display:flex;flex-direction:column;align-items:center">'
          f'<div class="badge" style="width:120px;height:120px">{icon(ic, 62)}</div>'
          f'<div style="margin-top:20px"><span class="tag">{nm}</span></div></div>')
b += '</div>'
b += ('<div class="P solo" style="top:660px;font-size:29px">No <b>MBV</b>, imersão de três dias para donos de pequenas e médias empresas, '
      'você aprende a fazer a gestão dos três pilares: Lucratividade, Crescimento e Cultura.</div>')
b += ('<div class="solo" style="position:absolute;left:50%;transform:translateX(-50%);top:930px;white-space:nowrap;background:#fff;color:' + RED + ';'
      'font-weight:800;font-size:38px;letter-spacing:-.5px;padding:24px 44px;border-radius:6px;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)">QUERO PARTICIPAR DO MBV</div>')
b += '<div class="solo" style="position:absolute;left:0;right:0;top:1065px;text-align:center;font-weight:800;font-size:26px;letter-spacing:.2em">LINK NA BIO &rarr;</div>'
w(6, b)
print('ok')
