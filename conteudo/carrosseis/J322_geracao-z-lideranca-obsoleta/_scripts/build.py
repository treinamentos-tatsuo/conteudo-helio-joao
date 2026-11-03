#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel J322 (editorial-punch, "Geração Z não quer só dinheiro", 03/11).
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
slide(at(1),  st(("GERAÇÃO Z NÃO QUER", A), ("SÓ DINHEIRO.", A))
            + st(("E você só tem salário pra oferecer.", B), mt=26), top=280, fs=48)
slide(at(2),  st(("Em toda sala de empresário eu escuto:", B), ("“essa geração é fraca,", B), ("não se compromete com nada.”", B))
            + st(("O menino pede as contas pelo WhatsApp", B), ("e o dono jura que o problema é o menino.", R)), fs=42)
slide(at(3),  st(("Pode reclamar, eu também já reclamei.", B), ("Mas me responde uma coisa.", B))
            + st(("Dos bons que você contratou", B), ("nos últimos dois anos,", B), ("quantos ainda trabalham com você?", R)), fs=42)
slide(at(4),  st(("A geração do seu pai ficava trinta anos", B), ("na mesma empresa", B), ("porque emprego bom era coisa rara.", B))
            + st(("Hoje quem é bom tem três propostas na mesa.", B), ("E escolhe com quem vai trabalhar.", R)), fs=42)
slide(at(5),  st(("Aí o dono faz o que aprendeu:", B), ("“manda quem pode, obedece quem tem juízo.", B), ("Quem paga o seu salário sou eu.”", B))
            + st(("Isso segurava gente nos anos 90.", B), ("Hoje, isso vira pedido de demissão.", R)), fs=42)
slide(at(6),  st(("As gerações mudam.", B), ("E a liderança tem que mudar junto.", B))
            + st(("Não é culpa da geração.", B), ("É culpa da sua liderança obsoleta.", R)), fs=44)
slide(at(7),  st(("Essa geração quer o que você", B), ("queria com vinte anos: olhar pro chefe", B), ("e pensar “com esse cara eu aprendo”.", B))
            + st(("Quer saber pra onde vai crescer", B), ("e pra que serve o que faz.", R)), fs=42)
slide(at(8),  st(("O concorrente cobre a sua proposta amanhã.", B), ("Mais quinhentos reais e o seu", B), ("melhor funcionário vai embora.", B))
            + st(("O que ele não cobre é um líder que o time admira.", B), ("Esse, ninguém troca por quinhentos reais.", R)), fs=40)
slide(at(9),  st(("Enquanto você reclama da geração,", B), ("o seu concorrente contrata os melhores dela.", B))
            + st(("Daqui a dez anos, eles vão ser os gerentes.", B), ("Da empresa dele, não da sua.", R)), fs=42)
slide(at(10), st(("Eu tenho um treinamento de gestão", B), ("pra donos de pequena e média empresa,", B))
            + st(("inclusive gestão de pessoas,", B), ("cultura e liderança.", R)), fs=44)
slide(at(11), st(("Quer um time que fica", B), ("porque quer, e não porque precisa?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">GERAÇÃO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
