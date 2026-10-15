#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel 141 (editorial-punch, "Crise pra culpar").
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

slide(at(1),  st(("Todo dono que quebra", B), ("tem uma crise pra culpar.", B))
            + st(('<span style="font-size:54px">Mas nenhum tem</span>', R), ('<span style="font-size:54px">uma DRE pra mostrar.</span>', R), mt=30), top=280, fs=48)
slide(at(2),  st(("Crise todo mundo enfrenta.", B), ("O concorrente da sua rua também.", B))
            + st(("Mesmo juros, mesmo cliente, mesmo Brasil.", B), ("E ele continua de porta aberta.", R)), fs=42)
slide(at(3),  st(("A diferença não é o cenário.", B), ("É o que cada um já fazia antes dele.", B))
            + st(("Ele tinha número. Você tinha achismo.", B), ("A crise só cobrou a diferença.", R)), fs=42)
slide(at(4),  st(("Você culpa o mercado.", B), ("Mas nunca soube a sua margem.", B))
            + st(("Nunca leu uma DRE como dono.", B), ("E a sua cultura é reclamar do funcionário.", R)), fs=42)
slide(at(5),  st(("Sua empresa não é frágil", B), ("por causa do Brasil.", B))
            + st(("É FRÁGIL PORQUE VOCÊ", A), ("TOCA ELA NO ACHISMO.", A), mt=30), fs=46)
slide(at(6),  st(("Não tem número. Não tem rotina.", B), ("Não tem critério.", B))
            + st(("Mas desculpa tem de sobra:", B), ("o banco, o governo,", R), ("o funcionário que não entrega...", R)), fs=42)
slide(at(7),  st(("Empresa é reflexo do dono.", B), ("Ela não vai ter critério se você não tem.", B))
            + st(("E ELA SÓ MUDA", A), ("QUANDO O DONO MUDA.", A), mt=30), fs=42)
slide(at(8),  st(("Assumir o comando não é discurso.", B), ("É margem calculada antes de vender.", B))
            + st(("É caixa controlado todo mês.", B), ("É rotina que cobra o time toda semana.", R)), fs=42)
slide(at(9),  st(("Vítima pergunta o que o mercado vai fazer.", B), ("Dono responde o que ele vai fazer.", B))
            + st(("A crise não abriu o buraco.", B), ("Só te obrigou a olhar pra ele.", R)), fs=42)
slide(at(10), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino a assumir esse comando:", B))
            + st(("dominar o lucro, o caixa", B), ("e montar a rotina que cobra resultado.", R)), fs=42)
slide(at(11), st(("Crise vai existir sempre.", B), ("Dono no comando é que é raro.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">DRE</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24), fs=42)
