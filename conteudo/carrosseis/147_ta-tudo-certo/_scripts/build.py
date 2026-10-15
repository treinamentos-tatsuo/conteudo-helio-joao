#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 147 (editorial-punch, "Ta tudo certo, chefe").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {6: "15% bottom"}
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
  .anton .oq{ margin-left:-0.466em; } .anton .cq{ margin-right:-0.466em; }
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

Q1, Q2 = '<span class="oq">&ldquo;</span>', '<span class="cq">&rdquo;</span>'
slide(at(1),  st(("Empresa não avisa quando estraga.", B)) + st(("ELA APODRECE ONDE", A), ("O DONO NÃO CONFERE.", A), mt=10), top=280, fs=48)
slide(at(2),  st(("O estoque que ninguém conta.", B), ("O fiado que ninguém cobra.", B), ("O preço que ninguém mexe faz um ano.", B))
            + st(("Tudo isso custando dinheiro todo dia.", R)))
slide(at(3),  st(("Tem uma frase que engana", B), ("dono amador todo dia:", B))
            + st((f"{Q1}TÁ TUDO CERTO, CHEFE.{Q2}", A), mt=14))
slide(at(4),  st(("Tá tudo certo até o fornecedor ligar cobrando.", B), ("Até o cliente bom sumir.", B), ("Até aparecer o buraco no caixa.", R)), fs=40)
slide(at(5),  st(("Eu sei como é:", B))
            + st(("você entrega uma parte pra alguém", R), ("de confiança e vai cuidar do resto.", R)))
slide(at(6),  st(("Só que delegar sem acompanhar é pôr", B), ("o feijão na pressão e ir tomar banho.", B))
            + st(("Quando o cheiro chega em você, já queimou.", R)), fs=42)
slide(at(7),  st(("Presta atenção, porque essa dica vale ouro:", B))
            + st(("Gente, qualquer gente, só cumpre", B), ("o combinado quando alguém confere.", R)), fs=42)
slide(at(8),  st(("Carro que ninguém revisa, quebra.", B), ("Dente que ninguém trata, vira canal.", B))
            + st(("E tarefa que ninguém acompanha", R), ("não fica do jeito que você combinou.", R)))
slide(at(9),  st(("Dono não deve fazer tudo.", B)) + st(("MAS DEVE CONFERIR TUDO.", A), mt=14))
slide(at(10), st(("Conferir tem dia e hora marcados:", B), ("todo dia, toda semana.", B))
            + st(("Até o time saber", B), ("que você vai perguntar.", R)))
slide(at(11), st(("Isso tem nome: RITO.", R))
            + st((f"Aí o &ldquo;tá tudo certo, chefe&rdquo; volta a valer.", B), ("Porque agora ele chega com número do lado.", R)), fs=42)
slide(at(12), st(("Só que rito sem número", B), ("vira reunião de &ldquo;tá tudo certo, chefe&rdquo;.", R))
            + st(("E a maioria dos donos nem sabe", B), ("qual número tinha que estar na mesa.", B)))
slide(at(13), st(("Seja sincero, você sabe hoje", R), ("onde a sua empresa está apodrecendo?", R)))
slide(at(14), st(("Eu tenho uma aula onde você faz o raio-x dela:", B), ("o que entra, o que sai e onde o dinheiro vaza.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">RAIO-X</span></div>\n'
            + st(("que eu te mando a aula no direct.", B), mt=6), fs=38)
