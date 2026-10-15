#!/usr/bin/env python3
"""Monta os HTMLs do carrossel 41 (FABULA papagaio). Uso: build.py [n ...] — sem args, todos.
Layout FABULA v2 (2026-08-06): conteudo compacto 175/1.42/1.15em; moral com respiro 190/1.95em."""
import pathlib, sys

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
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
  .text{ margin-top:MTOPpx; padding:0 78px; text-align:center;
    font-weight:400; font-size:FSIZEpx; line-height:LHEIGHT; z-index:2; }
  .stanza + .stanza{ margin-top:SGAPem; }
  .text b{ font-weight:700; }
  .ilustra-box{ margin-top:28px; margin-bottom:60px; width:915px; flex:1 1 auto; min-height:0; z-index:1; }
  .ilustra-box img{ width:100%; height:100%; object-fit:cover; display:block; mix-blend-mode:multiply;
    -webkit-mask-image:
      linear-gradient(to right, transparent 0, #000 7%, #000 93%, transparent 100%),
      linear-gradient(to bottom, transparent 0, #000 6%, #000 94%, transparent 100%);
    -webkit-mask-composite: source-in; mask-composite: intersect; }
</style></head>
<body><div class="slide">
  <div class="text">
STANZAS
  </div>
  <div class="ilustra-box"><img src="../imagens/img-NN.png" alt=""></div>
</div></body></html>"""

CAPA = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap" rel="stylesheet">
<style>
  html,body{margin:0;padding:0;}
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#FBF9F4 url("../../_banco-referencias/elementos/moldura-fabula.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; color:#1F1B16; }
  .text{ position:absolute; top:215px; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .title{ font-size:60px; font-weight:700; line-height:1.05; white-space:nowrap; }
  .sub{ font-size:35px; font-weight:400; line-height:1.34; margin-top:30px; color:#2c281f; }
  .ilustra-box{ position:absolute; left:81px; width:915px; top:490px; height:780px; z-index:1; }
  .ilustra-box img{ width:100%; height:100%; object-fit:cover; display:block; mix-blend-mode:multiply;
    -webkit-mask-image:
      linear-gradient(to right, transparent 0, #000 7%, #000 93%, transparent 100%),
      linear-gradient(to bottom, transparent 0, #000 6%, #000 94%, transparent 100%);
    -webkit-mask-composite: source-in; mask-composite: intersect; }
</style></head>
<body><div class="slide">
  <div class="text">
    <div class="title">O Empresário Papagaio.</div>
    <div class="sub">Uma pequena fábula para pequenos<br>e médios empresários</div>
  </div>
  <div class="ilustra-box"><img src="../imagens/img-01.png" alt=""></div>
</div></body></html>"""

# layout: (margin-top, font-size, line-height, stanza-gap)
V2 = (175, 40, 1.42, 1.15)          # conteudo compacto (imagem dominante)
V2_38 = (175, 38, 1.42, 1.15)       # conteudo com mais texto
V2_36 = (175, 36, 1.42, 1.15)       # slide 12 (o mais textual fora a moral)
MORAL = (190, 38, 1.5, 1.95)        # respiro do gabarito

SLIDES = {
    2: (V2, ['Era uma vez um empresário...',
             'que tinha as <b>palavras mais bonitas</b><br>de toda a Florestapitalista.']),
    3: (V2, ['A loja dele era a prova viva.',
             'Paredes cheias de valores e princípios:',
             '<b>regras emolduradas em cada canto.</b>']),
    4: (V2, ['Todo dia, o mesmo discurso:',
             '"Aqui a gente atende bem.<br>Aqui ninguém se atrasa."',
             'O time ouvia. O time concordava.<br><b>E o time fazia igual sempre fez.</b>']),
    5: (V2, ['Bastava o papagaio cruzar a porta.',
             'O balcão esfriava. O cliente esperava.',
             '<b>As palavras ficavam na parede.<br>Nenhuma descia pro balcão.</b>']),
    6: (V2, ['Ele fez o que todo papagaio faz.',
             'Falou mais alto. Repetiu o discurso.<br>Pendurou mais quadros.',
             '<b>A parede encheu.<br>O comportamento nem se mexeu.</b>']),
    7: (V2, ['Até o dia em que ele entrou<br>no armazém das formigas.',
             'Ninguém dava ordem. Ninguém ficava parado.<br>Cada uma sabia a sua parte.',
             '<b>E tudo funcionava.</b>']),
    8: (V2, ['O papagaio procurou os cartazes. Nada.',
             'Procurou o manual. Nada.',
             '<b>"Onde está escrito como se faz?"</b>']),
    9: (V2, ['Ele voltou no dia seguinte. E no outro.',
             'E o padrão era sempre o mesmo:<br>a formiga velha fazia,<br>a formiga nova repetia.',
             '<b>Ninguém precisava mandar.</b>']),
    10: (V2, ['"Onde está escrita a cultura<br>desta casa?", perguntou.',
              'A formiga mais velha estranhou a pergunta.',
              '<b>"Cultura, aqui, não se lê. Se vê."</b>']),
    11: (V2, ['Foi quando o papagaio entendeu.',
              'Ele falava a cultura.<br>As formigas viviam a cultura.',
              '<b>E cultura que precisa de cartaz<br>pra lembrar ainda não é cultura.</b>']),
    12: (V2_36, ['Ele voltou pra loja e tirou<br>os quadros da parede.',
                 'No lugar de repetir palavras,<br>passou a repetir gestos:<br>chegava primeiro, atendia junto,<br>corrigia na hora.',
                 '<b>Todo dia. Até o time fazer sem pensar.</b>']),
    13: (V2_38, ['Meses depois, ele parou na calçada<br>e espiou a própria vitrine.',
                 'O cliente bem atendido.<br>O balcão vivo. Ninguém mandando.',
                 '<b>A regra mais forte da loja<br>era uma que ninguém escreveu.</b>']),
    14: (MORAL, ['E aqui fica a moral da história<br>do empresário papagaio:',
                 'cultura não é o que está na parede,<br>nem o que se fala na reunião.',
                 '<b>Cultura é o que o seu time faz sem pensar.<br>Principalmente quando ninguém está olhando.</b>']),
    15: (V2, ['Se na sua empresa o certo só acontece<br>com você por perto,',
              'você ainda não tem cultura.',
              '<b>Tem vigilância.</b>']),
    16: (V2, ['Agora, se você quer parar de decorar parede<br>e começar a formar comportamento...',
              '<b>comenta PAPAGAIO<br>que eu te mostro por onde começar.</b>']),
}

only = [int(a) for a in sys.argv[1:]] or None

for n in range(1, 17):
    if only and n not in only:
        continue
    if n == 1:
        html = CAPA
    else:
        (mtop, fsize, lh, gap), stanzas = SLIDES[n]
        body = "\n".join(f'    <div class="stanza">{s}</div>' for s in stanzas)
        html = (HEAD.replace("MTOP", str(mtop)).replace("FSIZE", str(fsize))
                .replace("LHEIGHT", str(lh)).replace("SGAP", str(gap))
                .replace("STANZAS", body).replace("NN", f"{n:02d}"))
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html OK")
