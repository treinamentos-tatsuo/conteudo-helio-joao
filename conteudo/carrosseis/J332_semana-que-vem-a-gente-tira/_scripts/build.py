#!/usr/bin/env python3
"""Gera os 9 HTMLs do carrossel J332 (editorial-punch, "Semana que vem a gente tira", 06/11).
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
slide(at(1),  st(("O seu time fechou a semana", B), ("atrás da meta, e o gerente jurou:", B))
            + st(("SEMANA QUE VEM A GENTE TIRA.", A), mt=18), top=280, fs=48)
slide(at(2),  st(("Eu escuto essa promessa há 38 anos.", B), ("O vendedor promete dez ligações, faz três", B), ("e jura que amanhã faz dezessete.", B))
            + st(("E eu sempre respondo:", B), ("quem não fez dez ontem", R), ("não vai fazer dezessete hoje.", R)), fs=42)
slide(at(3),  st(("A diferença não some. Ela só muda de data:", B), ("vai pra amanhã, pra semana que vem,", B), ("pro dia 25.", B))
            + st(("E no dia 30, quando não tem mais", B), ("pra onde empurrar,", B), ("ela vira desconto.", R)), fs=42)
slide(at(4),  st(("É aí que o vendedor liga pro cliente", B), ("oferecendo dez por cento, prazo de", B), ("noventa dias e o frete por sua conta.", B))
            + st(("O mês fecha bonito no painel.", B), ("Você bateu a meta e não sobrou nada.", R)), fs=42)
slide(at(5),  st(("Aí você faz o que todo dono faz", B), ("na última semana: reunião de emergência,", B), ("grito e campanha relâmpago.", B))
            + st(("Cobrança no dia 25 não salva o mês.", B), ("Só escolhe quem vai levar a culpa.", R)), fs=42)
slide(at(6),  st(("Eu faço diferente.", B), ("Peço pro vendedor um número", B), ("que ele bate chova ou faça sol.", B))
            + st(("Nem o que me agrada,", B), ("nem o que é fácil pra ele.", B), ("O número que ele bate,", R), ("e que eu cobro todo dia.", R)), fs=42)
slide(at(7),  st(("Quando ele fica devendo, a conversa", B), ("do dia seguinte é outra: qual cliente", B), ("ele vai ligar, em que horário", B), ("e quem vai ajudar.", B))
            + st(("Porque promessa sem plano", B), ("é só o atraso com data marcada.", R)), fs=42)
slide(at(8),  st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME: o MBV.", B))
            + st(("Lá eu ensino o dono a cobrar o número", B), ("todo dia e a tirar a diferença", B), ("antes que ela vire desconto:", B), ("Lucratividade, Crescimento e Cultura.", R)), fs=42)
slide(at(9),  st(("Quer tirar a diferença na terça-feira,", B), ("e não no dia 30?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PLANO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
