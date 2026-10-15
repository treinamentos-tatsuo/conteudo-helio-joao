#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 46 (porta pra dentro) — v5."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/46_porta-pra-dentro")
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
        <div class="line capa">Você não está perdendo pro mercado.</div>
        <div class="line capa red">Está perdendo dentro de casa.</div>
      </div>
    </div>
'''

# 2 — a lista de culpados 2+2
S[2] = photo(2, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você tem a lista de culpados pronta:</div>
        <div class="line">a crise, o governo, o concorrente.</div>
      </div>
      <div class="stanza">
        <div class="line">Todo mês fecha no aperto,</div>
        <div class="line red">e a culpa nunca dorme em casa.</div>
      </div>
    </div>
'''

# 3 — concessão 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E lá fora o jogo é duro mesmo.</div>
        <div class="line">Imposto, juros, cliente sumindo.</div>
      </div>
      <div class="stanza">
        <div class="line">Lá fora tem adversário de verdade.</div>
        <div class="line red">Só que não é lá que você sangra.</div>
      </div>
    </div>
'''

# 4 — onde você sangra 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Onde você sangra não tem crise.</div>
        <div class="line">Não tem governo nem concorrente.</div>
      </div>
      <div class="stanza">
        <div class="line">É margem, custo, caixa, rotina.</div>
        <div class="line red">E nesse jogo só existe você.</div>
      </div>
    </div>
'''

# 5 — pedrada 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">É o jogo mais fácil da empresa.</div>
        <div class="line">Nada ali reage. Nada revida.</div>
      </div>
      <div class="stanza">
        <div class="line red">E é exatamente nele</div>
        <div class="line red">que a maioria perde.</div>
      </div>
    </div>
'''

# 6 — a cena 2+2
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você sabe o preço do concorrente.</div>
        <div class="line">Sabe a promoção da loja vizinha.</div>
      </div>
      <div class="stanza">
        <div class="line">Agora, a sua própria margem,</div>
        <div class="line red">você sabe de cabeça?</div>
      </div>
    </div>
'''

# 7 — grito (heroi: 1 serif + 2 linhas Anton)
S[7] = photo(7, fade=26) + f'''    <div class="top" style="top:260px">
      <div class="line">O mercado nunca te venceu.</div>
      <div class="line anton" style="font-size:{FIT.get("7", 76)}px;margin-top:22px">VOCÊ PERDE ONDE</div>
      <div class="line anton" style="font-size:{FIT.get("7", 76)}px">NÃO TEM ADVERSÁRIO.</div>
    </div>
'''

# 8 — vigia a rua 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Enquanto a culpa mora lá fora,</div>
        <div class="line">a solução não entra aqui dentro.</div>
      </div>
      <div class="stanza">
        <div class="line">Você passa o dia vigiando a rua.</div>
        <div class="line red">E o jogo de casa segue sem dono.</div>
      </div>
    </div>
'''

# 9 — doutrina 2+2
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Lá fora se briga por cliente.</div>
        <div class="line">Da porta pra dentro, por lucro.</div>
      </div>
      <div class="stanza">
        <div class="line">E o jogo de fora só se ganha</div>
        <div class="line red">com o de dentro ganho antes.</div>
      </div>
    </div>
'''

# 10 — a régua 2+2
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Faz o teste agora, sem planilha:</div>
        <div class="line">quanto sobra em cada venda?</div>
      </div>
      <div class="stanza">
        <div class="line">Se a resposta for um chute,</div>
        <div class="line red">você está perdendo em casa.</div>
      </div>
    </div>
'''

# 11 — o desejo 2+2
S[11] = photo(11, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem ganha da porta pra dentro</div>
        <div class="line">aguenta qualquer lá fora.</div>
      </div>
      <div class="stanza">
        <div class="line">Crise aperta, mercado balança,</div>
        <div class="line red">e sobra dinheiro mesmo assim.</div>
      </div>
    </div>
'''

# 12 — o primeiro passo 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O primeiro passo cabe num papel:</div>
        <div class="line">pega a sua última venda.</div>
      </div>
      <div class="stanza">
        <div class="line">Tira imposto, mercadoria e frete.</div>
        <div class="line red">O que sobrou é o jogo de verdade.</div>
      </div>
    </div>
'''

# 13 — treinamento 2+2
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Esse jogo de dentro tem método:</div>
        <div class="line">número na mão e rotina de cobrança.</div>
      </div>
      <div class="stanza">
        <div class="line red">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 14 — CTA exclusivo (palavra única do post: DENTRO)
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">DENTRO</span>,</div>
      <div class="cta-sm">que eu te mostro como ganhar o jogo<br>da porta pra dentro da sua empresa<br>e fazer o lucro sobrar todo mês.</div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
