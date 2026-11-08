#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel J341 (editorial-punch, "Que dia você começa a lucrar", 08/11).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text(encoding='utf-8')).items()}
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
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.36; letter-spacing:0.5px; color:#A91C20; }
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
    (OUT / f"slide-{n:02d}.html").write_text(html, encoding='utf-8'); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n
slide(at(1),  st(("O mês já está na segunda semana.", B), ("E a sua empresa ainda", B))
            + st(("NÃO GANHOU UM REAL.", A), mt=18), top=220, fs=52)
slide(at(2),  st(("Lembra da conta:", B), ("estrutura de 150 mil,", B), ("margem de 40%.", B))
            + st(("Precisa vender 375 mil", R), ("só pra empatar.", R)), top=280, fs=54)
slide(at(3),  st(("Vendendo 20 mil por dia,", B), ("sobram 8 mil", B), ("pra pagar a estrutura.", B))
            + st(("A estrutura só fica paga", R), ("no dia 19.", R)), top=280, fs=54)
slide(at(4),  st(("Do dia 1 ao dia 18,", B), ("você trabalha pro aluguel,", B), ("pra folha e pro sistema.", B))
            + st(("O lucro do mês inteiro", R), ("cabe em seis dias.", R)), top=280, fs=52)
slide(at(5),  st(("E quando o mês atrasa,", B), ("ele não come o começo.", B))
            + st(("Come o fim.", R), ("Justo os dias do lucro.", R)), top=280, fs=56)
slide(at(6),  st(("Tem dois jeitos", B), ("de o lucro chegar antes.", B))
            + st(("E nenhum deles é", R), ("vender mais.", R)), top=280, fs=56)
slide(at(7),  st(("O primeiro: cortar 15 mil", B), ("do que você paga por costume.", B))
            + st(("A linha chega no dia 17,", R), ("e o lucro vai a 65 mil.", R)), top=280, fs=52)
slide(at(8),  st(("O segundo: subir a margem", B), ("de 40% pra 45%.", B))
            + st(("Dia 17 de novo,", R), ("e o lucro vai a 75 mil.", R)), top=280, fs=54)
slide(at(9),  st(("Dois dias a menos", B), ("pagando a estrutura", B))
            + st(("são dois dias inteiros", R), ("de lucro.", R)), top=280, fs=56)
slide(at(10), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV,", B))
            + st(("onde eu ensino essa conta", B), ("com os números da sua empresa.", R)), top=300, fs=46)
slide(at(11), st(("Quer saber em que dia", B), ("a sua empresa começa a lucrar?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">LUCRAR</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), top=300, fs=48)
