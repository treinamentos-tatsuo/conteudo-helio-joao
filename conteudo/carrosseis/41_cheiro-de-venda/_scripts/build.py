#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 41 (cheiro de venda)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/41_cheiro-de-venda")
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


def photo(n, fade=26, lift=0, fadebot=0):
    if fadebot:
        grad = f'linear-gradient(to bottom,transparent 0%,#000 {fade}%,#000 {100-fadebot}%,transparent 100%)'
    else:
        grad = f'linear-gradient(to bottom,transparent 0%,#000 {fade}%)'
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:{lift}px;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:{grad};'
            f'mask-image:{grad};z-index:1;">\n')


S = {}

# 1 — capa (isca): impacto negrito 48 + punch vermelho negrito 58
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:300px">
      <div class="line" style="font-size:48px;font-weight:700">Dá pra saber se uma empresa vende</div>
      <div class="line red" style="font-size:58px;margin-top:18px">sem olhar um número sequer.</div>
    </div>
'''

# 2 — tapa (grito puro Anton, 1 linha, alvo 640)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:310px">
      <div class="line anton" style="font-size:{FIT.get("2", 100)}px">É SÓ SENTIR O CHEIRO.</div>
    </div>
'''

# 3 — cheira a venda (âncora + estrofe)
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Tem empresa que cheira a venda.</div>
      </div>
      <div class="stanza">
        <div class="line">Telefone tocando, balcão vivo,</div>
        <div class="line red">gente correndo atrás de cliente.</div>
      </div>
    </div>
'''

# 4 — cheira a hospital (âncora + estrofe)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E tem empresa que cheira a hospital.</div>
      </div>
      <div class="stanza">
        <div class="line">Silêncio no balcão, pressa nenhuma,</div>
        <div class="line red">todo mundo esperando o cliente vir.</div>
      </div>
    </div>
'''

# 5 — a leitura errada 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aí as vendas caem. E você corre</div>
        <div class="line">pro mesmo lugar de sempre:</div>
      </div>
      <div class="stanza">
        <div class="line red">treina vendedor, troca gerente,</div>
        <div class="line red">contrata um novo que promete.</div>
      </div>
    </div>
'''

# 6 — não muda (âncora + estrofe)
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:280px">
      <div class="stanza">
        <div class="line">E nada muda.</div>
      </div>
      <div class="stanza">
        <div class="line">Porque o problema não mora</div>
        <div class="line red">dentro do departamento.</div>
      </div>
    </div>
'''

# 7 — doutrina 2+2 (2a estrofe inteira vermelha)
S[7] = photo(7, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Cultura de venda não é setor.</div>
        <div class="line">É a empresa inteira.</div>
      </div>
      <div class="stanza">
        <div class="line red">O porteiro tem que ter.</div>
        <div class="line red">A copeira tem que ter.</div>
      </div>
    </div>
'''

# 8 — reveal (heroi: serif + Anton casando na referência)
S[8] = photo(8, fade=26) + f'''    <div class="top" style="top:280px">
      <div class="line">E essa temperatura não nasce no time.</div>
      <div class="line anton" style="font-size:{FIT.get("8", 90)}px;margin-top:22px">NASCE NO DONO.</div>
    </div>
'''

# 9 — pedrada (estrofe única)
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line">Time frio não nasce frio.</div>
        <div class="line red">Ele esfria olhando pra você.</div>
      </div>
    </div>
'''

# 10 — o teste 2+2
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Faz o teste amanhã cedo:</div>
        <div class="line">entra na empresa como cliente.</div>
      </div>
      <div class="stanza">
        <div class="line">Para na porta, respira fundo,</div>
        <div class="line red">e sente o que o cliente sente.</div>
      </div>
    </div>
'''

# 11 — bordão 2+2 (2a estrofe inteira vermelha)
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você pode ter meta na parede,</div>
        <div class="line">processo desenhado, planilha em dia.</div>
      </div>
      <div class="stanza">
        <div class="line red">Máquina de venda sem cheiro de venda</div>
        <div class="line red">não é máquina de venda.</div>
      </div>
    </div>
'''

# 12 — desejo 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Na empresa com cheiro de venda,</div>
        <div class="line">o cliente percebe na entrada.</div>
      </div>
      <div class="stanza">
        <div class="line red">A venda começa antes</div>
        <div class="line red">do vendedor abrir a boca.</div>
      </div>
    </div>
'''

# 13 — como 2+2
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Esse calor não vem de palestra</div>
        <div class="line">de motivação no fim do ano.</div>
      </div>
      <div class="stanza">
        <div class="line red">Vem de rotina: meta acompanhada,</div>
        <div class="line red">venda comemorada, dono presente.</div>
      </div>
    </div>
'''

# 14 — treinamento 2+2
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa:</div>
      </div>
      <div class="stanza">
        <div class="line red">como criar a cultura de venda</div>
        <div class="line red">que esquenta a empresa inteira.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (CTA no topo + foto impactante sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir<br>a cultura que esquenta a sua empresa<br>e transforma ambiente em venda.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
