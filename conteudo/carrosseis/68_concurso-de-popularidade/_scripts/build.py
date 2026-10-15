#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 68 (editorial-punch, "Empresa nao e concurso de popularidade")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# gritos Anton: 1 (capa), 4 (comando), 6 (favor)
DEFAULT_ANTON = {1: 96, 4: 96, 6: 130}
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
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:35px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
  .cta-last{ font-size:32px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:34px; font-style:italic; }
</style>
</head>
<body>
"""


def img(n, fade=26):
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')


# slides de grito Anton pedem faixa clara mais alta atras do texto
FADE = {1: 44, 3: 40, 4: 42, 6: 42}
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


# 1 — CAPA (2 linhas, sem sussurro): serif preta + grito Anton. Texto do user.
make(at(1), st(("<b>Empresa não é concurso de popularidade.</b>", B))
      + st(("E VOCÊ NÃO É", A), ("COLÍRIO DA CAPRICHO", A), cls_extra=' style="margin-top:40px"'),
     top=206, fs=43)

# 2 — o cerco: quem cobra leveza nao assina a folha
make(at(2), st(("Vão te chamar de duro.", B), ("De chato. De implicante.", B), ("Vão dizer que falta leveza na sua gestão.", B))
      + st(("Quem fala isso não assina a folha.", R)), fs=42)

# 3 — o cargo: sustentar (anafora)
make(at(3), st(("Ser dono é sustentar o que você mandou.", B))
      + st(("Na segunda. Na quarta. Na sexta.", B), ("Depois da cara feia.", B), ("Depois do choro.", B), ("E sem esperar aplauso por isso.", R)),
     top=224, fs=42)

# 4 — GRITO: a tese
make(at(4), st(("Cobrar, todo mundo cobra.", B), ("Comando não é o que <b>você cobra</b>.", B))
      + st(("É O QUE VOCÊ SUSTENTA.", A), cls_extra=' style="margin-top:46px"'), top=216, fs=42)

# 5 — a tentacao do dia seguinte (universal, sem humilhar)
make(at(5), st(("A tentação nunca é na hora da cobrança.", B), ("É no <b>dia seguinte</b>.", B))
      + st(("É comprar a paz com um adiantamento,", B), ("um galho quebrado, uma exceção aberta.", B), ("Todo dono já fez isso.", R)),
     top=222, fs=41)

# 6 — GRITO: favor
make(at(6), st(("E aí vem a parte que ninguém te conta.", B))
      + st(("FAVOR NÃO COMPRA", A), ("LEALDADE.", A), cls_extra=' style="margin-top:48px"'), top=212, fs=42)

# 7 — a conta que ninguem assinou
make(at(7), st(("Cada favor desses vira uma conta na sua cabeça.", B), ("A outra pessoa nunca soube que essa conta existia.", B))
      + st(("Por isso, no dia em que ele sai, parece ingratidão.", B), ("E é só uma dívida que só você assinou.", R)), fs=38)

# 8 — o afeto de brinde (texto do user)
make(at(8), st(("Você abriu uma empresa pra ganhar dinheiro.", B))
      + st(("E ficou lá dentro mendigando simpatia.", B), ("Você paga o salário", R), ("e ainda quer o afeto de brinde.", R)), fs=42)

# 9 — o que o time precisa
make(at(9), st(("O seu time não precisa de mais um amigo.", B), ("Amigo ele já tem.", B))
      + st(("Precisa de alguém que sustente o combinado", R), ("no mês em que a coisa aperta.", R)), fs=42)

# 10 — a firmeza (o barco)
make(at(10), st(("Firmeza não espanta gente boa.", B), ("Firmeza mostra pra eles com quem dá pra contar.", B))
       + st(("E quem sabe com quem conta", B), ("não pula do barco quando o barco balança.", R)), fs=40)

# 11 — a linha fina
make(at(11), st(("Só que tem uma linha fina aqui.", B), ("Exigir sem rumo é <b>implicância</b>.", B))
       + st(("Se ninguém sabe onde a empresa tem que chegar,", B), ("cobrança vira perseguição.", R)), fs=41)

# 12 — o que esta na parede
make(at(12), st(("Cobrança com rumo é comando.", B), ("Cobrança sem rumo é mau humor.", B))
       + st(("A diferença não está no seu tom.", B), ("Está no que está escrito na parede.", R)), fs=42)

# 13 — querido x respeitado
make(at(13), st(("Ser querido dura até a primeira cobrança.", B))
       + st(("Ser respeitado dura o ano inteiro.", R), ("E é isso que segura empresa de pé.", R)), fs=43)

# 14 — CTA
cta = ('      <div class="line" style="font-size:40px">Se você prefere ser respeitado a ser querido,</div>\n'
       '      <div class="cta-big" style="margin-top:26px">comenta <span class="red">RESPEITO</span></div>\n'
       '      <div class="cta-sm">que eu te chamo no direct e te mostro, no meu treinamento<br>'
       'de gestão pra pequena e média empresa, como construir<br>'
       'o rumo que faz o seu time te levar a sério.</div>\n'
       '      <div class="cta-last">O resto continua comprando lealdade com favor.</div>\n')
make(at(14), cta, top=210)
