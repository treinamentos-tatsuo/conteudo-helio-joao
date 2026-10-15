#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 137 (editorial-punch, "Esse alguém é você").
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

slide(at(1),  st(("Seu funcionário dorme às 22h", B), ('porque tem <span class="red">alguém decidindo</span> por ele.', B)), top=280, fs=50)
slide(at(2),  st(("ESSE ALGUÉM É VOCÊ.", A)), top=280)
slide(at(3),  st(("Não é o trabalho de empresário", B), ("que nos tira o sono.", B), ("Trabalho cansa o corpo, e o corpo dorme.", R)), fs=42)
slide(at(4),  st(("O que tira o sono é a decisão.", R), ("E decisão não se divide.", R)), fs=44)
slide(at(5),  st(("Folha de sexta com caixa de quinta.", B), ("Funcionário que tem que sair.", B), ("Conta que não sabe de onde", R), ("vai vir o dinheiro pra pagar...", R)), fs=42)
slide(at(6),  st(("Isso não dorme com ninguém da empresa.", B), ("Dorme com você.", R)), fs=44)
slide(at(7),  st(("Então você aceita:", B), ("dinheiro maior, sono menor.", B))
            + st(("Eu achei isso por anos.", R), ("Estava errado.", R)), fs=44)
slide(at(8),  st(("Não era o cargo que me tirava o sono.", B), ("Era eu.", B))
            + st(("Eu decidia no escuro.", R), ("Sem saber quanto entrava,", R), ("quanto saía, quanto sobrava...", R)), fs=42)
slide(at(9),  st(("Presta atenção nisso:", B))
            + st(("NOITE EM CLARO NÃO É", A), ("PREÇO DE DONO. É PREÇO", A), ("DE DECIDIR NO ESCURO.", A)), fs=48)
slide(at(10),  st(("Pressão é o preço. Essa você paga.", B), ("Decisão difícil é o cargo.", B))
            + st(("Mas a noite mal dormida que se repete", B), ("é falta de fundamento, não de coragem.", R)), fs=42)
slide(at(11), st(("Quem tem o número decide de dia", B), ("e dorme de noite.", B))
            + st(("Quem não tem, adia de dia", B), ("e paga de noite.", R)))
slide(at(12), st(("A decisão continua sendo sua.", B), ("Ninguém vai tomar por você.", B))
            + st(("E ela cabe em uma reunião de manhã,", B), ("com número na mesa...", R)), fs=42)
slide(at(13), st(("Ou em uma madrugada,", R), ("te assombrando a noite inteira.", R)), fs=46)
slide(at(14), st(("Eu tenho um treinamento pra donos", B), ("onde ensino a decidir com número na mão:", B))
            + st(("quanto entra, quanto sai, quanto sobra.", B), ("De dia, não de madrugada.", R), mt=26), fs=42)
slide(at(15), st(("Sono menor não é o cargo.", B), ("É falta de fundamento, de método, de clareza.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">DECISÃO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24), fs=40)
