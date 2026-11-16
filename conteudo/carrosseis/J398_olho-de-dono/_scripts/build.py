#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel J398 (editorial-punch, "Olho de dono nao se terceiriza", 16/11).
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
slide(at(1),  st(("OLHO DE DONO", A), ("NÃO SE TERCEIRIZA.", A)), top=230)
slide(at(2),  st(("Crescer era o plano.", B))
            + st(("Virou a dor de cabeça.", R)), top=300, fs=60)
slide(at(3),  st(("Em dois anos veio a segunda loja,", B), ("mais gente, mais estoque, mais conta.", B))
            + st(("E os problemas correram", R), ("na frente da empresa.", R)), top=270, fs=44)
slide(at(4),  st(("Você saiu atrás do culpado:", B), ("a crise, o mercado, o funcionário.", B))
            + st(("Trocou gente, apagou incêndio.", R), ("E nada voltou pro lugar.", R)), top=270, fs=46)
slide(at(5),  st(("Até que você aceitou", B), ("a explicação mais perigosa:", B))
            + st(("“crescer dói mesmo.", R), ("É normal.”", R)), top=280, fs=54)
slide(at(6),  st(("Não é normal.", B), ("A explicação é bem mais simples:", B))
            + st(("VOCÊ TIROU O OLHO.", A), mt=10), top=260, fs=50)
slide(at(7),  st(("Foi só isso.", B))
            + st(("Não tem outro motivo.", R)), top=300, fs=60)
slide(at(8),  st(("Quando a empresa era pequena,", B), ("você via tudo.", B))
            + st(("Cada venda, cada erro, cada cliente.", R), ("Nada escapava.", R)), top=270, fs=46)
slide(at(9),  st(("Aí a empresa cresceu, você foi", B), ("cuidar de outras frentes", B))
            + st(("e pôs alguém no seu lugar", R), ("pra fazer o que você fazia.", R)), top=270, fs=48)
slide(at(10), st(("Não fez.", R))
            + st(("E você só ficou sabendo", B), ("quando a conta chegou.", B)), top=290, fs=58)
slide(at(11), st(("O perigo nunca é", B), ("a empresa pequena.", B))
            + st(("O perigo é a hora", R), ("em que ela começa a crescer.", R)), top=280, fs=54)
slide(at(12), st(("Olhar não é voltar a fazer tudo.", B), ("É comandar de perto.", B))
            + st(("Número na mesa, reunião toda semana,", R), ("cobrança que não falha.", R)), top=270, fs=44)
slide(at(13), st(("Ver a empresa inteira", B), ("não é talento. É método.", B))
            + st(("Com método, o erro aparece na semana.", B), ("Sem método, aparece no caixa.", R)), top=270, fs=44)
slide(at(14), st(("Eu tenho um treinamento de gestão", B), ("pra donos de PME, o MBV,", B))
            + st(("onde eu ensino o que olhar,", R), ("onde cobrar e como fazer", R), ("o time entregar.", R)), top=280, fs=46)
slide(at(15), '      <div class="cta-big">Comenta <span class="red">CONTROLE</span></div>\n'
            + st(("que eu te mostro como crescer", B), ("sem perder a empresa de vista.", B), mt=26), top=300, fs=50)
