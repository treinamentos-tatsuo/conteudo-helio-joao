#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 125 (editorial-punch, "Convencer um adulto a fazer o trabalho dele" / COMBINADO).
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

slide(at(1),  st(("Ninguém te contou que 70%", B), ("da gestão de pessoas é isto:", B))
            + st(("CONVENCER UM ADULTO", A), ("A FAZER O TRABALHO DELE.", A)), top=280, fs=48)
slide(at(2),  st(("Sem ele achar que está sendo perseguido.", B), ("Sem ele achar que é pessoal.", B))
            + st(("Você paga, combina o serviço", B), ("e ainda tem que cobrar com jeito.", R)), fs=42)
slide(at(3),  st(("Cobrou o prazo, ele fechou a cara.", B), ("Cobrou de novo, virou “o chefe pega no meu pé”.", B))
            + st(("Na terceira vez", B), ("você já cobra pedindo desculpa.", R)), fs=40)
slide(at(4),  st(("Aí você para de cobrar pra não brigar", B), ("e chama isso de manter o clima.", B))
            + st(("O clima fica ótimo.", B), ("O trabalho, não.", R)))
slide(at(5),  st(("E ainda dorme achando que o problema é você:", B), ("“acho que eu não sei explicar”.", B))
            + st(("Você explicou.", B), ("O que faltou não foi explicação.", R)), fs=40)
slide(at(6),  st(("COBRANÇA SÓ VIRA", A), ("PESSOAL QUANDO", A), ("NÃO TEM COMBINADO.", A)))  # 3 linhas curtas em vez de Anton < 80 px (modelo, 11/09)
slide(at(7),  st(("Sem regra escrita, toda cobrança", B), ("é a sua opinião contra a dele.", B))
            + st(("E opinião contra opinião", B), ("é briga de gente, não gestão.", R)))
slide(at(8),  st(("Você cobra de memória: “eu já falei”.", B), ("Cobra quando lembra, quando irrita.", B))
            + st(("Cobrança de surpresa parece perseguição.", B), ("Porque é surpresa.", R)), fs=42)
slide(at(9),  st(("Com o combinado no papel,", B), ("você não cobra a pessoa. Cobra a página.", B))
            + st(("“Nós combinamos. Está aqui.”", B), ("Não é o seu humor. É o combinado.", R)), fs=42)
slide(at(10), st(("Mesma hora, mesmo número,", B), ("todo mundo na mesa.", B))
            + st(("Cobrado assim, todo dia,", B), ("ele não é perseguido. É acompanhado.", R)))
slide(at(11), st(("COBRANÇA SEM REGRA", A), ("É PERSEGUIÇÃO.", A)) + st(("COM RITO, É GESTÃO.", A)))
slide(at(12), st(("Adulto não precisa gostar de ser cobrado.", B), ("Precisa saber que não é sobre ele.", B))
            + st(("É sobre o combinado.", B), ("E o combinado quem escreve é você.", R)), fs=42)
slide(at(13), st(("Eu tenho um treinamento pra donos de PME", B), ("onde ensino a montar isso:", B))
            + st(("combinado no papel, número na mesa", B), ("e o rito que cobra sem virar briga.", R)), fs=42)
slide(at(14), st(("Cobrar não é perseguir.", B), ("É conferir o combinado.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">COMBINADO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", R), mt=24))
