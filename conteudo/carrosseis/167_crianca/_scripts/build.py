#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 167 (editorial-punch, "Só sobrou a casa", D1-S27 versão topo).
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

slide(at(1),  st(("Ah, mas eu não gosto...", B)) + st(("QUEM SÓ FAZ O QUE", A), ("GOSTA É CRIANÇA.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Eu também não gosto de tudo, não.", B))
            + st(("Gestão é chato pra cacete,", B), ("eu sempre gostei de vender.", R)), fs=44)
slide(at(3),  st(("Agora, número, planilha,", B), ("reunião de acompanhamento?", B))
            + st(("Nunca gostei. Até hoje não gosto.", R)), fs=44)
slide(at(4),  st(("Mas eu faço. Todo dia.", B), ("Olho o número, confiro a margem, cobro a tarefa.", B))
            + st(("Porque foi isso, e não a venda,", B), ("que manteve a minha empresa de pé.", R)), fs=40)
slide(at(5),  st(("Agora me fala, empresário:", B), ("o que você não faz porque é chato?", B))
            + st(("Olhar o número toda semana?", B), ("Acompanhar tarefa todo dia?", B), ("Tomar decisão difícil?", R)), fs=40)
slide(at(6),  st(("Você fatura milhões.", B), ("Mas a parte chata da empresa", B), ("continua sem dono.", B))
            + st(("E o que fica sem dono na sua empresa", R), ("acaba mandando nela.", R)), fs=40)
slide(at(7),  st(("E quando alguém pergunta,", B), ("você tem a resposta pronta:", B))
            + st(("Gestão não é a minha praia.", R)), fs=44)
slide(at(8),  st(("Pode chamar de perfil, de jeito, de estilo.", B))
            + st(("EU CHAMO DE BIRRA.", A), mt=26), fs=44)
slide(at(9),  st(("A conta da empresa não pergunta", B), ("do que você gosta.", B))
            + st(("O boleto vence, o concorrente cresce,", B), ('a margem vaza. <span class="red">Com ou sem a sua vontade.</span>', B)), fs=40)
slide(at(10), st(("Depois de 38 anos como empresário,", B), ("eu te garanto:", B))
            + st(("a parte que você não gosta", B), ("é justamente a que está travando a sua empresa.", R)), fs=40)
slide(at(11), st(("Fazer o básico bem feito, todo dia,", B), ("é chato mesmo.", B))
            + st(("Por isso quase ninguém faz.", B), ("E por isso funciona pra quem faz.", R)), fs=42)
slide(at(12), st(("No meu treinamento eu ensino", B), ("exatamente a parte chata:", B))
            + st(("ler o número, montar a máquina de vendas", B), ("e cobrar o time todo dia.", B))
            + st(("Não pra você gostar. Pra você saber fazer.", R)), fs=40)
slide(at(13), st(("Ou você faz a parte chata,", R), ("ou a parte chata desfaz a sua empresa.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">ADULTO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", B), mt=18), fs=40)
