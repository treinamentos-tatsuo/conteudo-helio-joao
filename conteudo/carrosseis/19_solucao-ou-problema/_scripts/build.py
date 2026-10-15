#!/usr/bin/env python3
"""Monta os 13 HTMLs do carrossel 19 (solucao ou problema — postura x curriculo)."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/19_solucao-ou-problema/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"

# Anton (grito). Ajustar apos render.
A_CAPA = 72     # S1  "SOLUCAO OU PROBLEMA." (1 linha)
A_FOME = 80     # S8  "IMPORTA SE ELE TEM FOME" (1 linha)
A_REFLEXO = 86  # S12 "A EQUIPE E O REFLEXO DO LIDER" (2 linhas)

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


def photo(n, fade=22):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def figura(n, top, height, cls=""):
    return (f'    <img class="figura{(" " + cls) if cls else ""}" src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="top:{top}px;height:{height}px">\n')


S = {}

# 1 — capa / binario: setup + Anton punch (1 linha)
S[1] = photo(1, 18) + f'''    <div class="top" style="top:360px">
      <div class="setup" style="font-size:43px">Todo funcion&aacute;rio &eacute; uma de duas coisas.</div>
      <div class="line anton" style="font-size:{A_CAPA}px;margin-top:24px">Solu&ccedil;&atilde;o ou problema.</div>
    </div>
'''

# 2 — o teste (2+2)
S[2] = photo(2) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">D&ecirc; o mesmo problema</div>
        <div class="line">a dois funcion&aacute;rios.</div>
      </div>
      <div class="stanza">
        <div class="line">Um vai te trazer uma sa&iacute;da.</div>
        <div class="line red">O outro, um culpado.</div>
      </div>
    </div>
'''

# 3 — o culpado (2+2)
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O vitimista sempre acha um culpado.</div>
        <div class="line">O mercado, o cliente, o colega, voc&ecirc;.</div>
      </div>
      <div class="stanza">
        <div class="line">S&oacute; n&atilde;o acha o &uacute;nico que</div>
        <div class="line red">ele pode mudar: ele mesmo.</div>
      </div>
    </div>
'''

# 4 — a anestesia (2+2)
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Enquanto a culpa &eacute; dos outros,</div>
        <div class="line">ele n&atilde;o precisa evoluir.</div>
      </div>
      <div class="stanza">
        <div class="line">Reclamar n&atilde;o resolve o problema.</div>
        <div class="line red">S&oacute; anestesia o fracasso dele.</div>
      </div>
    </div>
'''

# 5 — o protagonista (2+2)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O protagonista n&atilde;o procura culpado.</div>
        <div class="line">Ele procura sa&iacute;da.</div>
      </div>
      <div class="stanza">
        <div class="line">Se vira, arrega&ccedil;a a manga,</div>
        <div class="line red">e d&aacute; o seu jeito.</div>
      </div>
    </div>
'''

# 6 — assume e cresce (2+2)
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ele assume o problema como dele.</div>
        <div class="line">E o que &eacute; dele, ele resolve.</div>
      </div>
      <div class="stanza">
        <div class="line">N&atilde;o anestesia o fracasso.</div>
        <div class="line red">Cresce em cima dele.</div>
      </div>
    </div>
'''

# 7 — o ponto cego (2+2)
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E isso n&atilde;o est&aacute; em curr&iacute;culo nenhum.</div>
        <div class="line">Nenhuma faculdade forma postura.</div>
      </div>
      <div class="stanza">
        <div class="line">D&aacute; pra ler toda a experi&ecirc;ncia dele</div>
        <div class="line">e n&atilde;o achar <span class="red">uma linha de postura.</span></div>
      </div>
    </div>
'''

# 8 — a fome / virada (heroi Anton + remate)
S[8] = photo(8) + f'''    <div class="top" style="top:246px">
      <div class="stanza">
        <div class="line">No fim, pouco importa a bagagem.</div>
      </div>
      <div class="line anton" style="font-size:{A_FOME}px;margin-top:40px">Importa se ele tem fome</div>
      <div class="line" style="margin-top:26px">de carregar a pr&oacute;pria evolu&ccedil;&atilde;o.</div>
    </div>
'''

# 9 — a conta do dono (2+2)
S[9] = photo(9) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Todo dia que voc&ecirc; segura um vitimista,</div>
        <div class="line">voc&ecirc; paga a conta dele.</div>
      </div>
      <div class="stanza">
        <div class="line">E o resto do time aprende</div>
        <div class="line red">que reclamar tamb&eacute;m &eacute; op&ccedil;&atilde;o.</div>
      </div>
    </div>
'''

# 10 — cultura (2+2)
S[10] = photo(10) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Cultura forte n&atilde;o &eacute; feita de curr&iacute;culo.</div>
        <div class="line">&Eacute; feita de gente que resolve.</div>
      </div>
      <div class="stanza">
        <div class="line">Um protagonista puxa a empresa pra frente.</div>
        <div class="line red">Um vitimista puxa todo mundo pra baixo.</div>
      </div>
    </div>
'''

# 11 — formar (2+2)
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Protagonista pronto &eacute; raro.</div>
        <div class="line">Voc&ecirc; n&atilde;o compra, voc&ecirc; forma.</div>
      </div>
      <div class="stanza">
        <div class="line">Cultura forte transforma</div>
        <div class="line red">vitimista em protagonista.</div>
      </div>
    </div>
'''

# 12 — reflexo do lider (heroi Anton 2 linhas)
S[12] = photo(12) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Cultura forte n&atilde;o nasce sozinha.</div>
        <div class="line">Ela vem de cima.</div>
      </div>
      <div class="line anton" style="font-size:{A_REFLEXO}px;margin-top:44px">A equipe &eacute;<br>o reflexo do l&iacute;der.</div>
    </div>
'''

# 13 — fechamento + CTA (sanduiche: setup topo + figura + CTA rodape)
S[13] = f'''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Ningu&eacute;m te ensinou a formar gente.</div>
        <div class="line red">Mas isso se aprende.</div>
      </div>
    </div>
''' + figura(13, 358, 566, "fade") + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro o treinamento de lideran&ccedil;a e cultura<br>pra formar um time de protagonistas.</div>
    </div>
'''

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
