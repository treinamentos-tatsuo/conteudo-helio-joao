#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 45 (autoridade moral) — v2 pós-revisão."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/45_autoridade-moral")
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

# 1 — capa-tapa (grito puro Anton vermelho, o ditado)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:200px">
      <div class="line anton" style="font-size:{FIT.get("1", 90)}px">MANDA QUEM PODE,<br>OBEDECE QUEM TEM JUÍZO.</div>
    </div>
'''

# 2 — a ponte 2+2
S[2] = photo(2, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você carrega essa frase no bolso.</div>
        <div class="line">E na sua empresa, <span class="red">ela funciona.</span></div>
      </div>
      <div class="stanza">
        <div class="line">Você fala, <b>todo mundo faz.</b></div>
        <div class="line">Ninguém discute, ninguém enrola.</div>
      </div>
    </div>
'''

# 3 — herói: a frase sozinha
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:300px">
      <div class="line red" style="font-size:52px">Na sua frente, tudo anda.</div>
    </div>
'''

# 4 — o motor único 2+2 (2a estrofe vermelha)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Só que obediência tem alcance curto.</div>
        <div class="line">Ela chega até onde a sua voz chega.</div>
      </div>
      <div class="stanza">
        <div class="line red">E foi assim que você virou</div>
        <div class="line red">o único motor da empresa.</div>
      </div>
    </div>
'''

# 5 — o suspense (2 linhas, sem vermelho)
S[5] = photo(5, fade=28) + '''    <div class="top" style="top:280px">
      <div class="stanza">
        <div class="line">Porque essa frase leva uma empresa</div>
        <div class="line"><span class="red">até um certo ponto...</span></div>
      </div>
    </div>
'''

# 6 — o que se compra (estrofe única)
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:280px">
      <div class="stanza">
        <div class="line">O cargo faz o time te <b>obedecer</b>.</div>
        <div class="line">O salário faz o time <b>cumprir</b>.</div>
      </div>
    </div>
'''

# 7 — grito Anton: o punch simplificado
S[7] = photo(7, fade=26) + f'''    <div class="top" style="top:190px">
      <div class="line anton" style="font-size:{FIT.get("7", 96)}px">MAS NENHUM DOS DOIS<br>FAZ O TIME QUERER.</div>
    </div>
'''

# 8 — a tese 2+1 vermelha
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Liderança é outro tipo de autoridade.</div>
        <div class="line">É autoridade moral.</div>
      </div>
      <div class="stanza">
        <div class="line red">Essa você não pede. Você conquista.</div>
      </div>
    </div>
'''

# 9 — a pedrada 2+2 (2a estrofe vermelha)
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Se o seu time só anda empurrado,</div>
        <div class="line">o problema não é o juízo deles.</div>
      </div>
      <div class="stanza">
        <div class="line red">É a autoridade que</div>
        <div class="line red">você nunca construiu.</div>
      </div>
    </div>
'''

# 10 — o desejo 2+1+2 vermelha
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line">Time liderado de verdade</div>
        <div class="line">não fica esperando ordem.</div>
      </div>
      <div class="stanza">
        <div class="line">Resolve, avisa antes, joga junto.</div>
      </div>
      <div class="stanza">
        <div class="line red">Obedecer é o mínimo.</div>
        <div class="line red">Querer é o jogo.</div>
      </div>
    </div>
'''

# 11 — o primeiro passo 1+2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line">E isso começa simples:</div>
      </div>
      <div class="stanza">
        <div class="line">a regra que você cobra,</div>
        <div class="line red">você cumpre primeiro.</div>
      </div>
      <div class="stanza">
        <div class="line">Na frente de todo mundo.</div>
        <div class="line">Todo santo dia.</div>
      </div>
    </div>
'''

# 12 — fechamento A: construída com método 1+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Essa autoridade não nasce com o dono.</div>
      </div>
      <div class="stanza">
        <div class="line">Ela é construída. Através de método.</div>
        <div class="line red">E tem como aprender.</div>
      </div>
    </div>
'''

# 13 — fechamento B: o treinamento 3+2, corpo 42px
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line" style="font-size:42px">No meu treinamento de gestão</div>
        <div class="line" style="font-size:42px">pra pequena e média empresa,</div>
        <div class="line" style="font-size:42px">eu ensino esse caminho:</div>
      </div>
      <div class="stanza">
        <div class="line red" style="font-size:42px">a liderança e a cultura</div>
        <div class="line red" style="font-size:42px">que fazem o time jogar com você.</div>
      </div>
    </div>
'''

# 14 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como formar um time<br>que entrega porque quer,<br>não porque você mandou.</div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
