"""Post 243 — os melhores vendedores (apostila pp. 99, 117, 120-125), 8 slides no layout G (padrao do 224/229: fundo escuro,
Montserrat, vermelho so #A91C20, titulo da capa em bloco branco, sem paginacao). Cada slide tem um recurso visual que guia
o olhar e um cartao "DE ONDE VEM" com a peca do ambiente que forma a caracteristica. Texto = o aprovado (v1)."""
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
.sub{{position:absolute;left:100px;width:880px;text-align:center;font-weight:600;font-size:26px}}
.P{{position:absolute;left:130px;width:820px;text-align:center;font-weight:500;font-size:27px;line-height:1.45;color:#e8e8e8;text-wrap:balance}}
.P b{{color:#fff;font-weight:800}}
.badge{{border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 9px #0d0d0d}}
.tag{{display:inline-block;background:{RED};color:#fff;border-radius:6px;padding:6px 14px 5px;font-weight:800;font-size:22px;text-transform:uppercase;letter-spacing:.02em;white-space:nowrap}}
.tagw{{background:#fff;color:#0d0d0d}}
.cap{{font-weight:700;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#bdbdbd}}
.dest{{position:absolute;left:50%;transform:translateX(-50%);white-space:nowrap;background:#fff;color:{RED};font-weight:800;font-size:34px;
  padding:18px 34px;border-radius:6px;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)}}
.card{{position:absolute;border-radius:14px;background:linear-gradient(160deg,#1f1f1f,#141414);border:2px solid {RED}}}
.hl{{color:#fff;background:{RED};padding:0 8px;border-radius:4px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.arr{{position:absolute;right:110px;top:1200px;font-weight:700;font-size:20px;letter-spacing:.2em;color:#9a9a9a}}
"""

TOTAL = 8


def w(n, body):
    foot = '<div class="arr">ARRASTE &rarr;</div>' if n < TOTAL else ''
    html = (f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="s"><div class="conteudo">{body}{foot}</div></div></body></html>')
    (POST / 'instagram' / f'slide-{n:02d}.html').write_text(html, encoding='utf-8', newline='\n')


def svg(inner, h=1350):
    return f'<svg width="1080" height="{h}" viewBox="0 0 1080 {h}" style="position:absolute;inset:0;overflow:visible">{inner}</svg>'


ARROW_DEFS = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
              f'<path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>'
              f'<marker id="ag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
              f'<path d="M0,0 L10,5 L0,10 z" fill="#8a8a8a"/></marker>'
              f'<marker id="aw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
              f'<path d="M0,0 L10,5 L0,10 z" fill="#ffffff"/></marker></defs>')


def titulo(l1, l2, top=120):
    return f'<div class="T solo" style="top:{top}px">{l1}<br><span class="v">{l2}</span></div>'


def de_onde_vem(texto, top=955):
    return (f'<div class="card solo" style="left:130px;top:{top}px;width:820px;padding:22px 34px 24px;text-align:center">'
            f'<span class="tag">De onde vem</span>'
            f'<div style="margin-top:14px;font-weight:600;font-size:25px;line-height:1.42;color:#e8e8e8;text-wrap:balance">{texto}</div></div>')


# ---------------- 1 CAPA: as cinco coisas em volta do time ----------------
b = ('<div class="tb solo" style="top:112px;font-size:46px;white-space:nowrap">Os melhores vendedores têm<br>'
     '<span class="v" style="font-size:58px">cinco coisas em comum</span></div>')
CX, CY, R = 540, 630, 235
CAP5 = [('flag-3', 'Crença'), ('gauge', 'Número'), ('list-check', 'Padrão'), ('calendar-event', 'Ritmo'), ('coin', 'Incentivo')]
g = ''
pos = []
for i in range(5):
    a = math.radians(-90 + 72 * i)
    x, y = CX + R * math.cos(a), CY + R * math.sin(a)
    pos.append((x, y))
    g += f'<line x1="{CX}" y1="{CY}" x2="{x:.0f}" y2="{y:.0f}" stroke="#3a3a3a" stroke-width="3" stroke-dasharray="8 8"/>'
b += svg(g)
b += f'<div class="badge solo" style="position:absolute;left:{CX-80}px;top:{CY-80}px;width:160px;height:160px;background:#fff">{icon("users", 84, RED)}</div>'
for (x, y), (ic, nm) in zip(pos, CAP5):
    b += (f'<div class="solo" style="position:absolute;left:{x-100:.0f}px;top:{y-58:.0f}px;width:200px;display:flex;flex-direction:column;align-items:center">'
          f'<div class="badge" style="width:116px;height:116px">{icon(ic, 60)}</div>'
          f'<div style="margin-top:14px"><span class="tag tagw" style="font-size:20px">{nm}</span></div></div>')
b += '<div class="sub solo" style="top:985px;font-size:32px;font-weight:700">E nenhuma delas vem no currículo.</div>'
b += '<div class="dest solo" style="top:1055px">Entenda de onde elas vêm &rarr;</div>'
w(1, b)

# ---------------- 2 CRENCA: no que vende + no sonho ----------------
b = titulo('Acreditam no que vendem', 'e no próprio sonho').replace('top:120px', 'top:120px;font-size:50px')
b += ('<div class="P solo" style="top:285px">Acreditam que o produto muda a vida de quem compra e que trabalhar ali muda a vida deles. '
      '<b>Sem a primeira crença, o vendedor vende preço. Sem a segunda, vai embora no primeiro real a mais.</b></div>')
VY = 650
for x, ic, nm, falta in ((300, 'building-store', 'No que vende', 'sem ela, vende preço'), (780, 'flag-3', 'No próprio sonho', 'sem ela, vai embora')):
    b += (f'<div class="solo" style="position:absolute;left:{x-170}px;top:{VY-85}px;width:340px;display:flex;flex-direction:column;align-items:center">'
          f'<div class="badge" style="width:170px;height:170px">{icon(ic, 90)}</div>'
          f'<div style="margin-top:22px"><span class="tag tagw" style="font-size:24px">{nm}</span></div>'
          f'<div class="cap" style="margin-top:14px;font-size:18px">{falta}</div></div>')
b += f'<div class="solo" style="position:absolute;left:500px;top:{VY-60}px;width:80px;text-align:center;font-weight:900;font-size:90px;line-height:1;color:{RED}">+</div>'
b += de_onde_vem('<span class="hl">Informação e prova.</span> Conhecer o cliente satisfeito e ver quanto dá para ganhar performando.')
w(2, b)

# ---------------- 3 NUMERO: a parede ----------------
b = titulo('Sabem o próprio número', 'sem perguntar')
b += ('<div class="P solo" style="top:285px">Olham para o lado e sabem quanto falta para a meta, sem planilha e sem perguntar a ninguém. '
      '<b>Quem está na frente quer continuar na frente, e quem está atrás quer sair de lá.</b></div>')
rank = [(560, True), (470, False), (390, False), (300, False)]
rows = ''
for i, (wd, top1) in enumerate(rank):
    cor = f'background:{RED};border:2px solid {RED}' if top1 else 'background:#2c2c2c;border:2px solid #5a5a5a'
    ico = f'<div style="margin-left:12px">{icon("trophy", 34, RED)}</div>' if top1 else ''
    rows += (f'<div style="display:flex;align-items:center;margin-top:12px"><div style="width:56px;font-weight:900;font-size:24px;color:{"#fff" if top1 else "#bdbdbd"}">{i+1}º</div>'
             f'<div style="width:{wd}px;height:32px;border-radius:5px;{cor}"></div>{ico}</div>')
b += (f'<div class="card solo" style="left:150px;top:478px;width:780px;padding:26px 40px 30px;border-color:#5a5a5a">'
      f'<div class="cap" style="color:#fff">Meta do mês</div>'
      f'<div style="margin-top:12px;position:relative;height:46px;border-radius:6px;border:2px solid #fff;overflow:hidden">'
      f'<div style="position:absolute;left:0;top:0;bottom:0;width:70%;background:{RED};display:flex;align-items:center;padding-left:16px;font-weight:800;font-size:20px;letter-spacing:.08em">REALIZADO</div>'
      f'<div style="position:absolute;right:16px;top:0;bottom:0;display:flex;align-items:center;font-weight:800;font-size:20px;letter-spacing:.08em">FALTA</div></div>'
      f'<div class="cap" style="color:#fff;margin-top:26px">Ranking</div>{rows}</div>')
b += de_onde_vem('<span class="hl">A parede.</span> Meta do mês, realizado atualizado à mão e ranking dos vendedores, à vista de todo mundo.')
w(3, b)

# ---------------- 4 PADRAO: jeito do fulano x padrao da empresa ----------------
b = titulo('Vendem do jeito', 'da empresa')
b += ('<div class="P solo" style="top:285px">O vendedor que aprende “indo junto com o fulano” aprende o jeito do fulano, com os acertos e com os vícios dele. '
      '<b>O bom vendedor segue o padrão que a empresa escreveu.</b></div>')
CT, CH = 490, 410
b += (f'<div class="card solo" style="left:130px;top:{CT}px;width:390px;height:{CH}px;border-color:#5a5a5a;text-align:center;padding-top:24px">'
      f'<span class="tag" style="background:#2c2c2c;border:2px solid #5a5a5a">O jeito do fulano</span></div>')
b += (f'<div class="card solo" style="left:560px;top:{CT}px;width:390px;height:{CH}px;text-align:center;padding-top:24px">'
      f'<span class="tag">O padrão da empresa</span></div>')
g = ARROW_DEFS
ox, oy = 200, 740
for ex, ey, cx, cy in ((440, 590, 300, 600), (470, 700, 360, 760), (430, 850, 260, 860), (330, 600, 230, 640), (470, 790, 380, 700)):
    g += f'<path d="M{ox},{oy} Q{cx},{cy} {ex},{ey}" fill="none" stroke="#8a8a8a" stroke-width="5" stroke-linecap="round" marker-end="url(#ag)"/>'
g += f'<circle cx="{ox}" cy="{oy}" r="12" fill="#8a8a8a"/>'
for y in (610, 670, 730, 790, 850):
    g += f'<line x1="600" y1="{y}" x2="790" y2="{y}" stroke="{RED}" stroke-width="6" stroke-linecap="round" marker-end="url(#ah)"/>'
b += svg(g)
b += f'<div style="position:absolute;left:820px;top:690px;width:90px;height:90px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center">{icon("target-arrow", 56, RED)}</div>'
b += de_onde_vem('<span class="hl">Treinamento todo dia,</span> no produto, na técnica e no playbook da empresa. O time evolui para onde é treinado.')
w(4, b)

# ---------------- 5 RITMO: o rito diario ----------------
b = titulo('Têm ritmo', 'todo dia')
b += ('<div class="P solo" style="top:285px">Começam o dia sabendo o que fizeram ontem, o que está travando e o que vão fazer hoje. '
      '<b>Sem esse momento fixo, a empresa só percebe o problema depois do resultado ruim.</b></div>')
BX, BY = 255, 700
clock = (f'<svg width="96" height="96" viewBox="0 0 96 96"><circle cx="48" cy="48" r="38" fill="none" stroke="#fff" stroke-width="6"/>'
         f'<line x1="48" y1="48" x2="48" y2="24" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
         f'<line x1="48" y1="48" x2="66" y2="48" stroke="#fff" stroke-width="6" stroke-linecap="round"/></svg>')
b += (f'<div class="solo" style="position:absolute;left:{BX-110}px;top:{BY-90}px;width:220px;display:flex;flex-direction:column;align-items:center">'
      f'<div class="badge" style="width:180px;height:180px">{clock}</div>'
      f'<div style="margin-top:20px;font-weight:900;font-size:34px">15 MIN</div>'
      f'<div class="cap" style="margin-top:4px;font-size:18px;white-space:nowrap">em pé, mesma hora</div></div>')
g = ARROW_DEFS
TY = [590, 690, 790]
for ty in TY:
    g += f'<path d="M{BX+100},{BY} C{BX+170},{BY} {BX+140},{ty} {455},{ty}" fill="none" stroke="{RED}" stroke-width="6" marker-end="url(#ah)"/>'
b += svg(g)
for ty, t in zip(TY, ('O que foi feito ontem', 'O que está travando', 'O que será feito hoje')):
    b += f'<div class="solo" style="position:absolute;left:470px;top:{ty-25}px"><span class="tag tagw" style="font-size:25px;padding:9px 18px 8px">{t}</span></div>'
b += de_onde_vem('<span class="hl">O rito diário.</span> Quinze minutos, em pé, sempre na mesma hora, com problema ou sem problema.')
w(5, b)

# ---------------- 6 INCENTIVO: meta 1, 2, 3 ----------------
b = titulo('Correm porque', 'correr compensa')
b += ('<div class="P solo" style="top:285px">Sabem quanto ganham na meta 1, na meta 2 e na meta 3, e fazem essa conta de cabeça. '
      '<b>Quando quem corre e quem anda ganham parecido no fim do mês, o time aprende a andar.</b></div>')
BASE = 895
for i, (x, h) in enumerate(((190, 150), (440, 250), (690, 350))):
    last = i == 2
    estilo = f'background:{RED};border:2px solid {RED}' if last else 'background:#2c2c2c;border:2px solid #5a5a5a'
    moedas = ''.join(icon('coin', 44) for _ in range(i + 1))
    b += (f'<div class="solo" style="position:absolute;left:{x}px;top:{BASE-h}px;width:200px;height:{h}px;border-radius:8px 8px 0 0;{estilo};'
          f'display:flex;flex-direction:column;align-items:center;padding-top:22px">'
          f'<div style="font-weight:900;font-size:30px">META {i+1}</div><div style="margin-top:14px;display:flex;gap:4px">{moedas}</div></div>')
b += svg(f'<line x1="150" y1="{BASE}" x2="930" y2="{BASE}" stroke="#6a6a6a" stroke-width="2"/>')
b += de_onde_vem('<span class="hl">Incentivo claro,</span> que não muda toda hora, e venda comemorada na hora, na frente de todo mundo.')
w(6, b)

# ---------------- 7 VIRADA: o ambiente molda ----------------
b = titulo('O ambiente', 'molda o vendedor', top=200)
b += ('<div class="P solo" style="top:365px;font-size:29px">Nenhuma dessas cinco coisas vem pronta. '
      '<b>Todas vêm do ambiente que a empresa oferece.</b></div>')
down = icon('trending-up', 70).replace('<svg', '<svg style="transform:scaleY(-1)"', 1)
b += ('<div class="solo" style="position:absolute;left:110px;top:520px;width:860px;display:flex;gap:28px">'
      f'<div class="card" style="position:relative;flex:1;padding:30px 24px 32px;text-align:center;border-color:#5a5a5a">{icon("trending-up", 70)}'
      f'<div style="margin-top:10px;font-weight:900;font-size:40px">MEDIANO</div><div style="font-weight:800;font-size:22px;letter-spacing:.04em">EM AMBIENTE FORTE</div>'
      f'<div style="margin-top:18px;font-weight:500;font-size:23px;line-height:1.4;color:#dcdcdc;text-wrap:balance">performa, porque o ambiente não deixa acomodar</div></div>'
      f'<div class="card" style="position:relative;flex:1;padding:30px 24px 32px;text-align:center;background:{RED};border-color:{RED}">{down}'
      f'<div style="margin-top:10px;font-weight:900;font-size:40px">BOM</div><div style="font-weight:800;font-size:22px;letter-spacing:.04em">EM AMBIENTE MORTO</div>'
      f'<div style="margin-top:18px;font-weight:500;font-size:23px;line-height:1.4;color:#fff;text-wrap:balance">se acomoda e entra no ritmo dos outros</div></div></div>')
b += '<div class="dest solo" style="top:950px;font-size:31px;line-height:1.35;text-align:center">Talvez o problema não sejam os vendedores.<br>Talvez seja o ambiente.</div>'
w(7, b)

# ---------------- 8 CTA ----------------
b = '<div class="T solo" style="top:150px;font-size:60px">A sua empresa forma<br><span class="v">bons vendedores?</span></div>'
pil = [('coin', 'Lucratividade'), ('trending-up', 'Crescimento'), ('hierarchy-2', 'Cultura')]
b += '<div class="solo" style="position:absolute;left:130px;top:380px;width:820px;display:flex;justify-content:space-between">'
for ic, nm in pil:
    b += (f'<div style="width:240px;display:flex;flex-direction:column;align-items:center">'
          f'<div class="badge" style="width:120px;height:120px">{icon(ic, 62)}</div>'
          f'<div style="margin-top:20px"><span class="tag">{nm}</span></div></div>')
b += '</div>'
b += ('<div class="P solo" style="top:650px;font-size:29px">No <b>MBV</b>, treinamento de três dias para donos de pequenas e médias empresas, '
      'você aprende a construir o ambiente que faz o time vender, dentro da gestão dos três pilares: Lucratividade, Crescimento e Cultura.</div>')
b += ('<div class="solo" style="position:absolute;left:50%;transform:translateX(-50%);top:950px;white-space:nowrap;background:#fff;color:' + RED + ';'
      'font-weight:800;font-size:38px;letter-spacing:-.5px;padding:24px 44px;border-radius:6px;box-shadow:0 0 0 6px rgba(169,28,32,.55),0 12px 30px rgba(0,0,0,.5)">QUERO PARTICIPAR DO MBV</div>')
b += '<div class="solo" style="position:absolute;left:0;right:0;top:1085px;text-align:center;font-weight:800;font-size:26px;letter-spacing:.2em">LINK NA BIO &rarr;</div>'
w(8, b)
print('ok')
