#!/usr/bin/env python3
"""Gera os 10 HTMLs do carrossel 90 (editorial-punch, "o óbvio do dono"). Layout do modelo.md: corpo top:160, capa ~200."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
try: HEIGHT = {int(k): v for k, v in json.loads((SCR/"imgheight.json").read_text()).items()}
except FileNotFoundError: HEIGHT = {}
HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,700&display=swap" rel="stylesheet">
<style>
  *{ margin:0; padding:0; box-sizing:border-box; }
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; }
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""
def img(n, fade=26):
    h = HEIGHT.get(n)
    box = f'height:{h}px;object-fit:cover;object-position:center bottom;' if h else ''
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')
def slide(n, body, fade=26, top=160, fs=None):
    override = f'<style>.line{{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = [f'        <div class="line{cls}">{txt}</div>' for txt, cls in lines]
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R = "", " red"

slide(1, st(("O óbvio", R), ("tem que ser dito.", R)), top=200, fs=66)
slide(2, st(("O caixa fechou errado de novo.", B), ("O cliente esperou um retorno que não veio.", B)) + st(("E você solta a frase de sempre:", B), ("“gente, isso é óbvio!”", R)))
slide(3, st(("Óbvio pra quem?", B)) + st(("Você faz do seu jeito há vinte anos.", B), ("E o funcionário entrou em março.", R)))
slide(4, st(("Cada “óbvio” que você grita", B), ("é uma regra que só existe na sua cabeça.", B)) + st(("Nunca foi escrita. Nunca foi treinada.", B), ("Só foi cobrada.", R)))
slide(5, st(("Aí você conclui o de sempre:", B), ("“ninguém pensa, ninguém se importa”.", B)) + st(("Troca o funcionário.", B), ("O próximo erra no mesmo lugar.", R)))
slide(6, st(("Se é óbvio pra você e ninguém faz,", B), ("não é óbvio. É segredo.", R)), fs=48)
slide(7, st(("Ser dono é tirar o óbvio da cabeça", B), ("e colocar na parede da empresa.", B)) + st(("Escrever. Mostrar. Repetir.", B), ("Cobrar do mesmo jeito toda semana.", R)))
slide(8, st(("Clareza não é o que você disse.", B), ("É o que o time repete", R), ("quando você não está.", R)), fs=46)
slide(9, st(("Padrão escrito, ensinado", B), ("e cobrado toda semana.", B), ("Isso é gestão, o básico que funciona.", B)) + st(("O resto é o dono gritando “óbvio”", B), ("de uma regra que só ele conhece.", R)))
cta = (st(("É isso que eu ensino no meu treinamento", B), ("de gestão pra pequena e média empresa.", B))
       + '      <div class="cta-big" style="margin-top:44px">Comenta <span class="red">OBVIO</span></div>\n'
       + st(("e eu te mando o link no direct.", R), mt=20))
slide(10, cta)
