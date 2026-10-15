#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 77 (editorial-punch, "Risco tem dono")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)

DEFAULT_ANTON = {1: 104, 4: 86, 6: 78, 9: 96}
try:
    ANTON = {**DEFAULT_ANTON, **{int(k): v for k, v in json.loads((SCR/"antonfit.json").read_text()).items()}}
except FileNotFoundError:
    ANTON = DEFAULT_ANTON
try:
    HEIGHT = {int(k): v for k, v in json.loads((SCR/"imgheight.json").read_text()).items()}
except FileNotFoundError:
    HEIGHT = {}

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
  .top{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:50px; }
  .line{ font-size:44px; line-height:1.28; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton.blk{ color:#1A1A1A; }
  .anton .red{ color:#A91C20; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""

FADE = {4: 40, 6: 38, 9: 40}
current = [0]

def img(n, fade=26):
    h = HEIGHT.get(n)
    box = f'height:{h}px;object-fit:cover;object-position:center bottom;' if h else ''
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0],96)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R, A = "", " red", " anton"
def at(n): current[0] = n; return n
def make(n, *a, **k): slide(n, *a, **k)

# 1 — CAPA: 1 linha, direcao do user
make(at(1), st(("SE A EMPRESA", A+" blk"), ('<span class="red">QUEBRAR</span> AMANHÃ,', A+" blk")), top=250)

# 2, 3 — a anafora continua, 1 linha cada
make(at(2), st(("o gerente atualiza o currículo.", B)), top=250, fs=52)
make(at(3), st(("O contador manda a última fatura.", B)), top=250, fs=52)

# 4 — GRITO que fecha a anafora
make(at(4), st(("E VOCÊ ATENDE O ADVOGADO.", A)), top=250)

# 5 — punch vermelho em serif (Anton removido a pedido do user)
make(at(5), st(("Todo mundo sai andando.", B), ("VOCÊ SAI DEVENDO.", R),
      cls_extra=' style="line-height:1.5"'), top=290, fs=50)

# 6 — o cargo: setup 2 linhas + grito
make(at(6), st(("E não adianta cobrar que sintam o mesmo.", B), ("Ninguém ali dentro tem o seu sonho.", B))
      + st(("POR ISSO O RISCO", A), ("TEM DONO.", A), cls_extra=' style="margin-top:46px"'), top=212, fs=41)

# 7 — a cena que ele nao nega
make(at(7), st(("Agora repara uma coisa.", B), ("Você nunca atrasou a folha.", B))
      + st(("Nunca atrasou fornecedor, nunca atrasou imposto.", B),
           ("Mas o seu você empurra pro mês que vem.", R)), fs=40)

# 8 — a fila
make(at(8), st(("Fornecedor, funcionário, governo...", B), ("todo mundo ganha primeiro.", B))
      + st(("Todos com uma fatia do seu resultado.", R)), fs=42)

# 9 — a verdade incomoda: grito no topo + linha serif embaixo
make(at(9), st(("ENQUANTO VOCÊ", A), ("FICA COM O RESTO.", A))
      + st(("O dono que se contenta em viver de pró-labore.", B), cls_extra=' style="margin-top:44px"'),
     top=212, fs=39)

# 10 — a distincao
make(at(10), st(("Entenda de uma vez por todas:", B), ("Pró-labore você tira por <b>trabalhar</b>.", B))
      + st(("Lucro líquido você tira por <b>arriscar</b>.", R)), fs=42)

# 11 — o que nunca chegou
make(at(11), st(("Pró-labore entra todo mês, certinho.", B), ("Lucro líquido você nunca viu na vida.", B))
      + st(("E não é que não exista.", B), ("É que você nunca foi medir.", R)), fs=41)

# 12 — como ele decide hoje
make(at(12), st(("Você olha o saldo do banco", B), ("e decide se o mês foi bom.", B))
      + st(("Mas saldo não é lucro.", B), ("É dinheiro que não é seu.", R)), fs=42)

# 13 — a virada
make(at(13), st(("Dono que sabe os números da sua empresa", B), ("para de esperar sobrar. E decide quanto tira.", B))
      + st(("Não é sorte, não é sobra.", B), ("É conta fechada todo mês.", R)), fs=40)

# 14 — CTA parte 1: o metodo
make(at(14), st(("E isso não se conserta trabalhando mais.", B),
                ("Se conserta, primeiro,", B),
                ("sabendo quanto sobra de cada venda.", B))
      + st(("É aí o lucro para de ser surpresa", B), ("e vira decisão sua.", R)), fs=40)

# 15 — CTA parte 2: o convite
cta = (st(("Eu criei o meu treinamento de gestão", B), ("pra pequena e média empresa por isso.", B))
       + st(("Não pra você vender mais.", B), ("Pra você finalmente receber.", R))
       + '      <div class="cta-big" style="margin-top:50px">Comenta <span class="red">LIQUIDO</span></div>\n')
make(at(15), cta, top=208, fs=41)
