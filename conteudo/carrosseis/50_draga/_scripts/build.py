#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 50 (editorial-punch, D2-S5 draga)."""
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
     st(("Essa empresa fatura", " capa"), ("50 milhões por ano.", " capa"))
     + st(("E engoliu 20 milhões do dono.", " capa-punch"))
     + '      <div class="stanza" style="margin-top:30px"><div class="line sussurro">aos poucos. sem ele perceber.</div></div>\n',
     top=210)

# 2 — o caso
make(2, st(("Caso real, de um aluno meu.", B), ("Lá, <span class=\"red\">vender nunca foi problema.</span>", B))
      + st(("Pedido entrando todo dia.", B), ("<b>Faturamento de gente grande.</b>", B)), top=210)

# 3 — o dinheiro de casa
make(3, st(("Mas todo ano o dono punha dinheiro de casa.", B), ("Um aporte aqui, um socorro ali.", B))
      + st(("Ninguém chamava isso de rombo.", B), ("Chamavam de fase.", R)), fs=40)

# 4 — o número
make(4, st(("Em cinco anos, a conta fechou:", B), ("<b>quase 20 milhões do patrimônio pessoal.</b>", B))
      + st(("Sem crise. Sem golpe. Sem aviso.", B), ("A empresa dragou o dono em silêncio.", R)), fade=40)

# 5 — ninguém viu
make(5, st(("E aqui vem a parte que assusta:", B), ("ninguém viu acontecer.", B))
      + st(("Porque dinheiro entrando todo dia", B), ("faz rombo parecer detalhe.", R)))

# 6 — grito (Anton puro)
current[0] = 6
make(6, st(("VENDA É ANESTESIA.", " anton")), top=300)

# 7 — doutrina
make(7, st(("Enquanto a venda flui, a dor não chega.", B), ("A margem podre não grita.", B))
      + st(("O custo inchado não reclama.", B), ("E o buraco do caixa fecha <span class=\"red\">com o seu dinheiro.</span>", B)), fs=39)

# 8 — espelho (estrofe inteira vermelha)
make(8, st(("Você não precisa faturar 50 milhões", B), ("pra viver o mesmo filme.", B))
      + st(("É o cartão cobrindo o caixa.", R), ("É o salário de dono que você nunca tira.", R)), top=330)

# 9 — pedrada
make(9, st(("Quando o fluxo inverte,", B), ("você já não tem uma empresa.", B))
      + st(("Você tem uma despesa", B), ("com CNPJ e folha de pagamento.", R)))

# 10 — a régua
make(10, st(("A régua cabe numa pergunta:", B), ("<b>quem está pagando quem?</b>", B))
       + st(("Se o dinheiro anda de casa pra empresa,", B), ("a draga está ligada.", R)))

# 11 — o desejo
make(11, st(("No sentido certo, o fluxo é um só:", B), ("venda vira lucro, lucro vira caixa.", B))
       + st(("A empresa te paga todo mês.", B), ("E o seu patrimônio cresce fora dela.", R)))

# 12 — o primeiro passo
make(12, st(("O primeiro passo é uma conta que dói.", B), ("Soma o que saiu do seu bolso pra empresa.", B))
       + st(("Aporte, cartão, salário que ficou lá.", B), ("Esse número é o tamanho da draga.", R)), fs=40)

# 13 — fechamento
make(13, st(("A draga não se desliga com venda.", B), ("Se desliga com <span class=\"red\">margem, custo e caixa.</span>", B))
       + st(("É isso que eu ensino no meu treinamento", B), ("de gestão pra pequena e média empresa.", B)))

# 14 — CTA (exclusivo)
cta = ('      <div class="cta-big">Comenta <span class="red">DRAGA</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como desligar a sua<br>'
       'e fazer a empresa pagar você todo mês.</div>\n')
make(14, cta)
