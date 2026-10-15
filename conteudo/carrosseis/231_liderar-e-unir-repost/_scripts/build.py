#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel 231 (editorial-punch, repost "Liderar não é mandar. É unir.").
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
  .sub{ font-size:36px !important; font-weight:400; color:#1A1A1A; }
  .big{ font-size:58px !important; }
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

# capa: diagramação da capa ORIGINAL (decisão do user 13/10, "ficou boa aquela"), medida no PNG postado:
# frase em serif 700 vermelha numa linha (tinta 300-351, largura 769) + subtítulo serif 400 preto (tinta 408-433)
slide(at(1), '      <div style="font-size:57.5px;font-weight:700;color:#A91C20;line-height:1.2">Liderar não é mandar. É unir.</div>\n'
             '      <div style="font-size:27.6px;font-weight:400;color:#1A1A1A;margin-top:35px">Isso tem nome, e vem de longe.</div>\n', top=299)
slide(at(2),  st(("Liderar pessoas é pegar gente", B), ("completamente diferente.", B))
            + st(("Backgrounds diferentes, metas diferentes,", R), ("habilidades diferentes.", R)), fs=42)
slide(at(3),  st(("E ter a capacidade de unir essas pessoas", B), ("num único objetivo.", R)), fs=44)
slide(at(4),  st(("Isso tem nome. Vem do Japão:", B), ("itaidoshin.", " red big"))
            + st(("Corpos diferentes, irmanados", R), ("em um único pensamento.", R)), fs=44)
slide(at(5),  st(("Não é uniformizar ninguém.", B), ("É gente diferente pensando", R), ("como um só grupo.", R)), fs=44)
slide(at(6),  st(("O verdadeiro teste não é a empresa bater meta.", B))
            + st(("É cada pessoa perceber que,", R), ("alcançando o objetivo da empresa,", R), ("ela alcança o dela também.", R)), fs=42)
slide(at(7),  st(("Enquanto o time enxerga o objetivo", B), ("da empresa como algo de fora,", B))
            + st(("cada um vai puxar pro seu lado.", R)), fs=44)
slide(at(8),  st(("Liderar é fazer esse objetivo", B), ("virar de dentro.", B))
            + st(("De cada um.", R)), fs=46)
slide(at(9),  st(("Não existe itaidoshin por acaso.", B))
            + st(("Existe porque alguém liderou", R), ("pra isso acontecer.", R)), fs=46)
slide(at(10), st(("Eu tenho um treinamento pra donos de empresa,", B), ("onde ensino gestão.", B))
            + st(("E um dos pilares é a cultura:", B), ("o que faz gente diferente puxar pro mesmo lado.", R)), fs=40)
slide(at(11), '      <div class="cta-big">Comenta <span class="red">UNIR</span></div>\n'
            + st(("que eu te mostro como unir o teu time", B), ("num único itaidoshin de verdade.", B), mt=22), fs=44)
