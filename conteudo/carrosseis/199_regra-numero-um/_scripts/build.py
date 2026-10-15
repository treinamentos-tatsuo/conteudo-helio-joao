#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 199 (editorial-punch, "Regra número um").
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

slide(at(1),  st(("Vou te falar uma verdade meio chata", B))
            + st(("SOBRE A MISSÃO", A), ("DE UM EMPRESÁRIO.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Gerar emprego. Servir o cliente.", B), ("Mudar o mundo.", B))
            + st(("NADA DISSO", A), ("VEM PRIMEIRO.", A), mt=22), fs=46)
slide(at(3),  st(("Todo palco ensina que empresário de verdade", B), ("vive de propósito.", B))
            + st(("Que falar de dinheiro pega mal.", B), ("E que o dono é sempre o último a receber.", R)), fs=40)
slide(at(4),  st(("E o dono acreditou.", B), ("A empresa fatura 20 milhões por ano,", B))
            + st(("tem 80 pessoas na folha, e o único dinheiro", B), ("que chega no bolso dele é o pró-labore.", R)), fs=40)
slide(at(5),  st(("Pró-labore paga o seu trabalho.", B), ("Isso qualquer gerente bom recebe.", B))
            + st(("Dividendo paga o seu risco:", B), ("o seu CPF amarrado no CNPJ.", R)), fs=42)
slide(at(6),  st(("Se é pra viver só de pró-labore,", B))
            + st(("MELHOR SER", A), ("EMPREGADO", A), ("DOS OUTROS.", A), mt=22), fs=46)
slide(at(7),  st(("Por isso, na pequena e média empresa,", B), ("tem uma regra que vem antes de tudo.", B))
            + st(("A regra número um:", B), ("a empresa tem que gerar dividendo pro dono.", R)), fs=40)
slide(at(8),  st(("E essa é a missão de verdade.", B), ("Porque empresa que não paga o dono", B))
            + st(("cobra dele todo santo dia.", B), ("Até ele ficar de saco cheio da própria empresa.", R)), fs=40)
slide(at(9),  st(("Dono de saco cheio não lidera.", B), ("Ele aguenta.", B))
            + st(("Adia o aumento, corta o treinamento,", B), ("e o time sente antes de qualquer conversa.", R)), fs=42)
slide(at(10), st(("Você quer pagar bem quem está com você.", B))
            + st(("MAS NINGUÉM DIVIDE", A), ("O QUE NÃO SOBRA.", A), mt=22), fs=46)
slide(at(11), st(("O emprego, o cliente bem servido,", B), ("o time prosperando: tudo isso é real.", B))
            + st(("Só que tudo isso é consequência.", B), ("Vem depois da regra número um.", R)), fs=42)
slide(at(12), st(("Empresa que paga o dono tem dono inteiro,", B), ("com vontade de construir na segunda-feira.", B))
            + st(("Ele paga bem, forma gente", B), ("e faz o time prosperar junto.", R)), fs=40)
slide(at(13), st(("E isso começa com uma pergunta", B), ("que todo dono tem que responder com número:", B))
            + st(("a minha empresa está me deixando", B), ("mais rico ou mais pobre?", R)), fs=40)
slide(at(14), st(("No MBV, o meu treinamento,", B), ("eu ensino gestão pra dono de PME:", B))
            + st(("Lucratividade, Crescimento e Cultura", B), ("pra empresa pagar o dono", R), ("e fazer o time prosperar.", R)), fs=42)
slide(at(15), st(("Empresa próspera faz gente próspera.", B), ("E começa pela regra número um.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PROSPERO</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=44)
