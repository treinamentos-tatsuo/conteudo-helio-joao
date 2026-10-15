#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 97 (editorial-punch, repost "Se você sente pressão").
Layout da skill (calibragem do 88/91: corpo top 200, capa 240; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {3: "20% bottom", 9: "30% bottom"}
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

slide(at(1),  st(("Se você sente <span class=\"anton\" style=\"font-size:78px;vertical-align:-0.04em;margin-left:6px\">PRESSÃO...</span>", B)), top=240, fs=52)
slide(at(2),  st(("PARABÉNS.", A), ("(você está no jogo certo)", B)))
slide(at(3),  st(("Boleto chega.", B), ("Funcionário depende de você.", B)) + st(("Imposto come seu caixa.", R)))
slide(at(4),  st(("Você respira fundo. Engole o medo.", B), ("E resolve.", R)))
slide(at(5),  st(("Empreender é isso.", B)) + st(("Pressão o tempo todo. Zero garantia.", B), ("Mil responsabilidades.", R)))
slide(at(6),  st(("Mas não esquece de uma coisa:", B)), fs=48)
slide(at(7),  st(("FOI VOCÊ QUE ESCOLHEU", A), ("ESSE JOGO.", A)))
slide(at(8),  st(("E nesse jogo...", B)), fs=48)
slide(at(9),  st(("quanto maior a pressão,", B), ("maior o prêmio no fim.", R)))
slide(at(10), st(("Só quem aguenta a pressão", B), ("é digno da recompensa.", R)))
slide(at(11), st(("Mas aguentar a pressão", B), ("não é o mesmo que ser pago por ela.", R)) + st(("Existem dois donos", B), ("vivendo a mesma pressão.", B)))
slide(at(12), st(("Um corre o risco todo mês e leva", B), ("pra casa um salário. (quando leva)", B)) + st(("O outro corre o mesmo risco e leva lucro.", B), ("Dividendo. Patrimônio.", R)), fs=42)
slide(at(13), st(("A diferença não é coragem.", B), ("Não é tamanho de empresa.", B)) + st(("É GESTÃO.", A)))
slide(at(14), st(("Gestão é saber a margem antes de vender.", B), ("É número na mesa toda semana.", B), ("É time que entrega o combinado.", R)), fs=42)
slide(at(15), st(("Sem gestão, o risco é todo seu", B), ("e o prêmio é de ninguém.", B)) + st(("Com gestão, o risco continua seu.", B), ("O prêmio também.", R)))
cta = (st(("Eu tenho um treinamento para donos", B), ("de pequenas e médias empresas, onde ensino:", B))
       + st(("segurar a pressão sem colapsar,", B), ("montar a gestão que paga o risco", B), ("e transformar responsabilidade em resultado.", B), mt=26)
       + '      <div class="cta-big" style="margin-top:30px;font-size:58px">Comenta <span class="red">RECOMPENSA</span></div>\n'
       + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=10))
slide(at(16), cta, top=180, fs=36)
