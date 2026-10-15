#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 116 (editorial-punch, "Lenha primeiro").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
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

slide(at(1),  st(("Salário alimenta o bolso.", B), ("A ALMA COME", A), ("OUTRA COISA.", A)), top=280, fs=48)
slide(at(2),  st(("Você paga em dia.", B), ("Vale, hora extra, bônus no mês bom.", B), ("E acha que está quite.", B))
            + st(("Quite com o bolso.", B), ("Com a alma, você nunca pagou um centavo.", R)), fs=40)
slide(at(3),  st(("A alma come reconhecimento.", R)), fs=58)
slide(at(4),  st(("O nome dele dito alto na frente de todos.", B), ("Perspectiva de crescimento.", B), ("Sentir que tem um propósito aí dentro.", B))
            + st(("Tudo isso vale mais", B), ("que 300 reais de aumento.", R)), fs=40)
slide(at(5),  st(("Dinheiro motiva.", B), ("Reconhecimento motiva mais.", B), ("E o dono esquece.", B))
            + st(("Esquece porque ninguém nunca", B), ("fez isso por ele.", R)), fs=42)
slide(at(6),  st(("Dono não ganha parabéns.", B), ("Ganha cobrança do cliente,", B), ("do banco, do time.", B))
            + st(("Aí ele monta uma empresa", B), ("onde ninguém é reconhecido.", R)), fs=42)
slide(at(7),  st(("Ninguém senta na frente", B), ("de uma lareira apagada esperando calor.", B))
            + st(("MAS VOCÊ COBRA CALOR", A), ("DE UM TIME QUE", A), ("NUNCA ALIMENTOU.", A)), fs=40)
slide(at(8),  st(("Não funciona.", B), ("Nem com fogo, nem com gente.", B))
            + st(("Quer comprometimento?", B), ("Faz por ele antes de cobrar dele.", B))
            + st(("Alimente a fogueira", R), ("para receber o calor.", R)), fs=40)
slide(at(9),  st(("Não é elogio solto. É rito.", B), ("Todo mês, na frente de todos,", B), ("o nome de quem entregou.", B))
            + st(("Troféu de plástico, foto no mural.", B), ("Isso segura o time.", R)), fs=40)
slide(at(10), st(('<span class="oq">&ldquo;</span>Parabéns. Você é o cara.<span class="cq">&rdquo;</span>', B), ("Dito na frente de todo mundo.", B))
            + st(("O troféu de dez reais", B), ("que vale mil na mesa dele.", R)), fs=42)
slide(at(11), st(("Gente alimentada não trabalha por favor.", B), ("Trabalha por orgulho.", B))
            + st(("E orgulho não pede", R), ("aumento toda segunda.", R)), fs=42)
slide(at(12), st(("Cobrar todo dia. Reconhecer todo mês.", B), ("Isso não nasce de bom coração.", B))
            + st(("Nasce de rotina.", B), ("E rotina, eu ensino a montar.", R)), fs=42)
slide(at(13), '      <div class="cta-big">Comenta <span class="red">ORGULHO</span></div>\n'
            + st(("e eu te mando os próximos passos.", R), mt=24))
