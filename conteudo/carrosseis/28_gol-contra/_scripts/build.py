#!/usr/bin/env python3
"""Monta os 13 HTMLs do carrossel 28 (gol contra)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/28_gol-contra")
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
  .impact{ font-size:54px; font-weight:700; line-height:1.28; color:#1A1A1A; }
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

# 1 — capa (a regra)
S[1] = photo(1) + '''    <div class="top" style="top:400px">
      <div class="impact" style="font-size:48px">Quem toma gol contra perde<br><span class="red">o direito de reclamar do juiz.</span></div>
    </div>
'''

# 2 — a ponte (o juiz da empresa) 2+2
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Na sua empresa também tem juiz.</div>
        <div class="line">Governo, imposto, crise, mercado.</div>
      </div>
      <div class="stanza">
        <div class="line">E gol contra sai todo mês.</div>
        <div class="line red">E você continua olhando só pro juiz.</div>
      </div>
    </div>
'''

# 3 — a cena (a explicação pronta) 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Fim de mês, resultado magro.</div>
        <div class="line">E a explicação já vem pronta:</div>
      </div>
      <div class="stanza">
        <div class="line">foi o imposto, foi a crise.</div>
        <div class="line red">O juiz roubou mais uma vez.</div>
      </div>
    </div>
'''

# 4 — o frango 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Frango, o mercado faz você tomar.</div>
        <div class="line">O chute veio forte, a bola escapou.</div>
      </div>
      <div class="stanza">
        <div class="line">Errar no mercado é isso.</div>
        <div class="line red">Faz parte de estar em campo.</div>
      </div>
    </div>
'''

# 5 — o gol contra 2+2 (2ª estrofe toda vermelha)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Gol contra é outra história.</div>
        <div class="line">Ninguém atacou. Ninguém chutou.</div>
      </div>
      <div class="stanza">
        <div class="line red">A bola entrou na sua rede</div>
        <div class="line red">empurrada pelo seu próprio pé.</div>
      </div>
    </div>
'''

# 6 — dentro de casa 2+2 (2ª estrofe toda vermelha)
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O gol contra da sua empresa</div>
        <div class="line">acontece dentro de casa:</div>
      </div>
      <div class="stanza">
        <div class="line red">preço sem margem, custo sem medida,</div>
        <div class="line red">caixa misturado com o seu bolso.</div>
      </div>
    </div>
'''

# 7 — o grito (herói: 1 serif + 1 Anton)
S[7] = photo(7, fade=24) + f'''    <div class="top" style="top:250px">
      <div class="line">O frango, você toma.</div>
      <div class="line anton" style="font-size:{FIT.get("7",80)}px;margin-top:18px">O GOL CONTRA, VOCÊ FAZ.</div>
    </div>
'''

# 8 — o juiz apita pros dois 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O juiz apita pros dois times.</div>
        <div class="line">O imposto do concorrente é o mesmo.</div>
      </div>
      <div class="stanza">
        <div class="line">Tem empresa crescendo agora</div>
        <div class="line red">no campo que você chama de injusto.</div>
      </div>
    </div>
'''

# 9 — reclamar não desconta 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Reclamar do juiz é confortável.</div>
        <div class="line">A culpa nunca sobra pra você.</div>
      </div>
      <div class="stanza">
        <div class="line">Só que reclamar não desconta gol.</div>
        <div class="line red">E amanhã você toma outro igual.</div>
      </div>
    </div>
'''

# 10 — o replay 2+2
S[10] = photo(10, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Antes de reclamar do juiz,</div>
        <div class="line">tenha coragem de ver o replay.</div>
      </div>
      <div class="stanza">
        <div class="line">O replay da sua empresa</div>
        <div class="line red">são os números que você não olha.</div>
      </div>
    </div>
'''

# 11 — a bola no seu pé 2+2
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Governo, imposto, mercado:</div>
        <div class="line">esse apito você não controla.</div>
      </div>
      <div class="stanza">
        <div class="line">Preço, custo, margem, caixa:</div>
        <div class="line red">essa bola está no seu pé.</div>
      </div>
    </div>
'''

# 12 — método + treinamento 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Defesa treinada não toma gol contra.</div>
        <div class="line">Empresa com gestão também não.</div>
      </div>
      <div class="stanza">
        <div class="line">É isso que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 13 — fechamento + CTA (foto subida + fade duplo)
S[13] = (f'    <img src="../imagens/img-13.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O apito não vai mudar.</div>
        <div class="line">O seu jogo pode.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como parar de tomar gol contra<br>e construir uma empresa que dá lucro de verdade.</div>
    </div>
''')

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
