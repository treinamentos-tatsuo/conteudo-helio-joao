#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 41 (baba de adulto)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/41_baba-de-adulto")
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

# 1 — capa-tapa (grito puro Anton vermelho, imagem do babador)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:200px">
      <div class="line anton" style="font-size:{FIT.get("1", 86)}px">GESTOR É BABÁ<br>DE ADULTO.</div>
    </div>
'''

# 2 — espelho (ex-capa): impacto preto + punch vermelho maior + sussurro
S[2] = photo(2, fade=26) + '''    <div class="top" style="top:300px">
      <div class="line" style="font-size:48px;font-weight:700">Você treinou o seu time inteiro.</div>
      <div class="line red" style="font-size:50px;margin-top:26px;white-space:nowrap">Na segunda-feira, estava tudo igual.</div>
      <div class="line" style="font-size:30px;margin-top:30px">E o curso não foi barato.</div>
    </div>
'''

# 3 — a cena do sucesso 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O treinamento foi ótimo.</div>
        <div class="line">Todo mundo saiu concordando.</div>
      </div>
      <div class="stanza">
        <div class="line red">Anotaram. Aplaudiram.</div>
        <div class="line red">Prometeram aplicar.</div>
      </div>
    </div>
'''

# 4 — o dia seguinte 2+2 (2a estrofe vermelha)
S[4] = photo(4, fade=30) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">No dia seguinte, cada um</div>
        <div class="line">voltou pro jeito de sempre.</div>
      </div>
      <div class="stanza">
        <div class="line red">O caderno ficou na gaveta.</div>
        <div class="line red">A promessa ficou na sala.</div>
      </div>
    </div>
'''

# 5 — a conclusão errada 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aí você conclui que treinamento</div>
        <div class="line">é dinheiro jogado fora.</div>
      </div>
      <div class="stanza">
        <div class="line">E que <span class="red">o problema</span></div>
        <div class="line">é esse time que não evolui.</div>
      </div>
    </div>
'''

# 6 — a virada (2 serif + Anton)
S[6] = photo(6, fade=26) + f'''    <div class="top" style="top:210px">
      <div class="line">O treinamento não falhou.</div>
      <div class="line">O seu time é gente normal.</div>
      <div class="line anton" style="font-size:{FIT.get("6", 62)}px;margin-top:24px">FALTOU O QUE VEM DEPOIS.</div>
    </div>
'''

# 7 — doutrina 2+2 + âncora vermelha
S[7] = photo(7, fade=28) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line">Ninguém escuta uma vez</div>
        <div class="line">e muda pra sempre.</div>
      </div>
      <div class="stanza">
        <div class="line">Ninguém sai de uma sala</div>
        <div class="line">fazendo tudo certo no outro dia.</div>
      </div>
      <div class="stanza">
        <div class="line red">Essa é a vida como ela é.</div>
      </div>
    </div>
'''

# 8 — o nome verdadeiro 2+2 (2a estrofe vermelha)
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O mercado deu um nome bonito</div>
        <div class="line">pra esse trabalho: follow up.</div>
      </div>
      <div class="stanza">
        <div class="line red">Eu chamo pelo nome verdadeiro:</div>
        <div class="line red">pajear gente grande.</div>
      </div>
    </div>
'''

# 9 — a ofensa de repetir (2 + âncora vermelha)
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você se ofende de repetir.</div>
        <div class="line">"Eu já falei mil vezes."</div>
      </div>
      <div class="stanza">
        <div class="line red">Falou. E vai falar de novo amanhã.</div>
      </div>
    </div>
'''

# 10 — régua (setup serif + Anton)
S[10] = photo(10, fade=26) + f'''    <div class="top" style="top:280px">
      <div class="line">Cobrar uma vez é aviso.</div>
      <div class="line anton" style="font-size:{FIT.get("10", 70)}px;margin-top:24px">COBRAR TODO DIA É GESTÃO.</div>
    </div>
'''

# 11 — desejo 2+2 (2a estrofe vermelha)
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Porque o combinado cobrado todo dia</div>
        <div class="line">uma hora vira automático.</div>
      </div>
      <div class="stanza">
        <div class="line red">E o padrão segura a empresa</div>
        <div class="line red">até no seu pior dia.</div>
      </div>
    </div>
'''

# 12 — primeiro passo 2+2 (2a estrofe vermelha)
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O primeiro passo é simples:</div>
        <div class="line">escreve o combinado, preto no branco.</div>
      </div>
      <div class="stanza">
        <div class="line red">E confere com o seu time</div>
        <div class="line red">todos os santos dias.</div>
      </div>
    </div>
'''

# 13 — fechamento (treinamento nomeado) 3+2
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line" style="font-size:42px">Construir essa rotina de gestão</div>
        <div class="line" style="font-size:42px">é o que eu ensino no meu treinamento</div>
        <div class="line" style="font-size:42px">pra pequena e média empresa:</div>
      </div>
      <div class="stanza">
        <div class="line red" style="font-size:42px">o que cobrar, como acompanhar</div>
        <div class="line red" style="font-size:42px">e como fazer o combinado virar cultura.</div>
      </div>
    </div>
'''

# 14 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como montar a rotina<br>que faz o seu time entregar de verdade.</div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
