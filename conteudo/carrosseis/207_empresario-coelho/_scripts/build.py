#!/usr/bin/env python3
"""Monta os 17 HTMLs do carrossel 207 (FABULA, O Empresário Coelho)."""
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
  .kw{ font-size:1.5em; letter-spacing:0.04em; }
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
        '    <div class="title">O Empresário Coelho.</div>\n'
        '    <div class="sub">Uma pequena fábula para pequenos<br>e médios empresários</div>\n'
        '  </div>')

OQ = '<span class="oq">&ldquo;</span>'
CQ = '<span class="cq">&rdquo;</span>'

SLIDES = {
 2:  ["Era uma vez, na Florestapitalista,<br>um empresário coelho...", "<b>o mais rápido de toda a floresta.</b>"],
 3:  ["Ele acordava antes do sol.<br>Abria filial, contratava, fechava contrato.", "<b>E nunca parava.</b>"],
 4:  ["Foram vinte anos assim.<br>A empresa crescia e a floresta inteira aplaudia.", "<b>Mesmo assim, ele vivia com<br>a sensação de estar atrasado.</b>"],
 5:  ["Um dia, correndo por uma estrada<br>que nunca tinha pegado,<br>ele chegou numa encruzilhada.", "<b>Três caminhos, e nenhum ele conhecia.</b>"],
 6:  ["Sentado no alto de uma placa de madeira,<br>um gato velho olhava ele chegar.", "Sem fôlego, o coelho perguntou:<br><b>" + OQ + "Qual caminho eu sigo?" + CQ + "</b>"],
 7:  ["Mas o gato não respondeu.<br>Primeiro, fez outra pergunta:", "<b>" + OQ + "Pra onde você quer ir?" + CQ + "</b>"],
 8:  ["O coelho olhou pra um lado.<br>Depois olhou pro outro.", "Pensou um pouco e respondeu:<br><b>" + OQ + "Eu não sei." + CQ + "</b>"],
 9:  ["Então o gato deu de ombros e disse:", "<b>" + OQ + "Se você não sabe pra onde quer ir,<br>qualquer caminho serve." + CQ + "</b>"],
 10: ["O coelho olhou pra trás.<br>20 anos de estrada, mais rápido<br>que qualquer bicho da floresta.", "<b>E nunca tinha escolhido pra onde ir.</b>"],
 11: ["Pra ele, correr nunca foi o problema.", "<b>Mas quanto mais rápido ele corria<br>na direção errada, mais longe ficava<br>da vida que queria.</b>"],
 12: ["<b>Moral da história:</b>", "Talvez você não esteja insatisfeito<br>porque escolheu o caminho errado.", "<b>Talvez você nunca tenha decidido<br>aonde queria chegar.</b>"],
 13: ["Filial nova, time maior, faturamento subindo.<br>Tudo isso parece progresso.", "<b>Mas estar em movimento não significa<br>estar indo pra algum lugar.</b>"],
 14: ["Quando você sabe aonde quer chegar,<br>até o caminho errado se corrige:<br>você volta e muda a rota.", "<b>Sem destino, não existe caminho certo.<br>Existe só movimento.</b>"],
 15: ["E a maior tragédia de um empresário<br>não é ficar parado.", "<b>É passar vinte anos correndo<br>na direção errada.</b>"],
 16: ["No MBV, o meu treinamento,<br>eu ensino gestão pra dono de PME.", "<b>Pra cada ano de corrida deixar você<br>mais perto, e não mais longe.</b>"],
 17: ["Se você corre há anos e nunca<br>escreveu aonde quer chegar,", 'comente <b class="kw">NORTE</b><br>que eu mando o link no seu direct.'],
}

WIDE = {5, 13, 15}
POS = {2: "88% center", 13: "92% center", 17: "8% center"}  # reenquadra quando o coelho nasce na borda direita

def write(n, css, body):
    cls = "ilustra-box wide" if n in WIDE else "ilustra-box"
    st = f' style="object-position:{POS[n]}"' if n in POS else ''
    il = f'  <div class="{cls}"><img src="../imagens/img-{n:02d}.png" alt=""{st}></div>'
    (OUT / f"slide-{n:02d}.html").write_text(
        HEAD % {"slidecss": css, "body": body, "n": n, "ilustra": il}, encoding="utf-8")

write(1, CSS_CAPA, CAPA)
for n, stanzas in SLIDES.items():
    body = '  <div class="text">\n' + "\n".join(
        f'    <div class="stanza">{s}</div>' for s in stanzas) + "\n  </div>"
    write(n, CSS_CONT, body)
print(f"{len(SLIDES)+1} HTMLs em {OUT}")
