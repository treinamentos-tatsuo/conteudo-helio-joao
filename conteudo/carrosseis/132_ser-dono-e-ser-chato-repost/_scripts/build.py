#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 132 (editorial-punch, repost "Ser dono é ser chato" / CHATO).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {4: "left bottom"}  # slide 4: preservar a mao da esquerda e a lasca
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

slide(at(1),  st(("Vou te falar uma verdade", B), ("que ninguém gosta de ouvir:", B))
            + st(("SER DONO", A), ("É SER CHATO.", A)), top=280, fs=48)
slide(at(2),  st(("Se você quer ser amado por todo mundo,", B), ("abre um bar.", B))
            + st(("Empresa não é", B), ("concurso de popularidade.", R)), fs=42)
slide(at(3),  st(("Ser dono é cobrar resultado.", B), ("É perguntar de novo. É pedir número.", B))
            + st(("É não aceitar \u201cmais ou menos\u201d.", B), ("E fazer isso todo santo dia.", R)), fs=42)
slide(at(4),  st(("É acompanhar o combinado.", B), ("Combinado que não é acompanhado", B))
            + st(("vira sugestão.", B), ("E sugestão não fecha a conta.", R)), fs=42)
slide(at(5),  st(("Ser dono é treinar a equipe.", B))
            + st(("De novo. E de novo. E de novo.", B), ("Até o padrão subir.", R)))
slide(at(6),  st(("É ficar em cima? É.", B), ("No começo ninguém faz melhor", B))
            + st(("do que você imagina.", B), ("E cultura não nasce sozinha.", R)), fs=42)
slide(at(7),  st(("Se você é o dono que quer ser amigo", B), ("de todo mundo, precisa entender de uma vez:", B))
            + st(("Você não foi feito para ser amigo.", B))
            + st(("VOCÊ FOI FEITO", A), ("PARA COMANDAR.", A)), fs=40)
slide(at(8),  st(("E comandar exige coragem.", B))
            + st(("Coragem de corrigir.", B), ("Coragem de confrontar.", B), ("Coragem de exigir.", R)))
slide(at(9),  st(("Na maioria das vezes a cultura da empresa", B), ("é reflexo do dono.", B))
            + st(("Baixo padrão no dono", B), ("vira baixo padrão na empresa.", R)), fs=42)
slide(at(10), st(("Se você tolera atraso, vai ter atraso.", B), ("Se você tolera desculpa, vai ter desculpa.", B))
            + st(("Se você tolera mediocridade,", B), ("vai ter mediocridade.", R)), fs=40)
slide(at(11), st(("Ser dono é ser chato mesmo.", B), ("É cobrar. É acompanhar. É treinar.", B))
            + st(("É garantir que o combinado", B), ("seja cumprido.", R)))
slide(at(12), st(("Porque tudo começa pelo dono.", B), ("Se você não assume o comando,", B))
            + st(("alguém assume no seu lugar.", B), ("E normalmente... não é do jeito certo.", R)), fs=42)
slide(at(13), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino a montar isso:", B))
            + st(("o rito de cobrar, acompanhar e treinar", B), ("até o combinado ser cumprido todo dia.", R)), fs=42)
slide(at(14), st(("Se você quer resultado, assuma o comando.", B), ("O resto continua reclamando do time.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">CHATO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24), fs=42)
