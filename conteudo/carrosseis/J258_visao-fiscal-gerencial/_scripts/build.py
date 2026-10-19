"""Post 258 — visao fiscal x visao gerencial (apostila p. 18), Frame Work tela unica (layout H): A x B em linhas."""
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


def titulo(l1, l2, fs1=46, fs2=56, fs=72):
    # cabecalho na linha do post da Academy de 19/10 (instagram.com/p/Deq_zH3payF): Anton, sem bloco, 1a linha branca e 2a vermelha
    return f'<div class="tb solo" style="top:110px;font-size:{fs}px">{l1}<br><span class="v">{l2}</span></div>'


def sub(texto, top=290, fs=28):
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


b = titulo('Duas leituras da', 'mesma empresa', 48, 58)
b += sub('Uma fecha o mês com o governo. A outra <u>decide o mês com você</u>', fs=24)
LIN = [('Para quem', 'Governo', 'Dono e gestor'),
       ('Foco', 'Impostos e obrigações', 'Tomada de decisão'),
       ('Periodicidade', 'Mensal', 'Diária e semanal'),
       ('Ângulo', 'Histórico: o que<br>já aconteceu', 'Direcional: o que<br>vai acontecer'),
       ('Resultado', 'DARF, SPED,<br>balanços', 'Estratégia, preço<br>e caixa')]
TOP, H = 345, 600
for x, cls, tag, quem, ic, k in ((110, 'cardg', 'tag tagg', 'para o contador', 'receipt', 1), (550, '', 'tag', 'para o empresário', 'gauge', 2)):
    linhas = ''
    for i, l in enumerate(LIN):
        sep = 'border-top:1px solid #3a3a3a;' if i else ''
        linhas += (f'<div style="{sep}padding:12px 0 12px"><div class="cap" style="font-size:15px">{l[0]}</div>'
                   f'<div style="margin-top:5px;font-weight:{800 if k == 2 else 700};font-size:22px;line-height:1.25;color:{"#fff" if k == 2 else "#d6d6d6"}">{l[k]}</div></div>')
    bg = 'background:#5a5a5a' if k == 1 else ''
    b += (f'<div class="card {cls} solo" style="left:{x}px;top:{TOP}px;width:420px;height:{H}px;padding:24px 30px 0;text-align:center">'
          f'<div style="display:flex;align-items:center;justify-content:center;gap:14px">'
          f'<div class="badge" style="width:58px;height:58px;{bg}">{icon(ic, 32)}</div><span class="{tag}">Visão {"fiscal" if k == 1 else "gerencial"}</span></div>'
          f'<div class="cap" style="margin-top:10px;color:#fff">{quem}</div>'
          f'<div style="margin-top:8px">{linhas}</div></div>')
b += fecho('Decidir só pela contabilidade fiscal é como dirigir para a frente olhando o retrovisor.', 975)
salvar(b)
