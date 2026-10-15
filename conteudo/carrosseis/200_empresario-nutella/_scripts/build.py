#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 200 (editorial-punch, "Empresário Nutella").
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif; Anton só nos gritos)."""
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
  .oq{ margin-left:-0.466em; } .cq{ margin-right:-0.466em; }
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
OQ, CQ = '<span class="oq">&ldquo;</span>', '<span class="cq">&rdquo;</span>'

slide(at(1),  st(("Não é o governo. Não é o funcionário.", B))
            + st(("O FRACO DA SUA", A), ("EMPRESA É VOCÊ.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Você reclama do funcionário que não quer", B), ("nada com nada, do juro, do imposto, de Brasília.", B))
            + st(("Reclama de tudo.", B), ("Menos de quem assina a folha.", R)), fs=40)
slide(at(3),  st(("Fatura 20 milhões, tem 60 funcionários", B), ("e se faz de vítima da própria empresa.", B))
            + st(("No fundo, no fundo, você sabe.", B), ("Só não tem coragem de admitir.", R)), fs=42)
slide(at(4),  st(("Reclamar é de graça.", B), ("Assumir é que custa.", B))
            + st(("Custa ver a margem que caiu", B), ("e engolir que a decisão errada foi sua.", R)), fs=42)
slide(at(5),  st(("Você quer o carro, o pró-labore de 50 mil", B), ("e o título de dono.", B))
            + st(("Só não quer o peso.", B), ("E isso tem nome.", R)), fs=42)
slide(at(6),  st(("Quem espera resultado sem pagar o preço.", B))
            + st(("É O EMPRESÁRIO", A), ("NUTELLA.", A), mt=22), fs=44)
slide(at(7),  st(("A demissão difícil, você empurra pro RH.", B), ("A meta furada, cobra no WhatsApp.", B))
            + st(("E a decisão que ninguém quer tomar", B), ("fica pra depois do feriado.", R)), fs=42)
slide(at(8),  st(("O seu melhor vendedor vê tudo isso.", B))
            + st(("E NINGUÉM BOM FICA", A), ("COM LÍDER FROUXO.", A), mt=22), fs=44)
slide(at(9),  st(("Porque quem é bom tem opção:", B), ("sai daqui e já tem outro emprego.", B))
            + st(("Quando vê o dono fugindo da decisão,", B), ("ele não reclama. Pede as contas.", R)), fs=42)
slide(at(10), st(("Fica quem não tem pra onde ir.", B), (f"E você reclama: &ldquo;ninguém mais quer trabalhar&rdquo;.", B))
            + st(("Mas foi o seu jeito de liderar", B), ("que escolheu quem ficou.", R)), fs=40)
slide(at(11), st(("Gente boa segue dono que pulsa a empresa.", B))
            + st(("Dono que faz o time pensar:", B), (f"{OQ}com esse cara eu vou mais longe{CQ}.", R)), fs=42)
slide(at(12), st(("Ser dono não é título.", B))
            + st(("É O PESO", A), ("QUE NINGUÉM CARREGA", A), ("POR VOCÊ.", A), mt=22), fs=46)
slide(at(13), st(("Quem não tem o número na mão", B), ("sempre acha um culpado lá fora.", B))
            + st(("Dono de verdade sabe onde a margem vazou", B), ("e cobra o responsável na segunda.", R)), fs=40)
slide(at(14), st(("No MBV, o meu treinamento", B), ("de gestão pra dono de PME,", B))
            + st(("eu ensino Lucratividade, Crescimento e Cultura", B), ("com número na mão e rito toda semana.", R)), fs=40)
slide(at(15), st(("Nutella reclama.", B), ("Dono de verdade tem pulso.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PULSO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
