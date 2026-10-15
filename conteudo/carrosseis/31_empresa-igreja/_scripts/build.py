#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 31 (empresa tem que ser igreja) — v2 pós-feedback."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/31_empresa-igreja")
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
  .bottom{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:46px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .impact{ font-size:48px; font-weight:700; line-height:1.28; color:#1A1A1A; }
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


S = {}

# 1 — capa/gancho (grito puro, Anton, 2 linhas)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:280px">
      <div class="line anton" style="font-size:{FIT.get("1",75)}px">EMPRESA TEM QUE SER</div>
      <div class="line anton" style="font-size:{FIT.get("1",75)}px">IGUAL UMA IGREJA.</div>
    </div>
'''

# 2 — vai porque acredita 2+2
S[2] = photo(2, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ninguém vai pra igreja</div>
        <div class="line">porque tem alguém mandando.</div>
      </div>
      <div class="stanza">
        <div class="line">Todo domingo a igreja enche.</div>
        <div class="line red">Porque o fiel acredita.</div>
      </div>
    </div>
'''

# 3 — você paga e não tem fé 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A igreja lota de manhã cedo</div>
        <div class="line">sem pagar nada a ninguém.</div>
      </div>
      <div class="stanza">
        <div class="line">Você paga todo santo mês.</div>
        <div class="line red">E o time nem veste a camisa.</div>
      </div>
    </div>
'''

# 4 — o segredo do pastor 2+2 (2a estrofe inteira vermelha)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E o pastor tem um segredo</div>
        <div class="line">que empresário nenhum respeita:</div>
      </div>
      <div class="stanza">
        <div class="line red">ele repete a mesma mensagem</div>
        <div class="line red">há dois mil anos.</div>
      </div>
    </div>
'''

# 5 — você falou uma vez 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você falou da sua cultura</div>
        <div class="line">uma vez, no dia da contratação.</div>
      </div>
      <div class="stanza">
        <div class="line">E cobra fé o ano inteiro</div>
        <div class="line red">de quem ouviu o credo um dia.</div>
      </div>
    </div>
'''

# 6 — lavagem cerebral? (heroi: 2 serif + 1 Anton)
S[6] = photo(6, fade=24) + f'''    <div class="top" style="top:280px">
      <div class="line">Você vai me perguntar:</div>
      <div class="line">isso não é lavagem cerebral?</div>
      <div class="line anton" style="font-size:{FIT.get("6",78)}px;margin-top:22px">É EXATAMENTE ISSO.</div>
    </div>
'''

# 7 — tiro o ruim, coloco o bom 2+2 (2a estrofe inteira vermelha)
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Eu tiro o que tem de ruim</div>
        <div class="line">da cabeça do meu time.</div>
      </div>
      <div class="stanza">
        <div class="line red">E coloco um monte</div>
        <div class="line red">de coisa boa no lugar.</div>
      </div>
    </div>
'''

# 8 — manipulação é controle (estrofe única)
S[8] = photo(8) + '''    <div class="top" style="top:280px">
      <div class="stanza">
        <div class="line">Isso não é manipulação.</div>
        <div class="line red">Manipulação é controle.</div>
      </div>
    </div>
'''

# 9 — é influência (âncora + 2)
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">É influência.</div>
      </div>
      <div class="stanza">
        <div class="line">E influência é livre-arbítrio:</div>
        <div class="line red">a pessoa escolhe acreditar.</div>
      </div>
    </div>
'''

# 10 — credo, rito e rotina (heroi: 2 serif + 1 Anton) — bloco alto pra não pegar no sino
S[10] = photo(10) + f'''    <div class="top" style="top:200px">
      <div class="line">Cultura se instala</div>
      <div class="line">do jeito que a fé se instala:</div>
      <div class="line anton" style="font-size:{FIT.get("10",78)}px;margin-top:22px">CREDO, RITO E ROTINA.</div>
    </div>
'''

# 11 — o unpack 2+2+2
S[11] = photo(11, fade=32) + '''    <div class="top" style="top:210px">
      <div class="stanza">
        <div class="line">Credo é no que você acredita</div>
        <div class="line">e defende sem negociar.</div>
      </div>
      <div class="stanza">
        <div class="line">Rito é treinamento, reunião,</div>
        <div class="line">padrão que ninguém pula.</div>
      </div>
      <div class="stanza">
        <div class="line red">Rotina é repetir todo dia</div>
        <div class="line red">até virar hábito no time.</div>
      </div>
    </div>
'''

# 12 — a pedrada do tempo 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O pastor tem uma hora por semana.</div>
        <div class="line">E forma gente que acredita.</div>
      </div>
      <div class="stanza">
        <div class="line">Você tem oito horas por dia.</div>
        <div class="line red">Como você está usando?</div>
      </div>
    </div>
'''

# 13 — quem não prega, não forma 2+2 — bloco alto + imagem cortada no topo (EXTRA_TOP)
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Se o seu time não acredita,</div>
        <div class="line">o problema não é o time.</div>
      </div>
      <div class="stanza">
        <div class="line">É que ali não tem pregação.</div>
        <div class="line red">Quem não prega, não forma.</div>
      </div>
    </div>
'''

# 14 — fechamento + CTA (figura flutuante recortada)
S[14] = ('    <img src="../imagens/img-14.png" alt="" onerror="this.style.display=\'none\'" '
         'style="position:absolute;top:585px;left:50%;transform:translateX(-50%);height:440px;'
         'mix-blend-mode:multiply;'
         '-webkit-mask-image:linear-gradient(to bottom,#000 55%,transparent 96%);'
         'mask-image:linear-gradient(to bottom,#000 55%,transparent 96%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Credo, rito e rotina</div>
        <div class="line">não nascem sozinhos. É método.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma cultura<br>que faz o seu time acreditar e jogar junto com você.</div>
    </div>
''')

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
