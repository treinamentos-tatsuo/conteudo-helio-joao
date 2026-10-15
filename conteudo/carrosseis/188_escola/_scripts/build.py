#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel 188 (editorial-punch, "Escola", D3-S40).
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

slide(at(1),  st(("Os seus melhores crescem aí dentro", B)) + st(("OU PRECISAM SAIR", A), ("PRA CRESCER?", A), mt=22), top=280, fs=46)
slide(at(2),  st(("Todo dono já viveu essa conversa.", B), ("O melhor do time pede um minuto,", B))
            + st(("agradece por tudo", B), ("e conta que recebeu uma proposta.", R)), fs=42)
slide(at(3),  st(("E o dono se consola:", B), ("\u201cele cresceu, faz parte\u201d.", B))
            + st(("Cresceu mesmo.", B), ("Só que foi crescer na empresa dos outros.", R)), fs=42)
slide(at(4),  st(("Eu sempre faço uma pergunta nessa hora:", B), ("se ele ficasse, o que ia aprender aqui?", B))
            + st(("Quando a resposta é \u201cnada de novo\u201d,", B), ("ele não saiu por dinheiro.", R)), fs=40)
slide(at(5),  st(("Empresa fértil é aquela em que o funcionário diz:", B), ("em 1 ano aqui eu aprendi mais", B), ("que em 10 anos lá fora.", B))
            + st(("Agora pensa:", B), ("a sua é a de um ano ou a de dez?", R)), fs=38)
slide(at(6),  st(("Isso não é dinheiro.", B))
            + st(("É MUITO MAIS FORTE.", A), mt=26), fs=48)
slide(at(7),  st(("Salário o concorrente cobre", B), ("na primeira proposta.", B))
            + st(("O que ele não cobre", B), ("é o quanto a pessoa cresce perto de você.", R)), fs=40)
slide(at(8),  st(("Muito dono não treina com medo", B), ("de preparar gente pro concorrente.", B))
            + st(("Só que o bom vai embora de qualquer jeito", B), ("no dia em que para de aprender.", R)), fs=40)
slide(at(9),  st(("É por isso que eu digo:", B), ("gente boa fica onde tem escola.", B))
            + st(("Alguém que ensina, o próximo degrau à vista", B), ("e um dono que acompanha cada um subindo.", R)), fs=38)
slide(at(10), st(("No meu treinamento eu ensino gestão.", B), ("Porque é gestão que transforma", B), ("a empresa numa escola", B))
            + st(("e faz o melhor do seu time", R), ("crescer aqui dentro.", R)), fs=42)
slide(at(11), st(("Quem cresce perto de você", R), ("não precisa ir embora pra crescer.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">ESCOLA</span></div>\n'
            + st(("que eu mando o link do treinamento", B), ("no seu direct.", B), mt=18), fs=42)
