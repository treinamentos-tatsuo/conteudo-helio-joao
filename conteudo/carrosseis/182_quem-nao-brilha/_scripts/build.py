#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel 182 (editorial-punch, "Brilho nao se treina").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {4: "40% bottom"}
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
slide(at(1),  st(("Você contratou um cara com brilho no olho.", B)) + st(("EM SEIS MESES, ELE", A), ("FICOU COM A SUA CARA.", A), mt=10), top=280, fs=42)
slide(at(2),  st(("Na entrevista ele chegou", B), ("cheio de ideia e pergunta.", B))
            + st(("Hoje chega às 08:01", B), ("e às 18h em ponto já está no estacionamento.", R)), fs=40)
slide(at(3),  st(("E você conclui o de sempre:", B), (f"{Q1}contratei errado{Q2}.", B))
            + st(("Não contratou. Ele só aprendeu rápido", R), ("como as coisas funcionam aí dentro.", R)), fs=42)
slide(at(4),  st(("Técnica se ensina em semanas.", B)) + st(("BRILHO NÃO SE TREINA.", A), ("SE PEGA.", A), mt=14))
slide(at(5),  st(("Garra, iniciativa, coragem, brilho no olho.", B))
            + st(("Nenhuma apostila ensina isso.", B), ("Quem ensina é o ambiente, todo dia, sem aviso.", R)), fs=40)
slide(at(6),  st(("E o ambiente da sua empresa é a sua cara:", B))
            + st(("o seu humor na segunda, a sua reclamação na copa,", B), (f"o seu &ldquo;deixa assim mesmo&rdquo; no erro de sempre.", R)), fs=38)
slide(at(7),  st(("Ninguém apagou o brilho dele.", B)) + st(("ELE SÓ BAIXOU PRO", A), ("NÍVEL DA CASA.", A), mt=14))
slide(at(8),  st(("Por isso o líder de verdade", B), ("não vive reclamando do time.", B))
            + st(("Ele sabe que o time é reflexo.", B), ("Falar mal do time é falar mal de si mesmo.", R)), fs=42)
slide(at(9),  st(("Brilho de casa se constrói", B), ("igual a qualquer hábito:", B))
            + st(("meta clara, número na mesa toda semana", B), ("e reconhecimento na frente de todo mundo.", R)), fs=42)
slide(at(10), st(("Aí o próximo que chegar com brilho no olho", B), ("não apaga. Acende os outros.", R)), fs=42)
slide(at(11), st(("Eu tenho um treinamento de gestão", B), ("pra pequena e média empresa,", B))
            + st(("inclusive gestão de pessoas,", B), ("cultura e liderança.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">BRILHO</span></div>\n'
            + st(("que eu te mando o link no direct.", B), mt=6))
