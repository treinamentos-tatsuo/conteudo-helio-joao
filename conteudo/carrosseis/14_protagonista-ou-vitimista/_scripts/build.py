#!/usr/bin/env python3
"""Monta os 11 HTMLs do carrossel 14 (protagonista ou vitimista)."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/14_protagonista-ou-vitimista/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"

# Anton (grito). Ajustar apos render.
A_CAPA = 64   # capa, 1 linha unica
A_VOCE = 150  # slide 6, "E VOCE"

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
  .figura{ position:absolute; left:50%; transform:translateX(-50%); mix-blend-mode:multiply; z-index:1; }
  .figura.fade{
    -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 55%,transparent 98%);
    mask-image:linear-gradient(to bottom,#000 0%,#000 55%,transparent 98%); }
  .top{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .bottom{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:46px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .scr{ position:relative; display:inline-block; }
  .scr .u{ position:absolute; left:-3%; width:106%; height:0.5em; bottom:-0.26em; pointer-events:none; }
  .impact{ font-size:50px; font-weight:700; line-height:1.22; color:#1A1A1A; }
  .setup{ font-size:35px; font-weight:400; line-height:1.3; color:#1A1A1A; }
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


def photo(n, fade=16):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def figura(n, top, height, cls=""):
    return (f'    <img class="figura{(" " + cls) if cls else ""}" src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="top:{top}px;height:{height}px">\n')


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


S = {}

# 1 — capa / gancho (reconhecimento): setup + Anton punch (2 linhas)
S[1] = photo(1) + f'''    <div class="top" style="top:372px">
      <div class="setup" style="font-size:43px">Todo ano voc&ecirc; jura que vai ser diferente.</div>
      <div class="line anton" style="font-size:{A_CAPA}px;margin-top:22px">E todo ano a culpa &eacute; de outro.</div>
    </div>
'''

# 2 — cena da culpa (2+2)
S[2] = photo(2) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Todo problema j&aacute; vem com um culpado pronto.</div>
        <div class="line">O mercado, o cliente, o funcion&aacute;rio, o governo.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; tem uma explica&ccedil;&atilde;o pra cada fracasso.</div>
        <div class="line red">E todas moram do lado de fora.</div>
      </div>
    </div>
'''

# 3 — refem (pedrada) (2+2)
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Se a culpa &eacute; sempre do outro,</div>
        <div class="line">a solu&ccedil;&atilde;o tamb&eacute;m &eacute; dele.</div>
      </div>
      <div class="stanza">
        <div class="line">Ou seja: voc&ecirc; virou ref&eacute;m</div>
        <div class="line red">de quem nem sabe que voc&ecirc; existe.</div>
      </div>
    </div>
'''

# 4 — a anestesia (2+2)
S[4] = photo(4) + '''    <div class="top" style="top:268px">
      <div class="stanza">
        <div class="line">Culpar os outros at&eacute; alivia.</div>
        <div class="line">Mas al&iacute;vio n&atilde;o &eacute; solu&ccedil;&atilde;o.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o resolve o seu fracasso.</div>
        <div class="line red">S&oacute; anestesia ele.</div>
      </div>
    </div>
'''

# 5 — rodando (2+1, estrofe vermelha)
S[5] = photo(5) + '''    <div class="top" style="top:252px">
      <div class="stanza">
        <div class="line">Muda o ano. Muda a desculpa.</div>
        <div class="line">A empresa continua exatamente igual.</div>
      </div>
      <div class="stanza">
        <div class="line red">Muito suor pra continuar parado.</div>
      </div>
    </div>
'''

# 6 — reveal + controle (heroi Anton + remate)
S[6] = photo(6) + f'''    <div class="top" style="top:204px">
      <div class="stanza">
        <div class="line">A pessoa que pode virar esse jogo</div>
        <div class="line">senta na sua cadeira todo dia.</div>
      </div>
      <div class="line anton" style="font-size:{A_VOCE}px;margin-top:30px">&Eacute; voc&ecirc;.</div>
      <div class="line" style="margin-top:24px">E o que &eacute; seu, voc&ecirc; resolve.</div>
    </div>
'''

# 7 — os dois tipos (1+2)
S[7] = photo(7) + '''    <div class="top" style="top:262px">
      <div class="stanza">
        <div class="line">No fim, existem s&oacute; dois tipos de gente.</div>
      </div>
      <div class="stanza">
        <div class="line">A que vira solu&ccedil;&atilde;o</div>
        <div class="line red">e a que vira problema.</div>
      </div>
    </div>
'''

# 8 — o protagonista (1+2, grifo)
S[8] = photo(8) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O protagonista n&atilde;o pergunta de quem &eacute; a culpa.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele pergunta {grifo("o que ele pode fazer")}</div>
        <div class="line">com o que est&aacute; na m&atilde;o dele.</div>
      </div>
    </div>
'''

# 9 — ponte x muro (2+2)
S[9] = photo(9) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Quem se vitimiza levanta muro.</div>
        <div class="line">Quem resolve constr&oacute;i ponte.</div>
      </div>
      <div class="stanza">
        <div class="line">Um se protege do mundo.</div>
        <div class="line red">O outro atravessa.</div>
      </div>
    </div>
'''

# 10 — controla o que conhece (2+2)
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o controla o mundo.</div>
        <div class="line">Voc&ecirc; controla o que voc&ecirc; conhece.</div>
      </div>
      <div class="stanza">
        <div class="line">E quem n&atilde;o conhece os pr&oacute;prios n&uacute;meros</div>
        <div class="line red">n&atilde;o controla a empresa. S&oacute; torce.</div>
      </div>
    </div>
'''

# 11 — fechamento + CTA (sanduiche: texto topo + figura + CTA rodape)
S[11] = f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Protagonista n&atilde;o joga no escuro.</div>
        <div class="line red">Ele conhece o pr&oacute;prio jogo.</div>
      </div>
    </div>
''' + figura(11, 360, 560, "fade") + '''    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro os n&uacute;meros que tiram a sua<br>empresa do achismo e botam de volta no seu controle.</div>
    </div>
'''

for n in range(1, 12):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
