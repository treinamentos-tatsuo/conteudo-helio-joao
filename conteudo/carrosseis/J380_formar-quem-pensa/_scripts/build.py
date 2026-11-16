#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel J341 (editorial-punch, "Que dia você começa a lucrar", 08/11).
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
slide(at(1),  st(("Cobrar todo mundo cobra.", B))
            + st(("LIDERAR É OUTRA COISA.", A), mt=18), top=230, fs=56)
slide(at(2),  st(("Quem só cobra meta, prazo", B), ("e entrega não está liderando.", B))
            + st(("Está só fiscalizando.", R)), top=280, fs=54)
slide(at(3),  st(("O trabalho de quem lidera", B), ("de verdade é outro:", B))
            + st(("fazer o time pensar.", R)), top=280, fs=56)
slide(at(4),  st(("Porque é pensando", B), ("que alguém cresce.", B))
            + st(("Amadurece. Ganha autonomia.", R), ("Aprende a decidir.", R)), top=280, fs=54)
slide(at(5),  st(("Quando o líder pensa por todo mundo,", B), ("o time não sai do lugar.", B))
            + st(("Só fica esperando por ele.", R)), top=280, fs=48)
slide(at(6),  st(("Aí o mesmo líder reclama:", B), ("“aqui ninguém resolve nada”.", B), ("Lógico.", B))
            + st(("Você ensinou o time inteiro", R), ("a esperar a sua resposta.", R)), top=260, fs=50)
slide(at(7),  st(("E começa o circo:", B))
            + st(("contrata, demite,", R), ("contrata, demite.", R)), top=280, fs=58)
slide(at(8),  st(("Isso não é gestão.", R))
            + st(("Além de quebrar a cultura,", B), ("você abre com a própria mão", B), ("um rombo na DRE.", B)), top=280, fs=52)
slide(at(9),  st(("Demitir é a última saída.", B))
            + st(("Antes disso, o seu trabalho", R), ("é formar gente.", R)), top=280, fs=56)
slide(at(10), st(("Só que quase ninguém faz isso.", B), ("Sabe por quê?", B))
            + st(("Porque formar gente dá trabalho.", R), ("Muito trabalho.", R)), top=280, fs=50)
slide(at(11), st(("Dá trabalho <span class=\"red\">perguntar</span>", B), ("<span class=\"red\">em vez de responder tudo.</span>", B))
            + st(("Dá trabalho <span class=\"red\">corrigir</span>", B), ("<span class=\"red\">em vez de só reclamar.</span>", B))
            + st(("Dá trabalho <span class=\"red\">acompanhar</span>", B), ("<span class=\"red\">em vez de fazer no lugar.</span>", B)), top=230, fs=46)
slide(at(12), st(("Mas é isso que muda um time.", B), ("Ensinar muda. Acompanhar muda.", B))
            + st(("Cobrança sozinha", R), ("não muda ninguém.", R)), top=280, fs=50)
slide(at(13), st(("Liderança não é crachá.", R))
            + st(("É postura.", B)), top=300, fs=60)
slide(at(14), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV,", B))
            + st(("onde eu ensino a cobrar", B), ("e a formar quem você cobra.", R)), top=290, fs=46)
slide(at(15), st(("Se você quer parar de trocar gente", B), ("e começar a formar gente forte,", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PENSAR</span></div>\n'
            + st(("que eu te mostro como.", B), mt=18), top=290, fs=46)
