#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel 135 (editorial-punch, repost "Você já viu um pato?" / PATO). v2 (21/09): os 7 slides do original LITERAIS; só os 4 finais são novos.
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,700&family=Anton&display=swap" rel="stylesheet">
<style>
  *{ margin:0; padding:0; box-sizing:border-box; }
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; }
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .line b{ font-weight:700; }
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""
def mask(F):
    if F <= 26: return f"linear-gradient(to bottom,transparent 0%,#000 {F}%)"
    return (f"linear-gradient(to bottom,transparent 0%,rgba(0,0,0,0.06) {F*0.25:.1f}%,rgba(0,0,0,0.30) {F*0.55:.1f}%,"
            f"rgba(0,0,0,0.72) {F*0.80:.1f}%,#000 {F:.1f}%)")
def img(n):
    h = HEIGHT.get(n); pos = OBJPOS.get(n, "center bottom")
    box = f'height:{h}px;object-fit:cover;object-position:{pos};' if h else ''
    m = mask(FADE.get(n, 26))
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:{m};mask-image:{m};z-index:1;">')
cur = [0]
def slide(n, body, top=240, fs=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n

slide(at(1),  st(("VOCÊ JÁ VIU", A), ("UM PATO?", A)), top=300)
slide(at(2),  st(("Ele voa. Anda. Nada.", B), ("Mas não faz nada disso bem feito.", B))
            + st(("(E é exatamente assim", R), ("que você tem que ser.)", R)), fs=42)
slide(at(3),  st(("Empresário não é especialista.", B), ("É generalista.", B))
            + st(("Você não precisa ser o melhor em marketing,", B), ("vendas, financeiro ou gestão...", B))
            + st(("Mas precisa entender", R), ("o suficiente pra comandar.", R)), fs=40)
slide(at(4),  st(("O que quebra empresário", B), ("não é falta de talento.", B))
            + st(("É delegar o que não entende.", B), ("É confiar no achismo do outro,", B))
            + st(("porque ele mesmo", R), ("não tem clareza.", R)), fs=40)
slide(at(5),  st(("Você não vai nadar como o peixe.", B), ("Nem voar como a águia.", B))
            + st(("Mas vai saber transitar em todas as áreas", B), ("para que seu negócio funcione.", B))
            + st(("Assim como o pato...", R)), fs=40)
slide(at(6),  st(("O empresário de verdade", B), ("não foge da responsabilidade.", B))
            + st(("Ele aprende o básico, entende o processo,", B), ("lidera o time.", B))
            + st(("E só depois... delega.", R)), fs=40)
slide(at(7),  st(("Você não precisa ser o melhor em tudo.", B), ("Mas precisa saber o que está fazendo.", B))
            + st(("Porque quem não entende o jogo...", B), ("Joga de qualquer jeito.", R)), fs=42)
slide(at(8),  st(("O jogo começa dentro da sua empresa:", B), ("quanto entra, quanto sai, quanto sobra.", B))
            + st(("Se você não sabe isso de cabeça,", B), ("está delegando o que não entende.", R)), fs=42)
slide(at(9),  st(("Transitar em todas as áreas, na prática,", B), ("é dominar o básico de negócios:", B))
            + st(("LUCRO. CAIXA. GENTE.", A))
            + st(("A fórmula básica para crescer sem quebrar.", R)), fs=40)
slide(at(10), st(("Eu tenho uma aula em que você faz", B), ("o raio-x da sua própria empresa.", B))
            + st(("Sai de lá entendendo o suficiente", B), ("pra comandar. Como o pato.", R)), fs=42)
slide(at(11), st(("O especialista cuida da área dele.", B), ("Entender o jogo inteiro é papel do dono.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PATO</span></div>\n'
            + st(("que eu te mando a aula do raio-x no seu direct.", R), mt=24), fs=42)
