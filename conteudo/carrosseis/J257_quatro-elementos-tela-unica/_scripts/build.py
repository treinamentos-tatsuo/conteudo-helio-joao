"""Post 257 — os 4 elementos de um bom modelo de negocio em UMA tela (Frame Work, apostila p. 9).
Layout F do 224 (circulo em fatias) com 4 quadrantes: nome em etiqueta + definicao curta dentro de cada fatia, badge na borda,
e o CTA do MBV numa faixa no rodape. Fundo escuro, Montserrat, vermelho so #A91C20."""
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


CSS = f"""@import url('https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@500;600;700;800;900&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#0e0e0e}}
.s{{position:relative;width:1080px;height:1350px;background:url('../imagens/fundo.png');color:#fff;font-family:'Montserrat',sans-serif;overflow:hidden}}
.s::after{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.45) 100%);pointer-events:none}}
.conteudo{{position:absolute;inset:0;z-index:2}}
.tb{{position:absolute;left:90px;width:900px;text-align:center;font-family:'Anton',sans-serif;color:#fff;text-transform:uppercase;line-height:1.2;letter-spacing:.5px;white-space:nowrap;text-shadow:0 4px 18px rgba(0,0,0,.45)}}
.tb .v{{color:{RED}}}
.sub{{position:absolute;left:100px;width:880px;text-align:center;font-family:'Source Serif 4',serif;font-weight:400;font-size:28px;color:#ececec;white-space:nowrap}}
.sub u{{color:{RED};text-decoration-thickness:2px;text-underline-offset:6px}}
.badge{{border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 9px #0d0d0d}}
.fat .t{{display:inline-block;background:{RED};color:#fff;border-radius:6px;padding:6px 12px 5px;box-shadow:0 6px 16px rgba(0,0,0,.35);
  font-weight:800;font-size:21px;line-height:1.15;text-transform:uppercase;letter-spacing:-.3px;white-space:nowrap}}
.fat .d{{margin-top:12px;font-weight:500;font-size:20px;line-height:1.4;color:#e4e4e4;text-wrap:balance}}
.cta{{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;display:flex;align-items:center;gap:22px}}
.btn{{background:#fff;color:{RED};font-weight:800;font-size:26px;letter-spacing:-.3px;padding:15px 28px;border-radius:6px;
  box-shadow:0 0 0 5px rgba(169,28,32,.55),0 10px 24px rgba(0,0,0,.5)}}
.bio{{font-weight:800;font-size:22px;letter-spacing:.18em}}
"""

CX, CY, R = 540, 745, 380
RI_RED, RI_BLK = 92, 58


def pt(r, a):
    return (CX + r * math.cos(math.radians(a)), CY + r * math.sin(math.radians(a)))


def fatia(a0, a1, r0=RI_RED):
    x0, y0 = pt(R, a0); x1, y1 = pt(R, a1); x2, y2 = pt(r0, a1); x3, y3 = pt(r0, a0)
    return f'M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} A{r0},{r0} 0 0 0 {x3:.1f},{y3:.1f} Z'


DIV = (180, 270, 0, 90)
SECT = [(180, 270), (270, 360), (0, 90), (90, 180)]
g = ('<defs><radialGradient id="gf" cx="540" cy="745" r="380" gradientUnits="userSpaceOnUse">'
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
b = f'<svg width="1080" height="1350" viewBox="0 0 1080 1350" style="position:absolute;inset:0">{g}</svg>'
b += ('<div class="tb solo" style="top:110px;font-size:72px">Os 4 elementos de um<br>'
      '<span class="v">bom modelo de negócio</span></div>')
b += '<div class="sub solo" style="top:290px;font-size:28px">Quanto mais fortes na sua empresa, <u>mais fácil é crescer com lucro</u></div>'
b += f'<div style="position:absolute;left:{CX-40}px;top:{CY-40}px">{icon("building-store", 80, "#ffffff", 1.7)}</div>'

# (nome, definicao da p. 9, icone, angulo do badge, centro do bloco)
EL = [('Estrutura de<br>capital baixa', 'Exige pouco dinheiro parado para operar e crescer.', 'wallet', 200, (375, 590)),
      ('Margem de<br>contribuição alta', 'Sobra bastante de cada venda para pagar a estrutura.', 'coin', 340, (702, 590)),
      ('Alta capacidade<br>de crescimento', 'O negócio escala sem reconstruir a operação inteira.', 'trending-up', 20, (708, 905)),
      ('Recorrência<br>na receita', 'O cliente volta, e a receita se repete no tempo.', 'calendar-event', 160, (372, 905))]
for nome, d, ic, ang, (cx, cy) in EL:
    bx, by = pt(R, ang)
    b += f'<div class="badge solo" style="position:absolute;left:{bx-42:.0f}px;top:{by-42:.0f}px;width:84px;height:84px">{icon(ic, 46)}</div>'
    b += (f'<div class="fat solo" style="position:absolute;left:{cx-140}px;top:{cy-82}px;width:280px;text-align:center">'
          f'<div class="t">{nome}</div><div class="d">{d}</div></div>')

b += ('<div class="cta solo" style="top:1158px"><div class="btn">QUERO PARTICIPAR DO MBV</div>'
      '<div class="bio">LINK NA BIO &rarr;</div></div>')

html = (f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
        f'<div class="s"><div class="conteudo">{b}</div></div></body></html>')
(POST / 'instagram' / 'slide-01.html').write_text(html, encoding='utf-8', newline='\n')
print('ok')
