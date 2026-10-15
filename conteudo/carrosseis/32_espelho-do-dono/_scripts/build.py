#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 32 (o espelho do dono / cultura nao se delega)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/32_espelho-do-dono")
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
  .impact{ font-size:46px; font-weight:700; line-height:1.22; color:#1A1A1A; }
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

# 1 — capa (a frase que o dono fala)
S[1] = photo(1) + '''    <div class="top" style="top:352px">
      <div class="setup">Você achou que isso resolvia:</div>
      <div class="impact" style="margin-top:26px">"Contratei um RH pra cuidar da <span class="red">cultura</span>."</div>
    </div>
'''

# 2 — CULTURA NAO SE DELEGA (heroi Anton puro)
S[2] = photo(2) + f'''    <div class="top" style="top:290px">
      <div class="line anton" style="font-size:{FIT.get("2",96)}px">CULTURA NÃO SE DELEGA.</div>
    </div>
'''

# 3 — o limite do RH 2+2
S[3] = photo(3, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O RH contrata, organiza e treina.</div>
        <div class="line">E a empresa precisa disso.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas existe o que ele não alcança:</div>
        <div class="line red">o que o time vê em você todo dia.</div>
      </div>
    </div>
'''

# 4 — o mecanismo 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem trabalha debaixo de você</div>
        <div class="line">vai se parecer com você.</div>
      </div>
      <div class="stanza">
        <div class="line">Não é teoria e não é elogio.</div>
        <div class="line red">Acontece querendo ou não.</div>
      </div>
    </div>
'''

# 5 — a prova 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você atrasa, o time atrasa.</div>
        <div class="line">Você releva, o time releva.</div>
      </div>
      <div class="stanza">
        <div class="line">Você fala mal de cliente,</div>
        <div class="line red">e o time fala mal de você.</div>
      </div>
    </div>
'''

# 6 — a reclamacao 2+2 (grifo)
S[6] = photo(6) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E no fim do dia, você reclama.</div>
        <div class="line">Do desânimo. Da moleza.</div>
      </div>
      <div class="stanza">
        <div class="line">De ninguém pensar como dono,</div>
        <div class="line">{grifo("de ninguém vestir a camisa.")}</div>
      </div>
    </div>
'''

# 7 — a isca da virada (suspense, estrofe unica)
S[7] = photo(7) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">Antes da próxima reclamação,</div>
        <div class="line">olha com atenção pra esse time...</div>
      </div>
    </div>
'''

# 8 — O FILHO E TEU (heroi invertido: Anton + remate serif)
S[8] = photo(8) + f'''    <div class="top" style="top:250px">
      <div class="line anton" style="font-size:{FIT.get("8",100)}px">O FILHO É TEU.</div>
      <div class="line" style="margin-top:26px">E ele cresceu se espelhando no pai.</div>
    </div>
'''

# 9 — a pedrada 2+2 (estrofe inteira vermelha)
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O que mais te irrita no seu time</div>
        <div class="line">ele aprendeu te observando.</div>
      </div>
      <div class="stanza">
        <div class="line red">Você reclama do time e não vê:</div>
        <div class="line red">está reclamando de você mesmo.</div>
      </div>
    </div>
'''

# 10 — grito doutrinario (heroi: estrofe serif + Anton em 2 linhas)
S[10] = photo(10) + f'''    <div class="top" style="top:224px">
      <div class="stanza">
        <div class="line">Não é o RH que constrói.</div>
        <div class="line">Não é o mercado que define.</div>
      </div>
      <div class="stanza">
        <div class="line anton" style="font-size:{FIT.get("10",88)}px">CULTURA COMEÇA E TERMINA</div>
        <div class="line anton" style="font-size:{FIT.get("10",88)}px">NO DONO.</div>
      </div>
    </div>
'''

# 11 — o outro lado do espelho (desejo) 2+2
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Mas esse espelho tem outro lado:</div>
        <div class="line">ele também reflete o seu melhor.</div>
      </div>
      <div class="stanza">
        <div class="line">Time que cobra porque te vê cobrar.</div>
        <div class="line red">Que entrega porque te vê entregar.</div>
      </div>
    </div>
'''

# 12 — o como (metodo) 2+2
S[12] = photo(12, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Não nasce de mural nem de palestra.</div>
        <div class="line">Nasce de exemplo com método:</div>
      </div>
      <div class="stanza">
        <div class="line">o comportamento certo, repetido</div>
        <div class="line red">todo dia, até virar automático.</div>
      </div>
    </div>
'''

# 13 — fechamento (treinamento) 2+2
S[13] = photo(13) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Esse espelho não muda sozinho.</div>
        <div class="line">Ele muda na rotina, com método.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 14 — CTA exclusivo (texto no topo + foto impactante sangrada)
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma cultura<br>em que o seu time reflete o seu melhor,<br>e não os seus defeitos.</div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
