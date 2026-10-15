#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 195 (editorial-punch, "O sucesso deixa pegadas").
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

slide(at(1),  st(("O sucesso deixa pegadas.", B))
            + st(("NENHUMA PASSA", A), ("PELO ATALHO.", A), mt=26), top=280, fs=50)
slide(at(2),  st(("Em 38 anos de empresa, eu vi", B), ("muito dono dar certo e muito dono afundar.", B))
            + st(("E a diferença entre um e outro", B), ("nunca foi sorte, mercado ou crise.", R)), fs=42)
slide(at(3),  st(("O dono que afunda fatura milhões,", B), ("vive apagando incêndio e jura", B), ("que não tem tempo pra aprender.", B))
            + st(("Mas tem tempo pra assistir", R), ("guru no Instagram.", R)), fs=42)
slide(at(4),  st(("Aquele do carrão, do relógio e do jatinho,", B), ("prometendo dez vezes mais em um ano.", B))
            + st(("Amigo, você vai levar a dor da sua empresa", B), ("pra quem nunca pagou uma folha de pagamento?", R)), fs=40)
slide(at(5),  st(("Guru vende o que dono cansado quer ouvir.", B), ("Fórmula, segredo, três passos.", B))
            + st(("E você compra.", B), ("Porque estudar dá trabalho.", R)), fs=42)
slide(at(6),  st(("Paga, aplica, e na segunda-feira", B), ("a empresa está igualzinha.", B))
            + st(("Mesmo problema, mesmo incêndio.", B), ("Só que com menos dinheiro no caixa.", R)), fs=42)
slide(at(7),  st(("Vou te falar na cara:", B))
            + st(("O CAMINHO FÁCIL", A), ("SEMPRE É UM ERRO.", A), mt=26), fs=46)
slide(at(8),  st(("Eu não tenho faculdade.", B), ("Parei de estudar aos quinze anos.", B))
            + st(("Aos vinte, descobri que era analfabeto funcional.", B), ("Lia uma página de livro e não entendia nada.", R)), fs=40)
slide(at(9),  st(("Se tinha alguém com desculpa", B), ("pra procurar atalho, era eu.", B))
            + st(("Fui atrás de livro, de curso, de MBA", B), ("e de gente mais inteligente do que eu.", R)), fs=42)
slide(at(10), st(("Essa é a pegada de todo empresário", B), ("que deu certo que eu conheci.", B))
            + st(("Todos, sem exceção, foram aprender", B), ("gestão, gente, modelo de negócio e venda.", R)), fs=42)
slide(at(11), st(("Aí o dono me fala: Hélio, eu virei", B), ("empresário porque não gosto de estudar.", B))
            + st(("Então se acostuma com a empresa que você tem.", B), ("Ela nunca vai passar do tamanho da sua cabeça.", R)), fs=40)
slide(at(12), st(("Foi pra isso que eu criei o MBV.", B), ("Lá não tem fórmula nem segredo.", B))
            + st(("Tem Lucratividade, Crescimento e Cultura.", B), ("E vai ter que estudar.", R)), fs=42)
slide(at(13), st(("Se você quer atalho, passa reto.", B), ("Se quer o caminho,", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PEGADA</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
