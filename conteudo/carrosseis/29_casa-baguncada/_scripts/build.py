#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 29 (decorar a casa bagunçada)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/29_casa-baguncada")
DEST = BASE / "instagram"
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"
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
  .scr{ position:relative; display:inline-block; }
  .scr .u{ position:absolute; left:-3%; width:106%; height:0.5em; bottom:-0.26em; pointer-events:none; }
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


def photo(n, fade=22):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


S = {}

# 1 — capa (a visita)
S[1] = photo(1) + '''    <div class="top" style="top:400px">
      <div class="impact">A sua casa está uma bagunça.<br><span class="red">E você quer chamar mais visita.</span></div>
    </div>
'''

# 2 — o tapa (herói: 2 serif + 2 Anton)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:225px">
      <div class="line">Cada venda nova é uma visita</div>
      <div class="line">entrando pela porta da frente.</div>
      <div class="line anton" style="font-size:{FIT.get("2",80)}px;margin-top:18px">E VISITA</div>
      <div class="line anton" style="font-size:{FIT.get("2",80)}px">REPARA EM TUDO.</div>
    </div>
'''

# 3 — tour dos comodos 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O estoque é um quarto entulhado.</div>
        <div class="line">A operação, um corredor apertado.</div>
      </div>
      <div class="stanza">
        <div class="line">Você conhece cada canto dessa casa.</div>
        <div class="line red">E aposta que crescendo se ajeita.</div>
      </div>
    </div>
'''

# 4 — o quarto fechado (financeiro) 2+2
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E tem um quarto nessa casa</div>
        <div class="line">que você não abre há meses.</div>
      </div>
      <div class="stanza">
        <div class="line"><span class="red">O financeiro.</span> Justamente o quarto</div>
        <div class="line">onde a bagunça custa mais caro.</div>
      </div>
    </div>
'''

# 5 — mecanismo (carrega bagunca) 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E cada venda nova atravessa</div>
        <div class="line">essa casa de ponta a ponta.</div>
      </div>
      <div class="stanza">
        <div class="line">O pedido entra limpo na porta.</div>
        <div class="line red">E sai carregando bagunça.</div>
      </div>
    </div>
'''

# 6 — escala (nao diluiu, multiplicou) 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Dez vendas, dez problemas pequenos.</div>
        <div class="line">Mil vendas, um problema gigante.</div>
      </div>
      <div class="stanza">
        <div class="line">A bagunça não diluiu.</div>
        <div class="line red">Multiplicou junto com a venda.</div>
      </div>
    </div>
'''

# 7 — aumentou tudo 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E pra dar conta de vender mais,</div>
        <div class="line">você aumentou a empresa inteira.</div>
      </div>
      <div class="stanza">
        <div class="line">Mais gente, mais estoque, mais custo.</div>
        <div class="line red">Tudo cresceu. Menos o lucro.</div>
      </div>
    </div>
'''

# 8 — o grito (heroi: 1 serif + 2 Anton)
S[8] = photo(8, fade=26) + f'''    <div class="top" style="top:250px">
      <div class="line">No papel, a empresa dobrou.</div>
      <div class="line anton" style="font-size:{FIT.get("8",90)}px;margin-top:18px">NA PRÁTICA,</div>
      <div class="line anton" style="font-size:{FIT.get("8",90)}px">DOBROU O ESTRESSE.</div>
    </div>
'''

# 9 — a alusao (heroi, estrofe unica)
S[9] = photo(9) + '''    <div class="top" style="top:300px">
      <div class="line">Vender mais com a empresa bagunçada</div>
      <div class="line red">é decorar uma casa desarrumada.</div>
    </div>
'''

# 10 — o tapa da decoracao 2+2 (estrofe inteira vermelha)
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A decoração não arruma a casa.</div>
        <div class="line">Não limpa, não organiza, não resolve.</div>
      </div>
      <div class="stanza">
        <div class="line red">Ela vira só mais uma coisa</div>
        <div class="line red">largada no meio da bagunça.</div>
      </div>
    </div>
'''

# 11 — a ordem certa (heroi, estrofe unica, grifo)
S[11] = photo(11) + f'''    <div class="top" style="top:300px">
      <div class="line">Toda casa tem uma ordem certa.</div>
      <div class="line">Primeiro se {grifo("arruma")}. Depois se decora.</div>
    </div>
'''

# 12 — arrumar e gestao 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Arrumar a empresa é conhecer o custo,</div>
        <div class="line">acertar o preço, ajustar o processo.</div>
      </div>
      <div class="stanza">
        <div class="line">É fazer uma venda dar certo inteira</div>
        <div class="line red">antes de sair multiplicando.</div>
      </div>
    </div>
'''

# 13 — sintese 2+2
S[13] = photo(13) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Crescimento não conserta empresa.</div>
        <div class="line">Só aumenta aquilo que ela já é.</div>
      </div>
      <div class="stanza">
        <div class="line">Casa arrumada multiplica lucro.</div>
        <div class="line red">Casa bagunçada multiplica problema.</div>
      </div>
    </div>
'''

# 14 — fechamento + CTA (figura flutuante recortada)
S[14] = ('''    <img src="../imagens/img-14.png" alt="" onerror="this.style.display='none'"
      style="position:absolute;top:620px;left:50%;transform:translateX(-50%);height:440px;mix-blend-mode:multiply;
      -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 78%,transparent 99%);
      mask-image:linear-gradient(to bottom,#000 0%,#000 78%,transparent 99%);z-index:1;">
''' + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Arrumar a casa não é dom. É método.</div>
      </div>
      <div class="stanza">
        <div class="line">É isso que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como arrumar a sua empresa<br>e crescer multiplicando lucro, não problema.</div>
    </div>
''')

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
