#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 81 (editorial-punch, "Tempo de resposta")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)

DEFAULT_ANTON = {1: 74, 5: 130}
try:
    ANTON = {**DEFAULT_ANTON, **{int(k): v for k, v in json.loads((SCR/"antonfit.json").read_text()).items()}}
except FileNotFoundError:
    ANTON = DEFAULT_ANTON
try:
    HEIGHT = {int(k): v for k, v in json.loads((SCR/"imgheight.json").read_text()).items()}
except FileNotFoundError:
    HEIGHT = {}

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
  .stanza + .stanza{ margin-top:50px; }
  .line{ font-size:44px; line-height:1.28; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton.blk{ color:#1A1A1A; }
  .anton .red{ color:#A91C20; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""

FADE = {1: 34, 5: 36}
current = [0]

def img(n, fade=26):
    h = HEIGHT.get(n)
    box = f'height:{h}px;object-fit:cover;object-position:center bottom;' if h else ''
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0],90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R, A = "", " red", " anton"
def at(n): current[0] = n; return n
def make(n, *a, **k): slide(n, *a, **k)

# 1 — CAPA: desculpa em serif, tapa em Anton, o cliente responde em serif
make(at(1), st(("Faltou gente? Tava corrido?", B))
      + st(("F@DA-SE. O PROBLEMA É TEU.", A), cls_extra=' style="margin-top:36px"')
      + st(("Eu, como seu cliente,", B), ("não tô nem aí pro seu motivo.", B), cls_extra=' style="margin-top:40px"'),
     top=178, fs=42)

# 2 — a desculpa dele, entre aspas, e o tapa
make(at(2), st(("&ldquo;Ah, mas não dá pra", B), ("responder na hora.&rdquo;", B))
      + st(("Se vira.", B), ("O problema é teu.", R)), top=270, fs=48)

# 3 — o cliente vai embora
make(at(3), st(("Eu te mandei mensagem.", B), ("Não vou te cobrar resposta.", B))
      + st(("Eu vou no próximo.", B), ("E tem trezentos iguais a você.", R)), top=262, fs=44)

# 4 — sem briga, sem chance
make(at(4), st(("Eu não brigo com você.", B), ("Não peço pra falar com o dono.", B))
      + st(("Não te dou chance de consertar.", B), ("Eu só não volto.", R)), top=254, fs=43)

# 5 — o erro de diagnostico + reveal "PRESSA."
make(at(5), st(("E você nunca vai saber por quê.", B))
      + st(("Vai achar que foi o preço.", B), ("Vai baixar a margem pra", B), ("resolver o que era simples...", B),
           cls_extra=' style="margin-top:42px"')
      + st(("PRESSA.", A), cls_extra=' style="margin-top:44px"'), top=196, fs=42)

# 6 — o inventario do que ele mede
make(at(6), st(("Você sabe o seu faturamento.", B), ("Sabe quanto tem em estoque.", B))
      + st(("Mas não sabe quantos minutos", B), ("o seu cliente espera.", R)), top=254, fs=43)

# 7 — nao e a atendente
make(at(7), st(("Não adianta brigar com a atendente.", B), ("Ela não inventou esse prazo.", B))
      + st(("Ninguém nunca combinou com ela", B), ("o tempo médio de resposta.", R)), top=250, fs=41)

# 8 — de quem e a caneta
make(at(8), st(("Quem desenha o processo", B), ("de venda é o dono.", B))
      + st(("Não é o gerente. Não é ela.", B), ("É você, e você não desenhou.", R)), top=258, fs=44)

# 9 — o teste
make(at(9), st(("Faz o teste. Manda um zap", B), ("pra sua empresa e pede um preço.", B))
      + st(("Depois olha o relógio.", B), ("Aquilo ali é a sua empresa.", R)), top=254, fs=43)

# 10 — a saida: escrever
make(at(10), st(("Isso não se resolve gritando.", B), ("Se resolve escrevendo.", B))
      + st(("O que você sabe de venda", B), ("tem que virar manual.", R)), top=258, fs=44)

# 11 — manual sem rito nao vale
make(at(11), st(("E manual na gaveta não vale nada.", B), ("Depois de escrito, se treina.", B))
      + st(("Se acompanha. Se cobra.", B), ("Toda semana, no mesmo dia.", R)), top=254, fs=43)

# 12 — a maquina comeca na cabeca do dono
make(at(12), st(("Máquina de vendas não começa", B), ("no vendedor que você contrata.", B))
      + st(("Começa manualizando", B), ("o conhecimento do dono.", R)), top=254, fs=43)

# 13 — o que falta
make(at(13), st(("O que falta não é vendedor.", B))
      + st(("É método e processo e gestão", B), ("pra tocar área de vendas.", R), cls_extra=' style="margin-top:44px"'),
     top=282, fs=46)

# 14 — CTA
cta = (st(("Meu treinamento de gestão", B), ("é pra pequena e média empresa.", B))
       + '      <div class="cta-big" style="margin-top:54px">Comenta <span class="red">TEMPO</span></div>\n'
       + st(("que eu te ensino a montar", B), ("a sua máquina de vendas.", R), cls_extra=' style="margin-top:30px"'))
make(at(14), cta, top=250, fs=43)
