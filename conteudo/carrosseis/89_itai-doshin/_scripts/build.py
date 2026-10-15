#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 89 (editorial-punch, "Itai Doshin")."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
DEFAULT_ANTON = {1: 86, 3: 190, 4: 112, 5: 100, 7: 100, 9: 108, 11: 120, 13: 82, 15: 74}
try: ANTON = {**DEFAULT_ANTON, **{int(k): v for k, v in json.loads((SCR/"antonfit.json").read_text()).items()}}
except FileNotFoundError: ANTON = DEFAULT_ANTON
try: HEIGHT = {int(k): v for k, v in json.loads((SCR/"imgheight.json").read_text()).items()}
except FileNotFoundError: HEIGHT = {}
try: EXTRA = json.loads((SCR/"extra.json").read_text())   # html extra por slide (ex: kanji do 11)
except FileNotFoundError: EXTRA = {}
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
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .oq{ margin-left:-0.42em; } .cq{ margin-right:-0.42em; }
</style>
</head>
<body>
"""
FADE = {}
POS = {}   # recorte lateral: de que lado ancorar quando a imagem sobe
current = [0]
def img(n, fade=26):
    h = HEIGHT.get(n)
    box = f'height:{h}px;object-fit:cover;object-position:{POS.get(n,"center bottom")};' if h else ''
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')
def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    extra = EXTRA.get(str(n), "")
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n{extra}    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0],90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A, AB = "", " red", " anton", " anton blk"
def at(n): current[0] = n; return n
def make(n, *a, **k): slide(n, *a, **k)

make(at(1), st(("Deixa eu te falar uma verdade meio chata:", B))
          + st(("FUNCIONÁRIO BOM NÃO FICA", A), ("SÓ POR SALÁRIO.", A), cls_extra=' style="margin-top:14px"'), top=200, fs=46)
make(at(2), st(("Salário é o básico.", B))
          + st(("O que faz alguém ficar de verdade", R), ("é outra coisa.", R), cls_extra=' style="margin-top:34px"'), top=160, fs=46)
make(at(3), st(("O SONHO.", A)), top=160)
make(at(4), st(("Porque ninguém acorda animado", B))
          + st(("PRA BATER PONTO.", A), cls_extra=' style="margin-top:20px"'), top=160, fs=46)
make(at(5), st(("Acorda animado", B))
          + st(("PRA FAZER PARTE", A), ("DE ALGO.", A), cls_extra=' style="margin-top:20px"'), top=160, fs=46)
make(at(6), st(("Quando a empresa tem sonho,", B), ("o cara não tem só um trabalho.", B))
          + st(("Ele sente que tem um lugar.", R)), top=160, fs=44)
make(at(7), st(("E aí muda tudo.", B), ("Ele não faz só tarefa.", B))
          + st(("ELE COMPRA A BRIGA.", A), cls_extra=' style="margin-top:30px"'), top=160, fs=44)
make(at(8), st(("Agora vem a pergunta que incomoda:", B))
          + st(("qual é o sonho que a sua empresa", R), ("tá oferecendo?", R), cls_extra=' style="margin-top:34px"'), top=160, fs=44)
make(at(9), st(("E NÃO É", A), ("O SEU SONHO, TÁ?", A)), top=160)
make(at(10), st(("É o sonho que o time consegue falar", B), ("sem pensar muito:", B))
           + st(('<span class="oq">&ldquo;</span>eu tô aqui por isso.<span class="cq">&rdquo;</span>', R), cls_extra=' style="margin-top:34px"'), top=160, fs=44)
make(at(11), st(("Os japoneses têm um nome bonito pra isso:", B), ("ITAI DOSHIN.", A))
           + st(("Corpos diferentes,", B), ("irmanados num único coração.", R), cls_extra=' style="margin-top:26px"'), top=160, fs=40)
make(at(12), st(("Cada um num papel...", B))
           + st(("mas todo mundo puxando", R), ("pro mesmo sonho.", R), cls_extra=' style="margin-top:30px"'), top=160, fs=46)
make(at(13), st(("Sem isso, eles só enxergam escala.", B), ("ESCALA NÃO DÁ PERTENCIMENTO.", A))
           + st(("Escala dá rotatividade.", B), ("Apareceu algo melhor, o cara vai.", B), cls_extra=' style="margin-top:30px"'), top=160, fs=42)
make(at(14), st(("Por isso cultura não é frase na parede.", B))
           + st(("Cultura é o sonho vivido todo dia,", B), ("em decisão, rotina, padrão e exemplo.", R), cls_extra=' style="margin-top:40px"'), top=160, fs=42)
make(at(15), st(("Quer gente leal?", B))
           + st(("ENTÃO CONSTRÓI UM SONHO QUE", A), ("VALHA A PENA VIVER JUNTO.", A), cls_extra=' style="margin-top:24px"'), top=160, fs=48)
make(at(16), '      <div class="cta-big">Comenta <span class="red">JUNTOS</span></div>\n'
           + st(("que eu te mostro como colocar", B), ("Itai Doshin em prática na sua empresa.", B), cls_extra=' style="margin-top:30px"'), top=160, fs=43)
