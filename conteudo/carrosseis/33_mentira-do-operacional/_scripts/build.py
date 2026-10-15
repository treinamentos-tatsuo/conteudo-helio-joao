#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 33 (a mentira mais bem embalada do mercado)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/33_mentira-do-operacional")
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
  .punch-capa{ font-size:58px; font-weight:700; line-height:1.2; color:#A91C20; margin-top:38px; }
  .whisper{ font-size:30px; font-weight:400; line-height:1.3; color:#1A1A1A; margin-top:34px; }
  .cta-big{ font-size:74px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.4; color:#1A1A1A; margin-top:22px; }
</style>
</head>
<body>
  <div class="slide">
"""
FOOT = """  </div>
</body>
</html>
"""


def photo(n, fade=18, down=0):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:{-down}px;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


S = {}

# 1 — capa (impact + punch red + sussurro discreto)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:300px">
      <div class="impact" style="font-size:42px">Te venderam o sonho mais ridículo do mercado:</div>
      <div class="punch-capa" style="margin-top:8px">Fugir da própria empresa</div>
      <div class="whisper" style="margin-top:26px">e você caiu como um pato.</div>
    </div>
'''

# 2 — tapa (grito puro, Anton, 2 linhas)
S[2] = photo(2, fade=24) + f'''    <div class="top" style="top:280px">
      <div class="line anton" style="font-size:{FIT.get("2",95)}px">É A MENTIRA MAIS BEM</div>
      <div class="line anton" style="font-size:{FIT.get("2",95)}px">EMBALADA DO MERCADO.</div>
    </div>
'''

# 3 — o alvo fácil 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Essa mentira vende porque</div>
        <div class="line">mira num alvo fácil:</div>
      </div>
      <div class="stanza">
        <div class="line">o dono que trabalha, trabalha,</div>
        <div class="line red">e não vê a cor do dinheiro.</div>
      </div>
    </div>
'''

# 4 — dono de longe (imagem: dono de WhatsApp) 2+2
S[4] = photo(4, fade=24, down=120) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Quem vive nessa roda</div>
        <div class="line">só quer ouvir uma coisa:</div>
      </div>
      <div class="stanza">
        <div class="line">que dá pra ser dono de longe,</div>
        <div class="line red">comandando pelo celular.</div>
      </div>
    </div>
'''

# 5 — vende alívio (heroi: 2 serif + 1 Anton)
S[5] = photo(5, fade=24) + f'''    <div class="top" style="top:280px">
      <div class="line">O guru sabe disso.</div>
      <div class="line">Por isso ele não vende solução.</div>
      <div class="line anton" style="font-size:{FIT.get("5",78)}px;margin-top:22px">ELE VENDE ALÍVIO.</div>
    </div>
'''

# 6 — quem vendeu não fica 2+2 (2a estrofe inteira vermelha)
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E alívio comprado no palco</div>
        <div class="line">custa caro no chão da empresa.</div>
      </div>
      <div class="stanza">
        <div class="line red">Quem te vendeu a saída</div>
        <div class="line red">não fica pra ver o estrago.</div>
      </div>
    </div>
'''

# 7 — apodrece em silêncio 2+2
S[7] = photo(7, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O dia que você some de verdade,</div>
        <div class="line">a empresa não para na hora.</div>
      </div>
      <div class="stanza">
        <div class="line">Ela apodrece em silêncio.</div>
        <div class="line red">E de longe, você não sente.</div>
      </div>
    </div>
'''

# 8 — a conta chega 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A decisão piora de qualidade.</div>
        <div class="line">O problema cresce escondido.</div>
      </div>
      <div class="stanza">
        <div class="line">E quando a conta aparece,</div>
        <div class="line red">já é grande demais.</div>
      </div>
    </div>
'''

# 9 — precisa de um comprador (2 + âncora red)
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quer mesmo fugir da sua empresa?</div>
        <div class="line">Então não precisa de guru.</div>
      </div>
      <div class="stanza">
        <div class="line red">Precisa de um comprador.</div>
      </div>
    </div>
'''

# 10 — carregar tudo sozinho 2+2
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Se você quer continuar dono,</div>
        <div class="line">o seu problema é outro.</div>
      </div>
      <div class="stanza">
        <div class="line">Você não cansa de trabalhar.</div>
        <div class="line red">Cansa de carregar tudo sozinho.</div>
      </div>
    </div>
'''

# 11 — por escolha, não por refém 2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O certo é a empresa parar</div>
        <div class="line">de precisar de você.</div>
      </div>
      <div class="stanza">
        <div class="line">E você continuar dentro</div>
        <div class="line red">por escolha, não por refém.</div>
      </div>
    </div>
'''

# 12 — número, rotina, gente formada 2+2
S[12] = photo(12, fade=32) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Isso não se compra no palco.</div>
        <div class="line">Se constrói com gestão:</div>
      </div>
      <div class="stanza">
        <div class="line">número na mão, rotina de comando,</div>
        <div class="line red">e gente formada pra executar.</div>
      </div>
    </div>
'''

# 13 — o primeiro passo 2+2
S[13] = photo(13) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O primeiro passo é pequeno:</div>
        <div class="line">uma função que só você faz.</div>
      </div>
      <div class="stanza">
        <div class="line">Escreve como se faz, treina alguém,</div>
        <div class="line red">e acompanha todo santo dia.</div>
      </div>
    </div>
'''

# 14 — fechamento 2+2
S[14] = photo(14) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">É assim que a empresa, aos poucos,</div>
        <div class="line">sai das suas costas sem cair.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[15] = photo(15, fade=28) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir<br>uma empresa que anda com método<br>e um dono no comando por escolha.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
