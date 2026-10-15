#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 52 (editorial-punch, D1-S61 ladrao silencioso)."""
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

# 1 — capa (o crime anunciado: grito Anton puro + sussurro)
make(1,
     st(("VOCÊ ESTÁ SENDO", " anton"), ("ROUBADO.", " anton"))
     + '      <div class="stanza" style="margin-top:34px"><div class="line sussurro">por alguém de dentro da sua casa.</div></div>\n',
     top=230)

# 2 — a cena
make(2, st(("Você vende o mês inteiro.", B), ("Dia trinta: <b>cadê o dinheiro?</b>", B))
      + st(("Na conta da empresa, pouco.", B), ("No seu bolso, nada.", R)))

# 3 — a promessa adiada
make(3, st(("Todo mês você promete:", B), ("<b>esse mês eu faço uma retirada.</b>", B))
      + st(("E todo mês o dinheiro some", B), ("antes de chegar em você.", R)))

# 4 — conclusão errada (herói: setup + 2 linhas Anton)
make(4, st(("Até você chegar na conclusão amarga:", B))
      + st(("ESSE NEGÓCIO", " anton"), ("NÃO DÁ DINHEIRO.", " anton"), cls_extra=' style="margin-top:44px"'),
     top=220, fs=42)

# 5 — a ponte (desmente e reconecta no roubo)
make(5, st(("A conclusão está errada.", B), ("O dinheiro existe e entra todo dia.", B))
      + st(("Ele só não fica.", B), ("Tem alguém levando antes de você.", R)), fs=42)

# 6 — como ele entra
make(6, st(("Esse ladrão não arromba a porta.", B), ("<b>Ele entra com a chave que você deu.</b>", B))
      + st(("Leva um pouco todo dia.", B), ("E não deixa rastro nenhum.", R)), fs=42)

# 7 — o nome dele
make(7, st(("O nome dele é <b>conta misturada</b>:", B), ("a da casa dentro da empresa.", B))
      + st(("Despesa saindo sem nome,", B), ("sem data e sem limite.", R)))

# 8 — o que o dono não sabe
make(8, st(("Tem dono que nem sabe a diferença", B), ("entre <b>pró-labore</b> e <b>dividendo</b>.", B))
      + st(("Quem não sabe o que é seu,", B), ("não sente quando é levado.", R)), fs=42)

# 9 — a porta aberta (devolver a culpa)
make(9, st(("E a parte que mais dói:", B), ("<b>quem deixou a porta aberta foi você.</b>", B))
      + st(("Empresa sem número é casa", B), ("com a porta escancarada.", R)), fs=42)

# 10 — doutrina
make(10, st(("Empresa existe pra colocar dinheiro", B), ("no bolso do dono. <b>Como lucro.</b>", B))
       + st(("O que ela não pode", B), ("é sustentar um ladrão.", R)), fs=42)

# 11 — caminho (a luz)
make(11, st(("O ladrão trabalha no escuro.", B), ("<b>A gestão acende a luz.</b>", B))
       + st(("Conta separada, pró-labore com nome,", B), ("lucro apurado todo mês.", R)), fs=41)

# 12 — desejo
make(12, st(("Com número claro, o dinheiro", B), ("para de sumir no caminho.", B))
       + st(("E a retirada chega, enfim,", B), ("no bolso de quem construiu.", R)))

# 13 — fechamento (a caçada vira)
make(13, st(("Flagrar esse ladrão é o que eu ensino", B), ("no meu treinamento de gestão.", B))
       + st(("Feito pra pequena e média empresa.", B), ("Pro dono enxergar cada centavo.", R)), fs=41)

# 14 — CTA (o flagrante)
cta = ('      <div class="cta-big">Comenta <span class="red">LADRAO</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como flagrar<br>'
       'o ladrão silencioso da sua empresa<br>'
       'e fazer o lucro chegar em você.</div>\n')
make(14, cta)
