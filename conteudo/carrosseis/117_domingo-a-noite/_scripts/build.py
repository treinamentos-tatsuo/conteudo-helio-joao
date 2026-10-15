#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 117 (editorial-punch, "Domingo à noite").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; capa setup serif + grito Anton)."""
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
  .whisper{ font-size:36px; font-weight:700; color:#A91C20; line-height:1.3; margin-top:14px; }
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
    override = f'<style>.line:not(.anton):not(.whisper){{font-size:{fs}px}}</style>\n' if fs else ""
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

slide(at(1),  st(("Seu funcionário conta os minutos pra ir embora.", B), ("E você chama isso de falta de vontade.", " whisper")), top=280, fs=38)
slide(at(2),  st(("Domingo, sete da noite,", B), ("o cara já está com o peito apertado.", B))
            + st(("A música do Fantástico é um terror pra ele.", R)), fs=42)
slide(at(3),  st(("Não é preguiça. Você sabe.", B), ("Já sentiu isso antes de ser dono.", B))
            + st(("É a sua empresa", B), ("que ele não quer ver na segunda.", R)))
slide(at(4),  st(("Segunda: cara amarrada, bom dia pela metade,", B), ("olho no relógio a cada dez minutos.", B)), fs=42)
slide(at(5),  st(("Esse povo não quer nada?", B), ("Quer sim. Ele só não quer o que <span class=\"red\">você</span> oferece.", B)), fs=42)
slide(at(6),  st(("Ninguém odeia trabalhar.", B), ("Odeia o lugar. A cobrança sem sentido.", B), ("O clima de velório.", B))
            + st(("Odeia ralar o dia inteiro, não ser reconhecido", B), ("e ainda ganhar mal.", R)), fs=40)
slide(at(7),  st(("A TRISTEZA", A), ("DO DOMINGO À NOITE", A), ("É O DIAGNÓSTICO", A), ("DA SUA EMPRESA.", A)))
slide(at(8),  st(("Isso não é humor de funcionário.", B), ("É atestado do clima que você permite.", R))
            + st(("Ninguém acorda animado pra bater ponto.", B), ("Acorda pra fazer parte de algo.", B)), fs=42)
slide(at(9),  st(("Gente só acorda com vontade pra um lugar", B))
            + st(("onde aprende,", B), ("ganha bem,", B), ("tem orgulho do que faz", B), ("e ainda por cima se diverte.", R)), fs=42)
slide(at(10), st(("TESTE RÁPIDO COM VOCÊ:", A))
            + st(("1. Seu funcionário aprende aí dentro?", B), ("Sabe mais hoje do que há um ano?", B))
            + st(("2. Dá pra sonhar com o salário que você paga?", B), ("Tem perspectiva de ganhar mais aí dentro?", R)), fs=40)
slide(at(11), st(("3. Ele enche a boca pra dizer onde trabalha?", B), ("Ou disfarça?", B))
            + st(("4. Tem gente rindo na sua empresa?", B), ("Ou só quando você sai da sala?", R)), fs=40)
slide(at(12), st(("Quantos dos quatro você garante hoje?", B))
            + st(("Se a resposta é nenhum,", B), ("a música do Fantástico vai continuar", B), ("batendo ponto na sua empresa.", R)), fs=42)
slide(at(13), st(("CLIMA RUIM", A), ("TEM DONO.", A)))
slide(at(14), st(("Time que chega na segunda com vontade", B), ("não é sorte. É liderança.", R)))
slide(at(15), st(("Quer aprender a aplicar esses quatro pilares", B), ("na prática, comigo?", B))
            + st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino exatamente isso.", R)), fs=42)
slide(at(16), st(("Domingo à noite, alguém do seu time", B), ("está com o peito apertado. Por sua causa.", R))
            + '      <div class="cta-big" style="margin-top:40px">Comenta <span class="red">CLIMA</span></div>\n'
            + st(("que eu te mando o link no seu direct.", B), mt=12), fs=42)
