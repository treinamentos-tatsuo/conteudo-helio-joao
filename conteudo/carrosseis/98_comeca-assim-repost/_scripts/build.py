#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 98 (editorial-punch, repost "Todo empreendedor no Brasil começa assim").
Layout da skill (calibragem registrada em erros-frequentes 04/09: corpo top 200, capa 240; Source Serif 44; Anton nos gritos)."""
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
def slide(n, body, top=200, fs=None):
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

slide(at(1),  st(("Todo empreendedor no Brasil", B), ("COMEÇA ASSIM:", A)), top=240, fs=52)
slide(at(2),  st(("FAZENDO.", A), ("FAZENDO.", A), ("FAZENDO.", A)))
slide(at(3),  st(("Sem muita estrutura. Sem muita direção.", B), ("Na força do instinto e da necessidade.", R)))
slide(at(4),  st(("E você chegou até aqui assim.", B)) + st(("Você fez acontecer.", B), ("NA RAÇA.", A)))
slide(at(5),  st(("Mas agora...", B), ("isso não é mais suficiente.", R)) + st(("Quando a empresa era pequena,", B), ("o seu olho alcançava tudo.", B)))
slide(at(6),  st(("Hoje ela cresceu", B), ("mais que o seu olho.", B)) + st(("Você decide no chute.", B), ("E chama isso de faro.", R)))
slide(at(7),  st(("Se você quer crescer de verdade,", B), ("precisa parar de só fazer.", B)) + st(("E começar a enxergar.", B), ("Decidir. Priorizar.", R)))
slide(at(8),  st(("Enxergar é ter o número na mesa.", B), ("Decidir é escolher pelo número, não pelo susto.", B), ("Priorizar é fazer primeiro o que paga a folha.", R)), fs=40)
slide(at(9),  st(("Sem saber o próximo passo,", B), ("você vai girar em círculos a vida toda.", R)) + st(("Não é sair do operacional.", B), ("É parar de ser só mais um", B), ("par de braços dentro dele.", B)), fs=42)
slide(at(10), st(("Empreendedor faz a empresa nascer.", B), ("Empresário faz a empresa crescer.", B)) + st(("Um trabalha dentro dela.", B), ("O outro comanda dentro dela.", R)))
slide(at(11), st(("Empresa não trava por falta de mercado.", B), ("Trava porque o dono ainda pensa, todo dia,", B), ("como quem começou do zero.", R)), fs=42)
slide(at(12), st(("Eu tenho um treinamento para donos", B), ("de pequenas e médias empresas, onde ensino:", B))
            + st(("enxergar a empresa pelo número,", B), ("decidir sem depender do instinto", B), ("e priorizar o que faz o lucro crescer.", R), mt=26), fs=40)
slide(at(13), '      <div class="cta-big">Comenta <span class="red">NUMERO</span></div>\n'
            + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=24))
