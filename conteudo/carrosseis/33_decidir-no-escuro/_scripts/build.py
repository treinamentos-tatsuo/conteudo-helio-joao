#!/usr/bin/env python3
# Gera os 13 HTMLs do carrossel 33 (decidir no escuro).
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "instagram"

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
  .bottom{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:46px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .impact{ font-size:48px; font-weight:700; line-height:1.28; color:#1A1A1A; }
  .cta-big{ font-size:74px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:34px; font-weight:400; line-height:1.32; color:#1A1A1A; margin-top:16px; }
</style>
</head>
<body>
  <div class="slide">
"""

FOOT = """  </div>
</body>
</html>
"""

def img(n, fade=26, extra=""):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;{extra}">\n')

def stanza(lines):
    s = '      <div class="stanza">\n'
    for cls, txt in lines:
        c = "line" + (" " + cls if cls else "")
        s += f'        <div class="{c}">{txt}</div>\n'
    s += '      </div>\n'
    return s

def top(block, y):
    return f'    <div class="top" style="top:{y}px">\n{block}    </div>\n'

slides = {}

# 1 — Capa (o paradoxo)
slides[1] = img(1) + top(
    '      <div class="impact">Tem coisa apodrecendo na sua empresa.</div>\n'
    '      <div class="impact"><span class="red">E ninguém vai te contar.</span></div>\n',
    260)

# 2 — A cena
slides[2] = img(2) + top(
    stanza([("", "Você subiu pro escritório,"), ("", "fechou a porta, virou estratégico.")]) +
    stanza([("", "Hoje a empresa que você criou"), ("red", "chega até você por relatório.")]),
    236)

# 3 — O grito (herói: setup + Anton casada na referência)
slides[3] = img(3) + top(
    '      <div class="line">Todo mundo chama isso de crescer.</div>\n'
    '      <div class="line anton" style="font-size:80px;margin-top:18px">VOCÊ DECIDE NO ESCURO.</div>\n',
    280)

# 4 — Consequência 1: a decisão
slides[4] = img(4) + top(
    stanza([("", "No escuro, a primeira coisa"), ("", "que morre é a decisão.")]) +
    stanza([("", "Relatório é retrato do mês passado."), ("red", "Decisão atrasada nasce errada.")]),
    236)

# 5 — Consequência 2: o problema
slides[5] = img(5) + top(
    stanza([("", "A segunda é o problema pequeno,"), ("", "aquele que ninguém te conta.")]) +
    stanza([("", "Longe da ponta, ele cresce quieto."), ("red", "Quando chega em você, é incêndio.")]),
    236)

# 6 — Consequência 3: a cultura
slides[6] = img(6) + top(
    stanza([("", "A terceira é a cultura,"), ("", "que ninguém constrói de longe.")]) +
    stanza([("", "Pequena empresa é a cara do dono."), ("red", "Dono ausente, jeitinho presente.")]),
    236)

# 7 — Consequência 4: a volta
slides[7] = img(7) + top(
    stanza([("", "E a quarta é a mais cara:"), ("", "um dia você precisa voltar.")]) +
    stanza([("", "Aí você paga caro pra reaprender"), ("red", "o que um dia soube de graça.")]),
    236)

# 8 — Não é voltar pro balcão
slides[8] = img(8) + top(
    stanza([("", "Calma. Isso não é ordem"), ("", "pra você voltar pro balcão.")]) +
    stanza([("", "Estar na operação nunca foi"), ("red", "vender pra ganhar comissão.")]),
    236)

# 9 — O cheiro da ponta (2+2+âncora)
slides[9] = img(9) + top(
    stanza([("", "É escutar o cliente reclamando"), ("", "e sentir o vendedor desanimar.")]) +
    stanza([("", "É notar o mercado mudando de humor"), ("", "antes que vire prejuízo.")]) +
    stanza([("red", "Isso é o cheiro da ponta.")]),
    220)

# 10 — A pedrada (estrofe inteira em vermelho)
slides[10] = img(10) + top(
    stanza([("", "Esse faro você leva anos"), ("", "pra construir na ponta.")]) +
    stanza([("red", "E perde do dia pra noite"), ("red", "atrás de uma porta fechada.")]),
    236)

# 11 — Estratégico de verdade
slides[11] = img(11) + top(
    stanza([("", "Estratégico não é o dono"), ("", "de porta fechada no escritório.")]) +
    stanza([("", "É o dono que decide de perto,"), ("red", "de onde o mercado se mexe.")]),
    236)

# 12 — Fechamento (método + treinamento)
slides[12] = img(12) + top(
    stanza([("", "Saber onde estar, o que olhar"), ("", "e a hora de cobrar é método.")]) +
    stanza([("", "É o que eu ensino no meu treinamento"), ("", "de gestão pra pequena e média empresa.")]),
    236)

# 13 — CTA (slide exclusivo, layout padrão)
slides[13] = img(13) + top(
    '      <div class="cta-big">Comenta <span class="red">307</span>,</div>\n'
    '      <div class="cta-sm">que eu te mostro como comandar de perto<br>'
    'uma empresa que cresce e dá lucro,<br>'
    'sem nunca mais decidir no escuro.</div>\n',
    236)

for n, body in slides.items():
    (OUT / f"slide-{n:02d}.html").write_text(HEAD + body + FOOT, encoding="utf-8")
print(f"{len(slides)} HTMLs gerados em {OUT}")
