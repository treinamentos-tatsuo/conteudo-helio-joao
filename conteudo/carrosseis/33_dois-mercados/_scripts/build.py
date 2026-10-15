#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 33 (dois mercados) — v2 pós-feedback."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/33_dois-mercados")
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

# 1 — gancho-tapa (grito puro, Anton, 2 linhas)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:280px">
      <div class="line anton" style="font-size:{FIT.get("1",75)}px">O SEU MAIOR CONCORRENTE</div>
      <div class="line anton" style="font-size:{FIT.get("1",75)}px">NÃO VENDE O QUE VOCÊ VENDE.</div>
    </div>
'''

# 2 — o que você vigia 2+2
S[2] = photo(2, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você vigia quem vende igual:</div>
        <div class="line">o preço, a promoção, a vitrine.</div>
      </div>
      <div class="stanza">
        <div class="line">Conhece o concorrente de cor.</div>
        <div class="line red">E acha que a guerra é só essa.</div>
      </div>
    </div>
'''

# 3 — dois mercados (herói: 2 serif + 1 Anton)
S[3] = photo(3, fade=30) + f'''    <div class="top" style="top:280px">
      <div class="line">A sua empresa disputa</div>
      <div class="line">dois mercados ao mesmo tempo:</div>
      <div class="line anton" style="font-size:{FIT.get("3",78)}px;margin-top:22px">O DE CLIENTE E O DE GENTE.</div>
    </div>
'''

# 4 — concorrente de cliente (A, estrofe única)
S[4] = photo(4) + '''    <div class="top" style="top:280px">
      <div class="stanza">
        <div class="line">Quem disputa o bolso do cliente,</div>
        <div class="line red">você já trata como inimigo.</div>
      </div>
    </div>
'''

# 5 — concorrente de gente (B, herói-tapa) — setup em linha única
S[5] = photo(5, fade=22) + f'''    <div class="top" style="top:280px">
      <div class="line">Mas quem disputa o seu funcionário</div>
      <div class="line anton" style="font-size:{FIT.get("5",78)}px;margin-top:22px">TAMBÉM É SEU CONCORRENTE.</div>
    </div>
'''

# 6 — a proposta invisível 2+2 (2a estrofe inteira vermelha)
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A proposta que mais te ameaça</div>
        <div class="line">não chega no seu e-mail.</div>
      </div>
      <div class="stanza">
        <div class="line red">Chega direto no WhatsApp</div>
        <div class="line red">do seu melhor funcionário.</div>
      </div>
    </div>
'''

# 7 — o inimigo nem é do seu ramo 2+2
S[7] = photo(7, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Pode vir do aplicativo, da obra,</div>
        <div class="line">da empresa de outro ramo.</div>
      </div>
      <div class="stanza">
        <div class="line">Todo negócio que precisa de gente</div>
        <div class="line red">está disputando com você.</div>
      </div>
    </div>
'''

# 8 — pedrada da assimetria 2+2 — bloco alto + imagem cortada no topo (EXTRA_TOP)
S[8] = photo(8, fade=24) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Quando você perde um cliente,</div>
        <div class="line">corre atrás no mesmo dia.</div>
      </div>
      <div class="stanza">
        <div class="line">Quando perde gente boa,</div>
        <div class="line red">chama de ingratidão.</div>
      </div>
    </div>
'''

# 9 — a conexão 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Só que quem atende, vende</div>
        <div class="line">e entrega, é o time.</div>
      </div>
      <div class="stanza">
        <div class="line">Quem perde a guerra por gente</div>
        <div class="line red">perde a de cliente junto.</div>
      </div>
    </div>
'''

# 10 — o lance mínimo 2+2
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você vai dizer: eu pago em dia.</div>
        <div class="line">Pago até acima do mercado.</div>
      </div>
      <div class="stanza">
        <div class="line">Salário todo concorrente cobre.</div>
        <div class="line red">É o lance mínimo da mesa.</div>
      </div>
    </div>
'''

# 11 — os 4 pilares 2+2
S[11] = photo(11, fade=30) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Gente boa escolhe onde aprende,</div>
        <div class="line">onde ganha e onde se diverte.</div>
      </div>
      <div class="stanza">
        <div class="line">E onde tem orgulho</div>
        <div class="line red">de dizer onde trabalha.</div>
      </div>
    </div>
'''

# 12 — a régua 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Nessa guerra ninguém fica preso.</div>
        <div class="line">Gente boa fica onde escolhe.</div>
      </div>
      <div class="stanza">
        <div class="line">E a pergunta que decide tudo:</div>
        <div class="line red">ela escolheria a sua empresa?</div>
      </div>
    </div>
'''

# 13 — o caminho 2+2+2
S[13] = photo(13, fade=24) + '''    <div class="top" style="top:210px">
      <div class="stanza">
        <div class="line">Esse ambiente não se constrói</div>
        <div class="line">com frase na parede.</div>
      </div>
      <div class="stanza">
        <div class="line">Se constrói com gestão:</div>
        <div class="line">treinamento que vira rotina,</div>
      </div>
      <div class="stanza">
        <div class="line red">meta clara, reconhecimento</div>
        <div class="line red">e um caminho pra crescer.</div>
      </div>
    </div>
'''

# 14 — fechamento 2+2
S[14] = photo(14, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Isso não é dom. É método.</div>
        <div class="line">E método se aprende.</div>
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
      <div class="cta-sm">que eu te mostro como construir a empresa<br>que gente boa escolhe<br>e o cliente não larga.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
