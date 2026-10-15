#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel 218 (editorial-punch, "Eu me ferrei", série Erros do Hélio nº 6).
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

slide(at(1),  st(("Já fui passado pra trás", B), ("dentro da minha própria empresa.", B))
            + st(("E A CULPA FOI MINHA.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Toda vez que eu entreguei pra alguém", B), ("mais preparado do que eu", B), ("uma área que eu não entendia,", B))
            + st(("eu me ferrei.", B), ("Não foi uma vez. Foi toda vez.", R)), fs=42)
slide(at(3),  st(("O cara chegava com a planilha pronta", B), ("e a explicação na ponta da língua.", B))
            + st(("E eu balançava a cabeça.", B), ("Não porque concordava.", R), ("Porque não tinha como discordar.", R)), fs=42)
slide(at(4),  st(("Terceirizar não é o erro.", B))
            + st(("O ERRO É TERCEIRIZAR", A), ("O QUE VOCÊ NÃO ENTENDE.", A), mt=22), fs=48)
slide(at(5),  st(("O contador diz que tem que pagar, e você paga.", B), ("O financeiro diz que o caixa aguenta,", B), ("e você contrata.", B))
            + st(("As decisões grandes da sua empresa", B), ("saindo da boca de quem você não sabe cobrar.", R)), fs=40)
slide(at(6),  st(("Tudo o que eles falam vira verdade.", B), ("Não porque é verdade.", B))
            + st(("Porque você não tem base pra olhar", B), ("no olho e falar: me mostra.", R)), fs=44)
slide(at(7),  st(("E o cara nem sempre é malandro.", B), ("Muitas vezes, o bobo era eu.", R))
            + st(("Entregava a chave da empresa", B), ("sem saber abrir a porta.", R)), fs=44)
slide(at(8),  st(("Você não precisa saber fazer tudo.", B), ("Precisa saber cobrar tudo.", R))
            + st(("E só cobra,", B), ("quem entende o que está cobrando.", R)), fs=44)
slide(at(9),  st(("Hoje eu só delego uma área", B), ("depois de entender o suficiente", B))
            + st(("pra ficar em cima: perguntar,", R), ("acompanhar e questionar.", R)), fs=44)
slide(at(10), st(("Foi por isso que eu criei o MBV.", B), ("Lá eu ensino gestão de verdade:", B))
            + st(("Lucratividade, Crescimento e Cultura,", B), ("pra você entender a sua empresa", R), ("antes de delegar qualquer área dela.", R)), fs=42)
slide(at(11), st(("Contrata gente boa.", B), ("Mas nunca mais no escuro.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">BASE</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=44)
