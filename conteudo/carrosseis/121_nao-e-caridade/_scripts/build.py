#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 121 (editorial-punch, "Não é caridade").
Layout do modelo.md (calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {9: "40% bottom", 6: "58% bottom"}
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

slide(at(1),  st(("EMPRESA NÃO É", A), ("INSTITUIÇÃO", A), ("DE CARIDADE.", A)), top=280)
slide(at(2),  st(("Empresa nasceu pra dar lucro.", B), ("Simples assim.", B))
            + st(("Quem acha o contrário", B), ("nunca lidou com uma folha de pagamento.", R)))
slide(at(3),  st(("E não vem com papo de patrão explorador,", B), ("de multinacional que espreme funcionário.", B))
            + st(("Isso é coisa distante.", B), ("Não mora na sua rua.", R)), fs=42)
slide(at(4),  st(("Eu estou falando de quem segura", B), ("a cadeia inteira em pé:", B))
            + st(("o pequeno e o médio empresário.", R)))
slide(at(5),  st(("Que botou a casa de garantia no banco,", B), ("o carro no nome da empresa", B))
            + st(("e a vida da família inteira", B), ("em cima de uma aposta.", R)))
slide(at(6),  st(("Empreender no Brasil não é luxo.", B), ("Não é hobby de rico.", B))
            + st(("É a saída que muita gente achou", B), ("pra mudar de vida.", R)))
slide(at(7),  st(("E é por todo esse risco que eu defendo", B), ("a regra número 1 dos negócios:", B))
            + st(("Empresa nasceu pra botar dinheiro", B), ("no bolso do DONO.", R)), fs=42)
slide(at(8),  st(("Porque quando a casa cai,", B), ("todo mundo segue a vida.", B))
            + st(("MENOS VOCÊ.", A), ("PORQUE ELA CAI", A), ("EM CIMA DE VOCÊ.", A)))
slide(at(9),  st(("Por isso o dono tem que ser", B), ("pago pelo risco que corre.", B))
            + st(("Caso contrário, fecha a empresa", B), ("e vai trabalhar pros outros.", R)))
slide(at(10), st(("E NÃO ESTOU FALANDO", A), ("DE PRÓ-LABORE.", A)))
slide(at(11), st(("15, 30 mil por mês um bom gerente ganha,", B), ("com carteira assinada e sem fiador.", B))
            + st(("Isso é no máximo um pró-labore,", B), ("e pró-labore não é salário de dono.", R)), fs=42)
slide(at(12), st(("Pró-labore paga as suas horas.", B), ("Seu risco se paga com lucro.", B))
            + st(("E lucro não é o que sobra.", B), ("É prêmio que entra no preço antes de vender.", R)), fs=42)
slide(at(13), st(("Isso não depende de crescer,", B), ("de contratar nem de dinheiro novo.", B))
            + st(("Depende de saber quanto cada venda deixa", B), ("depois de pagar todo mundo.", R)), fs=42)
slide(at(14), st(("É com a empresa que você já tem.", B), ("Com o dinheiro que já está lá, mas que escapa:", B))
            + st(("no preço sem margem ajustada,", B), ("no custo que ninguém mede,", B), ("no desconto dado no balcão.", R)), fs=40)
slide(at(15), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino isso:", B))
            + st(("a ser remunerado hoje,", B), ("com a empresa que você já tem,", B), ("pelo risco que você já corre.", R)), fs=42)
slide(at(16), st(("Você corre o risco.", B), ("A empresa te paga por ele.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">REMUNERADO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", B), mt=18))
