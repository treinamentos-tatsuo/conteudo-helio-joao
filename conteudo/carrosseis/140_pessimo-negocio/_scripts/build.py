#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 140 (editorial-punch, "Péssimo negócio").
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

slide(at(1),  st(("Selic a 14% não quebrou a sua empresa.", B))
            + st(("ELA SÓ MOSTROU QUEM É", A), ("O DONO DO SEU LUCRO.", A), mt=26), top=280, fs=48)
slide(at(2),  st(("Não é falta de venda. Não é o mercado.", B), ("É o modelo econômico do seu negócio.", B))
            + st(("Ele foi montado pra funcionar", B), ("com o dinheiro do banco no meio.", R)), fs=42)
slide(at(3),  st(("Você vende, entrega, cobra, recebe.", B), ("E o primeiro a receber não é você.", B))
            + st(("O banco é o único sócio", B), ("que tira todo mês, sem faltar um.", R)), fs=42)
slide(at(4),  st(("Se a sua empresa depende de dinheiro de fora pra funcionar,", B))
            + st(("HOJE ELA É", A), ("UM PÉSSIMO NEGÓCIO.", A), mt=26), top=280, fs=48)
slide(at(5),  st(("Com Selic a 2%, esse modelo parecia negócio.", B), ("A 14%, aparece o que ele sempre foi:", B))
            + st(("uma operação que nunca se pagou.", B), ("Quem pagava era o banco, e cobrava pouco.", R)), fs=41)
slide(at(6),  st(("JURO ALTO NÃO QUEBRA", A), ("EMPRESA BOA. ELE MOSTRA", A), ("QUAL ERA RUIM.", A)), top=280)
slide(at(7),  st(("Empreender no Brasil já é risco por natureza.", B), ("E estamos a duas semanas de uma eleição.", B))
            + st(("Se o cenário piorar,", B), ("quem depende do banco cai primeiro.", R)), fs=41)
slide(at(8),  st(("Empresa grande gira com dinheiro dos outros.", B), ("Só que lá o risco não é do dono:", B))
            + st(("se quebra, quem perde é o investidor.", B), ("Na sua, quem assina o aval é você.", R)), fs=42)
slide(at(9),  st(("Dinheiro de fora pra crescer é escolha.", B), ("Pra funcionar, é dependência.", B))
            + st(("E modelo que depende não é seu.", B), ("É alugado do banco.", R)), fs=42)
slide(at(10), st(("Modelo econômico bom se paga sozinho:", B), ("margem que cobre o custo, prazo que não afoga,", B), ("estoque que gira.", B))
            + st(("Isso não é sorte. É desenho.", B), ("E desenho o dono faz.", R)), fs=41)
slide(at(11), st(("Empresa nasceu pra botar dinheiro", B), ("no bolso do dono.", B))
            + st(("Se o lucro está indo pro banco,", B), ("a sua ainda não cumpriu pra que nasceu.", R)), fs=42)
slide(at(12), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino a ler e redesenhar", B), ("o modelo econômico da sua empresa:", B))
            + st(("pra ela se pagar sozinha", B), ("e o lucro voltar a ter o seu nome.", R), mt=26), fs=41)
slide(at(13), '      <div class="cta-big">Comenta <span class="red">MODELO</span></div>\n'
            + st(("e eu te mando o link no seu direct.", R), mt=24), fs=44)
