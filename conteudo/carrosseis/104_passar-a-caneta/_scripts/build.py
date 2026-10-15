#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 104 (editorial-punch, "Passar a caneta").
Layout da skill (calibragem registrada em erros-frequentes 04/09: corpo top 200, capa 240; Source Serif 44; Anton nos gritos)."""
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
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .src{ font-size:24px; font-weight:400; line-height:1.3; color:#1A1A1A; opacity:0.55; margin-top:18px; }
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
def slide(n, body, top=200, fs=None):
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
def src(txt): return f'      <div class="src">{txt}</div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n

slide(at(1),  st(("Dar o cargo pro filho é fácil.", B), ("DIFÍCIL É PASSAR A CANETA.", A)), top=240, fs=52)
slide(at(2),  st(("Você já contou pra todo mundo:", B), ("meu filho assumiu.", B)) + st(("Mas o pedido grande, o preço, a demissão,", B), ("tudo ainda passa pela sua mesa.", R)))
slide(at(3),  st(("E quando ele decide sem você", B), ("e você acha que vai dar errado,", B)) + st(("você desmancha.", B), ("Na frente da equipe.", R)))
slide(at(4),  st(("A equipe aprende em uma semana.", B), ("Pra que ouvir o filho, se o pai desfaz?", B)) + st(("Tudo volta pra sua mesa.", B), ("E você reclama que ele não assume.", R)))
slide(at(5),  st(("Você diz que ele não está pronto.", B), ("Ele diz que você não larga.", B)) + st(("Eu vou te falar uma coisa que dói:", B), ("os dois estão certos.", R)))
slide(at(6),  st(("Ele não está pronto porque nunca pôde errar.", B), ("Você não larga porque a regra é você.", B)) + st(("Está tudo na sua cabeça.", B), ("Não tem o que passar.", R)), fs=42)
slide(at(7),  st(("CANETA SÓ SAI DA MÃO", A), ("QUANDO A REGRA", A), ("ESTÁ NO PAPEL.", A)))
slide(at(8),  st(("De cada dez empresas familiares,", B), ("até nove não têm plano de sucessão nenhum.", B)) + st(("Não é falta de amor.", B), ("Amor não é método.", R)) + src("Fonte: PwC"), fs=42)
slide(at(9),  st(("Trinta anos de calo não cabem numa conversa.", B)) + st(("Calo o seu filho faz sozinho.", B), ("Se você deixar ele segurar a ferramenta.", R)), fs=42)
slide(at(10), st(("Largar a caneta é escrever a regra antes.", B), ("Até onde ele decide, o que sobe pra você.", B)) + st(("E a decisão dele vale.", B), ("Mesmo quando erra.", R)), fs=42)
slide(at(11), st(("Empresa que só anda com a sua assinatura", B), ("não é herança. É dependência.", B)) + st(("O que passa de pai pra filho", B), ("não é a cadeira. É o método.", R)))
slide(at(12), st(("Eu tenho um treinamento pra donos", B), ("de pequenas e médias empresas, onde ensino:", B)) + st(("tirar a empresa da sua cabeça,", B), ("colocar regra, número e ritual no papel", B), ("e passar a caneta sem perder o comando.", R), mt=26), fs=40)
slide(at(13), '      <div class="cta-big">Comenta <span class="red">SUCESSÃO</span></div>\n'
            + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=24))
