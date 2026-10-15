#!/usr/bin/env python3
"""Monta os 11 HTMLs do carrossel 31 (empresa nao e familia, e um time)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/31_empresa-nao-e-familia")
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
  .impact{ font-size:50px; font-weight:700; line-height:1.22; color:#1A1A1A; }
  .setup{ font-size:35px; font-weight:400; line-height:1.3; color:#1A1A1A; }
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


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


S = {}

# 1 — capa (a frase que o dono repete)
S[1] = photo(1) + '''    <div class="top" style="top:372px">
      <div class="setup">Você repete isso com orgulho:</div>
      <div class="impact" style="margin-top:26px">Aqui, somos uma <span class="red">família</span>.</div>
    </div>
'''

# 2 — EMPRESA NAO E FAMILIA (heroi Anton puro)
S[2] = photo(2) + f'''    <div class="top" style="top:290px">
      <div class="line anton" style="font-size:{FIT.get("2",96)}px">EMPRESA NÃO É FAMÍLIA.</div>
    </div>
'''

# 3 — a prova 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Família você não escolhe.</div>
        <div class="line">A sua equipe, você escolheu.</div>
      </div>
      <div class="stanza">
        <div class="line">Família ninguém manda embora.</div>
        <div class="line red">Na empresa, você já mandou.</div>
      </div>
    </div>
'''

# 4 — a mentira piedosa 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A palavra é bonita de falar.</div>
        <div class="line">Mas olha o que ela esconde.</div>
      </div>
      <div class="stanza">
        <div class="line">Família aceita, família releva.</div>
        <div class="line red">Família não cobra resultado.</div>
      </div>
    </div>
'''

# 5 — o custo 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E nessa família tem um detalhe:</div>
        <div class="line">só você se sacrifica por ela.</div>
      </div>
      <div class="stanza">
        <div class="line">O resto cumpre o horário</div>
        <div class="line red">e espera o dia do pagamento.</div>
      </div>
    </div>
'''

# 6 — reframe (heroi)
S[6] = photo(6) + f'''    <div class="top" style="top:250px">
      <div class="line">O que a sua empresa precisa</div>
      <div class="line anton" style="font-size:{FIT.get("6",88)}px;margin-top:14px">É DE UM TIME.</div>
    </div>
'''

# 7 — posicao e placar 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Time tem posição, tem placar</div>
        <div class="line">e tem cobrança todo dia.</div>
      </div>
      <div class="stanza">
        <div class="line">E ninguém bom se ofende com isso.</div>
        <div class="line red">Quem joga sério quer ser cobrado.</div>
      </div>
    </div>
'''

# 8 — o motor 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Time engajado não espera ordem.</div>
        <div class="line">Ele age por vontade própria.</div>
      </div>
      <div class="stanza">
        <div class="line">O motor não é "tem que fazer".</div>
        <div class="line red">O motor é "eu quero fazer".</div>
      </div>
    </div>
'''

# 9 — quem constroi 2+2 (grifo)
S[9] = photo(9) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Engajamento não se compra</div>
        <div class="line">com salário nem com festa.</div>
      </div>
      <div class="stanza">
        <div class="line">Engajamento se constrói.</div>
        <div class="line">{grifo("E quem constrói é o líder.")}</div>
      </div>
    </div>
'''

# 10 — grito final (heroi: estrofe + serif + Anton)
S[10] = photo(10) + f'''    <div class="top" style="top:224px">
      <div class="stanza">
        <div class="line">Engajar um time é um nível de gestão</div>
        <div class="line">que só o líder alcança.</div>
      </div>
      <div class="stanza">
        <div class="line">Ser dono não te credencia.</div>
        <div class="line anton" style="font-size:{FIT.get("10",80)}px;margin-top:14px">CNPJ NÃO FORMA LÍDER.</div>
      </div>
    </div>
'''

# 11 — fechamento + CTA (foto subida + fade duplo)
S[11] = (f'    <img src="../imagens/img-11.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Esse time não nasce por sorte.</div>
        <div class="line">Ele é construído com método.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir um time que joga<br>com você porque quer, não porque você manda.</div>
    </div>
''')

for n in range(1, 12):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
