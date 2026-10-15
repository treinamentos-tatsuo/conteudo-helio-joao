#!/usr/bin/env python3
"""Monta os 11 HTMLs do carrossel 28 (vender tomate e vender casa e igual)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/28_vender-tomate-e-casa")
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
  .impact{ font-size:52px; font-weight:700; line-height:1.22; color:#1A1A1A; }
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

# 1 — capa (a objecao-espelho)
S[1] = photo(1) + '''    <div class="top" style="top:260px">
      <div class="setup">&ldquo;H&eacute;lio, voc&ecirc; n&atilde;o entende:</div>
      <div class="impact" style="margin-top:26px">o meu mercado <span class="red">&eacute; diferente.&rdquo;</span></div>
    </div>
'''

# 2 — o tapa (grito puro Anton, alvo 640)
S[2] = photo(2) + f'''    <div class="top" style="top:300px">
      <div class="line anton" style="font-size:{FIT.get("2",100)}px">TEM DIFEREN&Ccedil;A NENHUMA.</div>
    </div>
'''

# 3 — a concessao (cadeira do vendedor) 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Pro vendedor, &eacute; diferente sim.</div>
        <div class="line">Muda a conversa, muda a abordagem.</div>
      </div>
      <div class="stanza">
        <div class="line">Vender tomate e vender casa</div>
        <div class="line red">s&atilde;o dois jogos na cadeira dele.</div>
      </div>
    </div>
'''

# 4 — a virada de otica (cadeira do dono) 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">S&oacute; que a cadeira do vendedor</div>
        <div class="line">nunca foi a sua cadeira.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; &eacute; o dono. E na sua cadeira,</div>
        <div class="line red">toda venda &eacute; igual.</div>
      </div>
    </div>
'''

# 5 — a anatomia (a maquina) 2+2 (grifo)
S[5] = photo(5) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Toda venda tem a mesma anatomia:</div>
        <div class="line">gente certa no papel certo.</div>
      </div>
      <div class="stanza">
        <div class="line">Processo, energia, dire&ccedil;&atilde;o</div>
        <div class="line">{grifo("e acompanhamento de perto.")}</div>
      </div>
    </div>
'''

# 6 — os papeis 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O vendedor &eacute; respons&aacute;vel</div>
        <div class="line">por uma coisa: vender.</div>
      </div>
      <div class="stanza">
        <div class="line">O dono constr&oacute;i o ambiente e a m&aacute;quina</div>
        <div class="line red">que faz a venda acontecer.</div>
      </div>
    </div>
'''

# 7 — o que o ambiente entrega 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quando o ambiente existe,</div>
        <div class="line">vender deixa de ser sorte.</div>
      </div>
      <div class="stanza">
        <div class="line">Vira consist&ecirc;ncia todo m&ecirc;s,</div>
        <div class="line red">margem e previsibilidade.</div>
      </div>
    </div>
'''

# 8 — a pedrada (a desculpa) 2+2, estrofe final inteira vermelha
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">&ldquo;Meu mercado &eacute; diferente&rdquo;</div>
        <div class="line">n&atilde;o &eacute; leitura de mercado.</div>
      </div>
      <div class="stanza">
        <div class="line red">&Eacute; a desculpa que te impede</div>
        <div class="line red">de montar a sua m&aacute;quina.</div>
      </div>
    </div>
'''

# 9 — o custo (a venda de heroi) 2+2 (cena mais escura -> fade maior)
S[9] = photo(9, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E enquanto a desculpa te protege,</div>
        <div class="line">a venda depende de her&oacute;i.</div>
      </div>
      <div class="stanza">
        <div class="line">Do vendedor bom, do m&ecirc;s bom,</div>
        <div class="line red">do cliente que resolve aparecer.</div>
      </div>
    </div>
'''

# 10 — a virada (metodo) 2+2
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">M&aacute;quina n&atilde;o nasce do mercado.</div>
        <div class="line">M&aacute;quina nasce de m&eacute;todo.</div>
      </div>
      <div class="stanza">
        <div class="line">E m&eacute;todo funciona igual</div>
        <div class="line red">pra tomate, casa e purificador.</div>
      </div>
    </div>
'''

# 11 — fechamento + CTA (foto subida + fade duplo)
S[11] = (f'    <img src="../imagens/img-11.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Montar essa m&aacute;quina se aprende.</div>
        <div class="line">N&atilde;o depende do seu mercado.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; o que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como montar a m&aacute;quina de vendas<br>da sua empresa: venda todo m&ecirc;s, com margem,<br>sem depender de sorte.</div>
    </div>
''')

for n in range(1, 12):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
