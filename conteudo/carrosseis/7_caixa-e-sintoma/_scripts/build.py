#!/usr/bin/env python3
"""Monta os 17 HTMLs do carrossel 7 (caixa e sintoma)."""
import json, pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/7_caixa-e-sintoma/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"
FIT = json.loads((pathlib.Path(__file__).parent / "antonfit.json").read_text()) if (pathlib.Path(__file__).parent / "antonfit.json").exists() else {}

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
    -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 50%,transparent 97%),linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%);
    -webkit-mask-composite:source-in;
    mask-image:linear-gradient(to bottom,#000 0%,#000 50%,transparent 97%),linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%);
    mask-composite:intersect; }
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
  .ell{ position:relative; display:inline-block; }
  .ell .e{ position:absolute; left:-9%; width:118%; height:1.78em; top:-0.36em; pointer-events:none; }
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


def photo(n, fade=16, extra=""):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;{extra}">\n')


def figura(n, top, height, cls=""):
    return (f'    <img class="figura{(" " + cls) if cls else ""}" src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="top:{top}px;height:{height}px">\n')


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


def elipse(txt, h=1.78, t=-0.36):
    return (f'<span class="ell">{txt}<img class="e" src="{EL}/elipse-larga-2.png" alt="" '
            f'style="height:{h}em;top:{t}em"></span>')


S = {}

# 1 — capa / gancho
S[1] = photo(1) + '''    <div class="top" style="top:440px">
      <div class="setup">Voc&ecirc; n&atilde;o tem problema de caixa.</div>
      <div class="impact" style="margin-top:26px">O caixa <span class="red">s&oacute; te entregou</span>.</div>
    </div>
'''

# 2 — o dado (split)
S[2] = photo(2) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">9 milh&otilde;es de CNPJs negativados no Brasil.</div>
        <div class="line">1,5 milh&atilde;o a mais do que um ano atr&aacute;s.</div>
      </div>
      <div class="stanza">
        <div class="line red">E quase nenhum deles quebrou...</div>
      </div>
    </div>
'''

# 3 — quebraram vendendo
S[3] = photo(3) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">...por falta de venda.</div>
        <div class="line">Quebraram {elipse("vendendo", h=1.50, t=-0.22)}.</div>
      </div>
    </div>
'''

# 4 — a desculpa
S[4] = photo(4) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">A&iacute; voc&ecirc; me diz que o problema &eacute; a Selic.</div>
        <div class="line">Que o juro est&aacute; imposs&iacute;vel.</div>
      </div>
      <div class="stanza">
        <div class="line">Eu n&atilde;o vou discordar do juro.</div>
        <div class="line red">Vou discordar do diagn&oacute;stico.</div>
      </div>
    </div>
'''

# 5 — o diagnostico
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Juro caro n&atilde;o cria o seu problema.</div>
        <div class="line red">Ele s&oacute; cobra mais caro por ele.</div>
      </div>
    </div>
'''

# 6 — o dinheiro ja tem dono
S[6] = photo(6, fade=32) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O dinheiro que entrou hoje j&aacute; tem dono.</div>
        <div class="line">Fornecedor, imposto, folha.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o est&aacute; com dinheiro em caixa.</div>
        <div class="line red">Voc&ecirc; est&aacute; com o dinheiro dos outros.</div>
      </div>
    </div>
'''

# 7 — anton
S[7] = photo(7) + f'''    <div class="top" style="top:206px">
      <div class="line">S&oacute; que voc&ecirc; olha o saldo e v&ecirc; lucro.</div>
      <div class="line anton" style="font-size:{FIT.get("7",130)}px;margin-top:12px">E gasta o que</div>
      <div class="line anton" style="font-size:{FIT.get("7",130)}px">ainda n&atilde;o &eacute; seu.</div>
    </div>
