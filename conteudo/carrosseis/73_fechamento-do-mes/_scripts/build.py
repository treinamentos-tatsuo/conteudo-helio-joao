#!/usr/bin/env python3
"""Gera os 10 HTMLs do carrossel 73 (editorial-punch, "Fechamento do mes")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# gritos Anton: 1 (capa), 5 (a pedrada), 9 (o remate do metodo)
DEFAULT_ANTON = {1: 80, 5: 104, 9: 96}
try:
    ANTON = {**DEFAULT_ANTON, **{int(k): v for k, v in json.loads((SCR / "antonfit.json").read_text()).items()}}
except FileNotFoundError:
    ANTON = DEFAULT_ANTON

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
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
</style>
</head>
<body>
"""

# altura da foto por slide (px). Sem entrada = altura natural (1080x720).
# Alturas maiores usam object-fit:cover ancorado embaixo: cortam o topo vazio da foto
# e SOBEM o assunto, matando o vao morto sem esticar a imagem.
try:
    HEIGHT = {int(k): v for k, v in json.loads((SCR / "imgheight.json").read_text()).items()}
except FileNotFoundError:
    HEIGHT = {}

def img(n, fade=26):
    h = HEIGHT.get(n)
    box = f'height:{h}px;object-fit:cover;object-position:center bottom;' if h else ''
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')

FADE = {1: 40, 5: 38, 9: 40}   # slides de grito Anton pedem faixa clara atras do texto
current = [0]

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0], 100)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R, A = "", " red", " anton"

def at(n):
    current[0] = n
    return n

def make(n, *args, **kw):
    current[0] = n
    slide(n, *args, **kw)

# 1 — CAPA: 2 linhas (setup serif + grito Anton). Sujeito baixo na foto -> texto no piso.
make(at(1), st(("O caixa começou o mês cheio.", B), ("E FECHA HOJE VAZIO. DE NOVO.", A),
               cls_extra=' style="line-height:1.5"'), top=340, fs=46)

# 2 — HOOK: a cena do dia 31
make(at(2), st(("Todo fim de mês tem a mesma cena.", B), ("O dono abre o banco antes de dormir.", B))
      + st(("O saldo está mais magro que no dia 1º.", B), ("E ele chama isso de <b>fechar o mês</b>.", R)), fs=42)

# 3 — o mes comecou cheio (sem punch: e continuidade narrativa)
make(at(3), st(("Começou diferente. No dia 5 <b>tinha dinheiro</b>.", B), ("Você olhou a conta e <b>respirou</b>.", B))
      + st(("Aí veio a folha. Veio o imposto.", B), ("E veio o boleto que ninguém lembrou.", R)), fs=41)

# 4 — a conclusao errada
make(at(4), st(("Hoje sobrou o de sempre.", B), ("O bastante pra chegar no dia 10.", B))
      + st(("E você dá o veredito do mês:", B), ("foi um mês ruim.", R)), fs=43)

# 5 — GRITO: a armadilha
make(at(5), st(("Ruim comparado com o quê?", B), ("Você não calculou nada. Você olhou e <b>sentiu</b>.", B))
      + st(("SALDO NÃO É LUCRO.", A), cls_extra=' style="margin-top:48px"'), top=212, fs=40)

# 6 — virada / mecanismo
make(at(6), st(("Fechar o mês não é olhar o saldo.", B), ("É comparar o mês inteiro com o anterior.", B))
      + st(("Sem isso você não fechou agosto.", B), ("Você só viu agosto acabar.", R)), fs=42)

# 7 — as tres perguntas (triade: estrofe de 3 linhas, excecao registrada)
make(at(7), st(("Fechar o mês é responder três perguntas:", B))
      + st(("Quanto sobrou de cada venda.", B), ("Se a empresa cresceu ou só inchou.", B), ("E se o time anda sem você empurrando.", R),
           cls_extra=' style="margin-top:44px"'), top=222, fs=41)

# 8 — consequencia
make(at(8), st(("Três perguntas. Nenhuma delas", B), ("tem resposta no extrato do banco.", B))
      + st(("Quem abre setembro sem elas", B), ("repete agosto inteiro.", R)), fs=43)

# 9 — GRITO: a ponte com o metodo
make(at(9), st(("Sou dono há mais de 38 anos.", B), ("Levei tempo pra aceitar uma coisa:", B))
      + st(("empresa não melhora por esforço.", B), ("MELHORA POR MÉTODO.", A), cls_extra=' style="margin-top:44px"'),
     top=206, fs=42)

# 10 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">LIVE</span>,</div>\n'
       '      <div class="cta-sm">que eu te mando o link da aula de hoje, 19h,<br>'
       'ao vivo e de graça: as três perguntas que<br>'
       'fecham um mês de verdade.</div>\n')
make(at(10), cta, top=210)
