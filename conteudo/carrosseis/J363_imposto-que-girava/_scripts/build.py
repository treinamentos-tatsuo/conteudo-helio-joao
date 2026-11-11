#!/usr/bin/env python3
"""Gera os 10 HTMLs do carrossel J363 (editorial-punch, "O imposto que girava a sua empresa", 11/11).
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
slide(at(1),  '      <div class="stanza">\n'
            '        <div class="line" style="font-size:46px">Em 2027,</div>\n'
            '        <div class="line anton" style="font-size:84px;line-height:1.15">O IMPOSTO VAI SAIR<br>DO SEU CAIXA</div>\n'
            '        <div class="line" style="font-size:46px;margin-top:14px">antes do dinheiro</div>\n'
            '        <div class="line anton" style="font-size:84px;line-height:1.15">CAIR NA SUA CONTA.</div>\n'
            '      </div>\n', top=190)
slide(at(2),  st(("Hoje você vende e recebe.", B))
            + st(("O imposto, você só paga", R), ("semanas depois.", R)), top=260, fs=52)
slide(at(3),  st(("Nesse meio tempo, esse dinheiro", B), ("paga fornecedor e cobre a folha.", B))
            + st(("O imposto está girando", R), ("a sua empresa.", R)), top=260, fs=48)
slide(at(4),  st(("Com o split payment, o imposto sai", B), ("na hora em que o cliente paga.", B))
            + st(("O dinheiro já chega", R), ("sem ele.", R)), top=260, fs=48)
slide(at(5),  st(("Uma consultoria fez a conta:", B))
            + st(("as empresas vão precisar de até", R), ("R$ 117 bilhões a mais de giro.", R)), top=260, fs=50)
slide(at(6),  st(("E onde o dono vai buscar", B), ("esse dinheiro? No banco.", B))
            + st(("Pagando juro pelo que", R), ("antes girava de graça.", R)), top=260, fs=50)
slide(at(7),  st(("Aí o dono culpa o governo.", B), ("Pode até ser.", B))
            + st(("Mas a conta de 2027", R), ("quem paga é você.", R)), top=260, fs=52)
slide(at(8),  st(("O split payment", B), ("não cria o buraco.", B))
            + st(("Ele só mostra", R), ("o buraco.", R)), top=260, fs=56)
slide(at(9),  st(("Quem fechava o mês", B), ("com o dinheiro do imposto", B))
            + st(("nunca teve capital de giro.", R), ("Tinha empréstimo do governo.", R)), top=260, fs=50)
slide(at(10), st(("Me responde: quanto do", B), ("seu caixa hoje é imposto?", B))
            + st(("Se você não sabe,", R), ("2027 vai te contar.", R)), top=260, fs=52)
slide(at(11), st(("Ainda dá tempo", B), ("de fazer essa conta.", B))
            + st(("Quem fizer em 2026 depende", R), ("menos do banco em 2027.", R)), top=260, fs=50)
slide(at(12), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME.", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">FOLEGO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), top=280, fs=48)
