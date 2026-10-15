#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 122 (editorial-punch, "Lenha no seu funcionario").
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

slide(at(1),  st(("Escuta o conselho:", B), ("LENHA NO SEU", A), ("FUNCIONÁRIO.", A)), top=280, fs=48)
slide(at(2),  st(("Calma. Ninguém está mandando", B), ("bater em ninguém. Nem explorar.", B))
            + st(("É o contrário.", B), ("Lenha é o que você põe na fogueira", R), ("antes de exigir calor dela.", R)), fs=40)
slide(at(3),  st(("Você quer fogo?", B), ("Quer comprometimento, atitude, garra?", R)), fs=46)
slide(at(4),  st(("Pois 8 horas por dia ele passa com você.", B), ("E o que você faz por ele nessas 8 horas?", R)), fs=42)
slide(at(5),  st(("Você dá ordem. Dá bronca. Dá meta.", B), ("E chama isso de gerir o time.", B))
            + st(("Ordem não é lenha.", B), ("É sopro em cima de cinza.", R)), fs=42)
slide(at(6),  st(("Você cobra calor de um time", R), ("que nunca alimentou.", R))
            + st(("É como sentar na frente de uma lareira apagada", B), ("esperando que ela te esquente.", B)), fs=40)
slide(at(7),  st(("Lenha é sentar do lado e mostrar como faz.", B), ("É o porquê antes da ordem.", B))
            + st(("A meta que ele entende.", B), ("O degrau seguinte que ele enxerga.", B))
            + st(("É a realização dos sonhos dele", R), ("através da sua empresa.", R)), fs=40)
slide(at(8),  st(("Lenha é treinamento que repete.", B), ("Hoje, amanhã, depois de amanhã.", B))
            + st(("Porque fogo não nasce no dia do treinamento.", B), ("Nasce no dia a dia,", R), ("tarefa por tarefa, rito por rito.", R)), fs=40)
slide(at(9),  st(("Cobrança de comprometimento não existe.", B), ("Ninguém se compromete por ordem.", B))
            + st(("Se compromete porque quer.", B), ("E quer quando o combustível veio antes.", R)), fs=40)
slide(at(10), st(("LENHA PRIMEIRO.", A), ("CALOR DEPOIS.", A))
            + st(("Assim que se constrói cultura.", B)), fs=42)
slide(at(11), st(("Time com lenha não precisa de vigia.", B), ("O fogo se espalha sozinho.", R))
            + st(("O erro é corrigido antes de você ver.", B), ("A meta, batida antes de você cobrar.", B)), fs=40)
slide(at(12), st(("E se, com lenha, o fogo não pega?", R))
            + st(("Aí não é falta de lenha, é fogueira apagada", B), ("e isso não tem lenha que resolva.", B)), fs=40)
slide(at(13), st(("Porque motivação é obra sua,", B), ("mas caráter vem de casa.", B), ("Um você acende. O outro você seleciona.", B))
            + st(("Quem confunde os dois", B), ("passa a vida soprando cinza.", R)), fs=40)
slide(at(14), st(("Lenha todo dia não é bom coração.", B), ("É ROTINA DE GESTÃO.", A))
            + st(("Tem hora, tem método, tem cobrança.", B), ("E rotina, eu ensino a montar.", R)), fs=42)
slide(at(15), '      <div class="cta-big">Comenta <span class="red">LENHA</span></div>\n'
            + st(("que eu te mostro como incendiar", R), ("a cultura da sua empresa.", R), mt=24))
