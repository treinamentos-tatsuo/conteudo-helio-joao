#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 193 (editorial-punch, "Só sobrou a casa", D1-S27 versão topo).
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

slide(at(1),  st(("Vou te contar o preço de ser empresário", B), ("que ninguém gosta de compartilhar.", B)), top=280, fs=48)
slide(at(2),  st(("Durante anos eu trabalhei feito um maluco.", B), ("Diabete explodindo, empresa crescendo.", B))
            + st(("E os meus filhos cresceram", B), ("sem eu ver.", R)), fs=42)
slide(at(3),  st(("Não era falta de esforço.", B), ("Ninguém trabalhava mais do que eu.", B))
            + st(("E mesmo assim, se alguém me perguntasse", B), ("se eu estava ficando mais rico ou mais pobre,", B), ("eu não sabia responder.", R)), fs=40)
slide(at(4),  st(("Eu achava que estava construindo", B), ("alguma coisa pra deixar pra eles.", B))
            + st(("Mas a realidade é que eu nunca tinha", B), ("parado pra fazer essa conta.", B), ("Eu só trabalhava, e torcia.", R)), fs=42)
slide(at(5),  st(("E aprendi da pior forma:", B))
            + st(("A IGNORÂNCIA COBRA", A), ("MENSALIDADE E NÃO", A), ("MANDA BOLETO.", A), mt=26), fs=46)
slide(at(6),  st(("E quem paga essa conta não é a empresa.", B), ("É a família do dono.", B))
            + st(("São os filhos que crescem enquanto ele", B), ("trabalha pra uma empresa", B), ("que não devolve nada.", R)), fs=40)
slide(at(7),  st(("Agora me responde com o coração:", B), ("nos últimos cinco anos,", B), ("a sua família ficou mais rica", B))
            + st(("ou a empresa foi engolindo", R), ("o que vocês tinham juntado?", R)), fs=42)
slide(at(8),  st(("Conheço dono que fatura milhões", B), ("e já vendeu o sítio pra cobrir o caixa.", B))
            + st(("Já mexeu na reserva da família,", B), ("já deu a casa de garantia no banco.", R)), fs=42)
slide(at(9),  st(("E em casa ninguém sabe.", B), ("Ele não conta.", B))
            + st(("Porque nem ele sabe responder", B), ("se a empresa está deixando ele rico ou pobre.", R)), fs=40)
slide(at(10), st(("Os anos que passaram não voltam.", B), ("Mas os próximos ainda são seus.", B))
            + st(("E eles começam no dia em que você souber,", B), ("todo mês, se está ficando", R), ("mais rico ou mais pobre.", R)), fs=40)
slide(at(11), st(("Aí você me diz: Hélio, gestão é chato.", B), ("É chato pra cacete, eu sei.", B))
            + st(("Chato mesmo é o seu filho crescer", R), ("e você descobrir pela foto no celular.", R)), fs=42)
slide(at(12), st(("Foi por isso que eu criei o MBV.", B), ("Trabalhei anos sem saber se ficava", B), ("mais rico ou mais pobre", B))
            + st(("e paguei com a saúde e com a infância", B), ("dos meus filhos. Não quero que nenhum", R), ("empresário passe por isso.", R)), fs=40)
slide(at(13), st(("Lá eu ensino gestão de verdade:", B), ("Lucratividade, Crescimento e Cultura,", B))
            + st(("pra você saber todo mês", B), ("se a empresa está te deixando mais rico.", R)), fs=42)
slide(at(14), st(("Faz pelos seus filhos", R), ("o que eu não fiz pelos meus.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">CLAREZA</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
