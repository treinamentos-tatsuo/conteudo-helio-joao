#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 118 (FABULA visual, humanos, sem Florestapitalista). Base: build.py do 69."""
import pathlib
OUT = pathlib.Path(__file__).parent.parent / "instagram"; OUT.mkdir(parents=True, exist_ok=True)
HEAD = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap" rel="stylesheet">
<style>
  html,body{margin:0;padding:0;}
%(slidecss)s
  .ilustra-box img{ width:100%%; height:100%%; object-fit:cover; display:block; mix-blend-mode:multiply;
    -webkit-mask-image:
      linear-gradient(to right, transparent 0, #000 7%%, #000 93%%, transparent 100%%),
      linear-gradient(to bottom, transparent 0, #000 6%%, #000 94%%, transparent 100%%);
    -webkit-mask-composite: source-in; mask-composite: intersect; }
  .ilustra-box.duo{ display:flex; gap:16px; }
  .ilustra-box.duo img{ width:calc(50%% - 8px); }
  .ilustra-box.duo img:nth-child(1){ object-position:%(dp1)s center; }
  .ilustra-box.duo img:nth-child(2){ object-position:%(dp2)s center; }
  .ilustra-box.wide{ max-height:830px; margin-top:auto; }
  .ilustra-box.sq img{ object-fit:contain; }
  .oq{ margin-left:-0.415em; } .cq{ margin-right:-0.430em; }
  .moral-title{ font-weight:700; font-size:44px; }
</style></head><body><div class="slide">
%(body)s
%(ilustra)s
</div></body></html>
"""
BG = 'background:#FBF9F4 url("../../_banco-referencias/elementos/moldura-fabula.png") center/cover no-repeat;'
CSS_CAPA = """  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden; %(bg)s font-family:'Source Serif Pro',serif; color:#1F1B16; }
  .text{ position:absolute; top:215px; left:0; right:0; padding:0 80px; text-align:center; z-index:2; }
  .title{ font-size:60px; font-weight:700; line-height:1.05; white-space:nowrap; }
  .sub{ font-size:35px; font-weight:400; line-height:1.34; margin-top:30px; color:#2c281f; }
  .ilustra-box{ position:absolute; left:81px; width:915px; top:490px; height:780px; z-index:1; }""" % {"bg": BG}
CSS_CONT = """  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden; display:flex; flex-direction:column; align-items:center; %(bg)s font-family:'Source Serif Pro',serif; color:#1F1B16; }
  .text{ margin-top:175px; padding:0 78px; text-align:center; font-weight:400; font-size:40px; line-height:1.42; z-index:2; }
  .stanza + .stanza{ margin-top:1.15em; }
  .text b{ font-weight:700; }
  .ilustra-box{ margin-top:28px; margin-bottom:60px; width:915px; flex:1 1 auto; min-height:0; z-index:1; }""" % {"bg": BG}
CSS_MORAL = CSS_CONT.replace("margin-top:175px", "margin-top:190px").replace("font-size:40px", "font-size:38px").replace("margin-top:1.15em", "margin-top:1.4em")

CAPA = ('  <div class="text">\n    <div class="title">A aposta dos dois lenhadores.</div>\n'
        '    <div class="sub">Uma pequena fábula para pequenos<br>e médios empresários</div>\n  </div>')
OQ, CQ = '<span class="oq">&ldquo;</span>', '<span class="cq">&rdquo;</span>'
SLIDES = {
 2:  ["Dois lenhadores fizeram uma aposta.", "<b>Quem derrubava mais árvores<br>até o sol se pôr.</b>"],
 3:  ["Um tinha 25 anos.<br>Forte. Rápido. Incansável.", "O outro tinha 70.", "<b>E a cara de quem já viu muita coisa.</b>"],
 4:  ["Deu o sinal e o jovem<br>saiu derrubando tudo.", "Uma. Duas. Dez.", "<b>Não parou nem pra beber água.</b>"],
 5:  ["O velho também derrubava.", "<b>Mas de tempo em tempo ele parava.</b>"],
 6:  ["O jovem olhava de longe e ria.", f"<b>{OQ}Esse aí já cansou.<br>Essa aposta é minha.{CQ}</b>"],
 7:  ["O velho voltava. Derrubava mais umas.", "Parava de novo. Voltava de novo.", "<b>E o jovem batendo, batendo, batendo.</b>"],
 8:  ["O sol se pôs e contaram as árvores.", "<b>O velho tinha derrubado mais.</b>"],
 9:  ["O jovem ficou sem entender.", f"{OQ}Mas eu vi você parando.<br>O que você fazia enquanto você parava?", f"<b>Eu tinha certeza que eu ganhava<br>essa competição.{CQ}</b>"],
 10: ["O velho respondeu, sem pressa:", f"<b>{OQ}Eu afiava o machado.{CQ}</b>"],
 11: ["O jovem deu mais golpes do que o velho.", "<b>Só que cada golpe dele valia menos.</b>"],
 12: ['<span class="moral-title">Moral da história</span>',
      "Talvez você também não esteja parando.<br>Doze horas por dia, vendendo,<br>atendendo, apagando incêndio.", "<b>E batendo com o machado cego.</b>"],
 13: ["Pro dono de empresa, afiar o machado<br>é parar pra aprender.", "<b>Aprender a administrar a empresa<br>que você mesmo abriu.</b>"],
 14: ["Força você tem. Garra você tem.", "<b>O que cansa você não é o trabalho.<br>É o machado cego.</b>"],
 15: ["Eu parei pra afiar depois<br>de muito golpe em vão.", "Hoje é o que eu faço com dono<br>de empresa na imersão MBV.", "<b>Comenta MACHADO que eu te mostro o caminho.</b>"],
}
DUO, WIDE, SQ = 3, {2, 5, 8}, {7}
POS = {"dp1": "50%", "dp2": "50%", 2: "50%", 8: "50%"}  # object-position, ajustar após ver as gravuras

def write(n, css, body):
    if n == DUO:
        il = '  <div class="ilustra-box duo"><img src="../imagens/img-3a.png" alt=""><img src="../imagens/img-3b.png" alt=""></div>'
    else:
        cls = "ilustra-box" + (" wide" if n in WIDE else "") + (" sq" if n in SQ else "")
        st = f' style="object-position:{POS[n]} center"' if n in POS else ""
        il = f'  <div class="{cls}"><img src="../imagens/img-{n:02d}.png" alt=""{st}></div>'
    (OUT / f"slide-{n:02d}.html").write_text(HEAD % {"slidecss": css, "body": body, "ilustra": il, "dp1": POS["dp1"], "dp2": POS["dp2"]}, encoding="utf-8")

write(1, CSS_CAPA, CAPA)
for n, st in SLIDES.items():
    body = '  <div class="text">\n' + "\n".join(f'    <div class="stanza">{s}</div>' for s in st) + "\n  </div>"
    write(n, CSS_MORAL if n == 12 else CSS_CONT, body)
print(f"{len(SLIDES)+1} HTMLs em {OUT}")
