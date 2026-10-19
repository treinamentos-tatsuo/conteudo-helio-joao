"""Post 259 — a DRE gerencial em cinco perguntas (apostila pp. 21-22; valores da empresa-exemplo da p. 27), Frame Work tela unica (layout H)."""
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
.tb{{position:absolute;left:110px;width:860px;text-align:center;background:#fff;color:#0d0d0d;border-radius:6px;padding:18px 0 16px;
  font-weight:800;text-transform:uppercase;letter-spacing:-1.2px;line-height:1.08;box-shadow:0 12px 30px rgba(0,0,0,.5);white-space:nowrap}}
.tb .v{{color:{RED}}}
.sub{{position:absolute;left:100px;width:880px;text-align:center;font-weight:600;font-size:25px;white-space:nowrap}}
.sub u{{color:{RED};text-decoration-thickness:3px;text-underline-offset:6px}}
.badge{{border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center}}
.tag{{display:inline-block;background:{RED};color:#fff;border:2px solid {RED};border-radius:6px;padding:6px 14px 5px;font-weight:800;font-size:22px;
  text-transform:uppercase;letter-spacing:.01em;white-space:nowrap}}
.tagw{{background:#fff;color:#0d0d0d;border-color:#fff}}
.tagg{{background:#2c2c2c;border-color:#5a5a5a}}
.cap{{font-weight:700;font-size:17px;letter-spacing:.12em;text-transform:uppercase;color:#bdbdbd}}
.card{{position:absolute;border-radius:14px;background:linear-gradient(160deg,#1f1f1f,#141414);border:2px solid {RED}}}
.cardg{{border-color:#5a5a5a}}
.cardr{{background:{RED};border-color:{RED}}}
.fecho{{position:absolute;left:130px;width:820px;text-align:center;background:#fff;color:{RED};font-weight:800;font-size:25px;line-height:1.36;
  padding:16px 30px;border-radius:6px;text-wrap:balance;box-shadow:0 0 0 5px rgba(169,28,32,.55),0 10px 24px rgba(0,0,0,.5)}}
.cta{{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;display:flex;align-items:center;gap:22px}}
.btn{{background:#fff;color:{RED};font-weight:800;font-size:26px;letter-spacing:-.3px;padding:15px 28px;border-radius:6px;
  box-shadow:0 0 0 5px rgba(169,28,32,.55),0 10px 24px rgba(0,0,0,.5)}}
.bio{{font-weight:800;font-size:22px;letter-spacing:.18em}}
"""

DEFS = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
        f'<marker id="ag" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="#8a8a8a"/></marker>'
        f'<marker id="aw" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="#ffffff"/></marker></defs>')


def svg(inner):
    return f'<svg width="1080" height="1350" viewBox="0 0 1080 1350" style="position:absolute;inset:0;overflow:visible">{DEFS}{inner}</svg>'


def titulo(l1, l2, fs1=46, fs2=56):
    return f'<div class="tb solo" style="top:110px;font-size:{fs1}px">{l1}<br><span class="v" style="font-size:{fs2}px">{l2}</span></div>'


def sub(texto, top=282, fs=25):
    return f'<div class="sub solo" style="top:{top}px;font-size:{fs}px">{texto}</div>'


def fecho(texto, top):
    return f'<div class="fecho solo" style="top:{top}px">{texto}</div>'


CTA = ('<div class="cta solo" style="top:1158px"><div class="btn">QUERO PARTICIPAR DO MBV</div>'
       '<div class="bio">LINK NA BIO &rarr;</div></div>')


def salvar(b):
    html = (f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="s"><div class="conteudo">{b}{CTA}</div></div></body></html>')
    (POST / 'instagram' / 'slide-01.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok')


b = titulo('A DRE gerencial', 'em cinco perguntas', 48, 56)
b += sub('Cada linha responde uma pergunta <u>do seu negócio</u>')
LIN = [('R$', 'Faturamento', 'Quanto entrou de venda?', 'Não é lucro, é o volume.', 100, '1 milhão', 'w'),
       ('−', 'Gastos variáveis', 'Quanto custou para poder vender?', 'imposto, produto, comissão, frete, maquininha', 60, '600 mil', 'r'),
       ('=', 'Margem de contribuição', 'Quanto sobra de cada venda para pagar a estrutura?', '', 40, '400 mil', 'w'),
       ('−', 'Gastos fixos', 'Quanto custa manter a empresa de pé?', 'aluguel, salário, energia, contador', 35, '350 mil', 'r'),
       ('=', 'Resultado operacional', 'O que o negócio gerou para o dono?', 'É daqui que sai o dividendo.', 5, '50 mil', 'w')]
TOP, H, GAP = 342, 138, 12
for i, (sg, nome, q, ex, pct, val, cor) in enumerate(LIN):
    y = TOP + i * (H + GAP)
    fim = i == 4
    bcor = f'background:#fff;color:{RED}' if sg != '−' else 'background:#2c2c2c;color:#fff;border:2px solid #5a5a5a'
    barra = '#ffffff' if cor == 'w' else RED
    exs = f'<div style="margin-top:4px;font-weight:500;font-size:17px;color:#bdbdbd">{ex}</div>' if ex else ''
    b += (f'<div class="card {"" if fim else "cardg"} solo" style="left:110px;top:{y}px;width:860px;height:{H}px;display:flex;align-items:center;padding:0 26px 0 22px;gap:20px">'
          f'<div style="flex:0 0 62px;height:62px;border-radius:50%;{bcor};display:flex;align-items:center;justify-content:center;font-weight:900;font-size:{24 if sg == "R$" else 34}px">{sg}</div>'
          f'<div style="flex:1;min-width:0"><span class="tag {"" if fim else "tagw"}" style="font-size:18px;padding:4px 10px 3px">{nome}</span>'
          f'<div style="margin-top:7px;font-weight:800;font-size:22px;line-height:1.22">{q}</div>{exs}</div>'
          f'<div style="flex:0 0 210px"><div style="font-weight:800;font-size:19px;text-align:right">R$ {val}</div>'
          f'<div style="margin-top:6px;height:22px;background:#2a2a2a;border-radius:4px"><div style="width:{max(pct, 3) * 2.1:.0f}px;height:22px;border-radius:4px;background:{barra}"></div></div></div></div>')
b += '<div class="cap solo" style="position:absolute;left:110px;top:1096px;width:860px;text-align:center;font-size:14px;color:#9a9a9a">Valores de uma empresa-exemplo que fatura R$ 1 milhão</div>'
salvar(b)
