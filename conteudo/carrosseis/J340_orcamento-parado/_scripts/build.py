#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel J340 (editorial-punch, "Abre a gaveta de orçamentos", 08/11).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text(encoding='utf-8')).items()}
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
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.36; letter-spacing:0.5px; color:#A91C20; }
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
    (OUT / f"slide-{n:02d}.html").write_text(html, encoding='utf-8'); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n
slide(at(1),  st(("Antes de mandar o time", B), ("atrás de cliente novo,", B))
            + st(("ABRE A GAVETA", A), ("DE ORÇAMENTOS.", A), mt=18), top=220, fs=52)
slide(at(2),  st(("O cliente pediu o preço,", B), ("ouviu o valor e disse:", B), ("“vou pensar”.", B))
            + st(("E ninguém ligou de volta.", R)), top=280, fs=54)
slide(at(3),  st(("Um aluno meu descobriu", B), ("setenta orçamentos parados", B), ("na empresa dele.", B))
            + st(("Setenta clientes que já tinham", R), ("levantado a mão.", R)), top=280, fs=52)
slide(at(4),  st(("O vendedor passou o preço", B), ("e foi atrás do próximo.", B))
            + st(("E ninguém mandou ele voltar.", R)), top=280, fs=54)
slide(at(5),  st(("Aí, no meio do mês,", B), ("o dono manda o time", B), ("buscar cliente novo.", B))
            + st(("Bater em quarenta portas", R), ("pra dez atenderem.", R)), top=280, fs=52)
slide(at(6),  st(("Enquanto isso, quem já pediu preço", B), ("esfria na gaveta.", B))
            + st(("A venda mais barata é a que", R), ("já está no seu funil.", R)), top=280, fs=50)
slide(at(7),  st(("Por isso, toda segunda-feira,", B), ("eu olho o funil com o time.", B))
            + st(("Quantos negócios estão abertos", R), ("e quais estão parados.", R)), top=280, fs=52)
slide(at(8),  st(("Pra cada orçamento parado,", B), ("eu faço uma pergunta só.", B))
            + st(("Quem liga, e até quando?", R)), top=280, fs=56)
slide(at(9),  st(("Porque o time não faz", B), ("follow-up sozinho.", B))
            + st(("Ou alguém acompanha,", R), ("ou o orçamento morre.", R)), top=280, fs=56)
slide(at(10), st(("O mês ainda tem três semanas.", B), ("E a venda mais rápida delas", B))
            + st(("já pediu orçamento", R), ("pra você.", R)), top=280, fs=54)
slide(at(11), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV,", B))
            + st(("onde eu ensino a acompanhar o funil", B), ("antes que o mês acabe.", R)), top=300, fs=46)
slide(at(12), st(("Quer um time que volta", B), ("em todo orçamento?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">FUNIL</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), top=300, fs=50)
