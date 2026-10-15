#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 184 (editorial-punch, "Só sobrou a casa", D1-S27 versão topo).
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

slide(at(1),  st(("Quando foi a última vez que você perguntou", B)) + st(("QUAL É O SONHO", A), ("DO SEU FUNCIONÁRIO?", A), mt=22), top=280, fs=44)
slide(at(2),  st(("É muito fácil reclamar do time.", B), ("Do funcionário que não veste a camisa,", B))
            + st(("do gerente que não se compromete,", B), ("da geração que não quer nada com nada.", R)), fs=42)
slide(at(3),  st(("Difícil é admitir uma coisa:", B), ("você sabe o salário, o cargo", B), ("e o horário de cada um.", B))
            + st(("Mas não sabe", B), ("pelo que ele levanta de manhã.", R)), fs=42)
slide(at(4),  st(("E cada um tem um motivo.", B), ("A casa que ainda é de aluguel,", B))
            + st(("a faculdade do filho,", B), ("o carro que ele promete pra família todo ano.", R)), fs=40)
slide(at(5),  st(("Você não sabe o que cada um enfrenta", B), ("quando vai embora pra casa.", B))
            + st(("Mas cobra que ele chegue no dia seguinte", B), ("com o mesmo fogo que você.", R)), fs=40)
slide(at(6),  st(("Sua empresa é o seu sonho.", B))
            + st(("NÃO É O SONHO DELE.", A), mt=26), fs=48)
slide(at(7),  st(("Tenho um braço direito", B), ("com 29 anos de casa.", B))
            + st(("Ele me disse uma vez:", B), ("a Hoken não é o meu sonho.", R), ("É a ponte pro meu sonho.", R)), fs=42)
slide(at(8),  st(("E ele está certo.", B), ("Ninguém fica 29 anos pelo sonho do patrão.", B))
            + st(("Fica porque, ano após ano,", B), ("a ponte levou ele um pouco mais longe.", R)), fs=40)
slide(at(9),  st(("Só que, pra acreditar que o sonho dele", B), ("cabe aí dentro, ele precisa", B), ("ver a empresa crescer.", B))
            + st(("E precisa ver que você", B), ("sabe pra onde ele quer ir.", R)), fs=40)
slide(at(10), st(("Então faz a pergunta.", B), ("Senta com cada um, olha no olho:", B))
            + st(("o que você quer da vida?", B), ("E mostra o pedaço do caminho", R), ("que passa por aqui.", R)), fs=42)
slide(at(11), st(("No meu treinamento eu ensino a montar a cultura", B), ("que faz o time crescer junto com a empresa:", B))
            + st(("o plano de carreira, a meta que vira conquista", B), ("e o rito de acompanhar cada um.", R)), fs=38)
slide(at(12), st(("Gente comprometida não se contrata pronta.", R), ("Se constrói.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">SONHO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=42)
