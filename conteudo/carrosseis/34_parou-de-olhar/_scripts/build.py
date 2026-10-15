#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 34 (parou de olhar)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/34_parou-de-olhar")
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


def photo(n, fade=18):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


S = {}

# 1 — capa-grito (Anton vermelho, 1 linha)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:300px">
      <div class="line anton" style="font-size:{FIT.get("1", 96)}px">DONO NÃO TIRA O OLHO.</div>
    </div>
'''

# 2 — espelho-paradoxo (estrofe única)
S[2] = photo(2, fade=24) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line">Crescer era o sonho.</div>
        <div class="line red">Virou o problema.</div>
      </div>
    </div>
'''

# 3 — dobrou tudo 2+2 (2a estrofe inteira vermelha)
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Em dois anos você dobrou o estoque,</div>
        <div class="line">dobrou o time, dobrou a estrutura.</div>
      </div>
      <div class="stanza">
        <div class="line red">Só que os problemas cresceram</div>
        <div class="line red">mais rápido que a empresa.</div>
      </div>
    </div>
'''

# 4 — a caça aos culpados 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você foi caçar o culpado:</div>
        <div class="line">o mercado, a crise, o time.</div>
      </div>
      <div class="stanza">
        <div class="line">Trocou gente, apagou incêndio.</div>
        <div class="line red">E a empresa seguiu desandando.</div>
      </div>
    </div>
'''

# 5 — a conclusão errada 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Até que você engoliu</div>
        <div class="line">a conclusão mais perigosa:</div>
      </div>
      <div class="stanza">
        <div class="line red">crescer é assim mesmo.</div>
        <div class="line red">Dor de crescimento é normal.</div>
      </div>
    </div>
'''

# 6 — reveal (heroi: 2 serif + 1 Anton)
S[6] = photo(6, fade=24) + f'''    <div class="top" style="top:260px">
      <div class="line">Não é.</div>
      <div class="line">O que aconteceu é bem mais simples:</div>
      <div class="line anton" style="font-size:{FIT.get("6", 78)}px;margin-top:22px">VOCÊ PAROU DE OLHAR.</div>
    </div>
'''

# 7 — só isso (estrofe única)
S[7] = photo(7) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line">Só isso.</div>
        <div class="line red">Nada mais.</div>
      </div>
    </div>
'''

# 8 — o olho estava em tudo 2+2
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quando a empresa era pequena,</div>
        <div class="line">o seu olho estava em tudo.</div>
      </div>
      <div class="stanza">
        <div class="line">Cada venda, cada erro, cada cliente.</div>
        <div class="line red">Nada passava sem você ver.</div>
      </div>
    </div>
'''

# 9 — outras frentes 2+2
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aí a empresa cresceu</div>
        <div class="line">e você foi cuidar de outras frentes.</div>
      </div>
      <div class="stanza">
        <div class="line">E no seu lugar entrou alguém</div>
        <div class="line red">pra fazer o que você fazia.</div>
      </div>
    </div>
'''

# 10 — não fez (âncora + estrofe)
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Não fez.</div>
      </div>
      <div class="stanza">
        <div class="line">E você só foi descobrir</div>
        <div class="line red">quando a conta chegou.</div>
      </div>
    </div>
'''

# 11 — o grande problema é crescer 2+2 (2a estrofe inteira vermelha)
S[11] = photo(11, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O grande problema nunca é</div>
        <div class="line">quando a empresa é pequena.</div>
      </div>
      <div class="stanza">
        <div class="line red">O grande problema é a hora</div>
        <div class="line red">que ela começa a crescer.</div>
      </div>
    </div>
'''

# 12 — olhar é comandar de perto 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E olhar não é fazer tudo sozinho.</div>
        <div class="line">Olhar é comandar de perto.</div>
      </div>
      <div class="stanza">
        <div class="line red">Número na mesa, reunião de rotina,</div>
        <div class="line red">cobrança que não falha.</div>
      </div>
    </div>
'''

# 13 — a promessa do método 2+2
S[13] = photo(13, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Enxergar a empresa inteira</div>
        <div class="line">não é dom. É método.</div>
      </div>
      <div class="stanza">
        <div class="line">Com método, o erro aparece cedo.</div>
        <div class="line red">Sem método, aparece no prejuízo.</div>
      </div>
    </div>
'''

# 14 — o treinamento 2+2
S[14] = photo(14, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa:</div>
      </div>
      <div class="stanza">
        <div class="line red">o que olhar, onde cobrar</div>
        <div class="line red">e como fazer o time entregar.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro o método pra crescer<br>sem perder a empresa de vista,<br>com controle, lucro e time que entrega.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
