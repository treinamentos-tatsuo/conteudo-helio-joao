#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 142 (editorial-punch, "Ta f@da empreender no Brasil").
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Anton so nos gritos)."""
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

# 1 capa: setup serif + grito Anton (capa toda em Anton reprova, 11/09)
slide(at(1),  st(("Vou dizer o que tá entalado:", B))
            + st(("TÁ F@DA EMPREENDER", A), ("NO BRASIL.", A), mt=34), top=280, fs=48)
slide(at(2),  st(("Às vésperas de uma eleição e, ao redor,", B), ("escândalos, crise, bancos, juros, medo.", R)), fs=44)
slide(at(3),  st(("Só que o boleto não quer saber.", B), ("A folha, o aluguel, o imposto: tudo vence.", R)), fs=44)
slide(at(4),  st(("A pior parte?", B), ("Você olha o caixa e não sabe o que ali é seu.", B))
            + st(("Aí, pra fechar o mês,", B), ("você põe dinheiro do seu bolso na empresa.", R)), fs=42)
slide(at(5),  st(("E não é porque você não trabalhou.", B))
            + st(("VOCÊ NÃO SABE QUANTO", A), ("GANHOU ESSE ANO.", A), mt=34), fs=46)
slide(at(6),  st(("Passa um ano. Passa dois.", B), ("A empresa continua aberta", B), ("e você continua apertado.", B))
            + st(("Você chama isso de ano difícil.", B), ("Já foram cinco anos difíceis seguidos.", R)), fs=42)
slide(at(7),  st(("Uma hora você para e vê:", B))
            + st(("AGUENTAR VIROU", A), ("O SEU PLANO.", A), mt=34), fs=46)
slide(at(8),  st(("Você não é fraco. Fraco já tinha fechado.", B), ("Você aguenta mais que a maioria,", B), ("e eu respeito isso.", B))
            + st(("Só que aguentar não paga folha,", B), ("e ano que vem a história se repete.", R)), fs=42)
slide(at(9),  st(("O Brasil vai continuar difícil.", B), ("Isso não tá na sua mão.", B))
            + st(("O que tá na sua mão é saber todos os números", B), ("da sua empresa antes do dia 5 chegar.", R)), fs=42)
slide(at(10), st(("Dono que vai bem sabe três coisas de cabeça:", B), ("quanto entra, quanto sai,", B), ("quanto sobra em cada venda.", B))
            + st(("Não é planilha bonita. É saber se a sua empresa", B), ("realmente dá lucro ou come o seu patrimônio.", R)), fs=40)
slide(at(11), st(("Você sabe que a loja tá aberta.", B), ("Não sabe se a empresa tá de pé.", R))
            + st(("Eu tenho uma aula onde você faz o raio-x da sua:", B), ("o que entra, o que sai e onde o dinheiro vaza.", R)), fs=40)
slide(at(12), st(("Aguentar você já provou que sabe.", B), ("Agora eu quero te mostrar quanto sobra.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">SOBRA</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24), fs=42)
