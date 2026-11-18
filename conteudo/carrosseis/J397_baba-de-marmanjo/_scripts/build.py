#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel J397 (editorial-punch, "Todo lider e baba de marmanjo", 16/11).
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
W = '      <div class="line" style="font-size:32px;font-weight:400;margin-top:24px">E não foi barato.</div>\n'
slide(at(1),  st(("TODO LÍDER É", A), ("BABÁ DE MARMANJO.", A)), top=230)
slide(at(2),  st(("Você pagou curso", B), ("pro time inteiro.", B))
            + st(("Na segunda-feira,", R), ("ninguém lembrava de nada.", R)) + W, top=260, fs=54)
slide(at(3),  st(("Foi um dia bonito.", B), ("Todo mundo balançando a cabeça.", B))
            + st(("Encheram o caderno.", R), ("Juraram que ia mudar.", R)), top=280, fs=52)
slide(at(4),  st(("Uma semana depois, cada um", B), ("tinha voltado pro jeito antigo.", B))
            + st(("O caderno sumiu na mochila.", R), ("A promessa ficou no estacionamento.", R)), top=260, fs=46)
slide(at(5),  st(("Aí vem a conclusão de sempre:", B), ("treinamento é dinheiro jogado no lixo.", B))
            + st(("E <span class=\"red\">o culpado</span> é esse", B), ("time que não aprende.", B)), top=280, fs=50)
slide(at(6),  st(("O treinamento fez a parte dele.", B), ("O seu time é gente como qualquer um.", B))
            + st(("Faltou alguém conferir, na segunda,", B), ("se o que foi ensinado", B), ("estava sendo feito.", B))
            + st(("NINGUÉM CUIDOU", A), ("DO DIA SEGUINTE.", A), mt=10), top=220, fs=46)
slide(at(7),  st(("Ninguém ouve uma vez", B), ("e muda pro resto da vida.", B))
            + st(("Ninguém sai de um treinamento", B), ("acertando tudo na segunda.", B))
            + st(("Gente é assim. Você também.", R)), top=240, fs=50)
slide(at(8),  st(("Tem quem chame esse trabalho", B), ("de acompanhamento.", B))
            + st(("Eu chamo pelo nome:", R), ("pajear adulto.", R)), top=280, fs=54)
slide(at(9),  st(("Você fica bravo de falar de novo.", B), ("“Eu já expliquei 100 vezes.”", B))
            + st(("Explicou. E amanhã vai", R), ("explicar pela 101ª vez.", R)), top=280, fs=48)
slide(at(10), st(("Avisar uma vez,", B), ("qualquer um avisa.", B))
            + st(("CONFERIR TODO DIA", A), ("É GESTÃO.", A), mt=10), top=260, fs=56)
slide(at(11), st(("O combinado conferido todo dia", B), ("uma hora vira costume.", B))
            + st(("E a empresa anda certa", R), ("até no dia em que você não está.", R)), top=280, fs=48)
slide(at(12), st(("Começa pelo básico:", B), ("põe o combinado no papel.", B))
            + st(("E confere com o seu time", R), ("todo santo dia.", R)), top=280, fs=54)
slide(at(13), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV.", B))
            + st(("E um dos pilares é a cultura:", B), ("o que faz o combinado", R), ("virar o jeito da casa.", R)), top=290, fs=46)
slide(at(14), '      <div class="cta-big">Comenta <span class="red">ENTREGA</span></div>\n'
            + st(("que eu te mostro como fazer", B), ("o seu time entregar", B), ("o combinado todo dia.", B), mt=26), top=300, fs=50)
