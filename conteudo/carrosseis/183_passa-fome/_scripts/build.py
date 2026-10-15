#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 183 (editorial-punch, "R$ 30 mil não é salário de dono", pauta dívida R$ 11 tri).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
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
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .line b{ font-weight:700; }
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
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
cur = [0]
def slide(n, body, top=240, fs=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n

slide(at(1),  st(("Com o Brasil devendo R$ 11 trilhões,", B))
            + st(("R$ 30 MIL NÃO É", A), ("SALÁRIO DE DONO.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Saiu agora: a dívida do Brasil", B), ("passou de R$ 11 trilhões.", B))
            + st(("E, pela primeira vez na história,", B), ("os juros passaram de R$ 1 trilhão", R), ("em doze meses.", R)), fs=42)
slide(at(3),  st(("Esse número não fica em Brasília.", B), ("Ele chega na sua mesa.", B))
            + st(("Crédito mais caro, imposto mudando,", B), ("e a regra trocando no meio do jogo.", R)), fs=42)
slide(at(4),  st(("É nesse país que você assina", B), ("o empréstimo da empresa.", B))
            + st(("Dá o aval no seu nome.", B), ("E põe a sua casa na garantia.", R)), fs=44)
slide(at(5),  st(("Se der errado, o funcionário", B), ("sai com a rescisão.", B), ("O gerente do banco muda de agência.", B))
            + st(("E você perde a casa", B), ("onde a sua família dorme.", R)), fs=42)
slide(at(6),  st(("Com todo esse risco nas costas,", B), ("sabe quanto a maioria dos donos tira?", B))
            + st(("R$ 15 mil. R$ 20. R$ 30 mil.", B), ("E ainda acha que está bem pago.", R)), fs=42)
slide(at(7),  st(("Eu vou falar do jeito que é:", B))
            + st(("ISSO NÃO É", A), ("SALÁRIO DE DONO.", A), ("É PASSA-FOME.", A), mt=22), fs=46)
slide(at(8),  st(("R$ 30 mil um bom gerente ganha.", B), ("E ele não assinou nada no banco.", B))
            + st(("Ele não dorme com a casa na garantia.", B), ("Você dorme.", R)), fs=42)
slide(at(9),  st(("Eu pergunto isso pra todo dono", B), ("que senta na minha frente:", B))
            + st(("por que você paga o salário do funcionário", B), ("e não paga o risco do empresário?", R)), fs=40)
slide(at(10), st(("O pró-labore paga o seu trabalho.", B), ("O seu risco quem paga", R), ("é o lucro que volta pra você.", R))
            + st(("Dono que vive só de pró-labore", B), ("é funcionário da própria empresa,", R), ("com a casa em jogo.", R)), fs=40)
slide(at(11), st(("Ninguém sabe como o Brasil vai estar", B), ("daqui a dois anos.", B), ("Eu também não sei.", B))
            + st(("Por isso o seu risco tem que ser pago", B), ("todo ano, enquanto a empresa está de pé.", R)), fs=40)
slide(at(12), st(("No meu treinamento eu ensino gestão.", B), ("Porque é gestão que faz a empresa pagar", B), ("a folha, o banco e o governo", B))
            + st(("e ainda pagar o dono", B), ("pelo risco que ele corre.", R)), fs=40)
slide(at(13), st(("O seu risco tem preço.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">GARANTIA</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=48)
