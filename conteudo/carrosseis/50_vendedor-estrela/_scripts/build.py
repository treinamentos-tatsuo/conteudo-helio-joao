#!/usr/bin/env python3
"""Gera os 18 HTMLs do carrossel 50 (editorial-punch) — v2 pós-revisão do user (21/08)."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

try:
    ANTON = {int(k): v for k, v in json.loads((SCR / "antonfit.json").read_text()).items()}
except FileNotFoundError:
    ANTON = {}
AN3 = ANTON.get(3, 100)
AN10 = ANTON.get(10, 80)
AN12 = ANTON.get(12, 100)

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
  .capa1{ font-size:48px; line-height:1.3; font-weight:600; }
  .capa2{ font-size:58px; line-height:1.25; }
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

def st(*lines, margin=None):
    parts = []
    for item in lines:
        txt, cls = item[0], item[1]
        px = item[2] if len(item) > 2 else None
        style = f' style="font-size:{px}px"' if px else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    mstyle = f' style="margin-top:{margin}px"' if margin is not None else ""
    return f'      <div class="stanza"{mstyle}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R = "", " red"

# 1 — capa (3 níveis, gaps apertados, bloco alto)
capa = (st(("Tem um câncer na sua empresa.", " capa1"))
        + st(("E ele bate meta todo mês.", " capa2 red"), margin=16)
        + st(("Por isso você nunca cortou.", " sussurro"), margin=12))
slide(1, capa, top=250)

# 2 — a cena (2 estrofes; o punch virou o slide 3)
slide(2, st(("Você sabe de quem eu estou falando.", B), ("Ele <b>vende como ninguém</b>.", B))
        + st(("Chega na hora que quer.", B), ("Passa por cima de qualquer regra.", B)))

# 3 — NOVO: o grito do silêncio
slide(3, st(("E ninguém fala nada.", B))
        + st(("NEM VOCÊ.", " anton", AN3), margin=24), top=220)

# 4 — o número comprou o silêncio
slide(4, st(("Não é medo dele. É medo do número.", B))
        + st(("Ele carrega trinta, às vezes quarenta", B), ("por cento do seu faturamento.", B))
        + st(("O número dele comprou o seu silêncio.", R)), top=200, fs=42)

# 5 — o feudo (2 estrofes; o punch virou o slide 6)
slide(5, st(("Com o tempo ele arruma companhia.", B), ("Vira um grupinho. Vira um <b>feudo</b>.", B))
        + st(("Vendedor novo entra,", B), ("não performa e vai embora.", B)), top=200)

# 6 — NOVO: punch do feudo em slide próprio
slide(6, st(("Não é falta de talento.", R, 50), ("O feudo não deixa ninguém crescer.", R, 50)), top=300)

# 7 — por que câncer (3 estrofes, exceção aceita: a 3ª é curta)
slide(7, st(("É por isso que a palavra é câncer.", B), ("Ele não avisa que chegou.", B))
        + st(("Cresce em silêncio enquanto", B), ("o exame diz que está tudo bem.", B))
        + st(("O seu exame é o faturamento.", R)))

# 8 — do tamanho que ele permite
slide(8, st(("Enquanto isso, você não monta processo.", B), ("Não forma gente. Não constrói máquina.", B))
        + st(("A sua empresa ficou", R), ("do tamanho que ele permite.", R)), fs=42)

# 9 — a prova da oscilação (2 estrofes; o grito virou o slide 10)
slide(9, st(("Eu conheço uma empresa assim.", B), ("Num mês, três milhões de faturamento.", B))
        + st(("No seguinte, um. No outro, cinco.", B), ("E foi assim durante anos.", B)), fs=42)

# 10 — NOVO: roleta russa (grito Anton sobre o revólver)
slide(10, st(("AQUILO NÃO ERA VENDA.", " anton", AN10), ("ERA ROLETA RUSSA.", " anton", AN10)), top=240, fade=38)

# 11 — a armadilha
slide(11, st(("Eu sei o que você está pensando.", B), ("“Se ele sair, eu quebro.”", B))
         + st(("É por essa frase que ele fica anos.", R)))

# 12 — ele vai sair (grito + remate)
slide(12, st(("ELE VAI SAIR.", " anton", AN12))
         + st(("Não é se. É quando.", B))
         + st(("E vai levar junto o faturamento", R), ("que você deixou morar na mão dele.", R)), fade=20, top=200, fs=42)

# 13 — a comissão
slide(13, st(("E a parte que mais dói:", B), ("esse câncer não entrou sozinho.", B))
         + st(("Você alimenta ele", R), ("todo mês. Com comissão.", R)))

# 14 — a prova (gestão entrou)
slide(14, st(("Naquela empresa, um dia entrou <b>gestão</b>.", B), ("Regra clara, igual pra todo mundo.", B))
         + st(("Sabe o que os estrelas fizeram?", B), ("Foram embora.", B))
         + st(("Estrela que não aceita regra", R), ("nunca jogou pelo seu time.", R)), fs=42)

# 15 — a régua
slide(15, st(("Empresa forte não caça estrela.", B), ("Ela constrói máquina de vendas.", B))
         + st(("Processo que ensina, meta clara,", B), ("regra que vale pra todo mundo.", B))
         + st(("Meta não compra exceção.", R)), top=200)

# 16 — o desejo
slide(16, st(("É assim que a venda vira previsível.", B))
         + st(("Mês parecido com mês.", B), ("Vendedor novo performando.", B))
         + st(("Time inteiro jogando o mesmo jogo.", B), ("E ninguém segurando você refém.", R)), fs=42)

# 17 — fechamento (treinamento nomeado)
slide(17, st(("É isso que eu ensino no meu treinamento", B), ("de gestão pra pequena e média empresa:", B))
         + st(("tirar a venda da mão de um herói", B), ("e colocar dentro de um processo.", B))
         + st(("Máquina não depende de humor.", R)), top=200, fs=41)

# 18 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">ESTRELA</span>,</div>\n'
       '      <div class="cta-sm">que eu te chamo no direct e te mostro<br>'
       'como construir uma máquina de vendas<br>que não fica refém de ninguém.</div>\n')
slide(18, cta)
