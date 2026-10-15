#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 205 (editorial-punch, "Sem direção").
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

slide(at(1),  st(("Você não está sem esperança.", B))
            + st(("ESTÁ SEM DIREÇÃO.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Quando você não sabe", B), ("pra onde está indo,", B))
            + st(("qualquer problema parece uma bomba", B), ("prestes a explodir na sua vida.", R)), fs=44)
slide(at(3),  st(("O cliente grande que cancelou.", B), ("O banco que cortou o limite.", B))
            + st(("O gerente que pediu as contas.", B), ("A decisão que você adia há meses.", R)), fs=44)
slide(at(4),  st(("Sem direção,", B))
            + st(("TUDO PARECE", A), ("URGENTE.", A), mt=22), fs=46)
slide(at(5),  st(("Você não sabe o que proteger", B), ("nem o que priorizar.", B))
            + st(("Então resolve o que aparece na frente.", B), ("E o que aparece na frente é o incêndio.", R)), fs=42)
slide(at(6),  st(("Doze horas apagando incêndio.", B), ("Chega em casa moído.", B))
            + st(("Mas se alguém pergunta", B), ("o que você está construindo,", B))
            + st(("VOCÊ NÃO SABE", A), ("RESPONDER.", A), mt=22), fs=42)
slide(at(7),  st(("Eu tenho 38 anos de empresa", B), ("e já vi muito dono bom jogar a toalha.", B))
            + st(("Quase nunca por falta de cliente.", B), ("Por cansaço de lutar sem saber pra quê.", R)), fs=42)
slide(at(8),  st(("Por isso você precisa, desesperadamente,", B), ("de uma visão de futuro.", B))
            + st(("Não pra prever o que vai acontecer.", B), ("Pra decidir aonde você quer chegar.", R)), fs=42)
slide(at(9),  st(("Que empresa você quer daqui a dez anos.", B), ("E quanto ela coloca no seu bolso.", B))
            + st(("Que vida você quer dar pra sua família.", B), ("O que precisa mudar pra chegar lá.", R)), fs=42)
slide(at(10), st(("Quando essas respostas ficam claras,", B), ("os problemas não desaparecem.", B))
            + st(("Mas nenhum imprevisto tem mais o poder", B), ("de decidir o seu futuro.", R)), fs=42)
slide(at(11), st(("Você olha o problema,", B), ("lembra aonde quer chegar", B))
            + st(("E ESCOLHE", A), ("O PRÓXIMO PASSO.", A), mt=22), fs=46)
slide(at(12), st(("Depois mais um. E mais um.", B), ("É nesse movimento que a esperança volta.", B))
            + st(("Os problemas continuam lá.", B), ("Só que agora você sabe pra onde vai.", R)), fs=42)
slide(at(13), st(("Começa com uma folha de papel:", B), ("onde a sua empresa tem que estar", B), ("em dez anos.", B))
            + st(("Toda segunda, antes do primeiro incêndio,", B), ("pergunta: o que dessa semana", R), ("me leva até lá?", R)), fs=42)
slide(at(14), st(("No MBV, o meu treinamento,", B), ("eu ensino gestão pra dono de PME:", B))
            + st(("Lucratividade, Crescimento e Cultura", B), ("pra empresa crescer na direção", R), ("que você escolheu.", R)), fs=42)
slide(at(15), st(("Problema sempre vai ter.", B), ("Só não deixa ele escolher o seu caminho.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">RUMO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=42)
