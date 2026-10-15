#!/usr/bin/env python3
"""Monta os 11 HTMLs do carrossel 18 (nao trabalha pra voce)."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/18_nao-trabalha-pra-voce/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"

# Anton (grito) — ajustar apos render.
A_CAPA = 74    # capa, "Ele nao trabalha pra voce." (linha longa preenche a coluna)
A_MESMO = 132  # slide 3, "Pra ele mesmo." (heroi)
A_LIBERTA = 96 # slide 9, "Emprego liberta." (punch)

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


def photo(n, fade=18):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def figura(n, top, height, cls=""):
    return (f'    <img class="figura{(" " + cls) if cls else ""}" src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="top:{top}px;height:{height}px">\n')


S = {}

# 1 — capa / gancho: setup (2 linhas) + Anton punch + subtitulo
S[1] = photo(1) + f'''    <div class="top" style="top:182px">
      <div class="setup" style="font-size:47px;line-height:1.3">N&atilde;o importa o que seu funcion&aacute;rio<br>faz na sua empresa.</div>
      <div class="line anton" style="font-size:{A_CAPA}px;margin-top:26px">Ele n&atilde;o trabalha pra voc&ecirc;.</div>
      <div class="setup" style="font-size:34px;font-style:italic;font-weight:700;margin-top:24px">E isso voc&ecirc; tem que deixar claro pra eles.</div>
    </div>
'''

# 2 — nao importa o cargo (2+2)
S[2] = photo(2) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">N&atilde;o importa se ele lava o banheiro,</div>
        <div class="line">opera a c&acirc;mera ou fecha a venda.</div>
        <div class="line">Cuida do estoque, do RH, do jur&iacute;dico.</div>
      </div>
      <div class="stanza">
        <div class="line red">Nenhum deles trabalha pra voc&ecirc;.</div>
      </div>
    </div>
'''

# 3 — pra ele mesmo (heroi Anton)
S[3] = photo(3) + f'''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">Se n&atilde;o &eacute; pra voc&ecirc;, ent&atilde;o &eacute; pra quem?</div>
      </div>
      <div class="line anton" style="font-size:{A_MESMO}px;margin-top:44px">Pra ele mesmo.</div>
    </div>
'''

# 4 — constroi a propria vida (2+2)
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Cada um deles est&aacute; construindo</div>
        <div class="line">a pr&oacute;pria vida dentro da sua empresa.</div>
      </div>
      <div class="stanza">
        <div class="line">O sal&aacute;rio &eacute; s&oacute; o come&ccedil;o.</div>
        <div class="line red">O prop&oacute;sito &eacute; o que segura.</div>
      </div>
    </div>
'''

# 5 — o trabalho do dono (2+2)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O seu trabalho n&atilde;o &eacute; dar ordem.</div>
        <div class="line">&Eacute; vender esse prop&oacute;sito pro time.</div>
      </div>
      <div class="stanza">
        <div class="line">Fazer cada um enxergar</div>
        <div class="line red">que trabalha por ele, n&atilde;o por voc&ecirc;.</div>
      </div>
    </div>
'''

# 6 — veste a camisa (2+2)
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Funcion&aacute;rio que entende isso</div>
        <div class="line">n&atilde;o entrega o m&iacute;nimo.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele veste a camisa</div>
        <div class="line red">porque a camisa virou dele.</div>
      </div>
    </div>
'''

# 7 — melhorar = gerar emprego (2+2)
S[7] = photo(7) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Eu falo isso pro meu time o tempo todo.</div>
        <div class="line">Qualquer que seja o papel dele,</div>
        <div class="line">ele ajuda a melhorar a empresa.</div>
      </div>
      <div class="stanza">
        <div class="line red">E empresa melhor gera mais emprego.</div>
      </div>
    </div>
'''

# 8 — o ciclo (2+2)
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Gente que passou pelas minhas empresas</div>
        <div class="line">hoje tem neg&oacute;cio pr&oacute;prio.</div>
      </div>
      <div class="stanza">
        <div class="line">Emprega 5, 10, 50 pessoas.</div>
        <div class="line red">Gera emprego. Forma empres&aacute;rio.</div>
      </div>
    </div>
'''

# 9 — emprego liberta (2 + 1 + Anton punch)
S[9] = photo(9) + f'''    <div class="top" style="top:214px">
      <div class="stanza">
        <div class="line">N&atilde;o existe projeto social mais forte</div>
        <div class="line">pra uma na&ccedil;&atilde;o do que o emprego.</div>
      </div>
      <div class="stanza">
        <div class="line">Emprego tira gente do assistencialismo.</div>
        <div class="line anton" style="font-size:{A_LIBERTA}px;margin-top:26px">Emprego liberta.</div>
      </div>
    </div>
'''

# 10 — emprega por missao (2+2)
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O dono que entende isso</div>
        <div class="line">para de mandar e passa a liderar.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele n&atilde;o emprega por obriga&ccedil;&atilde;o.</div>
        <div class="line red">Ele emprega por miss&atilde;o.</div>
      </div>
    </div>
'''

# 11 — fechamento + CTA (sanduiche: texto topo + figura + CTA rodape)
S[11] = f'''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Time engajado n&atilde;o se compra com sal&aacute;rio.</div>
        <div class="line red">Se constr&oacute;i com cultura.</div>
      </div>
    </div>
''' + figura(11, 372, 540, "fade") + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir um time engajado<br>que joga junto, sem aumentar um real de sal&aacute;rio.</div>
    </div>
'''

for n in range(1, 12):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
