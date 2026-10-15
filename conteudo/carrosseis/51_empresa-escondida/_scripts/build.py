#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 51 (editorial-punch, D1-S58 empresa escondida)."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# tamanhos da Anton medidos pelo fit.js (roda depois do 1o build)
try:
    ANTON = {int(k): v for k, v in json.loads((SCR / "antonfit.json").read_text()).items()}
except FileNotFoundError:
    ANTON = {}

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
  .stanza + .stanza{ margin-top:52px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .capa{ font-size:48px; line-height:1.28; font-weight:700; }
  .capa-punch{ font-size:58px; line-height:1.24; font-weight:700; color:#A91C20; }
  .sussurro{ font-size:30px; font-weight:400; color:#1A1A1A; }
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
</style>
</head>
<body>
"""

def img(n, fade=26):
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')

def slide(n, body, fade=26, top=236, fs=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = ""
        if "anton" in cls:
            style = f' style="font-size:{ANTON.get(current[0], 84)}px"'
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R = "", " red"
current = [0]

def make(n, *args, **kw):
    current[0] = n
    slide(n, *args, **kw)

# 1 — capa (impacto + punch vermelho + sussurro)
make(1,
     st(("Tem uma empresa mais rica que a sua", " capa"))
     + st(("escondida aí dentro.", " capa-punch"), cls_extra=' style="margin-top:26px"')
     + '      <div class="stanza" style="margin-top:30px"><div class="line sussurro">e você nunca olhou pra ela.</div></div>\n',
     top=210)

# 2 — a dor
make(2, st(("Você fez tudo pra ela crescer.", B), ("Mais cliente, mais entrega, mais estrutura.", B))
      + st(("E a sobra do fim do mês", B), ("continua a mesma de anos atrás.", R)), fs=41)

# 3 — grito-convite (herói: setup + 2 linhas Anton)
make(3, st(("Não é falta de esforço. E eu te provo", B), ("com uma folha e um lápis.", B))
      + st(("DESENHA A TUA EMPRESA", " anton"), ("DO ZERO. NO PAPEL.", " anton")), top=200)

# 4 — a regra
make(4, st(("Nessa empresa nova, só entra", B), ("o que deixa lucro.", B))
      + st(("Nada entra por história,", R), ("por costume ou por tamanho.", R)))

# 5 — os clientes
make(5, st(("Começa pela carteira:", B), ("entra quem deixa margem de verdade.", B))
      + st(("O cliente que dá trabalho", B), ("e não deixa lucro? Fica de fora.", R)))

# 6 — os custos (âncora sozinha)
make(6, st(("Agora os custos, um por um:", B), ("entra o que sustenta o lucro.", B))
      + st(("O resto fica de fora.", R)))

# 7 — o que sobra
make(7, st(("No fim, olha o desenho:", B), ("a empresa do papel é menor.", B))
      + st(("Bem menor que a sua.", B), ("E agora vem a parte que dói.", R)))

# 8 — o reveal (estrofe inteira vermelha)
make(8, st(("Faz a conta dessa empresa menor.", B), ("Margem limpa, custo enxuto.", B))
      + st(("Ela ganha mais dinheiro", R), ("do que a sua inteira.", R)))

# 9 — a prova
make(9, st(("Isso não é teoria de quadro branco.", B), ("Já fiz essa conta com empresa de verdade.", B))
      + st(("Encolheu o faturamento", B), ("e multiplicou o lucro por cinco.", R)), fs=41, top=200)

# 10 — a tese (estrofe inteira vermelha)
make(10, st(("A empresa lucrativa não precisa", B), ("ser construída. Ela já existe.", B))
       + st(("Escondida dentro da empresa", R), ("que você insiste em carregar.", R)))

# 11 — o mecanismo
make(11, st(("E você nunca viu porque te ensinaram", B), ("que sucesso é crescer sempre.", B))
       + st(("Cada camada nova de tamanho", B), ("enterrou a empresa boa mais fundo.", R)), fs=42)

# 12 — doutrina
make(12, st(("Ninguém está mandando você encolher.", B), ("A ordem é que está errada.", B))
       + st(("Primeiro a empresa aprende a lucrar.", B), ("Depois cresce em cima do lucro.", R)), fs=42)

# 13 — o desejo
make(13, st(("Pensa nela funcionando:", B), ("menos cliente, mais margem.", B))
       + st(("Sobra dinheiro no fim do mês.", B), ("E sobra dono pra família.", R)))

# 14 — fechamento
make(14, st(("Tirar essa empresa do papel tem método:", B), ("<span class=\"red\">margem por cliente, custo na régua.</span>", B))
       + st(("É o que eu ensino no meu treinamento", B), ("de gestão pra pequena e média empresa.", B)), fs=41)

# 15 — CTA (exclusivo)
cta = ('      <div class="cta-big">Comenta <span class="red">ESCONDIDA</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como tirar do papel<br>'
       'a empresa lucrativa que existe dentro da sua.</div>\n')
make(15, cta)
