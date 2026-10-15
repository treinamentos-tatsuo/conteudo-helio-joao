#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 61 (editorial-punch, a sua empresa tem um setor so)."""
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

FADE = {1: 22}

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

def at(n):
    current[0] = n
    return n

def make(n, *args, **kw):
    current[0] = n
    slide(n, *args, **kw)

# 1 — capa: a tese como tapa
make(at(1), st(("Você acha que vendas é um setor.", " capa"))
      + st(("VENDAS É A EMPRESA INTEIRA.", " anton"), cls_extra=' style="margin-top:34px"')
      + st(("inclusive quem nunca viu um cliente.", " sussurro"), cls_extra=' style="margin-top:30px"'),
     top=210)

# 2 — as duas funcoes
make(at(2), st(("Dentro de uma empresa", B), ("só existem duas funções.", B))
      + st(("Ou a pessoa está vendendo,", B), ("ou está ajudando alguém a vender.", R)), top=216, fs=44)

# 3 — a ponte (promessa da analogia)
make(at(3), st(("Você entende isso melhor", B), ("olhando um restaurante.", R)), top=250, fs=46)

# 4 — o chef (o melhor trabalho do mundo)
make(at(4), st(("O chef pode preparar", B), ("<b>o melhor prato do dia.</b>", B)), top=250, fs=48)

# 5 — o garcom desfaz
make(at(5), st(("Se o garçom for grosso,", R), ("o cliente não volta.", R)), top=250, fs=48)

# 6 — quem derrubou a venda
make(at(6), st(("O cliente não foi embora", B), ("por causa da comida.", B))
      + st(("Foi embora por causa de quem", R), ("só carregou o prato até a mesa.", R)), top=216, fs=44)

# 7 — vira a mesa (grito)
make(at(7), st(("Você ainda não percebeu?", B), ("O DONO DO RESTAURANTE É VOCÊ.", " anton"))
      + st(("E o garçom é qualquer um", B), ("que trabalha na sua empresa.", R)), top=208, fs=44)

# 8 — o cliente nao separa
make(at(8), st(("O cliente não separa a empresa", B), ("das pessoas que trabalham nela.", B))
      + st(("E quem ainda não confia em você", R), ("julga pelo único contato que teve.", R)), top=214, fs=43)

# 9 — treinou so quem vende
make(at(9), st(("Você treinou o time de vendas.", B), ("O resto aprendeu sozinho.", B))
      + st(("Quem entrega e quem atende", B), ("aprendeu com a cultura.", R)), top=216, fs=44)

# 10 — a pedrada (o ambiente e obra sua)
make(at(10), st(("Você está perdendo cliente", B), ("por causa do ambiente que você formou.", B))
       + st(("E você nunca olhou pra isso", R), ("porque essa gente não bate meta.", R)), top=214, fs=41)

# 11 — nao e sorriso, e comportamento
make(at(11), st(("Isso não se resolve com sorriso", B), ("nem com reunião de bom dia.", B))
       + st(("Resolve alinhando o comportamento", R), ("que você permite aí dentro.", R)), top=214, fs=43)

# 12 — orgulho (grito)
make(at(12), st(("O seu colaborador tem orgulho", B), ("do que ele faz aí dentro?", B))
       + st(("ELE ACREDITA NO QUE FAZ?", " anton"), cls_extra=' style="margin-top:46px"')
       + st(("porque o cliente sente isso.", " sussurro"), cls_extra=' style="margin-top:30px"'),
     top=218, fs=44)

# 13 — ponte do CTA
make(at(13), st(("Não é mais um vendedor que te falta.", B), ("É uma empresa que <i><b>transpire</b></i> venda.", B))
       + st(("E isso não nasce sozinho.", B), ("Isso se constrói.", R)), top=216, fs=43)

# 14 — CTA
cta = (st(("Eu tenho um treinamento voltado para", B), ("donos de pequena e média empresa.", B))
       + '      <div class="cta-big" style="margin-top:52px">Comenta <span class="red">VENDA</span>,</div>\n'
       + '      <div class="cta-sm">que eu te mostro como construir<br>'
         'o ambiente onde a empresa inteira vende.</div>\n')
make(at(14), cta, top=214, fs=42)
