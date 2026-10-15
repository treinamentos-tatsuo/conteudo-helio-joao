#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 115 (editorial-punch, "Todas as vezes").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; capa setup serif + grito Anton)."""
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

slide(at(1),  st(("Quantas vezes eu tenho", B), ("que falar a mesma coisa?", B)) + st(("TODAS.", A), mt=44), top=280, fs=54)
slide(at(2),  st(("Você falou na segunda, mostrou na quarta", B), ("E na sexta o cliente esperou de novo.", B))
            + st(("Ninguém foi atender.", B), ("E ninguém deu nem bom dia.", R)), fs=42)
slide(at(3),  st(("Aí você conclui o que todo dono conclui:", B), ("Ninguém quer nada com nada.", B))
            + st(("E então para de corrigir.", R)), fs=42)
slide(at(4),  st(("Só que no dia que você para,", B), ("a cultura para junto.", R)))
slide(at(5),  st(("Cultura não é o que você fala.", B))
            + st(("É o que você repete até ninguém mais", B), ("precisar pensar para fazer.", R)), fs=42)
slide(at(6),  st(("Hoje você não pensa pra trocar a marcha.", B), ("Um dia pensou, errou e repetiu.", B))
            + st(("E hoje a mão vai sozinha.", B), ("É isso que você quer do seu time.", R)), fs=42)
slide(at(7),  st(("QUEM REPETE", A), ("CONSTANTEMENTE", A), ("FAZ A CULTURA", A), ("ENTRAR NA MENTE.", A)))
slide(at(8),  st(("A bronca vem depois do erro,", B), ("do jeito que a raiva mandou.", B))
            + st(("O rito vem antes do erro.", B), ("Mesma hora, mesmo jeito, todo dia.", R)), fs=42)
slide(at(9),  st(("Sem rito, o funcionário novo entra na empresa", B), ("e fica do lado de fora da cultura.", B))
            + st(("Entra na folha de pagamento.", B), ("Mas na cultura, não.", R)), fs=40)
slide(at(10), st(("Empresa com DNA", B), ("não é a que tem dono que acredita.", B), ("É a que tem dono que repete.", R))
            + st(("Cansa? Cansa.", B), ("Mas repetir é papel do dono.", B)), fs=42)
slide(at(11), st(("TIME CUMPRINDO", A), ("O COMBINADO TODO DIA", A), ("É OBRA DE REPETIÇÃO.", A)))
slide(at(12), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino a montar esse rito:", B))
            + st(("o que repetir, a que hora, de que jeito,", B), ("até o time fazer certo sem você em cima.", R)), fs=42)
slide(at(13), st(("Time que faz certo sem ninguém olhar", B), ("não nasce pronto. É repetido até nascer.", R))
            + '      <div class="cta-big" style="margin-top:40px">Comenta <span class="red">AUTOMATICO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", B), mt=12), fs=42)
