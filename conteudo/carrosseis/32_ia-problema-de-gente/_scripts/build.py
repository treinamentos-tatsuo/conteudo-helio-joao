#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 32 (quero ver a IA resolver o seu problema de gente)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/32_ia-problema-de-gente")
DEST = BASE / "instagram"
DEST.mkdir(parents=True, exist_ok=True)
FITP = pathlib.Path(__file__).parent / "antonfit.json"
FIT = json.loads(FITP.read_text()) if FITP.exists() else {}

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
  .top{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:46px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .impact{ font-size:48px; font-weight:700; line-height:1.28; color:#1A1A1A; }
  .cta-big{ font-size:74px; font-weight:700; line-height:1.2; color:#1A1A1A; }
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


def photo(n, fade=24):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


S = {}

# 1 — capa (a isca): impacto 2 linhas + punch vermelho
S[1] = photo(1, fade=22) + '''    <div class="top" style="top:290px">
      <div class="stanza">
        <div class="impact" style="white-space:nowrap">A IA vai acelerar a sua empresa inteira.</div>
      </div>
      <div class="stanza" style="margin-top:26px">
        <div class="line red" style="white-space:nowrap">Menos o problema que mais te cansa.</div>
      </div>
    </div>
'''

# 2 — o tapa (grito puro, Anton, 1 linha)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:300px">
      <div class="line anton" style="font-size:{FIT.get("2", 100)}px">O SEU PROBLEMA DE GENTE.</div>
    </div>
'''

# 3 — credito a tecnologia 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E eu n&atilde;o sou contra a tecnologia.</div>
        <div class="line">Eu uso. Eu recomendo.</div>
      </div>
      <div class="stanza">
        <div class="line">Na maioria das &aacute;reas,</div>
        <div class="line red">ela faz melhor que muita gente.</div>
      </div>
    </div>
'''

# 4 — a dor de gente 2+2
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Mas o que te tira o sono</div>
        <div class="line">n&atilde;o &eacute; processo.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; explicar a mesma coisa mil vezes.</div>
        <div class="line red">&Eacute; o time que s&oacute; anda empurrado.</div>
      </div>
    </div>
'''

# 5 — a esperanca escondida 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E no fundo voc&ecirc; olha pra IA</div>
        <div class="line">com uma esperan&ccedil;a escondida:</div>
      </div>
      <div class="stanza">
        <div class="line red">finalmente depender</div>
        <div class="line red">menos de gente.</div>
      </div>
    </div>
'''

# 6 — a seducao no pico 2+2
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E a vantagem &eacute; real.</div>
        <div class="line">Acabou a pregui&ccedil;a. Acabou a falta.</div>
      </div>
      <div class="stanza">
        <div class="line">Acabou a limita&ccedil;&atilde;o t&eacute;cnica.</div>
        <div class="line red">M&aacute;quina n&atilde;o tem dia ruim.</div>
      </div>
    </div>
'''

# 7 — a quebra 2+2
S[7] = photo(7, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Pois essa conta n&atilde;o fecha.</div>
        <div class="line">A IA n&atilde;o resolve cultura.</div>
      </div>
      <div class="stanza">
        <div class="line">N&atilde;o forma l&iacute;der. N&atilde;o segura cliente.</div>
        <div class="line red">E n&atilde;o engaja ningu&eacute;m.</div>
      </div>
    </div>
'''

# 8 — pedrada 2+2
S[8] = photo(8, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ela responde em segundos</div>
        <div class="line">qualquer pergunta do mundo.</div>
      </div>
      <div class="stanza">
        <div class="line">Menos por que o seu melhor</div>
        <div class="line red">funcion&aacute;rio pediu demiss&atilde;o.</div>
      </div>
    </div>
'''

# 9 — reveal (so o lider) 2+2
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Problema de gente n&atilde;o se automatiza.</div>
        <div class="line">Problema de gente se lidera.</div>
      </div>
      <div class="stanza">
        <div class="line">E quem faz isso &eacute; o l&iacute;der.</div>
        <div class="line red">S&oacute; o l&iacute;der.</div>
      </div>
    </div>
'''

# 10 — devolve a culpa 2+2
S[10] = photo(10, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem espera a IA resolver gente</div>
        <div class="line">n&atilde;o est&aacute; inovando.</div>
      </div>
      <div class="stanza">
        <div class="line">Est&aacute; fugindo da responsabilidade</div>
        <div class="line red">que s&oacute; o dono pode carregar.</div>
      </div>
    </div>
'''

# 11 — consequencia 2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Pode assinar toda ferramenta</div>
        <div class="line">que o mercado lan&ccedil;ar.</div>
      </div>
      <div class="stanza">
        <div class="line">Na m&atilde;o de um time desengajado,</div>
        <div class="line red">tecnologia &eacute; s&oacute; despesa.</div>
      </div>
    </div>
'''

# 12 — virada (o diferencial e gente) 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E quando todo mundo tiver</div>
        <div class="line">as mesmas ferramentas,</div>
      </div>
      <div class="stanza">
        <div class="line">o diferencial volta a ser o de sempre:</div>
        <div class="line red">gente boa, bem liderada.</div>
      </div>
    </div>
'''

# 13 — fechamento (doutrina) 2+1
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Liderar gente n&atilde;o &eacute; dom.</div>
        <div class="line">&Eacute; m&eacute;todo.</div>
      </div>
      <div class="stanza">
        <div class="line red">E m&eacute;todo se aprende.</div>
      </div>
    </div>
'''

# 14 — CTA (treinamento + Comenta 307, foto sangrada)
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">&Eacute; o que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
      <div class="stanza">
        <div class="cta-big">Comenta <span class="red">307</span>,</div>
        <div class="cta-sm">que eu te mostro como construir um time engajado,<br>que entrega o que nenhuma ferramenta entrega.</div>
      </div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
