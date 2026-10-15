#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 46 (nunca e dinheiro)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/46_nunca-e-dinheiro")
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

# 1 — capa: impacto preto (2 linhas) + punch vermelho maior + sussurro
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:210px">
      <div class="line" style="font-size:48px;font-weight:700">A frase que mais quebra</div>
      <div class="line" style="font-size:48px;font-weight:700">empresário no Brasil:</div>
      <div class="line red" style="font-size:58px;margin-top:26px;white-space:nowrap">"Se eu tivesse mais dinheiro."</div>
      <div class="line" style="font-size:30px;margin-top:30px">Você pensou isso essa semana.</div>
    </div>
'''

# 2 — tapa (grito puro Anton vermelho, 2 linhas)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:200px">
      <div class="line anton" style="font-size:{FIT.get("2", 86)}px">PROBLEMA DE NEGÓCIO<br>NUNCA É DINHEIRO.</div>
    </div>
'''

# 3 — prova interna 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Duvida? Lembra do teu melhor mês.</div>
        <div class="line">O dinheiro entrou de verdade.</div>
      </div>
      <div class="stanza">
        <div class="line">E três meses depois, cadê?</div>
        <div class="line red">Se fosse dinheiro, tinha resolvido.</div>
      </div>
    </div>
'''

# 4 — prova externa (isca, SEM ênfase — suspense)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você conhece a história: o filho</div>
        <div class="line">herda a empresa pronta e afunda tudo.</div>
      </div>
      <div class="stanza">
        <div class="line">Dinheiro tinha. Cliente tinha.</div>
      </div>
    </div>
'''

# 5 — punch-grito (Anton vermelho, 2 linhas)
S[5] = photo(5, fade=26) + f'''    <div class="top" style="top:200px">
      <div class="line anton" style="font-size:{FIT.get("5", 86)}px">FALTOU QUEM<br>SOUBESSE COMANDAR.</div>
    </div>
'''

# 6 — mecanismo 2+2
S[6] = photo(6, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Dinheiro não conserta empresa.</div>
        <div class="line">Ele aumenta o que ela já é.</div>
      </div>
      <div class="stanza">
        <div class="line">Na empresa arrumada, vira lucro.</div>
        <div class="line red">Na bagunçada, vira um buraco maior.</div>
      </div>
    </div>
'''

# 7 — empréstimo 2+2
S[7] = photo(7, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">É por isso que empréstimo não salva.</div>
        <div class="line">Entra dinheiro, o alívio dura pouco.</div>
      </div>
      <div class="stanza">
        <div class="line">O buraco fecha por uns meses.</div>
        <div class="line red">E volta maior, com os juros.</div>
      </div>
    </div>
'''

# 8 — virada 2+2
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O que falta na tua empresa</div>
        <div class="line">não entra por empréstimo.</div>
      </div>
      <div class="stanza">
        <div class="line">Não é capital financeiro.</div>
        <div class="line red">É capital intelectual.</div>
      </div>
    </div>
'''

# 9 — tradução 2+2
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Capital intelectual é isso:</div>
        <div class="line">saber quanto cada venda deixa,</div>
      </div>
      <div class="stanza">
        <div class="line">formar gente que entrega</div>
        <div class="line red">e cobrar o número certo.</div>
      </div>
    </div>
'''

# 10 — doutrina (herói: setup serif + Anton vermelho)
S[10] = photo(10, fade=28) + f'''    <div class="top" style="top:280px">
      <div class="line">Quer aumentar o resultado da empresa?</div>
      <div class="line anton" style="font-size:{FIT.get("10", 70)}px;margin-top:24px">AUMENTA O DONO PRIMEIRO.</div>
    </div>
'''

# 11 — contraste 2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Dinheiro, o banco te empresta.</div>
        <div class="line">Tem fila pra te oferecer.</div>
      </div>
      <div class="stanza">
        <div class="line">Conhecimento não tem crediário.</div>
        <div class="line red">Ou você constrói, ou vive sem.</div>
      </div>
    </div>
'''

# 12 — desejo 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Dono preparado muda a conta:</div>
        <div class="line">o mesmo dinheiro rende mais.</div>
      </div>
      <div class="stanza">
        <div class="line">A empresa cresce com o que já entra.</div>
        <div class="line red">Sem pedir fôlego pra banco nenhum.</div>
      </div>
    </div>
'''

# 13 — como (primeiro passo) 2+2
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Começa essa semana, simples:</div>
        <div class="line">descobre quanto sobra em cada venda.</div>
      </div>
      <div class="stanza">
        <div class="line">Esse número na mão muda</div>
        <div class="line red">toda decisão que você toma.</div>
      </div>
    </div>
'''

# 14 — fechamento (treinamento nomeado) 2+2
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Capital intelectual não cai do céu.</div>
        <div class="line">Se constrói. E tem caminho.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como virar o dono<br>que faz a empresa dar lucro<br>com o dinheiro que já entra.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
