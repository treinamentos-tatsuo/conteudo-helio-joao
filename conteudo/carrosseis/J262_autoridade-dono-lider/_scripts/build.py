"""Post 262 — autoridade de dono x autoridade de lider (apostila p. 154), Frame Work tela unica (layout H): A x B."""
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


b = titulo('Sua autoridade é', 'de dono ou de líder?', 48, 56)
b += sub('Nem todo dono é líder. <u>As duas vêm de lugares opostos</u>')
AB = [(110, 'cardg', 'tag tagg', 'Autoridade de dono', 'Ela obriga', 'building-bank', 'down', 'vem de cima',
       ['Vem do contrato social, desde o dia em que a empresa foi aberta.', 'Não depende de mérito nem de desempenho.', 'Ninguém de dentro pode retirar.']),
      (550, '', 'tag', 'Autoridade de líder', 'Ela mobiliza', 'users', 'up', 'vem de baixo',
       ['É concedida por quem é liderado.', 'Pode ser retirada a qualquer momento, sem ninguém dizer nada.', 'Quem segue, segue por escolha. É autoridade moral.'])]
TOP, H = 345, 590
for x, cls, tag, nome, mote, ic, dirc, de, itens in AB:
    seta = (f'<svg width="40" height="70" viewBox="0 0 40 70" style="{"transform:scaleY(-1)" if dirc == "up" else ""}">'
            f'<path d="M20,4 L20,56" stroke="{RED}" stroke-width="7" fill="none"/><path d="M6,46 L20,66 L34,46 z" fill="{RED}"/></svg>')
    bg = 'background:#5a5a5a' if dirc == 'down' else ''
    li = ''.join(f'<div style="margin-top:16px;display:flex;gap:10px;font-weight:600;font-size:21px;line-height:1.32;color:#e4e4e4;text-align:left"><span style="font-weight:900;color:{RED}">›</span><span>{t}</span></div>' for t in itens)
    b += (f'<div class="card {cls} solo" style="left:{x}px;top:{TOP}px;width:420px;height:{H}px;padding:26px 30px 0;text-align:center">'
          f'<span class="{tag}">{nome}</span>'
          f'<div style="margin-top:22px;display:flex;align-items:center;justify-content:center;gap:16px">'
          f'{seta if dirc == "down" else ""}<div class="badge" style="width:96px;height:96px;{bg}">{icon(ic, 52)}</div>{seta if dirc == "up" else ""}</div>'
          f'<div class="cap" style="margin-top:12px;color:#fff">{de}</div>'
          f'<div style="margin-top:12px;font-weight:900;font-size:34px;text-transform:uppercase;letter-spacing:-.5px;color:{RED if cls == "" else "#fff"}">{mote}</div>'
          f'<div style="margin-top:4px">{li}</div></div>')
b += fecho('Líder não é quem se autointitula. É o outro que caracteriza alguém como seu líder.', 968)
salvar(b)
