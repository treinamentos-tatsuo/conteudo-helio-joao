#!/usr/bin/env python3
"""Monta os 12 HTMLs do carrossel 25 (o imposto do achismo)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/25_imposto-do-achismo")
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

# 1 — capa (o imposto invisivel)
S[1] = photo(1) + '''    <div class="top" style="top:295px">
      <div class="setup">A sua empresa paga um imposto<br>que n&atilde;o aparece em boleto nenhum.</div>
      <div class="impact" style="margin-top:26px">O imposto do <span class="red">&ldquo;eu acho&rdquo;.</span></div>
    </div>
'''

# 2 — a cena ("acho que") 2+2
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Acho que esse pre&ccedil;o est&aacute; bom.</div>
        <div class="line">Acho que esse cliente compensa.</div>
      </div>
      <div class="stanza">
        <div class="line">Acho que d&aacute; pra contratar mais um.</div>
        <div class="line red">Acho que esse m&ecirc;s fecha no azul.</div>
      </div>
    </div>
'''

# 3 — o custo 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Parece experi&ecirc;ncia falando.</div>
        <div class="line">Parece o famoso faro de dono.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas cada &ldquo;acho&rdquo; desses tem um pre&ccedil;o.</div>
        <div class="line red">E quem paga &eacute; sempre voc&ecirc;.</div>
      </div>
    </div>
'''

# 4 — o mecanismo 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O pre&ccedil;o no chute come a margem.</div>
        <div class="line">O custo ignorado vira preju&iacute;zo.</div>
      </div>
      <div class="stanza">
        <div class="line">E esse dinheiro some calado:</div>
        <div class="line red">sem guia, sem aviso, sem recibo.</div>
      </div>
    </div>
'''

# 5 — a comparacao 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; reclama do imposto que chega.</div>
        <div class="line">Do governo, dos juros, da taxa.</div>
      </div>
      <div class="stanza">
        <div class="line">S&oacute; que o imposto mais caro de todos</div>
        <div class="line red">n&atilde;o vem do governo. Vem do &ldquo;acho&rdquo;.</div>
      </div>
    </div>
'''

# 6 — o grito (heroi Anton)
S[6] = photo(6) + f'''    <div class="top" style="top:250px">
      <div class="line">Chame de faro, chame de tino,</div>
      <div class="line">chame de vinte anos de experi&ecirc;ncia.</div>
      <div class="line anton" style="font-size:{FIT.get("6",92)}px;margin-top:14px">O &ldquo;ACHO&rdquo; CUSTA CARO.</div>
    </div>
'''

# 7 — o conforto 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Decidir no &ldquo;acho&rdquo; &eacute; confort&aacute;vel.</div>
        <div class="line">N&atilde;o pede n&uacute;mero, n&atilde;o pede estudo.</div>
      </div>
      <div class="stanza">
        <div class="line">Saber d&aacute; trabalho todos os dias.</div>
        <div class="line red">Achar s&oacute; apresenta a conta depois.</div>
      </div>
    </div>
'''

# 8 — a pedrada do ego 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; sabe de cabe&ccedil;a o pre&ccedil;o</div>
        <div class="line">de tudo o que a sua empresa compra.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas n&atilde;o sabe quanto sobra</div>
        <div class="line red">de cada venda que ela faz.</div>
      </div>
    </div>
'''

# 9 — a aposta 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Decidir sem n&uacute;mero n&atilde;o &eacute; decidir.</div>
        <div class="line">&Eacute; apostar. Todo dia. Todo m&ecirc;s.</div>
      </div>
      <div class="stanza">
        <div class="line">S&oacute; que a ficha dessa aposta</div>
        <div class="line red">sai do seu bolso todo fim de m&ecirc;s.</div>
      </div>
    </div>
'''

# 10 — a virada 2+2 (grifo)
S[10] = photo(10) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quando o n&uacute;mero entra, o jogo muda.</div>
        <div class="line">Margem, custo, pre&ccedil;o, lucro.</div>
      </div>
      <div class="stanza">
        <div class="line">Quem conhece os n&uacute;meros decide.</div>
        <div class="line">{grifo("Quem n&atilde;o conhece, paga pra achar.")}</div>
      </div>
    </div>
'''

# 11 — pedrada do CTA 2+2 (cena de fim de dia -> fade maior)
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o precisa vender mais.</div>
        <div class="line">Nem se matar mais do que j&aacute; se mata.</div>
      </div>
      <div class="stanza">
        <div class="line">Precisa parar de pagar, todo m&ecirc;s,</div>
        <div class="line red">o imposto de decidir no escuro.</div>
      </div>
    </div>
'''

# 12 — fechamento + CTA (foto subida + fade duplo)
S[12] = (f'    <img src="../imagens/img-12.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Tirar a empresa do achismo &eacute; m&eacute;todo.</div>
        <div class="line">E m&eacute;todo &eacute; coisa que se aprende.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; isso que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como decidir com n&uacute;meros<br>e fazer o lucro aparecer no seu bolso.</div>
    </div>
''')

for n in range(1, 13):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
