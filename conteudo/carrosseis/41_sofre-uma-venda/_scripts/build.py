#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 41 (sofre uma venda)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/41_sofre-uma-venda")
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
  .cover-impact{ font-size:48px; font-weight:700; line-height:1.24; color:#1A1A1A; }
  .cover-punch{ font-size:58px; font-weight:700; line-height:1.2; color:#A91C20; margin-top:8px; }
  .whisper{ font-size:30px; font-weight:400; line-height:1.26; color:#1A1A1A; margin-top:12px; }
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

# 1 — capa (impacto + punch vermelho + sussurro)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:228px">
      <div class="cover-impact">A sua empresa não pesca.</div>
      <div class="cover-punch">Ela espera o peixe pular no barco.</div>
      <div class="whisper">e você ainda chama isso de mês bom.</div>
    </div>
'''

# 2 — a cena 2+2 (2a estrofe inteira vermelha)
S[2] = photo(2, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Tem mês que entra pedido</div>
        <div class="line">e você não sabe dizer por quê.</div>
      </div>
      <div class="stanza">
        <div class="line red">Tem mês que o telefone some.</div>
        <div class="line red">E você também não sabe.</div>
      </div>
    </div>
'''

# 3 — o ritual do achismo 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você não foi buscar a venda.</div>
        <div class="line">Ela caiu no seu colo:</div>
      </div>
      <div class="stanza">
        <div class="line">o cliente ligou, alguém indicou,</div>
        <div class="line red">o vendedor acordou inspirado.</div>
      </div>
    </div>
'''

# 4 — reveal (heroi: 2 serif + 1 Anton)
S[4] = photo(4, fade=26) + f'''    <div class="top" style="top:232px">
      <div class="line">Peixe que pula no barco não é pesca.</div>
      <div class="line">E venda que cai no colo não é venda.</div>
      <div class="line anton" style="font-size:{FIT.get("4", 78)}px;margin-top:22px">VOCÊ SOFRE UMA VENDA.</div>
    </div>
'''

# 5 — o contraste 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem vende sabe de onde</div>
        <div class="line">vem a próxima venda.</div>
      </div>
      <div class="stanza">
        <div class="line red">Quem sofre uma venda</div>
        <div class="line red">espera o telefone tocar.</div>
      </div>
    </div>
'''

# 6 — pedrada (estrofe única)
S[6] = photo(6) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line">Você não tem previsão de venda.</div>
        <div class="line red">Você tem torcida.</div>
      </div>
    </div>
'''

# 7 — a armadilha 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Enquanto entra pedido,</div>
        <div class="line">o acaso parece mérito.</div>
      </div>
      <div class="stanza">
        <div class="line">Mês bom não prova sistema.</div>
        <div class="line red">Prova que a sorte trabalhou.</div>
      </div>
    </div>
'''

# 8 — consequência 2+2 (2a estrofe inteira vermelha)
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E o que a sorte traz,</div>
        <div class="line">a sorte leva embora.</div>
      </div>
      <div class="stanza">
        <div class="line red">No mês que ela falta,</div>
        <div class="line red">você chama de crise.</div>
      </div>
    </div>
'''

# 9 — virada (heroi: 2 serif + 1 Anton)
S[9] = photo(9, fade=26) + f'''    <div class="top" style="top:260px">
      <div class="line">Não é crise.</div>
      <div class="line">É o preço de esperar a venda.</div>
      <div class="line anton" style="font-size:{FIT.get("9", 78)}px;margin-top:22px">VENDA SE FABRICA.</div>
    </div>
'''

# 10 — o como 2+2
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Fabricar venda é ter processo:</div>
        <div class="line">meta, rotina, indicador, cobrança.</div>
      </div>
      <div class="stanza">
        <div class="line">O time roda a máquina.</div>
        <div class="line red">O dono comanda a máquina.</div>
      </div>
    </div>
'''

# 11 — doutrina 2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Com máquina, você sabe quanto</div>
        <div class="line">vai faturar antes do mês virar.</div>
      </div>
      <div class="stanza">
        <div class="line">O achismo chama isso de milagre.</div>
        <div class="line red">A gestão chama de previsibilidade.</div>
      </div>
    </div>
'''

# 12 — desejo 2+2 (2a estrofe inteira vermelha)
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Previsível, a empresa cresce</div>
        <div class="line">por decisão, não por surpresa.</div>
      </div>
      <div class="stanza">
        <div class="line red">Contrata sem medo, investe</div>
        <div class="line red">sem rezar, dorme sem torcer.</div>
      </div>
    </div>
'''

# 13 — primeiro passo 2+2
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Primeiro passo: pega as dez</div>
        <div class="line">últimas vendas que entraram.</div>
      </div>
      <div class="stanza">
        <div class="line">Quantas você sabe explicar?</div>
        <div class="line red">O que não se explica, não se repete.</div>
      </div>
    </div>
'''

# 14 — fechamento (treinamento) 2+2
S[14] = photo(14, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Máquina de vendas não se compra.</div>
        <div class="line">Se constrói, peça por peça.</div>
      </div>
      <div class="stanza">
        <div class="line red">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir<br>a máquina de vendas que fatura<br>por decisão, e não por sorte.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
