#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 58 (editorial-punch, o cliente virou patrao)."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

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
  .capa{ font-size:40px; line-height:1.28; font-weight:700; }
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

FADE = {1: 14}

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton):not(.capa):not(.sussurro){{font-size:{fs}px}}</style>\n' if fs else ""
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

# 1 — capa: ditado como armacao (serif) + virada no grito Anton + sussurro
make(1,
     st(("Se o cliente tem sempre razão,", " capa"))
     + st(("ELE NÃO É CLIENTE. É PATRÃO.", " anton"), cls_extra=' style="margin-top:14px"')
     + '      <div class="stanza" style="margin-top:30px"><div class="line sussurro">e é o pior que você já teve.</div></div>\n',
     top=240)

# 2 — a crenca desce pro dinheiro
make(2, st(("Essa frase não fica na conversa.", B), ("<b>Ela desce pro seu preço.</b>", B))
      + st(("Cada vez que você obedece,", B), ("ela sai do seu lucro.", R)))

# 3 — por que voce obedece (diagnostico de dono)
make(3, st(("E você obedece por um motivo simples:", B), ("<b>não sabe até onde pode ir.</b>", B))
      + st(("Não sabe o custo real, não sabe a margem.", B), ("E quem não sabe aceita qualquer coisa.", R)), fs=42)

# 4 — a regra (grito)
make(4, st(("A regra é seca e não tem exceção:", B))
      + st(("QUEM NÃO SABE O NÚMERO", " anton"), ("NÃO MANDA NO PREÇO.", " anton"), cls_extra=' style="margin-top:44px"'),
     top=220, fs=42)

# 5 — a ponte
make(5, st(("E repara na ironia:", B), ("o cliente não te paga pra <b>concordar</b>.", B))
      + st(("Se ele só quer ouvir o que já pensa,", B), ("ele não precisa de você.", R)), fs=42)

# 6 — o preco da bajulacao
make(6, st(("E essa bajulação tem preço.", B), ("Ele não aparece no contrato.", B))
      + st(("Aparece no dia trinta,", B), ("quando não sobra nada.", R)))

# 7 — o circulo (primeira volta)
make(7, st(("Você fecha a qualquer preço.", B), ("<b>Sem preço, não tem lucro.</b>", B))
      + st(("Sem lucro, você paga mal.", B), ("E quem é bom não fica.", R)))

# 8 — o circulo (segunda volta)
make(8, st(("Com time fraco, o trabalho piora.", B), ("Com trabalho pior, o cliente vai embora.", B))
      + st(("O mesmo cliente", B), ("que você tinha medo de perder.", R)), fs=42)

# 9 — a ironia (grito)
make(9, st(("Repara no tamanho da ironia:", B))
      + st(("VOCÊ SE HUMILHOU", " anton"), ("E ENTREGOU PIOR.", " anton"), cls_extra=' style="margin-top:44px"'),
     top=220, fs=42)

# 10 — a culpa
make(10, st(("E não foi o cliente que fez isso.", B), ("<b>Ninguém apontou uma arma pra você.</b>", B))
       + st(("Foi o medo que assinou o orçamento.", B), ("E medo é o que sobra quando falta número.", R)), fs=41)

# 11 — doutrina
make(11, st(("Negócio se sustenta na <b>verdade</b>,", B), ("não na cabeça baixa.", B))
       + st(("Quem concorda com tudo", B), ("não é fornecedor. É empregado.", R)))

# 12 — o circulo vira
make(12, st(("O círculo gira pro outro lado também.", B), ("<b>Cobra direito e sobra lucro.</b>", B))
       + st(("Com lucro você paga bem, atrai gente boa", B), ("e entrega um trabalho grande.", R)), fs=41)

# 13 — desejo
make(13, st(("Aí o cliente volta.", B), ("Não porque você concordou com ele.", B))
       + st(("Mas porque você resolveu o problema dele", B), ("melhor do que qualquer um.", R)), fs=42)

# 14 — primeiro passo
make(14, st(("Faz uma conta hoje: pega os últimos", B), ("cinco orçamentos que você fechou.", B))
       + st(("Soma o desconto que você deu.", B), ("Esse é o lucro que você doou.", R)), fs=42)

# 15 — fechamento
make(15, st(("Cobrar direito é <b>conta</b>, não é coragem.", B), ("Isso eu ensino no meu treinamento de gestão.", B))
       + st(("Feito pra pequena e média empresa.", B), ("Pro dono mandar no próprio preço.", R)), fs=40)

# 16 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">PATRAO</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como dominar o seu caixa,<br>'
       'cobrar o preço certo e parar de trabalhar<br>'
       'de graça pro cliente que você tem medo de perder.</div>\n')
make(16, cta)
