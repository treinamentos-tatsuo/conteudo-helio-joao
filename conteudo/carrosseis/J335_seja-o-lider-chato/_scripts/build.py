#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel J335 (editorial-punch, "Seja o líder chato", 07/11).
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
slide(at(1),  st(("O seu time acha você", B), ("um líder legal.", B))
            + st(("QUEM PAGA ISSO", A), ("É O SEU CLIENTE.", A), mt=18), top=220, fs=52)
slide(at(2),  st(("O cliente espera a resposta", B), ("até depois do almoço.", B))
            + st(("E ninguém fala nada,", R), ("porque o chefe é gente boa.", R)), top=280, fs=56)
slide(at(3),  st(("Por isso eu te falo:", B), ("seja o líder chato.", B))
            + st(("Chato com o padrão,", R), ("não com a pessoa.", R)), top=280, fs=56)
slide(at(4),  st(("Exija padrão.", B), ("O combinado é responder", B), ("em cinco minutos?", B))
            + st(("Então cinco minutos", R), ("não é sugestão.", R)), top=280, fs=50)
slide(at(5),  st(("Exija postura.", B), ("O cliente olha o vendedor", B), ("antes de olhar o produto.", B))
            + st(("Cara fechada também vende.", R), ("Pro concorrente.", R)), fs=54)
slide(at(6),  st(("Exija organização.", B))
            + st(("Pedido perdido é cliente", R), ("jogado fora na bagunça.", R)), top=280, fs=58)
slide(at(7),  st(("Exija comprometimento.", B), ("Prazo que o time te deu é prazo.", B))
            + st(("Não é estimativa.", R)), top=280, fs=52)
slide(at(8),  st(("Exija atenção ao cliente.", B), ("Ninguém volta só pelo preço.", B))
            + st(("Volta porque alguém", R), ("lembrou dele.", R)), top=280, fs=56)
slide(at(9),  st(("E repara numa coisa:", B), ("o seu time tem a sua cara.", B))
            + st(("Se ele está frouxo,", R), ("é porque alguém deixou.", R)), top=280, fs=56)
slide(at(10), st(("Ninguém bom quer trabalhar", B), ("com líder frouxo.", B))
            + st(("Ser chato é o que segura", R), ("os bons na sua empresa.", R)), top=280, fs=56)
slide(at(11), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV,", B))
            + st(("onde eu ensino gestão de pessoas,", B), ("cultura e liderança.", R)), top=300, fs=48)
slide(at(12), st(("Quer um time que segura o padrão", B), ("mesmo quando você não está?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PADRÃO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), top=300, fs=46)
