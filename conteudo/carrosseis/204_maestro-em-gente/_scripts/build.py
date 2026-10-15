#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 204 (editorial-punch, "Maestro em gente").
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
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

slide(at(1),  st(("Pra quem tem empresa, só existem", B))
            + st(("DOIS CAMINHOS.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Ou você aprende a construir resultado", B), ("através das outras pessoas.", B))
            + st(("Ou você vai passar a vida inteira", B), ("trabalhando para os outros.", R)), fs=42)
slide(at(3),  st(("E não precisa de carteira assinada pra isso.", B), ("Tem dono com 50 funcionários", B))
            + st(("que é o empregado mais ocupado", B), ("da própria empresa.", R)), fs=42)
slide(at(4),  st(("Todo orçamento, toda reclamação,", B), ("toda contratação passa pela mão dele.", B))
            + st(("O telefone não para.", B), ("E ele chama isso de ser dono.", R)), fs=42)
slide(at(5),  st(("Só que a empresa, quanto maior fica,", B), ("mais precisa de gente.", B))
            + st(("Mais cliente, mais entrega, mais operação.", B), ("E nada disso cabe numa pessoa só.", R)), fs=42)
slide(at(6),  st(("Sem gente formada, a sua empresa", B))
            + st(("TEM O TAMANHO", A), ("DA SUA AGENDA.", A), mt=22), fs=46)
slide(at(7),  st(("Eu passei a vida inteira", B), ("dependendo de gente.", B))
            + st(("E aprendi que quem reclama de gente", B), ("ainda não sabe trabalhar com gente.", R)), fs=44)
slide(at(8),  st(("O dono que não sabe olha pro time e pensa:", B), ("ninguém faz do jeito que eu faço.", B))
            + st(("Então ele faz. E cada coisa que ele faz", B), ("é uma pessoa que ele deixou de formar.", R)), fs=40)
slide(at(9),  st(("Vai a vida inteira assumindo tudo,", B), ("tentando dar conta de tudo.", B))
            + st(("E a empresa para de crescer", B), ("no limite do que ele aguenta.", R)), fs=44)
slide(at(10), st(("No final das contas,", B), ("a única coisa que ele ganha", B))
            + st(("É UM BURNOUT.", A), mt=22), fs=46)
slide(at(11), st(("Por isso o trabalho do dono é formar gente.", B), ("Gente boa, gente capacitada.", B))
            + st(("Gente que faz a coisa acontecer", B), ("sem precisar ligar pra ele.", R)), fs=42)
slide(at(12), st(("Eu chamo isso de", B), ("virar maestro em gente.", B))
            + st(("O maestro não toca nenhum instrumento.", B), ("E a música só acontece por causa dele.", R)), fs=42)
slide(at(13), st(("Por isso eu repito em toda turma:", B))
            + st(("QUEM NÃO ENTENDE", A), ("DE PESSOAS", A), ("NÃO ENTENDE", A), ("DE NEGÓCIOS.", A), mt=22), fs=46)
slide(at(14), st(("No MBV, o meu treinamento,", B), ("eu ensino gestão pra dono de PME:", B))
            + st(("Lucratividade, Crescimento e Cultura", B), ("pra empresa fazer resultado", R), ("através de gente.", R)), fs=42)
slide(at(15), st(("Escolha o caminho de quem constrói.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">MAESTRO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=44)
