#!/usr/bin/env python3
"""Monta os 13 HTMLs do carrossel 50 (nem sonho tem)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/50_nem-sonho-tem")
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
  .capa{ font-size:50px; line-height:1.3; font-weight:600; }
  .sussurro{ font-size:30px; font-weight:400; color:#1A1A1A; margin-top:30px; }
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
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

# 1 — capa (impacto + punch + sussurro)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:290px">
      <div class="line capa">Você aguenta tudo pelo seu sonho.</div>
      <div class="line capa red">O seu funcionário nem sonho tem.</div>
      <div class="line sussurro">e você aí, cobrando garra dele.</div>
    </div>
'''

# 2 — o combustível do dono (2+2+1red)
S[2] = photo(2) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">É o sonho que te tira da cama</div>
        <div class="line">antes do sol nascer.</div>
      </div>
      <div class="stanza">
        <div class="line">Que te faz aguentar o boleto,</div>
        <div class="line">o cliente e a madrugada.</div>
      </div>
      <div class="stanza">
        <div class="line red">Sonho é o combustível do dono.</div>
      </div>
    </div>
'''

# 3 — o lado dele (2+2)
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Agora olha pro seu time.</div>
        <div class="line">Que sonho puxa cada um deles?</div>
      </div>
      <div class="stanza">
        <div class="line">O seu você sabe de cor.</div>
        <div class="line red">O deles? Às vezes, nenhum.</div>
      </div>
    </div>
'''

# 4 — a quebra de ilusão (2+2, 2a estrofe inteira vermelha)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">E mesmo assim você cobra.</div>
        <div class="line">Cobra garra, cobra entrega.</div>
      </div>
      <div class="stanza">
        <div class="line red">Cobra atitude de sonhador</div>
        <div class="line red">de quem nunca teve um sonho.</div>
      </div>
    </div>
'''

# 5 — o grito (serif + 2 linhas Anton)
S[5] = photo(5) + f'''    <div class="top" style="top:228px">
      <div class="line">Aperta, promete, ameaça, motiva.</div>
      <div class="line anton" style="font-size:{FIT.get("5", 76)}px;margin-top:22px">TANQUE VAZIO</div>
      <div class="line anton" style="font-size:{FIT.get("5", 76)}px">NÃO RESPONDE.</div>
    </div>
'''

# 6 — a virada (2+2+1red)
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Quem enxerga isso?</div>
        <div class="line">Só o líder.</div>
      </div>
      <div class="stanza">
        <div class="line">O chefe cobra do time</div>
        <div class="line">um sonho que não existe.</div>
      </div>
      <div class="stanza">
        <div class="line red">O líder desperta um.</div>
      </div>
    </div>
'''

# 7 — despertar no concreto (2+2 vermelha)
S[7] = photo(7) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Despertar sonho não é palestra.</div>
        <div class="line">Não é frase na parede.</div>
      </div>
      <div class="stanza">
        <div class="line red">É mostrar que a pessoa pode mais.</div>
        <div class="line red">E que o caminho passa pela sua empresa.</div>
      </div>
    </div>
'''

# 8 — o futuro dele (2+2) — bloco em 200 (sujeito alto na foto)
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Ninguém sua a camisa</div>
        <div class="line">pelo sonho do <b>patrão</b>.</div>
      </div>
      <div class="stanza">
        <div class="line red">O funcionário entrega o melhor</div>
        <div class="line red">quando persegue o futuro dele.</div>
      </div>
    </div>
'''

# 9 — conquista (2+2)
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Confiança não se pede. <b>Se conquista.</b></div>
        <div class="line">Engajamento não se cobra. <b>Se conquista.</b></div>
      </div>
      <div class="stanza">
        <div class="line red">E pra ter o melhor dos outros,</div>
        <div class="line red">você dá o melhor de si primeiro.</div>
      </div>
    </div>
'''

# 10 — desejo (2+2)
S[10] = photo(10, fade=28) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">O dia que o sonho do funcionário</div>
        <div class="line">passa por dentro da sua empresa,</div>
      </div>
      <div class="stanza">
        <div class="line">você para de empurrar o time.</div>
        <div class="line red">Ele começa a puxar junto.</div>
      </div>
    </div>
'''

# 11 — o como (2+2 vermelha)
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Isso não nasce de discurso.</div>
        <div class="line">Nasce de liderança com método.</div>
      </div>
      <div class="stanza">
        <div class="line red">Um lugar onde se aprende, se ganha,</div>
        <div class="line red">se diverte e dá orgulho de estar.</div>
      </div>
    </div>
'''

# 12 — fechamento (treinamento) (2+2 vermelha)
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Despertar sonho é trabalho de líder.</div>
        <div class="line">E liderar se aprende.</div>
      </div>
      <div class="stanza">
        <div class="line red">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 13 — CTA exclusivo (palavra única do post: SONHO)
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:206px">
      <div class="cta-big">Comenta <span class="red">SONHO</span>,</div>
      <div class="cta-sm">que eu te mostro como formar um time<br>que joga pelo próprio futuro<br>dentro da sua empresa.</div>
    </div>
'''

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
