#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 75 (editorial-punch, "Lealdade nao vem em contrato")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# gritos Anton: 2 (o tapa), 6 (o risco), 9 (a doutrina)
DEFAULT_ANTON = {2: 62, 6: 92, 9: 96}
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

FADE = {2: 40, 6: 38, 9: 40}   # slides de grito pedem faixa clara atras do texto
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
    slide(n, *args, **kw)

# 1 — CAPA (isca conversacional). 2 linhas, serif grande, punch vermelho.
make(at(1), st(("Vou te falar uma verdade", B), ("meio chata:", R),
           cls_extra=' style="line-height:1.34"'), top=300, fs=54)

# 2 — O TAPA: setup serif + grito Anton. 2 linhas, regra dura.
make(at(2), st(("Você paga salário de funcionário.", B), ("E COBRA DEDICAÇÃO DE SÓCIO.", A),
           cls_extra=' style="line-height:1.55"'), top=382, fs=42)

# 3 — a cena
make(at(3), st(("Você chega às sete da manhã.", B), ("Sai depois das nove da noite.", B))
      + st(("E às seis em ponto o galpão já está vazio.", B), ("Aí você diz que ninguém quer nada.", R)), fs=41)

# 4 — a pergunta seca (1 + 2)
make(at(4), st(("Seja sincero comigo, empresário.", B))
      + st(("Por que ele ia ficar até nove da noite", B), ("numa empresa que nunca vai ser dele?", R)), fs=42)

# 5 — os fatos
make(at(5), st(("Ele não vê o seu <b>lucro</b>.", B), ("Não senta na reunião que decide nada.", B))
      + st(("Está há <b>quatro anos</b> na mesma função", B), ("e ninguém nunca disse como ele sobe.", R)), fs=41)

# 6 — GRITO: o risco
make(at(6), st(("A dívida do maquinário está no seu nome.", B), ("Se quebrar, a casa que vai é a sua.", B))
      + st(("O RISCO É SEU.", A), ("O LUCRO TAMBÉM.", A), cls_extra=' style="margin-top:48px"'), top=212, fs=40)

# 7 — o compromisso dele
make(at(7), st(("O compromisso dele é com o <b>salário</b>.", B), ("Com o aluguel, a escola do filho, a moto.", B))
      + st(("E está tudo certo.", B), ("Foi isso que vocês combinaram.", R)), fs=41)

# 8 — o erro e seu
make(at(8), st(("Ele não te traiu.", B), ("Você nunca prometeu nada além do <b>salário</b>.", B))
      + st(("E passou anos procurando sócio", B), ("na folha de pagamento.", R)), fs=41)

# 9 — GRITO: a doutrina
make(at(9), st(("Você já leu o contrato dele?", B), ("Tem hora, tem função, tem salário.", B))
      + st(("MAS LEALDADE NÃO VEM", A), ("EM CONTRATO.", A), cls_extra=' style="margin-top:48px"'), top=212, fs=42)

# 10 — os trezentos a mais
make(at(10), st(("Aí aparece alguém pagando <b>300 reais a mais</b>", B), ("e leva o seu melhor numa conversa.", B))
      + st(("Não foi deslealdade.", B), ("Você não tinha mais nada na mesa.", R)), fs=41)

# 11 — como se constroi
make(at(11), st(("Lealdade se constrói com coisa simples.", B), ("Um caminho pra ele subir.", B))
      + st(("Elogio quando acerta. Casa organizada.", B), ("E um líder que ele respeita.", R)), fs=41)

# 12 — a guarda
make(at(12), st(("E não é passar a mão na cabeça.", B), ("Ninguém bom fica em empresa frouxa.", B))
      + st(("Gente boa fica onde é <b>cobrada</b>", B), ("e onde tem pra onde crescer.", R)), fs=42)

# 13 — a ordem
make(at(13), st(("Quer que ele vista a camisa?", B), ("<b>Então para de pedir.</b>", B))
      + st(("A sua empresa não tem que ser o sonho dele.", B), ("Tem que ser onde ele realiza o sonho dele.", R)), fs=40)

# 14 — primeiro passo (1 + 2 + ancora curta)
make(at(14), st(("Faz uma coisa essa semana.", B))
      + st(("Chama o seu melhor pra conversar", B), ("e pergunta onde ele quer chegar.", B))
      + st(("Depois mostra o caminho aqui dentro.", R), cls_extra=' style="margin-top:44px"'), top=214, fs=41)

# 15 — ponte com o metodo
make(at(15), st(("Fazer isso todo mês, sem falhar, tem nome.", B), ("Chama cultura. E cultura se constrói.", B))
      + st(("É o que eu ensino no meu treinamento", B), ("de gestão pra pequena e média empresa.", R)), fs=41)

# 16 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">LEAL</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como construir um lugar<br>'
       'onde gente boa quer ficar. E crescer.</div>\n')
make(at(16), cta, top=282)
