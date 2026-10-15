#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 127 (editorial-punch, "Para de trabalhar").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
QW = 0.0  # largura da aspa serif (quotewidth.js), em em
try: QW = json.loads((SCR/"quotewidth.json").read_text())["em"]
except Exception: pass
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
  .oq{ margin-left:-QWem; } .cq{ margin-right:-QWem; }
</style>
</head>
<body>
""".replace("QW", f"{QW:.3f}")
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

slide(at(1),  st(("Vou te falar uma verdade meio chata:", B), ("VOCÊ TRABALHA DEMAIS", A), ("E COMANDA DE MENOS.", A)), top=280, fs=44)
slide(at(2),  st(("Você chega às sete e sai às nove.", B), ("Atende, cobra, entrega, resolve.", B))
            + st(("Virou o melhor funcionário da sua empresa.", B), ("E o pior dono.", R)), fs=40)
slide(at(3),  st(("Tudo passa por você.", B), ("O pedido, o cliente bravo, o boleto, a folha.", B))
            + st(("Você chama isso de dedicação.", B), ("Eu chamo de gargalo.", R)), fs=40)
slide(at(4),  st(("Quem fecha a venda? Você.", B), ("Quem confere o caixa? Você.", B), ("Quem resolve o cliente? Você.", B))
            + st(("Quem pensa na empresa?", B), ("Ninguém. Você não tem tempo.", R)), fs=40)
slide(at(5),  st(("Você é o motor da sua empresa.", B))
            + st(("MOTOR NÃO ESCOLHE", A), ("PRA ONDE VAI.", A)), fs=44)
slide(at(6),  st(("Quem escolhe é o volante.", B), ("E o volante da sua empresa está sem ninguém.", B))
            + st(("Ela anda. Anda muito.", B), ("Só não sabe pra onde.", R)), fs=40)
slide(at(7),  st(("Dono não é quem mais trabalha.", B), ("É quem decide, mede e cobra.", B))
            + st(("Trabalhar é fazer.", B), ("Comandar é fazer acontecer", R), ("através dos outros.", R)), fs=40)
slide(at(8),  st(("Empresa não precisa de mais um braço.", B), ("Braço se contrata.", B))
            + st(("Precisa de uma cabeça.", B), ("E essa não se contrata. É a sua.", R)), fs=40)
slide(at(9),  st(("Você bate ponto igual funcionário.", B), ("Sem folga, sem férias, sem o salário.", B))
            + st(("DONO NÃO PODE SER CLT", A), ("DA PRÓPRIA EMPRESA.", A)), fs=40)
slide(at(10), st(("Sai do balcão e senta no volante.", B), ("Número na mão, meta no time,", B), ("cobrança na rotina.", B))
            + st(("No começo a empresa anda mais devagar.", B), ("Depois anda sem você.", R)), fs=40)
slide(at(11), st(("Mas ninguém assume um volante", B), ("sem conhecer o carro.", B), ("Quanto entra, quanto sai, onde vaza.", B))
            + st(("Antes de dirigir,", B), ("você precisa de um raio-x da sua empresa.", R)), fs=40)
slide(at(12), '      <div class="cta-big">Comenta <span class="red">RAIO-X</span></div>\n'
            + st(("que eu te mando a aula em que você faz", R), ("o raio-x da sua empresa e enxerga o carro", R), ("antes de assumir o volante.", R), mt=24), fs=40)
