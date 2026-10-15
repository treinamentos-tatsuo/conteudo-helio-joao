#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 180 (editorial-punch, "A folha paga duas vezes").
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
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.24; letter-spacing:0.5px; color:#A91C20; }
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
slide(at(1),  st(("Folha de 40 funcionários.", B)) + st(("E O SERVIÇO VOLTA", A), ("TODO PRA MESA", A), ("DO DONO.", A), mt=10), top=280, fs=48)
slide(at(2),  st(("Você contratou um gerente de 15 mil.", B), ("Quem fecha o preço ainda é você.", B))
            + st(("Contratou um financeiro. E quem confere", B), ("o caixa às dez da noite é você.", R)), fs=42)
slide(at(3),  st(("Você paga o salário", B), ("e faz o serviço.", B))
            + st(("Paga a folha duas vezes:", B), ("uma em dinheiro, outra com seu tempo.", R)))
slide(at(4),  st(("E a conclusão vem pronta:", B), (f"{Q1}ninguém faz direito, é mais rápido eu fazer.{Q2}", B))
            + st(("Mais rápido hoje.", B), ("Amanhã o serviço volta pra sua mesa.", R)), fs=40)
slide(at(5),  st(("Agora me responde: alguém escreveu", B), ("o que ele foi contratado pra entregar?", B))
            + st(("Alguém treinou?", B), ("Alguém confere todo dia?", R)), fs=42)
slide(at(6),  st(("Ele não faz o que foi contratado pra fazer", B)) + st(("PORQUE NINGUÉM", A), ("DISSE O QUE ERA.", A), mt=14), fs=42)
slide(at(7),  st(("Isso não é preguiça do time.", B), ("É empresa sem gestão.", B))
            + st(("Gente adivinhando o que o dono quer", B), ("e um dono consertando o que saiu errado.", R)), fs=42)
slide(at(8),  st(("E enquanto você conserta o serviço", B), ("dos outros, ninguém faz o seu.", B))
            + st(("Ninguém lê o número, ninguém revisa", B), ("a margem, ninguém decide", R), ("pra onde a empresa vai.", R)), fs=42)
slide(at(9),  st(("Dono que faz o serviço do time", B)) + st(("DEIXA O SERVIÇO", A), ("DE DONO", A), ("SEM NINGUÉM.", A), mt=14))
slide(at(10), st(("Aí você tenta soltar: entrega a tarefa e some.", B), ("Em dois meses, está tudo de volta na sua mesa.", B))
            + st(("Isso não é delegar.", B), ("É delargar.", R)), fs=40)
slide(at(11), st(("Delegar é escrever o que a função entrega", B), ("e treinar quem vai fazer.", B))
            + st(("É acompanhar todo dia até o serviço", B), ("sair sem você precisar refazer.", R)), fs=42)
slide(at(12), st(("Aí cada um faz o que foi contratado pra fazer.", B), ("E a sua hora volta pro lugar dela:", B))
            + st(("o número, a margem,", R), ("o rumo da empresa.", R)), fs=40)
slide(at(13), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino gestão.", B))
            + st(("Porque é gestão que faz cada um entregar", B), ("o que foi contratado pra entregar.", R)), fs=42)
slide(at(14), '      <div class="cta-big">Comenta <span class="red">ENTREGA</span></div>\n'
            + st(("que eu te mando o link", B), ("e você para de pagar a folha duas vezes.", R), mt=10), fs=42)
