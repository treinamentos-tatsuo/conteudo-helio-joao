"""Post 256 — os 4 elementos de um bom modelo de negocio (apostila pp. 8-11 e 24), 7 slides no padrao vigente do infografico:
capa no layout F (circulo em 4 fatias, do 224), miolo no layout G (um recurso visual por slide, do 229/243), CTA do 224/243.
Fundo escuro, Montserrat, vermelho so #A91C20, sem paginacao. Texto = v1 do carousel-text.md."""
import math, pathlib, re

POST = pathlib.Path(__file__).resolve().parents[1]
RAIZ = next((p for p in pathlib.Path(__file__).resolve().parents if (p / '.claude/skills/carrossel').is_dir()), pathlib.Path.cwd())
ICO = RAIZ / '.claude/skills/carrossel/modelos/infografico/icones'
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
.T .n{{color:{RED};margin-right:6px}}
.sub{{position:absolute;left:100px;width:880px;text-align:center;font-weight:600;font-size:26px}}
.sub u{{color:{RED};text-decoration-thickness:3px;text-underline-offset:6px}}
.P{{position:absolute;left:130px;width:820px;text-align:center;font-weight:500;font-size:28px;line-height:1.45;color:#e8e8e8;text-wrap:balance}}
.P b{{color:#fff;font-weight:800}}
.badge{{border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 9px #0d0d0d}}
.tag{{display:inline-block;background:{RED};color:#fff;border-radius:6px;padding:6px 14px 5px;font-weight:800;font-size:22px;text-transform:uppercase;letter-spacing:.02em;white-space:nowrap;border:2px solid transparent}}
.tagw{{background:#fff;color:#0d0d0d}}
.tagg{{background:#2c2c2c;border:2px solid #5a5a5a}}
.cap{{font-weight:700;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#bdbdbd}}
.card{{position:absolute;border-radius:14px;background:linear-gradient(160deg,#1f1f1f,#141414);border:2px solid {RED}}}
.fecho{{position:absolute;left:130px;width:820px;text-align:center;background:#fff;color:{RED};font-weight:800;font-size:29px;line-height:1.38;
  padding:22px 36px;border-radius:6px;text-wrap:balance;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)}}
.arr{{position:absolute;right:110px;top:1200px;font-weight:700;font-size:20px;letter-spacing:.2em;color:#9a9a9a}}
"""

TOTAL = 7


def w(n, body):
    foot = '<div class="arr">ARRASTE &rarr;</div>' if n < TOTAL else ''
    html = (f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="s"><div class="conteudo">{body}{foot}</div></div></body></html>')
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html, encoding='utf-8', newline='\n')


def svg(inner, h=1350):
    return f'<svg width="1080" height="{h}" viewBox="0 0 1080 {h}" style="position:absolute;inset:0;overflow:visible">{inner}</svg>'


def titulo(num, l1, l2, top=120, fs=58):
    n = f'<span class="n">{num} ·</span>' if num else ''
    return f'<div class="T solo" style="top:{top}px;font-size:{fs}px">{n}{l1}<br><span class="v">{l2}</span></div>'


def fecho(texto, top):
    return f'<div class="fecho solo" style="top:{top}px">{texto}</div>'


# ---------------- 1 CAPA: circulo em 4 fatias (layout F) ----------------
CX, CY, R = 540, 800, 410
RI_RED, RI_BLK = 100, 64


def pt(r, a):
    return (CX + r * math.cos(math.radians(a)), CY + r * math.sin(math.radians(a)))


def fatia(a0, a1, r0=RI_RED):
    x0, y0 = pt(R, a0); x1, y1 = pt(R, a1); x2, y2 = pt(r0, a1); x3, y3 = pt(r0, a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r0},{r0} 0 0 0 {x3:.1f},{y3:.1f} Z'


DIV = (180, 270, 0, 90)                        # divisores: fatias sup-esq, sup-dir, inf-dir, inf-esq
SECT = [(180, 270), (270, 360), (0, 90), (90, 180)]
g = ('<defs><radialGradient id="gf" cx="540" cy="800" r="410" gradientUnits="userSpaceOnUse">'
     '<stop offset="0.3" stop-color="#1f1f1f"/><stop offset="1" stop-color="#121212"/></radialGradient></defs>')
for a0, a1 in SECT:
    g += f'<path d="{fatia(a0, a1)}" fill="url(#gf)"/>'
    x0, y0 = pt(R, a0 + 3); x1, y1 = pt(R, a1 - 3)
    g += f'<path d="M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="{RED}" stroke-width="3"/>'
for a in DIV:
    x0, y0 = pt(RI_BLK, a); x1, y1 = pt(R + 6, a)
    g += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#0d0d0d" stroke-width="16"/>'
g += f'<circle cx="{CX}" cy="{CY}" r="{RI_RED}" fill="{RED}"/><circle cx="{CX}" cy="{CY}" r="{RI_BLK}" fill="#0d0d0d"/>'
for a in DIV:
    x0, y0 = pt(RI_BLK - 2, a); x1, y1 = pt(RI_RED + 2, a)
    g += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#0d0d0d" stroke-width="16"/>'
b = svg(g)
b += ('<div class="tb solo" style="top:112px;font-size:48px;white-space:nowrap">Os 4 elementos de um<br>'
      '<span class="v" style="font-size:58px">bom modelo de negócio</span></div>')
b += '<div class="sub solo" style="top:292px;font-size:25px;white-space:nowrap">Quanto mais fortes na sua empresa, <u>mais fácil é crescer com lucro</u></div>'
b += f'<div style="position:absolute;left:{CX-44}px;top:{CY-44}px">{icon("building-store", 88, "#ffffff", 1.7)}</div>'
EL = [('1', 'Estrutura de<br>capital baixa', 'wallet', 225),
      ('2', 'Margem de<br>contribuição alta', 'coin', 315),
      ('3', 'Alta capacidade<br>de crescimento', 'trending-up', 45),
      ('4', 'Recorrência<br>na receita', 'calendar-event', 135)]
for num, nome, ic, ang in EL:
    bx, by = pt(R, ang)
    b += f'<div class="badge solo" style="position:absolute;left:{bx-48:.0f}px;top:{by-48:.0f}px;width:96px;height:96px">{icon(ic, 52)}</div>'
    tx, ty = pt(222, ang)
    b += (f'<div class="solo" style="position:absolute;left:{tx-140:.0f}px;top:{ty-62:.0f}px;width:280px;text-align:center">'
          f'<div style="font-weight:900;font-size:44px;line-height:1;color:{RED}">{num}</div>'
          f'<div style="margin-top:10px;font-weight:800;font-size:25px;line-height:1.18;text-transform:uppercase;letter-spacing:-.3px">{nome}</div></div>')
w(1, b)

# ---------------- 2 CAPITAL: modelo pesado x modelo leve ----------------
b = titulo('1', 'Estrutura de', 'capital baixa')
b += ('<div class="P solo" style="top:285px">É quanto dinheiro a empresa precisa deixar <b>preso</b> para funcionar e crescer: '
      'estoque, equipamento, prazo dado ao cliente.</div>')
CT, CH = 470, 440
nota = lambda n: ''.join(f'<div style="margin:5px">{icon("cash-banknote", 50, "#ffffff", 1.8)}</div>' for _ in range(n))
b += (f'<div class="card solo" style="left:130px;top:{CT}px;width:395px;height:{CH}px;background:{RED};border-color:{RED};'
      f'display:flex;flex-direction:column;align-items:center;padding-top:26px">'
      f'<span class="tag tagw">Modelo pesado</span>'
      f'<div style="margin-top:24px;width:300px;display:flex;flex-wrap:wrap;justify-content:center">{nota(12)}</div>'
      f'<div style="position:absolute;bottom:24px;font-weight:700;font-size:21px;line-height:1.3;text-align:center">muito dinheiro<br>parado na operação</div></div>')
b += (f'<div class="card solo" style="left:555px;top:{CT}px;width:395px;height:{CH}px;border-color:#5a5a5a;'
      f'display:flex;flex-direction:column;align-items:center;padding-top:26px">'
      f'<span class="tag tagg">Modelo leve</span>'
      f'<div style="margin-top:24px;width:300px;display:flex;flex-wrap:wrap;justify-content:center">{nota(3)}</div>'
      f'<div style="position:absolute;bottom:24px;font-weight:700;font-size:21px;line-height:1.3;color:#dcdcdc;text-align:center">pouco dinheiro<br>parado na operação</div></div>')
b += fecho('Quanto menos dinheiro parado, mais a empresa aguenta o aperto e mais liberdade o dono tem.', 975)
w(2, b)

# ---------------- 3 MARGEM: duas vendas de R$ 100 (p. 24) ----------------
b = titulo('2', 'Margem de', 'contribuição alta')
b += ('<div class="P solo" style="top:285px">É o que sobra de cada venda depois de pagar tudo o que só existe por causa dela: '
      'imposto, comissão, taxa do cartão, frete e o próprio produto.</div>')
BW = 800


def barra(top, rotulo, sobra):
    wr = int(BW * sobra / 100)
    return (f'<div class="solo" style="position:absolute;left:140px;top:{top}px;width:{BW}px">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="cap" style="color:#fff">{rotulo}</span>'
            f'<span style="font-weight:800;font-size:24px">venda de R$ 100</span></div>'
            f'<div style="margin-top:12px;display:flex;height:74px;border-radius:6px;overflow:hidden;border:2px solid #5a5a5a">'
            f'<div style="width:{wr}px;background:{RED};display:flex;align-items:center;justify-content:center;font-weight:900;font-size:{30 if sobra > 30 else 22}px;white-space:nowrap">'
            f'{"sobra R$ " + str(sobra) if sobra > 30 else "R$ " + str(sobra)}</div>'
            f'<div style="flex:1;background:#2c2c2c;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:21px;color:#bdbdbd;white-space:nowrap">'
            f'{100 - sobra} vão embora na venda</div></div></div>')


b += barra(480, 'Produto A', 60)
b += barra(650, 'Produto B', 15)
b += f'<div class="solo" style="position:absolute;left:140px;top:845px;width:800px;text-align:center"><span class="tag tagw" style="font-size:25px;padding:9px 18px 8px">O faturamento é igual. O resultado não.</span></div>'
b += fecho('Margem alta perdoa um erro de preço e segura um mês fraco. Margem baixa não deixa espaço para errar.', 975)
w(3, b)

# ---------------- 4 CRESCIMENTO: modelo que trava x modelo que escala ----------------
b = titulo('3', 'Alta capacidade', 'de crescimento')
b += ('<div class="P solo" style="top:285px">É o quanto a empresa consegue vender a mais sem precisar <b>reconstruir a operação</b> a cada passo.</div>')
CT, CH = 420, 520


def mini(rot, w1, w2, cor2):
    return (f'<div style="margin-top:24px;width:330px;text-align:left"><div class="cap" style="font-size:19px;color:#fff">{rot}</div>'
            f'<div style="margin-top:10px;display:flex;align-items:center;gap:12px"><div style="width:{w1}px;height:38px;border-radius:5px;background:#5a5a5a"></div>'
            f'<span class="cap" style="font-size:16px">hoje</span></div>'
            f'<div style="margin-top:8px;display:flex;align-items:center;gap:12px"><div style="width:{w2}px;height:38px;border-radius:5px;background:{cor2}"></div>'
            f'<span class="cap" style="font-size:16px;color:#fff;white-space:nowrap">no dobro</span></div></div>')


b += (f'<div class="card solo" style="left:130px;top:{CT}px;width:395px;height:{CH}px;display:flex;flex-direction:column;align-items:center;padding-top:26px">'
      f'<span class="tag">Modelo que trava</span>'
      f'{mini("Vendas", 75, 150, "#ffffff")}{mini("Estrutura", 75, 150, RED)}'
      f'<div style="position:absolute;bottom:24px;font-weight:700;font-size:21px;line-height:1.3;text-align:center;width:360px;font-size:20px">para vender o dobro, precisa do<br>dobro de gente, espaço e estoque</div></div>')
b += (f'<div class="card solo" style="left:555px;top:{CT}px;width:395px;height:{CH}px;border-color:#5a5a5a;display:flex;flex-direction:column;align-items:center;padding-top:26px">'
      f'<span class="tag tagg">Modelo que escala</span>'
      f'{mini("Vendas", 75, 150, "#ffffff")}{mini("Estrutura", 75, 95, "#8a8a8a")}'
      f'<div style="position:absolute;bottom:24px;font-weight:700;font-size:21px;line-height:1.3;text-align:center;color:#dcdcdc;width:330px">vende o dobro e a estrutura<br>cresce bem menos</div></div>')
b += fecho('Um bom modelo cresce sem que cada cliente novo vire um problema novo.', 995)
w(4, b)

# ---------------- 5 RECORRENCIA: barras mes a mes ----------------
b = titulo('4', 'Recorrência', 'na receita')
b += ('<div class="P solo" style="top:285px">É a parte do faturamento que <b>se repete todo mês</b>, sem precisar conquistar o cliente de novo.</div>')
BASE, BASEH = 860, 170
TOPS = [90, 150, 60, 130, 80, 170]
g = f'<line x1="150" y1="{BASE}" x2="930" y2="{BASE}" stroke="#6a6a6a" stroke-width="2"/>'
bx0, bw, gap = 175, 95, 34
for i, th in enumerate(TOPS):
    x = bx0 + i * (bw + gap)
    g += f'<rect x="{x}" y="{BASE-BASEH}" width="{bw}" height="{BASEH}" fill="{RED}"/>'
    g += f'<rect x="{x}" y="{BASE-BASEH-th-6}" width="{bw}" height="{th}" rx="4" fill="#2c2c2c" stroke="#6a6a6a" stroke-width="2"/>'
b += svg(g)
b += ''.join(f'<div class="cap" style="position:absolute;left:{bx0 + i*(bw+gap)}px;top:{BASE+12}px;width:{bw}px;text-align:center;font-size:16px">mês {i+1}</div>' for i in range(6))
b += (f'<div class="solo" style="position:absolute;left:130px;top:{BASE+52}px;width:820px;display:flex;justify-content:center;gap:40px">'
      f'<span style="display:flex;align-items:center;gap:12px;font-weight:700;font-size:22px"><span style="width:28px;height:28px;background:{RED};border-radius:4px"></span>a receita que volta</span>'
      f'<span style="display:flex;align-items:center;gap:12px;font-weight:700;font-size:22px;color:#dcdcdc"><span style="width:28px;height:28px;background:#2c2c2c;border:2px solid #6a6a6a;border-radius:4px"></span>a venda nova</span></div>')
b += fecho('Receita que volta todo mês dá previsibilidade, acalma o caixa e tira o dono do sufoco de começar do zero.', 985)
w(5, b)

# ---------------- 6 NAO EXISTE MODELO PERFEITO (p. 11) ----------------
b = titulo('', 'Não existe', 'modelo perfeito')
b += ('<div class="P solo" style="top:285px">Nenhum negócio é forte nos quatro elementos ao mesmo tempo. A pergunta não é se o seu modelo é bom ou ruim. '
      '<b>É onde ele é forte, onde é frágil e o que fazer a respeito.</b></div>')
PASSOS = [('gauge', 'Olhe para o seu modelo', 'Conheça as virtudes e as deficiências antes de decidir qualquer coisa.'),
          ('scale', 'Seja honesto', 'O problema está na gestão ou no modelo? Cada um pede uma correção diferente.'),
          ('target-arrow', 'Reinvente quando precisar', 'Se as deficiências superam as virtudes, é hora de mudar o modelo.')]
for i, (ic, t, d) in enumerate(PASSOS):
    top = 545 + i * 205
    b += (f'<div class="card solo" style="left:130px;top:{top}px;width:820px;height:170px;display:flex;align-items:center;gap:28px;padding:0 34px 0 26px">'
          f'<div class="badge" style="flex:0 0 100px;height:100px;box-shadow:none">{icon(ic, 54)}</div>'
          f'<div><span class="tag">{t}</span><div style="margin-top:12px;font-weight:500;font-size:24px;line-height:1.38;color:#e8e8e8">{d}</div></div></div>')
w(6, b)

# ---------------- 7 CTA ----------------
b = '<div class="T solo" style="top:120px;font-size:54px">Você sabe qual<br>dos quatro elementos<br><span class="v">é o ponto fraco</span><br>da sua empresa?</div>'
pil = [('coin', 'Lucratividade'), ('trending-up', 'Crescimento'), ('hierarchy-2', 'Cultura')]
b += '<div class="solo" style="position:absolute;left:130px;top:450px;width:820px;display:flex;justify-content:space-between">'
for ic, nm in pil:
    b += (f'<div style="width:240px;display:flex;flex-direction:column;align-items:center">'
          f'<div class="badge" style="width:120px;height:120px">{icon(ic, 62)}</div>'
          f'<div style="margin-top:20px"><span class="tag">{nm}</span></div></div>')
b += '</div>'
b += ('<div class="P solo" style="top:690px;font-size:29px">No <b>MBV</b>, treinamento de três dias para donos de pequenas e médias empresas, '
      'você aprende a fazer a gestão dos três pilares: Lucratividade, Crescimento e Cultura.</div>')
b += ('<div class="solo" style="position:absolute;left:50%;transform:translateX(-50%);top:950px;white-space:nowrap;background:#fff;color:' + RED + ';'
      'font-weight:800;font-size:38px;letter-spacing:-.5px;padding:24px 44px;border-radius:6px;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)">QUERO PARTICIPAR DO MBV</div>')
b += '<div class="solo" style="position:absolute;left:0;right:0;top:1085px;text-align:center;font-weight:800;font-size:26px;letter-spacing:.2em">LINK NA BIO &rarr;</div>'
w(7, b)
print('ok')
