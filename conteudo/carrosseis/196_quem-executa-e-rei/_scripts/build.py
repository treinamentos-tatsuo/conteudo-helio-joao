#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 196 (editorial-punch, "Quem executa é rei").
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

slide(at(1),  st(("O que mais tem hoje é empresário", B))
            + st(("COM OBESIDADE", A), ("MENTAL.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Come palestra, livro, podcast, curso.", B), ("Pergunta tudo pra IA.", B))
            + st(("Fala de gestão melhor que consultor.", B), ("E a empresa continua igual há cinco anos.", R)), fs=42)
slide(at(3),  st(("Volta de cada evento com o caderno cheio", B), ("e a cabeça fervendo.", B))
            + st(("Na segunda, o caderno vai pra gaveta.", B), ("E ele volta a apagar incêndio.", R)), fs=42)
slide(at(4),  st(("Eu parei de estudar com quinze anos.", B), ("Sempre teve gente mais preparada que eu.", B))
            + st(("Mas o pouco que eu sabia,", B), ("eu colocava em prática.", R)), fs=42)
slide(at(5),  st(("Foi assim que eu aprendi:", B))
            + st(("O JOGO DOS NEGÓCIOS", A), ("SE GANHA", A), ("NA EXECUÇÃO.", A), mt=22), fs=46)
slide(at(6),  st(("Hoje a inteligência artificial entrega", B), ("o plano pronto em dez segundos.", B))
            + st(("O que ficou raro é quem faz.", B), ("E quem executa é rei.", R)), fs=42)
slide(at(7),  st(("Não existe empresa que cresce", B), ("sem o dono pagar o preço.", B))
            + st(("E o preço não está no que você sabe.", B), ("Está no que você faz toda semana.", R)), fs=42)
slide(at(8),  st(("É a reunião de segunda às oito,", B), ("mesmo depois do pior fim de semana.", B))
            + st(("É olhar o número feio", B), ("e cobrar o gerente pela terceira vez.", R)), fs=42)
slide(at(9),  st(("E você foge desse preço", B), ("do jeito mais elegante: estudando.", B))
            + st(("Estudar não dói. Executar dói.", B), ("Por isso você sabe tanto e faz tão pouco.", R)), fs=42)
slide(at(10), st(("Fatura 30 milhões, já leu tudo sobre gestão", B), ("e não sabe a margem do que mais vende.", B))
            + st(("Não tem reunião de resultado.", B), ("Tem reunião quando dá problema.", R)), fs=40)
slide(at(11), st(("E o seu time está vendo tudo isso.", B), ("Cada ideia nova que morre na quinta-feira", B))
            + st(("ensina pra ele que, na sua empresa,", B), ("se fala muito e se faz pouco.", R)), fs=42)
slide(at(12), st(("Você não precisa saber mais.", B))
            + st(("PRECISA FAZER", A), ("O QUE JÁ SABE.", A), mt=22), fs=46)
slide(at(13), st(("Maestria só vem com repetição.", B), ("E ela começa num rito só:", B))
            + st(("toda semana, mesmo dia, mesma hora,", B), ("sentar com o número e cobrar o combinado.", R)), fs=42)
slide(at(14), st(("No MBV, o meu treinamento,", B), ("eu ensino gestão pra dono de PME:", B))
            + st(("Lucratividade, Crescimento e Cultura", B), ("saindo do caderno e virando", R), ("rotina da empresa.", R)), fs=42)
slide(at(15), st(("Saber, todo mundo sabe.", B), ("Quem executa é rei.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">REI</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
