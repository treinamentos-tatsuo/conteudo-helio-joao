#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel J399 (editorial-punch, "Toda empresa forte funciona como igreja", 16/11).
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
slide(at(1),  st(("TODA EMPRESA FORTE", A), ("FUNCIONA COMO IGREJA.", A)), top=230)
slide(at(2),  st(("Ninguém enche uma igreja no grito.", B))
            + st(("Domingo de manhã ela lota.", B), ("Porque quem vai acredita.", R)), top=280, fs=48)
slide(at(3),  st(("O fiel acorda cedo e não", B), ("ganha um centavo pra ir.", B))
            + st(("Você paga salário todo mês.", B), ("E o time nem veste a camisa.", R)), top=270, fs=48)
slide(at(4),  st(("E o pastor sabe uma coisa", B), ("que quase nenhum dono sabe:", B))
            + st(("ele repete a mesma mensagem", R), ("há dois mil anos.", R)), top=280, fs=50)
slide(at(5),  st(("Você explicou a sua cultura", B), ("uma vez, no primeiro dia.", B))
            + st(("E quer fé o ano inteiro", R), ("de quem ouviu o credo uma vez.", R)), top=280, fs=48)
slide(at(6),  st(("Aí você me pergunta:", B), ("“Hélio, isso é lavagem cerebral?”", B))
            + st(("É. EXATAMENTE ISSO.", A), mt=10), top=260, fs=48)
slide(at(7),  st(("Eu tiro da cabeça do meu time", B), ("o que não presta.", B))
            + st(("E coloco coisa boa no lugar.", R)), top=290, fs=50)
slide(at(8),  st(("Isso não é manipulação.", B))
            + st(("Manipular é controlar alguém.", R)), top=300, fs=54)
slide(at(9),  st(("Isso é influência.", B))
            + st(("E influência deixa a pessoa livre:", B), ("ela escolhe acreditar.", R)), top=290, fs=50)
slide(at(10), st(("A cultura entra na empresa", B), ("do mesmo jeito que a fé:", B))
            + st(("CREDO, RITO E ROTINA.", A), mt=10), top=260, fs=50)
slide(at(11), st(("Credo é aquilo em que você", B), ("acredita e não negocia.", B))
            + st(("Rito é treinamento, reunião", B), ("e padrão que ninguém pula.", B))
            + st(("Rotina é repetir todo dia", R), ("até o time fazer sem pensar.", R)), top=230, fs=44)
slide(at(12), st(("O pastor tem uma hora por semana", B), ("e forma gente que acredita.", B))
            + st(("Você tem oito horas por dia.", B), ("O que está fazendo com elas?", R)), top=270, fs=46)
slide(at(13), st(("Se o seu time não acredita,", B), ("o problema não é o time.", B))
            + st(("É que ninguém está pregando.", R), ("Quem não prega não forma.", R)), top=280, fs=50)
slide(at(14), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV,", B), ("onde a cultura é um dos pilares.", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">CAMISA</span></div>\n'
            + st(("que eu te mostro como fazer o seu", B), ("time acreditar na sua empresa.", B), mt=18), top=250, fs=44)
