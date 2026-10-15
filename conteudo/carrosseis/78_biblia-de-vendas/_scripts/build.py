#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 78 (editorial-punch, "Toda area de vendas precisa de uma biblia")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# gritos Anton: 1 e 5 (grito puro 2 linhas), 7 e 10 (heroi), 13 (punch Anton no fim do 2+2)
DEFAULT_ANTON = {1: 86, 5: 80, 7: 88, 10: 60, 13: 68}
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

# slides de grito pedem faixa clara maior atras do texto
FADE = {1: 42, 5: 42, 7: 38, 10: 38, 13: 38}
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


# 1 - CAPA: gancho-tapa, grito puro Anton em 2 linhas (padrao do 31)
make(at(1), st(("TODA ÁREA DE VENDAS", A), ("PRECISA DE UMA BÍBLIA.", A)), top=300)

# 2 - por que a igreja funciona
make(at(2), st(("Ninguém entra numa igreja", B), ("e prega o que quer.", B))
      + st(("Mil bocas, uma palavra só.", B), ("Porque está escrito.", R)), fs=44)

# 3 - voce tem escritura pra tudo (anafora de 3 curtas + punch)
make(at(3), st(("Tem ficha técnica na produção.", B), ("Tem checklist na entrega.", B),
               ("Tem o manual da máquina na gaveta.", B))
      + st(("E na venda não tem uma folha escrita.", R)), top=222, fs=42)

# 4 - o que acontece sem o livro
make(at(4), st(("O desconto, o prazo,", B), ("o que o seu produto faz.", B))
      + st(("Cada vendedor responde do jeito que acha.", B), ("E você descobre pelo cliente.", R)), fs=41)

# 5 - GRITO: a seita
make(at(5), st(("CADA VENDEDOR SEU", A), ("FUNDOU A PRÓPRIA SEITA.", A)), top=300)

# 6 - a autoria (a premissa)
make(at(6), st(("Cada um escreveu a própria escritura.", B), ("Do jeito que achou melhor.", B))
      + st(("E quem escreveu conhece a sua empresa", B), ("muito menos do que você.", R)), fs=41)

# 7 - objecao + tapa (heroi: 2 serif + Anton)
make(at(7), st(("Você vai me dizer:", B), ("isso não é engessar o vendedor?", B))
      + st(("É PRA ENGESSAR MESMO.", A), cls_extra=' style="margin-top:48px"'), top=262, fs=43)

# 8 - o limite (o que continua dele)
make(at(8), st(("Técnica é dele. O jeito de falar é dele.", B), ("Isso eu não tiro de ninguém.", B))
      + st(("Mas o que a sua empresa promete", B), ("não é opinião de funcionário.", R)), fs=41)

# 9 - a ponte: da palavra pro resultado
make(at(9), st(("Isso parece conversa de discurso.", B), ("Não é.", B))
      + st(("Onde a palavra não está escrita,", B), ("o resultado também não está.", R)), fs=43)

# 10 - a previsibilidade (heroi: 2 serif + Anton)
make(at(10), st(("Esse livro tem nome: <b>playbook</b>.", B), ("Sem ele, a sua empresa reza pra vender.", B))
      + st(("COM ELE, ELA VENDE COM MÉTODO.", A), cls_extra=' style="margin-top:48px"'), top=262, fs=42)

# 11 - primeiro passo
make(at(11), st(("Faz um teste, escreve em uma folha essa semana:", B), ("as cinco perguntas que todo cliente faz.", B))
      + st(("E do lado, a resposta que a sua empresa dá.", B), ("Não a que cada um inventa na hora.", R)), fs=40)

# 12 - o desejo (estrofe de 2 + ancora vermelha sozinha)
make(at(12), st(("A mesma equipe. O mesmo produto.", B), ("O mesmo mercado.", B),
                ("E mais venda entrando todo mês.", B))
      + st(("É isso que uma folha escrita muda.", R), cls_extra=' style="margin-top:48px"'), top=230, fs=41)

# 13 - escrever e metade do culto (2+2 com o punch em Anton)
make(at(13), st(("Mas só escrever não adianta.", B), ("Essa é só uma parte do culto.", B))
      + st(("O que garante o rito é o acompanhamento.", B), ("E ACOMPANHAMENTO É GESTÃO.", A),
           cls_extra=' style="margin-top:46px"'), top=234, fs=41)

# 14 - fechamento + CTA
cta = (st(("É isso que eu te ensino no meu treinamento", B), ("de gestão pra pequena e média empresa.", B))
       + '      <div class="cta-big" style="margin-top:56px">Comenta <span class="red">SAGRADO</span></div>\n'
       + '      <div class="cta-sm">que eu te ensino a comandar a área de vendas,<br>como dono.</div>\n')
make(at(14), cta, top=232, fs=41)
