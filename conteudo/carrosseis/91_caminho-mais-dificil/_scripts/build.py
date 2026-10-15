#!/usr/bin/env python3
"""Gera os 10 HTMLs do carrossel 91 (editorial-punch, "o caminho mais dificil"). Layout da skill (calibragem do 88: corpo top 200, capa 240)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE = _j("imgheight.json"), _j("fade.json")
OBJPOS = {}   # object-position por slide (default "center bottom")
HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,700&display=swap" rel="stylesheet">
<style>
  *{ margin:0; padding:0; box-sizing:border-box; }
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; }
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""
def mask(F):
    if F <= 26: return f"linear-gradient(to bottom,transparent 0%,#000 {F}%)"
    return (f"linear-gradient(to bottom,transparent 0%,rgba(0,0,0,0.06) {F*0.25:.1f}%,rgba(0,0,0,0.30) {F*0.55:.1f}%,"
            f"rgba(0,0,0,0.72) {F*0.80:.1f}%,#000 {F:.1f}%)")
def img(n):
    h = HEIGHT.get(n); pos = OBJPOS.get(n, "center bottom")
    box = f'height:{h}px;object-fit:cover;object-position:{pos};' if h else ''
    m = mask(FADE.get(n, 26))
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:{m};mask-image:{m};z-index:1;">')
def slide(n, body, top=200, fs=None):
    override = f'<style>.line{{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = [f'        <div class="line{cls}">{txt}</div>' for txt, cls in lines]
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R = "", " red"

slide(1, st(("Faturou mais e continua duro.", B), ("O problema não é a venda. É você.", R)), top=240, fs=52)
slide(2, st(("Todo dono sonha em vender mais.", B), ("Nenhum sonha em vender menos. Eu sei.", B)) + st(("Mas você já vendeu mais.", B), ("Ano passado, esse ano.", B), ("E cadê o dinheiro?", R)))
slide(3, st(("Eu te digo onde está: nunca entrou.", B)) + st(("Você vende um produto", B), ("que não sabe quanto custa", B), ("por um preço que você chutou.", R)))
slide(4, st(("Você não sabe a sua margem.", B), ("Não sabe o seu custo. Não sabe o seu preço.", B)) + st(("Isso não é falta de tempo.", B), ("É analfabetismo empresarial.", R)))
slide(5, st(("E o dono que não sabe o número", B), ("resolve como? Vendendo mais. Claro.", B)) + st(("Mais anúncio, mais vendedor, mais dívida.", B), ("Pra perder mais rápido.", R)))
slide(6, st(("Vender mais com a conta errada", B), ("é quebrar com mais trabalho.", R)), fs=48)
slide(7, st(("O dinheiro que você procura lá fora", B), ("já está aqui dentro.", B)) + st(("Na mesma operação, sem investir um real.", B), ("Organiza a casa e ele sobra.", R)))
slide(8, st(("Organizar a casa é entender", B), ("de finanças como dono, não como contador.", B)) + st(("Contador cuida do imposto.", B), ("Do seu lucro quem cuida é você.", R)))
slide(9, st(("DRE, margem, custo, gasto.", B), ("O básico, chato, mas que funciona!", B)) + st(("É o que separa o dono", B), ("do funcionário mais mal pago", R), ("da própria empresa.", R)))
cta = (st(("Eu tenho um treinamento que ensina o dono", B), ("a colocar mais dinheiro no bolso", B), ("com a empresa que ele já tem.", B))
       + '      <div class="cta-big" style="margin-top:44px">Comenta <span class="red">DONO</span></div>\n'
       + st(("e eu te mando o link no seu direct.", R), mt=20))
slide(10, cta, fs=40)
