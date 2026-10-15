#!/usr/bin/env python3
"""Monta os 16 HTMLs do carrossel 50 (piloto automático) — v1."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/50_piloto-automatico")
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

# 1 — capa-espelho (estrofe única, fonte de capa)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:330px">
      <div class="stanza">
        <div class="line capa">Tem funcionário que você já demitiu.</div>
        <div class="line capa red">Ele só ainda não ficou sabendo.</div>
      </div>
    </div>
'''

# 2 — a cena 2+2
S[2] = photo(2, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você já chamou pra conversar.</div>
        <div class="line">Uma, duas, cinco vezes.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele ouve, concorda, promete.</div>
        <div class="line red">Uma semana depois, tudo de novo.</div>
      </div>
    </div>
'''

# 3 — os sinais 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Chega atrasado no rito de todo dia.</div>
        <div class="line">Azeda o clima de qualquer sala.</div>
      </div>
      <div class="stanza">
        <div class="line">Entrega dez.</div>
        <div class="line red">Do lado de quem entrega quarenta.</div>
      </div>
    </div>
'''

# 4 — a ilusão 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E você insiste no conserto:</div>
        <div class="line">mais uma conversa, mais um curso.</div>
      </div>
      <div class="stanza">
        <div class="line">Convencido de que uma hora</div>
        <div class="line red">a ficha dele finalmente cai.</div>
      </div>
    </div>
'''

# 5 — a virada (âncora + estrofe)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line"><b>A ficha que precisa cair é a sua.</b></div>
      </div>
      <div class="stanza">
        <div class="line">Você não está falhando na cobrança.</div>
        <div class="line red">Está consertando a coisa errada.</div>
      </div>
    </div>
'''

# 6 — o que se corrige 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Abordagem errada, fechamento fraco,</div>
        <div class="line">processo torto: tudo isso se corrige.</div>
      </div>
      <div class="stanza">
        <div class="line">Erro técnico mora no conhecimento.</div>
        <div class="line red">E conhecimento se ensina.</div>
      </div>
    </div>
'''

# 7 — grito (herói: 1 serif + 1 linha Anton)
S[7] = photo(7) + f'''    <div class="top" style="top:280px">
      <div class="line">O técnico eu corrijo.</div>
      <div class="line anton" style="font-size:{FIT.get("7", 76)}px;margin-top:22px">O COMPORTAMENTO, NÃO.</div>
    </div>
'''

# 8 — o batismo 2+2 (batismo em negrito, punch vermelho)
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Comportamento não é escolha do dia.</div>
        <div class="line">É <b>piloto automático</b>.</div>
      </div>
      <div class="stanza">
        <div class="line">A sua conversa dura uma hora.</div>
        <div class="line red">O automático dirige a vida inteira.</div>
      </div>
    </div>
'''

# 9 — doutrina 2+2+âncora vermelha
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line">Não confunde as coisas:</div>
        <div class="line">time inteiro apagado é obra do dono.</div>
      </div>
      <div class="stanza">
        <div class="line">Agora, todo mundo entregando</div>
        <div class="line">e um só azedando o meio?</div>
      </div>
      <div class="stanza">
        <div class="line red">Isso não é falta de motivação.</div>
      </div>
    </div>
'''

# 10 — a plateia 2+2
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Enquanto você tem paciência,</div>
        <div class="line">quem faz as quarenta assiste.</div>
      </div>
      <div class="stanza">
        <div class="line">E aprende que, na sua empresa,</div>
        <div class="line red">entregar ou não dá no mesmo.</div>
      </div>
    </div>
'''

# 11 — a decisão (2 + âncora vermelha)
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Problema técnico, eu treino.</div>
        <div class="line">Problema de comportamento?</div>
      </div>
      <div class="stanza">
        <div class="line red">Demissão sumária. Tchau, na hora.</div>
      </div>
    </div>
'''

# 12 — não é frieza (âncora + estrofe)
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line"><b>Isso não é frieza com um.</b></div>
      </div>
      <div class="stanza">
        <div class="line">Frieza é obrigar o time inteiro</div>
        <div class="line red">a pagar pela decisão que você adia.</div>
      </div>
    </div>
'''

# 13 — desejo 2+2
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Empresa com régua é outra empresa.</div>
        <div class="line">Quem entrega sabe que vale a pena.</div>
      </div>
      <div class="stanza">
        <div class="line">Quem chega novo entende no primeiro dia</div>
        <div class="line red">o nível da casa onde entrou.</div>
      </div>
    </div>
'''

# 14 — primeiro passo 2+2
S[14] = photo(14) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O primeiro passo é simples:</div>
        <div class="line">escreve o que a sua casa não aceita.</div>
      </div>
      <div class="stanza">
        <div class="line">Três regras, ditas em voz alta.</div>
        <div class="line red">E cumpridas no primeiro teste.</div>
      </div>
    </div>
'''

# 15 — treinamento 2+2
S[15] = photo(15, fade=32) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Régua não se sustenta no grito.</div>
        <div class="line">Se sustenta com gestão.</div>
      </div>
      <div class="stanza">
        <div class="line red">É isso que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 16 — CTA exclusivo (palavra única do post: PILOTO)
S[16] = photo(16, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">PILOTO</span>,</div>
      <div class="cta-sm">que eu te mostro como construir<br>a cultura que protege quem entrega<br>e tira da frente quem contamina.</div>
    </div>
'''

for n in range(1, 17):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