'''

# 8 — 12x x 60 dias
S[8] = photo(8) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Voc&ecirc; recebe do cliente em 12 vezes</div>
        <div class="line">e paga o fornecedor em 60 dias.</div>
      </div>
      <div class="stanza">
        <div class="line red">Virou o banco do seu cliente.</div>
        <div class="line red">Sem cobrar nada por isso.</div>
      </div>
    </div>
'''

# 9 — Casas Bahia
S[9] = photo(9) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">A Casas Bahia faturou 27 bilh&otilde;es em 2024.</div>
      </div>
      <div class="stanza">
        <div class="line">No primeiro trimestre de 2026,</div>
        <div class="line red">perdeu 1 bilh&atilde;o.</div>
      </div>
    </div>
'''

# 10 — a conta nao fechou dentro
S[10] = photo(10, fade=26) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">N&atilde;o faltou cliente.</div>
        <div class="line">N&atilde;o faltou venda.</div>
      </div>
      <div class="stanza">
        <div class="line">A conta n&atilde;o fechou</div>
        <div class="line">{grifo("dentro da pr&oacute;pria opera&ccedil;&atilde;o.")}</div>
      </div>
    </div>
'''

# 11 — heroi: CAIXA E SINTOMA (figura solta)
S[11] = f'''    <div class="top" style="top:250px">
      <div class="line anton" style="font-size:{FIT.get("11",150)}px">Caixa &eacute; sintoma.</div>
      <div class="line" style="margin-top:14px">Nunca &eacute; a causa.</div>
    </div>
''' + figura(11, 600, 560, "fade")

# 12 — onde e a infeccao
S[12] = photo(12) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O extrato te d&aacute; a temperatura.</div>
        <div class="line">N&atilde;o te d&aacute; o lugar da infec&ccedil;&atilde;o.</div>
      </div>
      <div class="stanza">
        <div class="line">Ela est&aacute; no pre&ccedil;o que voc&ecirc; n&atilde;o calculou</div>
        <div class="line red">e no custo que voc&ecirc; nunca mediu.</div>
      </div>
    </div>
'''

# 13 — o emprestimo
S[13] = photo(13) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">A&iacute; voc&ecirc; toma empr&eacute;stimo pra tapar o giro</div>
        <div class="line">e dorme achando que resolveu.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o resolveu nada.</div>
        <div class="line red">Comprou tempo e pagou juro por ele.</div>
      </div>
    </div>
'''

# 14 — o furo continua
S[14] = photo(14) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O furo continua l&aacute;, comendo por dentro.</div>
        <div class="line">E agora a d&iacute;vida cresce em cima dele.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; trocou um problema de opera&ccedil;&atilde;o</div>
        <div class="line">{grifo("por um problema de d&iacute;vida.")}</div>
      </div>
    </div>
'''

# 15 — anton heroi
S[15] = photo(15) + f'''    <div class="top" style="top:196px">
      <div class="line anton" style="font-size:{FIT.get("15",140)}px">Ningu&eacute;m quebra</div>
      <div class="line anton" style="font-size:{FIT.get("15",140)}px">de repente.</div>
      <div class="line" style="margin-top:22px">A empresa quebra em parcelas.</div>
    </div>
'''

# 16 — gestao / metodo
S[16] = photo(16) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Gest&atilde;o n&atilde;o &eacute; olhar o saldo no fim do dia.</div>
        <div class="line">&Eacute; saber o custo de cada venda que voc&ecirc; faz.</div>
      </div>
      <div class="stanza">
        <div class="line">O pre&ccedil;o que sustenta a empresa</div>
        <div class="line">{grifo("e o prazo que o seu caixa aguenta.")}</div>
      </div>
    </div>
'''

# 17 — fechamento + CTA
S[17] = f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Pare de tratar o sintoma.</div>
        <div class="line">{grifo("V&aacute; atr&aacute;s da causa.")}</div>
      </div>
    </div>
''' + figura(17, 356, 596, "fade") + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro onde o seu lucro<br>est&aacute; ficando preso.</div>
    </div>
'''

for n in range(1, 18):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
