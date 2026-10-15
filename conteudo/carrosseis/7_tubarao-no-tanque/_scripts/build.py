#!/usr/bin/env python3
"""Monta os 16 HTMLs do carrossel 7."""
import json, pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/7_tubarao-no-tanque/instagram")
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
  .ell .e{ position:absolute; left:-9%; width:118%; height:1.50em; top:-0.08em; pointer-events:none; }
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


def elipse(txt):
    return f'<span class="ell">{txt}<img class="e" src="{EL}/elipse-larga-2.png" alt=""></span>'


S = {}

# 1 — capa / gancho
S[1] = photo(1) + '''    <div class="top" style="top:470px">
      <div class="setup">A sua empresa n&atilde;o est&aacute; em crise.</div>
      <div class="impact" style="margin-top:26px">Ela est&aacute; <span class="red">apodrecendo em &aacute;gua limpa</span>.</div>
    </div>
'''

# 2 — a ponte / promessa da historia (2 linhas)
S[2] = photo(2) + '''    <div class="top" style="top:360px">
      <div class="stanza">
        <div class="line">O que os pescadores do Jap&atilde;o v&atilde;o te ensinar</div>
        <div class="line red">sobre manter a sua empresa viva.</div>
      </div>
    </div>
'''

# 3 — o Japao e a distancia (2+2)
S[3] = photo(3) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Peixe que n&atilde;o chega fresco</div>
        <div class="line">n&atilde;o vale nada no Jap&atilde;o.</div>
      </div>
      <div class="stanza">
        <div class="line">A costa esvaziou, a viagem virou dias,</div>
        <div class="line red">e o peixe chegava sem valor.</div>
      </div>
    </div>
'''

# 4 — o tanque nao resolveu (2+2, grifo)
S[4] = photo(4) + f'''    <div class="top" style="top:268px">
      <div class="stanza">
        <div class="line">Puseram tanques de &aacute;gua nos barcos.</div>
        <div class="line">&Aacute;gua limpa, espa&ccedil;o, nenhum predador.</div>
      </div>
      <div class="stanza">
        <div class="line">{grifo("E chegava ruim do mesmo jeito.")}</div>
      </div>
    </div>
'''

# 5 — o pivo (heroi)
S[5] = photo(5) + f'''    <div class="top" style="top:204px">
      <div class="line">O problema nunca foi a viagem.</div>
      <div class="line anton" style="font-size:{FIT.get("5",118)}px;margin-top:10px">Eles morreram</div>
      <div class="line anton" style="font-size:{FIT.get("5",118)}px">por ficar parados.</div>
    </div>
'''

# 6 — o tubarao entra (2+1)
S[6] = photo(6) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Ent&atilde;o um pescador fez o que parecia</div>
        <div class="line">a maior burrice do mundo:</div>
      </div>
      <div class="stanza">
        <div class="line red">colocou um tubar&atilde;o dentro do tanque.</div>
      </div>
    </div>
'''

# 7 — o resultado (duas linhas)
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O tubar&atilde;o comia um peixe ou outro.</div>
        <div class="line red">O resto chegava fresco.</div>
      </div>
    </div>
'''

# 8 — voce e o peixe (heroi)
S[8] = photo(8) + f'''    <div class="top" style="top:228px">
      <div class="line">Sabe qual &eacute; a parte que incomoda?</div>
      <div class="line anton" style="font-size:{FIT.get("8",110)}px;margin-top:10px">Voc&ecirc; &eacute; o peixe.</div>
    </div>
'''

# 9 — a rotina confortavel (2+2, elipse)
S[9] = photo(9) + f'''    <div class="top" style="top:262px">
      <div class="stanza">
        <div class="line">Hoje ningu&eacute;m te cobra nada.</div>
        <div class="line">Ningu&eacute;m te questiona.</div>
      </div>
      <div class="stanza">
        <div class="line">A meta &eacute; a mesma do ano passado</div>
        <div class="line">{elipse("e voc&ecirc; bate ela dormindo.")}</div>
      </div>
    </div>
'''

# 10 — parece premio (2+2, grifo + vermelho)
S[10] = photo(10) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Isso n&atilde;o parece um problema.</div>
        <div class="line">{grifo("Parece pr&ecirc;mio.")}</div>
      </div>
      <div class="stanza">
        <div class="line">S&oacute; que conforto n&atilde;o te deixa parado.</div>
        <div class="line red">Te deixa lento.</div>
      </div>
    </div>
'''

# 11 — o tubarao do mercado (1+2)
S[11] = photo(11) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Cedo ou tarde um tubar&atilde;o entra no tanque.</div>
      </div>
      <div class="stanza">
        <div class="line">Concorrente novo, cliente grande que sai,</div>
        <div class="line red">caixa que aperta sem avisar.</div>
      </div>
    </div>
'''

# 12 — ele nao come um peixe so (heroi)
S[12] = photo(12) + f'''    <div class="top" style="top:228px">
      <div class="line">Esse voc&ecirc; n&atilde;o escolheu.</div>
      <div class="line anton" style="font-size:{FIT.get("12",82)}px;margin-top:8px">E ele n&atilde;o come um peixe s&oacute;.</div>
    </div>
'''

# 13 — escolher o proprio tubarao (duas linhas)
S[13] = photo(13) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Empres&aacute;rio bom n&atilde;o espera o tubar&atilde;o.</div>
        <div class="line">{grifo("Ele coloca o dele antes.")}</div>
      </div>
    </div>
'''

# 14 — o tubarao na pratica (2+2)
S[14] = photo(14) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Meta que voc&ecirc; ainda n&atilde;o sabe bater.</div>
        <div class="line">Prazo que aperta de verdade.</div>
      </div>
      <div class="stanza">
        <div class="line">N&uacute;mero na mesa toda semana,</div>
        <div class="line red">na frente de quem pode te questionar.</div>
      </div>
    </div>
'''

# 15 — o preco (2+1)
S[15] = photo(15) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Vai custar. O tubar&atilde;o come um peixe.</div>
        <div class="line">Alguma meta vai falhar, algu&eacute;m vai sair.</div>
      </div>
      <div class="stanza">
        <div class="line red">Mas a carga inteira chega viva.</div>
      </div>
    </div>
'''

# 16 — fechamento + CTA (sanduiche)
S[16] = f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Pare de esperar o mercado te acordar.</div>
        <div class="line">{grifo("Coloca o tubar&atilde;o voc&ecirc; mesmo.")}</div>
      </div>
    </div>
''' + figura(16, 338, 578, "fade") + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro qual desconforto<br>a sua empresa precisa agora.</div>
    </div>
'''

for n in range(1, 17):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
