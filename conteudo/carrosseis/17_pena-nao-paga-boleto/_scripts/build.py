#!/usr/bin/env python3
"""Monta os 13 HTMLs do carrossel 17 (pena nao paga boleto) — ritmo facil, 2 frases/slide."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/17_pena-nao-paga-boleto/instagram")
DEST.mkdir(parents=True, exist_ok=True)

A_CAPA = 70    # slide 1, "E TER PENA DE FUNCIONARIO"
A_BOLETO = 96  # slide 11, "PENA NAO PAGA BOLETO"

# slide -> numero do arquivo de imagem (imagens reaproveitadas + novas 08-13)
IMG = {1: 1, 2: 2, 3: 8, 4: 9, 5: 10, 6: 11, 7: 3, 8: 4, 9: 12, 10: 13, 11: 5, 12: 6, 13: 7}

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
  .top{ position:absolute; left:0; right:0; padding:0 80px; text-align:center; z-index:2; }
  .bottom{ position:absolute; left:0; right:0; padding:0 80px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:44px; }
  .line{ font-size:44px; line-height:1.3; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:72px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:34px; font-weight:400; line-height:1.32; color:#1A1A1A; margin-top:16px; }
</style>
</head>
<body>
  <div class="slide">
"""
FOOT = """  </div>
</body>
</html>
"""


def photo(slide, fade=32, scale=None, bottom=0):
    n = IMG[slide]
    tr = f"transform:scale({scale});transform-origin:bottom center;" if scale else ""
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:{bottom}px;left:0;width:100%;mix-blend-mode:multiply;{tr}'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def photo_raised(slide, bottom=250, top_fade=26, bot_start=74):
    n = IMG[slide]
    mask = (f"linear-gradient(to bottom,transparent 0%,#000 {top_fade}%,"
            f"#000 {bot_start}%,transparent 100%)")
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:{bottom}px;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:{mask};mask-image:{mask};z-index:1;">\n')


def stanza(lines):
    inner = "".join(f'        <div class="line{" red" if r else ""}">{t}</div>\n' for t, r in lines)
    return f'      <div class="stanza">\n{inner}      </div>\n'


def block(slide, top, stanzas, fade=32, scale=None, bottom=0):
    body = "".join(stanza(s) for s in stanzas)
    return photo(slide, fade, scale, bottom) + f'    <div class="top" style="top:{top}px">\n{body}    </div>\n'


S = {}

# 1 — capa / gancho literal (texto mais alto, imagem empurrada pra baixo)
S[1] = photo(1, fade=30, bottom=-80) + f'''    <div class="top" style="top:296px">
      <div class="line" style="font-size:44px">O maior erro de um empres&aacute;rio</div>
      <div class="line anton" style="font-size:{A_CAPA}px;margin-top:20px">&Eacute; ter pena de funcion&aacute;rio.</div>
    </div>
'''

# 2 — a pena comeca pequena (imagem subida via escala pra o relogio preencher mais)
S[2] = block(2, 210, [[("A pena come&ccedil;a pequena.", False),
                       ("Voc&ecirc; releva um atraso, aceita uma desculpa.", False)]], scale=1.28)

# 3 — vira rotina
S[3] = block(3, 238, [[("Perdoa o erro que j&aacute; virou rotina.", False),
                       ("Segura quem devia ter sa&iacute;do h&aacute; meses.", False)]])

# 4 — parece bondade, prejuizo cresce
S[4] = block(4, 238, [[("Parece bondade.", False),
                       ("Mas o preju&iacute;zo s&oacute; cresce no escuro.", True)]])

# 5 — nao e so voce que paga
S[5] = block(5, 238, [[("E n&atilde;o &eacute; s&oacute; voc&ecirc; que paga essa conta.", False),
                       ("A cultura da empresa paga junto.", False)]])

# 6 — a cultura fragiliza / dois pesos
S[6] = block(6, 238, [[("A cultura vai se fragilizando.", False),
                       ("E o time inteiro percebe os dois pesos.", True)]])

# 7 — quem entrega paga (hero vermelho)
S[7] = block(7, 238, [[("Quem entrega resultado", False),
                       ("paga o erro de quem n&atilde;o entrega.", True)]])

# 8 — a demissao ja chega tarde
S[8] = block(8, 238, [[("E quando voc&ecirc; demite, j&aacute; foi tarde.", False),
                       ("O time j&aacute; tinha tirado a conclus&atilde;o.", False)]])

# 9 — o recado fica
S[9] = block(9, 238, [[("Aqui, entregar ou n&atilde;o d&aacute; no mesmo.", False),
                       ("Ele vai embora, mas o recado fica.", True)]])

# 10 — empatia nao decide
S[10] = block(10, 238, [[("Empatia importa, e muito.", False),
                         ("Mas ela n&atilde;o decide por voc&ecirc;.", False)]])

# 11 — gestao se faz com criterio + Anton grito
S[11] = photo(11, 30) + f'''    <div class="top" style="top:180px">
      <div class="stanza">
        <div class="line" style="font-size:40px">Gest&atilde;o n&atilde;o se faz com d&oacute;, se faz com crit&eacute;rio.</div>
      </div>
      <div class="stanza">
        <div class="line">Resultado, comprometimento,</div>
        <div class="line">disciplina e responsabilidade.</div>
      </div>
      <div class="line anton" style="font-size:{A_BOLETO}px;margin-top:46px">Pena n&atilde;o paga boleto.</div>
    </div>
'''

# 12 — voce concorda? (engajamento)
S[12] = photo(12, 30) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line">E voc&ecirc;, concorda?</div>
      </div>
      <div class="stanza">
        <div class="line">Os empres&aacute;rios demoram a demitir por pena?</div>
        <div class="line">Ou o problema &eacute; outro?</div>
      </div>
      <div class="stanza">
        <div class="line red">Comenta aqui a sua opini&atilde;o.</div>
      </div>
    </div>
'''

# 13 — CTA (treinamento)
S[13] = '''    <div class="top" style="top:196px">
      <div class="stanza">
        <div class="line">Eu tenho um treinamento de gest&atilde;o</div>
        <div class="line">pra dono de pequena e m&eacute;dia empresa.</div>
      </div>
      <div class="stanza">
        <div class="line">Onde ensino como gerar resultado</div>
        <div class="line">atrav&eacute;s de pessoas.</div>
      </div>
    </div>
''' + photo_raised(13, bottom=250, top_fade=26, bot_start=74) + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">CULTURA</span>,</div>
      <div class="cta-sm">que eu te chamo no seu direct.</div>
    </div>
'''

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
