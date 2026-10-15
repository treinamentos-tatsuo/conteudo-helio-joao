#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 123 (editorial-punch, "Ninguém acorda cedo pelo sonho do outro").
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

slide(at(1),  st(("Vou te falar uma verdade meio chata:", B)), top=280, fs=52)
slide(at(2),  st(("NINGUÉM ACORDA CEDO", A), ("PELO SONHO DO OUTRO.", A))
            + st(("Acorda pela casa própria,", B), ("pelo filho, pelo carro na porta.", B)), top=280)
slide(at(3),  st(("Sua empresa é o seu sonho.", B), ("Só você sonha com ela.", B))
            + st(("O seu funcionário tem o dele.", B), ("E ele não veio aqui realizar o seu.", R)), fs=42)
slide(at(4),  st(("ELE NÃO TRABALHA", A), ("PELO SEU SONHO.", A), ("ELE TRABALHA PELO DELE.", A)))
slide(at(5),  st(("Você abriu com o seu dinheiro e o seu risco.", B), ("Ninguém do time estava lá.", B))
            + st(("E você cobra que ele sinta", B), ("o que nunca foi dele.", R)), fs=42)
slide(at(6),  st(("Então por que ele fica com você?", B), ("Simples: a sua empresa é a ponte.", B))
            + st(("Entre a vida que ele tem", B), ("e a vida que ele quer.", R)))
slide(at(7),  st(("SUA EMPRESA", A), ("É O SEU SONHO.", A)) + st(("E A PONTE PARA", A), ("O SONHO DELE.", A)))  # respiro entre as frases (user, 16/09)
slide(at(8),  st(("Enquanto a ponte leva a algum lugar, ele fica:", B), ("Dinheiro, cargo, aprendizado, pertencimento.", B))
            + st(("Quando ela para de levar,", B), ("ele encontra outro caminho.", R)), fs=40)
slide(at(9),  st(("Líder sabe pra onde cada um quer ir", B), ("e mostra o pedaço do caminho que passa aqui.", B))
            + st(("O sonho dele tem que caber", B), ("na sua empresa.", R)), fs=40)
slide(at(10), st(("Você pode cobrar o seu sonho", B), ("e viver trocando gente.", B))
            + st(("Ou descobrir o sonho de cada um", B), ("e formar gente que fica.", R)))
slide(at(11), st(("Eu tenho um treinamento pra donos", B), ("de pequenas e médias empresas, onde ensino:", B))
            + st(("a construir a cultura que faz", B), ("o sonho do time caber na sua empresa.", R), mt=26), fs=42)
slide(at(12), '      <div class="cta-big">Comenta <span class="red">PONTE</span></div>\n'
            + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=24))
