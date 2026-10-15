#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 171 (editorial-punch, "Só sobrou a casa", D1-S27 versão topo).
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

slide(at(1),  st(("Você lembra do dia do seu casamento.", B)) + st(("MAS NÃO LEMBRA O QUE", A), ("ALMOÇOU NA TERÇA.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Eu também não.", B), ("Se me perguntar o que eu comi", B), ("ontem no almoço, eu não sei.", B))
            + st(("Mas lembro de coisa que aconteceu há vinte anos", B), ("como se fosse hoje.", R)), fs=40)
slide(at(3),  st(("Sabe por quê?", B), ("A cabeça só guarda o que emociona.", B))
            + st(("Casamento, acidente, filho nascendo.", R)), fs=44)
slide(at(4),  st(("E o almoço de terça", B), ("não emociona ninguém.", R)), fs=48)
slide(at(5),  st(("Agora faz o mesmo teste com a sua empresa:", B), ("o que o seu time vai lembrar daqui a dez anos?", B))
            + st(("A meta batida que ninguém comemorou?", B), ("O aniversário que passou em branco?", R)), fs=38)
slide(at(6),  st(("Você tem 40, 50 funcionários.", B), ("Paga em dia, paga direito.", B))
            + st(("E mesmo assim, por trezentos reais a mais,", B), ("o seu melhor vai embora sem olhar pra trás.", R)), fs=40)
slide(at(7),  st(("Porque pra ele a sua empresa", B), ("é um almoço de terça.", B))
            + st(("E ninguém sente falta", B), ("do que nunca marcou.", R)), fs=44)
slide(at(8),  st(("Festa, churrasco, comemoração de meta?", B), ("Muito dono acha besteira.", B))
            + st(("BESTEIRA É SER ESQUECIDO.", A), mt=26), fs=44)
slide(at(9),  st(("A vida dentro da sua empresa", B), ("tem que ser forrada de emoção.", B))
            + st(("E o líder que sabe disso constrói um time", B), ("que não te troca nem pelo dobro do salário.", R)), fs=40)
slide(at(10),  st(("E nisso a pequena empresa tem uma força", B), ("que a multinacional não tem.", B))
            + st(("Ela não consegue pagar mais que a grande.", B), ("Mas consegue ser inesquecível.", R)), fs=40)
slide(at(11), st(("Você está lado a lado com o seu time.", B), ("Sabe o nome de cada um.", B))
            + st(("Então chega perto, descobre o sonho deles", B), ("e mostra que esse sonho cabe aí dentro.", R)), fs=40)
slide(at(12), st(("Meta batida se comemora na frente de todo mundo.", B), ("Aniversário se lembra. Conquista se celebra.", B))
            + st(("Não uma vez por ano.", B), ("Todo mês, virando rito.", R)), fs=38)
slide(at(13), st(("No meu treinamento eu ensino", B), ("a montar a cultura da sua empresa:", B))
            + st(("o que se cobra, o que se celebra", R), ("e os ritos de todo dia.", R)), fs=44)
slide(at(14), st(("Gente escolhe ficar", R), ("onde a vida dela foi marcada.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">VINCULO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", B), mt=18), fs=44)
