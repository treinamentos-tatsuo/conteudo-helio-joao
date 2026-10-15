#!/usr/bin/env python3
"""Monta os 17 HTMLs do carrossel 69 (FABULA visual, sem Florestapitalista)."""
import pathlib

OUT = pathlib.Path(__file__).parent.parent / "instagram"
OUT.mkdir(parents=True, exist_ok=True)

HEAD = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
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
  .ilustra-box.duo img:nth-child(1){ object-position:60%% center; }
  .ilustra-box.duo img:nth-child(2){ object-position:20%% center; }
  .ilustra-box.wide{ max-height:830px; margin-top:auto; }
  .ilustra-box.wide img{ object-position:40%% center; }
  .oq{ margin-left:-0.415em; }   /* aspa de abertura pendurada (medida em Source Serif Pro 400) */
  .cq{ margin-right:-0.430em; }  /* aspa de fechamento pendurada (medida em Source Serif Pro 700) */
</style></head>
<body><div class="slide">
%(body)s
%(ilustra)s
</div></body></html>
"""

BG = ('background:#FBF9F4 url("../../_banco-referencias/elementos/moldura-fabula.png") '
      'center/cover no-repeat;')

CSS_CAPA = """  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    %(bg)s
    font-family:'Source Serif Pro',serif; color:#1F1B16; }
  .text{ position:absolute; top:215px; left:0; right:0; padding:0 80px; text-align:center; z-index:2; }
  .title{ font-size:%(ts)dpx; font-weight:700; line-height:1.05; white-space:nowrap; }
  .sub{ font-size:35px; font-weight:400; line-height:1.34; margin-top:30px; color:#2c281f; }
  .ilustra-box{ position:absolute; left:81px; width:915px; top:490px; height:780px; z-index:1; }""" % {
    "bg": BG, "ts": 62}

CSS_CONT = """  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    display:flex; flex-direction:column; align-items:center;
    %(bg)s
    font-family:'Source Serif Pro',serif; color:#1F1B16; }
  .text{ margin-top:175px; padding:0 78px; text-align:center;
    font-weight:400; font-size:40px; line-height:1.42; z-index:2; }
  .stanza + .stanza{ margin-top:1.15em; }
  .text b{ font-weight:700; }
  .ilustra-box{ margin-top:28px; margin-bottom:60px; width:915px; flex:1 1 auto; min-height:0; z-index:1; }""" % {
    "bg": BG}

CAPA = ('  <div class="text">\n'
        '    <div class="title">A teoria do cavalo teimoso.</div>\n'
        '    <div class="sub">Uma pequena fábula para pequenos<br>e médios empresários</div>\n'
        '  </div>')

SLIDES = {
 2:  ["Certa vez, um homem levou<br>o seu cavalo até o rio."],
 3:  ["Água limpa. Brisa fresca.", "<b>Tudo perfeito.</b>"],
 4:  ["Ele tinha certeza de que o cavalo ia beber.",
      '<span class="oq">&ldquo;</span>O bicho está cansado, deve estar com sede.<br>'
      '<b>Essa água vai fazer bem pra ele.<span class="cq">&rdquo;</span></b>'],
 5:  ["Ele tinha boa intenção.", "<b>Ele se importava.</b>"],
 6:  ["Primeiro tentou no jeito.", "Puxou a rédea devagar. Bateu no pescoço.",
      "<b>Falou com o bicho<br>como quem pede um favor.</b>"],
 7:  ["Mas o cavalo não abaixou a cabeça.", "Não bebeu. Não se mexeu.",
      "<b>Simplesmente não estava com sede.</b>"],
 8:  ["O homem se irritou.", "Insistiu mais. Levantou a voz.",
      "<b>E tentou forçar o cavalo a beber.</b>"],
 9:  ["Só que quanto mais ele forçava,", "<b>mais o cavalo resistia.</b>"],
 10: ["Nenhum dos dois estava errado.", "<b>Mas os dois estavam sofrendo.</b>"],
 11: ["No fim, os dois ficaram exaustos.", "<b>E nada tinha mudado.</b>"],
 12: ["O homem tinha razão. A água era boa.", "<b>Só que ter razão<br>nunca fez ninguém beber.</b>"],
 13: ["Você pode levar alguém até o rio.", "Pode mostrar o caminho.<br>Pode dizer que a água é boa.",
      "<b>Mas não pode beber por essa pessoa.</b>"],
 14: ["E todo dono de empresa já tentou.", "<b>Beber no lugar do funcionário.</b>"],
 15: ["O seu papel é conduzir.", "<b>Não é arrastar.</b>"],
 16: ["Forçar alguém a mudar<br>não faz essa pessoa crescer.", "<b>Só faz vocês dois se acabarem.</b>"],
 17: ["As pessoas se movem<br>quando sentem sede.", "<b>E sede não se exige. Sede se cria.</b>"],
 18: ["Se hoje você é o único com sede<br>dentro da sua empresa,",
      "<b>talvez você ainda não tenha<br>despertado essa sede em ninguém.</b>"],
 19: ["Eu já fui esse homem puxando a corda.",
      "Levei mais de 38 anos de empresa pra aprender<br>que time não se arrasta. Se constrói.",
      "<b>Comenta FOME que eu te mostro<br>por onde essa construção começa.</b>"],
}

DUO = 10  # slide de diptico vertical (cara do homem x cara do cavalo)

def write(n, css, body):
    if n == DUO:
        il = ('  <div class="ilustra-box duo">'
              '<img src="../imagens/img-10a.png" alt="">'
              '<img src="../imagens/img-10b.png" alt=""></div>')
    else:
        cls = "ilustra-box wide" if n == 9 else "ilustra-box"
        il = f'  <div class="{cls}"><img src="../imagens/img-{n:02d}.png" alt=""></div>'
    (OUT / f"slide-{n:02d}.html").write_text(
        HEAD % {"slidecss": css, "body": body, "n": n, "ilustra": il}, encoding="utf-8")

write(1, CSS_CAPA, CAPA)
for n, stanzas in SLIDES.items():
    body = '  <div class="text">\n' + "\n".join(
        f'    <div class="stanza">{s}</div>' for s in stanzas) + "\n  </div>"
    write(n, CSS_CONT, body)
print(f"{len(SLIDES)+1} HTMLs em {OUT}")
