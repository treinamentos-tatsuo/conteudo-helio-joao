#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 100 (editorial-punch, repost "Você paga mediano... Cabeça de Dono").
Layout da skill (calibragem registrada em erros-frequentes 04/09: corpo top 200, capa 240; Source Serif 44; Anton nos gritos)."""
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
def slide(n, body, top=200, fs=None):
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

slide(at(1),  st(("Você paga mediano...", B), ("ENTREGA ESTRUTURA MEDIANA...", A)), top=240, fs=52)
slide(at(2),  st(("E espera que seu funcionário tenha", B), ("“CABEÇA DE DONO”", A)) + st(("kkkkk", R)))
slide(at(3),  st(("Todo empresário", B), ("reclama da equipe:", R)))
slide(at(4),  st(("“Meu funcionário é fraco.”", B), ("“Só faz o básico.”", B), ("“Não tem atitude.”", B)) + st(("Mas a verdade?", R)))
slide(at(5),  st(("VOCÊ ATRAI", A), ("O QUE CONSTRÓI.", A)))
slide(at(6),  st(("Gente boa custa caro,", B), ("não só no salário.", B)) + st(("Custa visão, ambiente,", B), ("clareza, comando.", R)))
slide(at(7),  st(("Gente boa não aceita trabalhar", B), ("em empresa desorganizada", B), ("com chefe confuso.", R)))
slide(at(8),  st(("QUER TALENTO?", A)) + st(("Ofereça mais do que “fixo + comissão”.", B), ("Ofereça liderança de verdade.", B), ("Ofereça desafio com direção.", R)), fs=42)
slide(at(9),  st(("Você NÃO colhe o time que deseja.", B)) + st(("Você colhe o time que", B), ("sua liderança é capaz de formar.", R)))
slide(at(10), st(("Se sua empresa", B), ("só tem gente mediana...", B)))
slide(at(11), st(("TALVEZ O MEDIANO", A), ("SEJA VOCÊ.", A)))
slide(at(12), st(("A equipe é reflexo direto", B), ("de quem comanda.", R)))
slide(at(13), st(("Antes de trocar mais um funcionário,", B), ("descubra o que a sua empresa está formando.", R)), fs=42)
slide(at(14), st(("Eu ofereço um diagnóstico gratuito", B), ("da sua empresa com um especialista", B), ("da minha equipe.", B))
            + st(("Ele te mostra onde a sua estrutura", B), ("está formando o time que você reclama.", R)), fs=42)
slide(at(15), '      <div class="cta-big">Comenta <span class="red">DIAGNÓSTICO</span></div>\n'
            + st(("e eu te mando o link no seu direct", R), ("pra agendar o seu diagnóstico.", R), mt=24))
