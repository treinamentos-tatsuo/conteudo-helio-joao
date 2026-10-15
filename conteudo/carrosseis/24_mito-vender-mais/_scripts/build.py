#!/usr/bin/env python3
"""Monta os 12 HTMLs do carrossel 24 (o mito do "tem que vender mais")."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/24_mito-vender-mais")
DEST = BASE / "instagram"
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"
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


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


S = {}

# 1 — capa (o mito)
S[1] = photo(1) + '''    <div class="top" style="top:372px">
      <div class="setup">Todo empres&aacute;rio j&aacute; acreditou nesse mito:</div>
      <div class="impact" style="margin-top:26px">&ldquo;N&atilde;o sobra dinheiro<br><span class="red">porque eu vendo pouco.&rdquo;</span></div>
    </div>
'''

# 2 — a cena 2+2
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O caixa aperta, o boleto vence</div>
        <div class="line">e a conta n&atilde;o fecha no fim do m&ecirc;s.</div>
      </div>
      <div class="stanza">
        <div class="line">E a sua cabe&ccedil;a repete o de sempre:</div>
        <div class="line red">&ldquo;se eu vendesse mais, teria ganho mais.&rdquo;</div>
      </div>
    </div>
'''

# 3 — a origem 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Foi assim que voc&ecirc; aprendeu.</div>
        <div class="line">Venda &eacute; o rem&eacute;dio pra tudo.</div>
      </div>
      <div class="stanza">
        <div class="line">Empres&aacute;rio bom &eacute; o que vende.</div>
        <div class="line red">O resto se ajeita depois.</div>
      </div>
    </div>
'''

# 4 — a prova (Sera?) 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ser&aacute;? Voc&ecirc; j&aacute; teve m&ecirc;s recorde.</div>
        <div class="line">J&aacute; vendeu mais do que esperava.</div>
      </div>
      <div class="stanza">
        <div class="line">Olhou pro bolso no fim do m&ecirc;s:</div>
        <div class="line red">e o dinheiro n&atilde;o estava l&aacute;.</div>
      </div>
    </div>
'''

# 5 — o mecanismo 2+2
S[5] = photo(5, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O dinheiro veio. E foi embora.</div>
        <div class="line">Pagou o custo, o erro e o furo.</div>
      </div>
      <div class="stanza">
        <div class="line">Vender mais, com a empresa assim,</div>
        <div class="line red">&eacute; encher um balde furado.</div>
      </div>
    </div>
'''

# 6 — a mentira (heroi Anton)
S[6] = photo(6) + f'''    <div class="top" style="top:250px">
      <div class="line">A mentira mais descarada</div>
      <div class="line">que o empres&aacute;rio conta pra si mesmo:</div>
      <div class="line anton" style="font-size:{FIT.get("6",92)}px;margin-top:14px">TEM QUE VENDER MAIS.</div>
    </div>
'''

# 7 — o conforto 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Essa mentira &eacute; confort&aacute;vel.</div>
        <div class="line">A culpa fica na crise, no mercado.</div>
      </div>
      <div class="stanza">
        <div class="line">E voc&ecirc; n&atilde;o precisa encarar</div>
        <div class="line red">o que est&aacute; errado dentro de casa.</div>
      </div>
    </div>
'''

# 8 — o problema real 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">S&oacute; que o seu problema n&atilde;o &eacute; venda.</div>
        <div class="line">&Eacute; gest&atilde;o. E sempre foi.</div>
      </div>
      <div class="stanza">
        <div class="line">Margem, custo, pre&ccedil;o, prazo:</div>
        <div class="line red">voc&ecirc; decide tudo isso no achismo.</div>
      </div>
    </div>
'''

# 9 — a pedrada 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E vender mais no achismo</div>
        <div class="line">n&atilde;o aumenta o lucro. Aumenta o buraco.</div>
      </div>
      <div class="stanza">
        <div class="line">Tem empresa que quebra</div>
        <div class="line red">no pr&oacute;prio ano recorde de venda.</div>
      </div>
    </div>
'''

# 10 — a virada 2+2 (grifo)
S[10] = photo(10) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quando a gest&atilde;o entra, o jogo vira.</div>
        <div class="line">A mesma venda come&ccedil;a a sobrar.</div>
      </div>
      <div class="stanza">
        <div class="line">Porque lucro n&atilde;o nasce de vender.</div>
        <div class="line">{grifo("Nasce do que voc&ecirc; faz com a venda.")}</div>
      </div>
    </div>
'''

# 11 — pedrada do CTA 2+2 (cena escura -> fade maior)
S[11] = photo(11, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Vender voc&ecirc; sempre deu um jeito.</div>
        <div class="line">Fazer sobrar, voc&ecirc; nunca conseguiu.</div>
      </div>
      <div class="stanza">
        <div class="line">E isso n&atilde;o se resolve com esfor&ccedil;o.</div>
        <div class="line red">Se resolve com gest&atilde;o.</div>
      </div>
    </div>
'''

# 12 — fechamento + CTA (figura flutuante recortada, meio-corpo, CTA sobre linho limpo)
S[12] = (f'    <img src="../imagens/img-12.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;top:512px;left:50%;transform:translateX(-50%);height:462px;'
         f'mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 86%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,#000 0%,#000 86%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Sobrar dinheiro n&atilde;o &eacute; sorte.</div>
        <div class="line">&Eacute; m&eacute;todo aplicado na empresa.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; isso que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como transformar a venda<br>que voc&ecirc; j&aacute; faz em lucro no seu bolso.</div>
    </div>
''')

for n in range(1, 13):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
