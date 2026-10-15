#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 30 (um terco da vida dele)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/30_um-terco-da-vida")
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

# 1 — capa (a isca)
S[1] = photo(1) + '''    <div class="top" style="top:380px">
      <div class="impact">Voc&ecirc; sabe o que o seu funcion&aacute;rio<br><span class="red">te vende</span> todo santo dia?</div>
    </div>
'''

# 2 — o tapa (grito puro, Anton, 1 linha)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:300px">
      <div class="line anton" style="font-size:{FIT.get("2",100)}px">1/3 DA VIDA DELE.</div>
    </div>
'''

# 3 — a conta 2+2
S[3] = photo(3, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">N&atilde;o &eacute; for&ccedil;a de express&atilde;o.</div>
        <div class="line">&Eacute; conta de padaria.</div>
      </div>
      <div class="stanza">
        <div class="line">Oito horas do dia dele,</div>
        <div class="line red">todo dia, s&atilde;o suas.</div>
      </div>
    </div>
'''

# 4 — mais tempo que a familia 2+2
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ele passa mais tempo com voc&ecirc;</div>
        <div class="line">do que com o pr&oacute;prio filho.</div>
      </div>
      <div class="stanza">
        <div class="line">Mais tempo no seu balc&atilde;o</div>
        <div class="line red">do que dentro da pr&oacute;pria casa.</div>
      </div>
    </div>
'''

# 5 — a objecao 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">"Ah, mas eu t&ocirc; pagando."</div>
        <div class="line">Entendo. T&aacute; pagando mesmo.</div>
      </div>
      <div class="stanza">
        <div class="line">Agora me responde uma coisa:</div>
        <div class="line red">voc&ecirc; sabe o peso do que compra?</div>
      </div>
    </div>
'''

# 6 — vira a camera 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Vira a mesa um instante.</div>
        <div class="line">Quanto vale um peda&ccedil;o da SUA vida?</div>
      </div>
      <div class="stanza">
        <div class="line">Pois &eacute; exatamente isso</div>
        <div class="line red">que ele te entrega todo dia.</div>
      </div>
    </div>
'''

# 7 — pedrada 2+2
S[7] = photo(7, fade=30) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A maioria dos empres&aacute;rios</div>
        <div class="line">nunca parou pra fazer essa conta.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas pra reclamar de gente,</div>
        <div class="line red">tem tempo todo santo dia.</div>
      </div>
    </div>
'''

# 8 — a direcao 2+2 (2a estrofe inteira vermelha)
S[8] = photo(8, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quer uma dire&ccedil;&atilde;o? &Eacute; uma r&eacute;gua s&oacute;.</div>
        <div class="line">E n&atilde;o tem nada a ver com sal&aacute;rio.</div>
      </div>
      <div class="stanza">
        <div class="line red">Cria um ambiente melhor</div>
        <div class="line red">do que a casa do seu funcion&aacute;rio.</div>
      </div>
    </div>
'''

# 9 — o concorrente do clima 2+2
S[9] = photo(9, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Porque o concorrente do seu clima</div>
        <div class="line">n&atilde;o &eacute; a empresa da esquina.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; a casa do seu funcion&aacute;rio.</div>
        <div class="line red">&Eacute; de l&aacute; que voc&ecirc; disputa ele.</div>
      </div>
    </div>
'''

# 10 — ambiente melhor e 2+2
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ambiente melhor n&atilde;o &eacute; mesa de sinuca</div>
        <div class="line">nem frase bonita na parede.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; lugar onde ele aprende, ganha,</div>
        <div class="line red">se diverte e tem orgulho de estar.</div>
      </div>
    </div>
'''

# 11 — a regua 2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem entende esse peso constr&oacute;i</div>
        <div class="line">um lugar que gente boa escolhe.</div>
      </div>
      <div class="stanza">
        <div class="line">Quem n&atilde;o entende, contrata, treina,</div>
        <div class="line red">e v&ecirc; todo mundo ir embora.</div>
      </div>
    </div>
'''

# 12 — a chave que vira 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Porque ningu&eacute;m fica pelo dono.</div>
        <div class="line">Ele fica pelo futuro dele.</div>
      </div>
      <div class="stanza">
        <div class="line">E o dia que essa chave vira,</div>
        <div class="line red">ele entrega porque quer.</div>
      </div>
    </div>
'''

# 13 — pedrada final 2+2 (2a estrofe inteira vermelha)
S[13] = photo(13) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Um ter&ccedil;o da vida de cada um deles</div>
        <div class="line">est&aacute; nas suas m&atilde;os agora.</div>
      </div>
      <div class="stanza">
        <div class="line red">E isso pesa mais do que</div>
        <div class="line red">qualquer folha de pagamento.</div>
      </div>
    </div>
'''

# 14 — fechamento (metodo + treinamento) 2+2
S[14] = photo(14) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Construir esse ambiente n&atilde;o &eacute; dom.</div>
        <div class="line red">&Eacute; m&eacute;todo. Cultura se constr&oacute;i.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; o que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
'''

# 15 — CTA (texto no topo + foto sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma cultura<br>que atrai gente boa, segura gente boa<br>e transforma o seu time em resultado.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
