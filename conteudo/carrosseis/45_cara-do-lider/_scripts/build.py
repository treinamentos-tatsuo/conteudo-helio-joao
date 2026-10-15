#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 45 (a cara do lider) — rodada 2."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/45_cara-do-lider")
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
  .hero{ font-size:62px; line-height:1.3; font-weight:700; color:#A91C20; }
  .cta-big{ font-size:74px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
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

# 1 — CAPA: a regua (heroi vermelho bold, imagem intima das maos)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line hero">Ningu&eacute;m sobe a r&eacute;gua</div>
        <div class="line hero">que o dono desceu.</div>
      </div>
    </div>
'''

# 2 — a reclamacao (Anton vermelho 2 linhas + isca negrito preto 1 linha)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:236px">
      <div class="line anton" style="font-size:{FIT.get("2", 84)}px">S&Oacute; TEM FUNCION&Aacute;RIO RUIM<br>NA MINHA EMPRESA.</div>
      <div class="line" style="font-size:38px;font-weight:700;margin-top:44px">Se voc&ecirc; j&aacute; pensou isso, esse post vai doer.</div>
    </div>
'''

# 3 — a cena 2+2 (ultima linha vermelha)
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; cobra, e a entrega</div>
        <div class="line">vem sempre pela metade.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; ensina, voc&ecirc; acompanha.</div>
        <div class="line red">E ningu&eacute;m segura o padr&atilde;o.</div>
      </div>
    </div>
'''

# 4 — troca de gente (2 linhas juntas, 2a vermelha)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:280px">
      <div class="stanza">
        <div class="line">A&iacute; voc&ecirc; troca de gente.</div>
        <div class="line red">E o novo fica igual ao antigo.</div>
      </div>
    </div>
'''

# 5 — a conclusao errada 2+2 (linha da geracao vermelha)
S[5] = photo(5, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A conclus&atilde;o parece &oacute;bvia:</div>
        <div class="line red">essa gera&ccedil;&atilde;o n&atilde;o quer nada com nada.</div>
      </div>
      <div class="stanza">
        <div class="line">O mercado piorou, gente boa sumiu.</div>
        <div class="line">E todo mundo concorda com voc&ecirc;.</div>
      </div>
    </div>
'''

# 6 — a isca 2+2 (2a estrofe vermelha, termina em reticencias)
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">S&oacute; que o seu time passa o dia</div>
        <div class="line">olhando pra uma pessoa s&oacute;.</div>
      </div>
      <div class="stanza">
        <div class="line red">Copiando o ritmo, o humor,</div>
        <div class="line red">o capricho e o desleixo de algu&eacute;m...</div>
      </div>
    </div>
'''

# 7 — o tapa (grito Anton)
S[7] = photo(7, fade=26) + f'''    <div class="top" style="top:210px">
      <div class="line anton" style="font-size:{FIT.get("7", 80)}px">ESSE ALGU&Eacute;M &Eacute; VOC&Ecirc;.</div>
    </div>
'''

# 8 — a tese (DNA) 2+2 vermelha
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A empresa carrega no DNA</div>
        <div class="line">o DNA do dono.</div>
      </div>
      <div class="stanza">
        <div class="line red">&Eacute; natural que ela</div>
        <div class="line red">se pare&ccedil;a com voc&ecirc;.</div>
      </div>
    </div>
'''

# 9 — o mecanismo 2+2 (ultima linha vermelha)
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; afrouxa no hor&aacute;rio,</div>
        <div class="line">o time afrouxa junto.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; aceita entrega pela metade,</div>
        <div class="line red">a metade vira o padr&atilde;o.</div>
      </div>
    </div>
'''

# 10 — a pedrada 2+2 vermelha
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ent&atilde;o quando voc&ecirc; reclama</div>
        <div class="line">que s&oacute; tem frouxo no seu time...</div>
      </div>
      <div class="stanza">
        <div class="line red">voc&ecirc; n&atilde;o est&aacute; descrevendo eles.</div>
        <div class="line red">Est&aacute; descrevendo o seu reflexo.</div>
      </div>
    </div>
'''

# 11 — trocar nao resolve 2+2 vermelha
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">&Eacute; por isso que trocar de gente</div>
        <div class="line">nunca resolveu de verdade.</div>
      </div>
      <div class="stanza">
        <div class="line red">Voc&ecirc; troca a imagem.</div>
        <div class="line red">O espelho continua o mesmo.</div>
      </div>
    </div>
'''

# 12 — a virada 2+2 vermelha
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E aqui mora a boa not&iacute;cia:</div>
        <div class="line">espelho n&atilde;o discute, ele reflete.</div>
      </div>
      <div class="stanza">
        <div class="line red">No dia em que o dono sobe a r&eacute;gua,</div>
        <div class="line red">o time inteiro sobe atr&aacute;s.</div>
      </div>
    </div>
'''

# 13 — fechamento 2+2+1 vermelha, corpo 42px
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line" style="font-size:42px">Ser esse dono n&atilde;o &eacute; dom,</div>
        <div class="line" style="font-size:42px">nem quest&atilde;o de pulso firme.</div>
      </div>
      <div class="stanza">
        <div class="line" style="font-size:42px">&Eacute; m&eacute;todo: regra clara, exemplo di&aacute;rio</div>
        <div class="line" style="font-size:42px">e cobran&ccedil;a que n&atilde;o escolhe dia.</div>
      </div>
      <div class="stanza">
        <div class="line red" style="font-size:42px">E m&eacute;todo se aprende.</div>
      </div>
    </div>
'''

# 14 — treinamento 2+2 vermelha, corpo 42px
S[14] = photo(14, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line" style="font-size:42px">No meu treinamento de gest&atilde;o</div>
        <div class="line" style="font-size:42px">pra pequena e m&eacute;dia empresa,</div>
      </div>
      <div class="stanza">
        <div class="line red" style="font-size:42px">eu ensino o dono a construir a cultura</div>
        <div class="line red" style="font-size:42px">que forma um time de padr&atilde;o alto.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como formar um time<br>que voc&ecirc; tenha orgulho<br>de ver no espelho.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
