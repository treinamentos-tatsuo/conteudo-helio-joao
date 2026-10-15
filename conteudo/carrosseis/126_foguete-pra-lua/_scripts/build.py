#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 126 (editorial-punch, "Foguete que vai pra lua").
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

slide(at(1),  st(("Ninguém quer estar num ônibus", B), ("que vai pro fim da rua.", B)), top=280, fs=54)
slide(at(2),  st(("TODO MUNDO QUER ESTAR NUM", A), ("FOGUETE QUE VAI PRA LUA.", A)), top=280)
slide(at(3),  st(("Se eu pudesse te dar um conselho", B), ("pra segurar os seus melhores, seria esse.", B))
            + st(("Gente boa de verdade", B), ("é atraída por crescimento.", R)), fs=42)
slide(at(4),  st(("Se a sua empresa não está crescendo", B), ("de verdade, esquece.", B))
            + st(("A sua chance de contratar ou segurar", B), ("gente competente é quase nenhuma.", R)), fs=41)
slide(at(5),  st(("O seu melhor pediu a conta", B), ("e você achou que foi por salário.", B))
            + st(("Não foi.", B), ("Ele olhou pra frente e viu o ponto final.", R)), fs=42)
slide(at(6),  st(("Gente boa fica quando sabe aonde", B), ("a empresa vai. E quando é longe.", B))
            + st(("Não é a meta do mês.", B), ("Meta é pra bater. Sonho é pra puxar.", R)), fs=41)
slide(at(7),  st(("Sonho grande segura o time unido,", B), ("porque ninguém chega na lua sozinho.", B))
            + st(("Todo mundo vai ter que se virar", B), ("pra fazer acontecer.", R)), fs=42)
slide(at(8),  st(("E quando acontece, ele ganha mais dinheiro.", B), ("Cresce. Se sente realizado.", B))
            + st(("É isso que segura gente boa.", B), ("Não é o plano de saúde.", R)), fs=42)
slide(at(9),  st(("Agora, se o seu ambiente é raso,", B), ("seja sincero:", B))
            + st(("VOCÊ NÃO SEGURA TUBARÃO", A), ("EM AQUÁRIO RASO.", A)), fs=46)
slide(at(10),  st(("No raso fica quem cabe no raso:", B), ("quem quer trabalhar menos e ganhar menos.", B))
            + st(("E depois você reclama", B), ("que não acha gente boa.", R)), fs=42)
slide(at(11), st(("Você não pode querer tubarão na empresa", B), ("sem ter profundidade de verdade.", B))
            + st(("E toda profundidade", B), ("vem com pressão.", R)), fs=42)
slide(at(12), st(("Pressão é cobrança, ritmo, meta que aperta.", B), ("Fundo é assim.", B))
            + st(("O tubarão aguenta.", B), ("Quem não aguenta é peixe de aquário.", R)), fs=42)
slide(at(13), st(("Primeiro, o seu sonho de dono", B), ("tem que ser grande.", B), ("Sonho pequeno cava empresa rasa.", B))
            + st(("NINGUÉM EMBARCA", A), ("NUM AVIÃO QUE", A), ("NÃO VAI DECOLAR.", A)), fs=40)
slide(at(14), st(("Define aonde a empresa vai chegar", B), ("e divide em metas que se batem.", B))
            + st(("Cria um rito e acompanha todo dia.", B), ("É assim que se cava profundidade.", R)), fs=42)
slide(at(15), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino a montar:", B))
            + st(("o destino, o plano que chega lá", B), ("e o time que aguenta a pressão.", R), mt=26), fs=42)
slide(at(16), st(("Gente boa não fica no ônibus.", B), ("A sua parte é construir o foguete.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">FOGUETE</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24), fs=42)
