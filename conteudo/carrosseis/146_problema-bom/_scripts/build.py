#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 146 (editorial-punch, "Vamos criar um problema bom").
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Anton so nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {9: "20% bottom"}
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
  .oq{ margin-left:-0.43em; } .cq{ margin-right:-0.43em; }
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

# 1-2 capa em isca (padrao 123/75): serif corpo maior, sem Anton
slide(at(1),  st(("Tem um desejo que todo dono", B), ("tem em comum:", B)), top=280, fs=54)
slide(at(2),  st(("ter menos problema.", R)), top=280, fs=54)
slide(at(3),  st(("Mas, amigo, vou te falar uma verdade chata:", B))
            + st(("Problema de dono não acaba.", B), ("Resolveu um, nasce outro no lugar.", R)), fs=42)
slide(at(4),  st(("Isso não é azar. É o cargo.", B))
            + st(("Não romantize a vida do empresário.", B))
            + st(("Ser dono é isso.", R)), fs=44)
slide(at(5),  st(("Então eu não peço menos problema.", B), ("Eu escolho qual problema eu quero ter.", B))
            + st(("É o que eu chamo de", B), ('<span class="oq">“</span>vamos criar um problema bom.<span class="cq">”</span>', R)), fs=42)
slide(at(6),  st(("Problema ruim é máquina parada,", B), ("funcionário esperando pedido,", B))
            + st(("é folha pra pagar", B), ("com o caixa vazio.", R)), fs=44)
slide(at(7),  st(("Problema bom é ter mais pedido", B), ("do que você consegue produzir,", B))
            + st(("é precisar contratar mais gente,", B), ("é o barracão ficando pequeno.", R)), fs=44)
slide(at(8),  st(("Os dois tiram o sono.", B))
            + st(("MAS SÓ UM", A), ("PAGA A CONTA.", A), mt=34), fs=46)
slide(at(9),  st(("Problema bom se resolve com dinheiro:", B), ("contrata, aluga, compra máquina.", B))
            + st(("Problema ruim não tem onde comprar.", B))
            + st(("PORQUE CLIENTE", A), ("NÃO SE CONTRATA.", A)), fs=42)
slide(at(10), st(("E problema bom não cai do céu.", B), ("Ele é fabricado.", B))
            + st(("E só existe uma fábrica", B), ("que produz ele:", R)), fs=44)
slide(at(11), st(("UMA MÁQUINA", A), ("DE VENDAS.", A)))
slide(at(12), st(("A tradução disso é:", B), ("mais gente querendo comprar", B), ("do que você consegue entregar.", B))
            + st(("Demanda infinita.", R)), fs=44)
slide(at(13), st(("Dono que tem máquina de vendas", B), ("escolhe com qual cliente vai trabalhar.", B))
            + st(("Cobra o preço que vale, com margem mais alta.", B), ("E tem mais dinheiro indo pro próprio bolso.", R)), fs=40)
slide(at(14), st(("Se for para perder o sono,", B), ("que seja pelo motivo certo:", B))
            + st(("UM PROBLEMA BOM.", A), mt=34), fs=46)
slide(at(15), st(("Eu tenho um treinamento pra donos", B), ("de pequena e média empresa", B))
            + st(("onde ensino a montar essa máquina.", R)), fs=44)
slide(at(16), st(("Problema você vai ter de qualquer jeito.", B), ("Então vamos criar um problema bom.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PROBLEMA</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24), fs=42)
