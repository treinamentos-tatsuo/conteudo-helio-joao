#!/usr/bin/env python3
"""Monta os HTMLs dos 16 slides da FABULA toupeira (carrossel 25).
Sistema v2 (feedback 2026-08-06): texto compacto (gap 1.15em, top 175px),
gravura dominante. Slide 15 (moral) mantém o layout aprovado (top 190 / gap 1.95)."""
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
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    display:flex; flex-direction:column; align-items:center;
    background:#FBF9F4 url("../../_banco-referencias/elementos/moldura-fabula.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; color:#1F1B16; }
  .text{ margin-top:%(mt)spx; padding:0 78px; text-align:center;
    font-weight:400; font-size:%(fs)spx; line-height:%(lh)s; z-index:2; }
  .stanza + .stanza{ margin-top:%(gap)sem; }
  .text b{ font-weight:700; }
  .ilustra-box{ margin-top:28px; margin-bottom:60px; width:915px; flex:1 1 auto; min-height:0; z-index:1; }
  .ilustra-box img{ width:100%%; height:100%%; object-fit:cover; display:block; mix-blend-mode:multiply;
    -webkit-mask-image:
      linear-gradient(to right, transparent 0, #000 7%%, #000 93%%, transparent 100%%),
      linear-gradient(to bottom, transparent 0, #000 6%%, #000 94%%, transparent 100%%);
    -webkit-mask-composite: source-in; mask-composite: intersect; }
</style>
</head>
<body>
<div class="slide">
  <div class="text">
%(stanzas)s  </div>
  <div class="ilustra-box"><img src="../imagens/img-%(n)02d.png" alt=""></div>
</div>
</body>
</html>
"""

CAPA = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap" rel="stylesheet">
<style>
  html,body{margin:0;padding:0;}
  .slide{
    width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#FBF9F4 url("../../_banco-referencias/elementos/moldura-fabula.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; color:#1F1B16;
  }
  .text{
    position:absolute; top:215px; left:0; right:0; padding:0 90px;
    text-align:center; z-index:2;
  }
  .title{ font-size:64px; font-weight:700; font-style:normal; line-height:1.05; white-space:nowrap; }
  .sub{ font-size:35px; font-weight:400; line-height:1.34; margin-top:30px; color:#2c281f; }
  .ilustra-box{
    position:absolute; left:81px; width:915px; top:490px; height:780px; z-index:1;
  }
  .ilustra-box img{
    width:100%; height:100%; object-fit:cover; display:block; mix-blend-mode:multiply;
    -webkit-mask-image:
      linear-gradient(to right, transparent 0, #000 7%, #000 93%, transparent 100%),
      linear-gradient(to bottom, transparent 0, #000 6%, #000 94%, transparent 100%);
    -webkit-mask-composite: source-in; mask-composite: intersect;
  }
</style>
</head>
<body>
<div class="slide">
  <div class="text">
    <div class="title">O Empresário Toupeira.</div>
    <div class="sub">Uma pequena fábula para pequenos<br>e médios empresários</div>
  </div>
  <div class="ilustra-box"><img src="../imagens/img-01.png" alt=""></div>
</div>
</body>
</html>
"""

TIGHT = {"mt": 175, "lh": "1.42", "gap": "1.15"}
ROOMY = {"mt": 190, "lh": "1.5", "gap": "1.95"}   # layout aprovado da moral

# (n, font-size, params, [stanzas])
SLIDES = [
    (2, 40, TIGHT, ["Era uma vez, em Florestapitalista,<br>um empresário toupeira.",
             "Ninguém conhecia o próprio negócio como ele.<br>Cada túnel. Cada raiz. Cada palmo de terra."]),
    (3, 40, TIGHT, ["E nada ali acontecia longe dele.",
             "Cavava os túneis.<br>Vistoriava os estoques.<br>Resolvia cada problema com o próprio focinho."]),
    (4, 40, TIGHT, ["Ele trabalhava com o nariz<br>encostado em tudo.",
             "E tinha orgulho disso.",
             "&ldquo;Aqui embaixo, nada me escapa.&rdquo;"]),
    (5, 40, TIGHT, ["Mas as grandes decisões<br>viviam saindo erradas.",
             "Cavou na direção do pomar.<br>O pomar secou.",
             "<b>Parecia certo de perto.<br>Saiu errado no todo.</b>"]),
    (6, 40, TIGHT, ["E toda vez que algo dava errado, ele<br>fazia a única coisa que sabia fazer.",
             "Cavava mais.<br>Mais horas. Mais túneis. Mais fundo."]),
    (7, 40, TIGHT, ["Na beira do rio, trabalhava<br>uma garça empresária.",
             "Todo santo dia, de sol a sol, com os<br>pés na lama. Igual a todo mundo.",
             "<b>Menos numa coisa: ela nunca<br>era pega de surpresa.</b>"]),
    (8, 40, TIGHT, ["Ele não entendia.",
             "&ldquo;Ela trabalha na lama,<br>igual eu trabalho na terra.&rdquo;",
             "&ldquo;Por que as escolhas dela dão certo...<br>e as minhas não?&rdquo;"]),
    (9, 40, TIGHT, ["Então ele passou a observar.",
             "E percebeu um padrão.",
             "Antes de qualquer decisão...<br><b>a garça subia.</b>"]),
    (10, 40, TIGHT, ["Um dia, a garça o levou pra cima.",
              "E ele viu o tronco.<br>Depois, a árvore inteira.<br>Depois... a floresta."]),
    (11, 40, TIGHT, ["Lá de cima, ele viu o rio mudando de curso.<br>Viu o lado da floresta que estava morrendo.",
              "<b>Ele cavava ali a vida inteira.<br>E nunca tinha visto a floresta.</b>"]),
    (12, 40, TIGHT, ["E ali, no alto, ele entendeu.",
              "Com o nariz encostado no tronco, ele<br>nem sabia que aquilo era uma árvore.",
              "<b>De tão perto, ele sabia tudo.<br>E não enxergava nada.</b>"]),
    (13, 40, TIGHT, ["E de repente, cada erro fez sentido.",
              "O pomar secou porque<br>o rio mudou de curso.",
              "<b>A resposta nunca esteve dentro<br>do túnel. Estava no todo.</b>"]),
    (14, 40, TIGHT, ["Ele não largou a terra.<br>Continuou cavando todos os dias.",
              "Porque é dentro do túnel<br>que se sente o negócio.",
              "<b>Mas é lá de cima que se<br>decide onde cavar.</b>"]),
    (15, 38, ROOMY, ["<b>Moral da história.</b>",
              "Talvez você não decida errado<br>por falta de esforço.",
              "Talvez esteja com o nariz tão encostado na<br>sua empresa que já não consegue enxergá-la.",
              "Quem está grudado na operação<br>enxerga apenas um palmo.<br><b>E decide o todo com a visão de um palmo.</b>"]),
    (16, 38, TIGHT, ["A sua empresa é uma floresta.<br>Venda, margem, time, caixa.<br>Está tudo ligado em tudo.",
              "<b>Se afastar não é abandonar a operação.<br>É enxergar o todo.</b>",
              "<b>Comente 307 se você entendeu.</b>"]),
]

(OUT / "slide-01.html").write_text(CAPA)
print("slide-01.html (capa)")
for n, fs, params, stanzas in SLIDES:
    body = "".join(f'    <div class="stanza">{s}</div>\n' for s in stanzas)
    ctx = {"fs": fs, "stanzas": body, "n": n}
    ctx.update(params)
    (OUT / f"slide-{n:02d}.html").write_text(HEAD % ctx)
    print(f"slide-{n:02d}.html")
print("OK")
