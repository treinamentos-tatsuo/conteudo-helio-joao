#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 164 (editorial-punch, "Só sobrou a casa", D1-S27 versão topo).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {9: "22% bottom"}
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

slide(at(1),  st(("Trinta anos de empresa aberta", B)) + st(("E SÓ SOBROU A CASA", A), ("ONDE MORA.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Eu conheço muito dono de empresa assim.", B), ("E não é gente que trabalhou pouco, não.", B))
            + st(("Eu comecei na feira, acordando uma da manhã.", B), ("Eles trabalharam tanto quanto eu. Às vezes mais.", R)), fs=40)
slide(at(3),  st(("Aí chega nos sessenta,", B), ("olha pra trás e pergunta pra si mesmo:", B))
            + st(("cadê o dinheiro", B), ("de trinta anos de empresa?", R)), fs=40)
slide(at(4),  st(("Passou tudo pela mão.", B), ("O aluguel da loja, a folha, a escola dos filhos.", B))
            + st(("Entrou num dia,", B), ("saiu no outro.", R)), fs=40)
slide(at(5),  st(("E todo ano a mesma história.", B), ("A empresa faturou mais,", B), ("a folha cresceu, a estrutura cresceu.", B))
            + st(("E o que sobra pra você", B), ("continua sendo o mesmo: pró-labore.", R)), fs=40)
slide(at(6),  st(("O pior nem é o cansaço.", B), ("É fazer a conta.", B))
            + st(("Dos milhões faturados,", B), ("quanto disso virou patrimônio seu?", R)), fs=40)
slide(at(7),  st(("Se for sincero, quase nada.", B), ("Tudo o que a empresa ganhou, ela mesma consumiu.", B))
            + st(("O CNPJ FICOU GRANDE.", A), ("E O CPF CONTINUOU", A), ("DO MESMO TAMANHO.", A), mt=26), fs=37)
slide(at(8),  st(("Depois de 38 anos como empresário, eu te pergunto:", B), ("se a empresa só te paga 30, 40 mil de pró-labore,", B))
            + st(("qual a razão de ter empresa?", B), ("Melhor ser funcionário. Pelo menos não tem risco.", R)), fs=38)
slide(at(9),  st(("Tem empresário que faturou muito e não tem nada.", B), ("E tem quem faturou menos e hoje dorme tranquilo.", B))
            + st(("A diferença é que um entende", B), ("o modelo de negócio dele.", B), ("O outro viu o mercado mudar e nem percebeu.", R)), fs=38)
slide(at(10), st(("E pra quem é dono,", B), ("isso dói em dobro.", B))
            + st(("Porque você arriscou tudo o que tinha pra no fim", B), ("viver igual quem não arriscou nada.", R)), fs=40)
slide(at(11), st(("Então pergunta pra sua empresa:", B), ("depois de pagar tudo, inclusive você,", B), ("sobra alguma coisa?", B))
            + st(("Se você não sabe,", R), ("eu me preocuparia seriamente.", R)), fs=40)
slide(at(12), st(("Eu gravei uma aula mostrando como eu leio", B), ("uma empresa em poucos minutos.", B))
            + st(("Com as 15 perguntas que eu faço pra todo dono,", B), ("você enxerga por que a sua", R), ("não coloca dinheiro no seu bolso.", R)), fs=40)
slide(at(13), st(("Uma aula agora,", R), ("ou mais dez anos tirando o mesmo pró-labore.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">RAIO-X</span></div>\n'
            + st(("que eu te mando a aula no seu direct.", B), mt=18), fs=40)
