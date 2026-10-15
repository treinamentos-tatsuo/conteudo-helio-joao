#!/usr/bin/env python3
"""Monta os 9 HTMLs do carrossel 21 (esforço não enriquece, risco calculado sim)."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/21_esforco-nao-enriquece/instagram")
DEST.mkdir(parents=True, exist_ok=True)

# Anton (grito) — ajustar apos render
A_CAPA = 70   # capa: "PRA VIVER APERTADO"
A3 = 88       # "DO PROPRIO NEGOCIO"
A8 = 82       # "E NO ESCURO SE QUEBRA"

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
  .figura{ position:absolute; left:50%; transform:translateX(-50%); mix-blend-mode:multiply; z-index:1; }
  .figura.fade{
    -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 55%,transparent 98%);
    mask-image:linear-gradient(to bottom,#000 0%,#000 55%,transparent 98%); }
  .top{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .bottom{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:52px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .setup{ font-size:43px; font-weight:400; line-height:1.3; color:#1A1A1A; }
  .sub{ font-size:31px; font-weight:400; line-height:1.34; color:#1A1A1A; }
  .impact{ font-size:56px; font-weight:400; line-height:1.24; color:#1A1A1A; }
  .hero{ font-size:50px; line-height:1.28; font-weight:400; color:#1A1A1A; }
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


def photo(n, fade=26):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def figura(n, top, height, cls=""):
    return (f'    <img class="figura{(" " + cls) if cls else ""}" src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="top:{top}px;height:{height}px">\n')


S = {}

# 1 — capa / gancho (paradoxo): serif, split no "...", punch vermelho + sub (crenca errada)
S[1] = photo(1, 26) + '''    <div class="top" style="top:330px">
      <div class="impact">Você trabalha demais...</div>
      <div class="impact red">pra viver apertado.</div>
      <div class="sub" style="margin-top:34px">E jura que a saída é trabalhar mais.</div>
    </div>
'''

# 2 — a prova (heroi): frase do Helio, punch vermelho
S[2] = photo(2, 28) + '''    <div class="top" style="top:300px">
      <div class="hero">Se esforço deixasse rico,</div>
      <div class="hero red" style="margin-top:12px">peão de metrô seria bilionário.</div>
    </div>
'''

# 3 — a dor (2+2, Anton grito)
S[3] = photo(3, 26) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Na sua empresa, você é quem mais trabalha.</div>
        <div class="line">E quem menos leva pra casa.</div>
      </div>
      <div class="stanza">
        <div class="line">Você virou o funcionário mais mal pago</div>
        <div class="line anton" style="font-size:{A3}px;margin-top:14px">do próprio negócio.</div>
      </div>
    </div>
'''

# 4 — o mecanismo (2+2)
S[4] = photo(4, 26) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">O mercado nunca pagou pelo seu esforço.</div>
        <div class="line">Ele paga pelo risco que você corre.</div>
      </div>
      <div class="stanza">
        <div class="line">Funcionário troca esforço por salário.</div>
        <div class="line red">Dono troca risco por lucro.</div>
      </div>
    </div>
'''

# 5 — a armadilha (2+2)
S[5] = photo(5, 30) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">Só que esforço não dá medo.</div>
        <div class="line">Arriscar dá. Decidir dá.</div>
      </div>
      <div class="stanza">
        <div class="line">Aí você se enterra no trabalho</div>
        <div class="line red">pra não ter que arriscar.</div>
      </div>
    </div>
'''

# 6 — a virada (2+2)
S[6] = photo(6, 24) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">O seu lucro nunca foi sorte.</div>
        <div class="line">É coragem, cobrada em dinheiro.</div>
      </div>
      <div class="stanza">
        <div class="line">O pagamento de um risco</div>
        <div class="line red">que mais ninguém quis correr.</div>
      </div>
    </div>
'''

# 7 — a ponte (2+2)
S[7] = photo(7, 26) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">Risco não é apostar no escuro.</div>
        <div class="line">Isso não é coragem, é burrice.</div>
      </div>
      <div class="stanza">
        <div class="line">O risco que enriquece</div>
        <div class="line red">é o risco calculado.</div>
      </div>
    </div>
'''

# 8 — o concreto (2+2, Anton grito)
S[8] = photo(8, 26) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem conhece a margem, o caixa e o número</div>
        <div class="line">arrisca com informação na mão.</div>
      </div>
      <div class="stanza">
        <div class="line">Quem não conhece corre no escuro.</div>
        <div class="line anton" style="font-size:{A8}px;margin-top:14px">E no escuro se quebra.</div>
      </div>
    </div>
'''

# 9 — fechamento + CTA: foto full-width subida com fade duplo (topo+rodape), CTA no linho limpo
S[9] = '''    <img src="../imagens/img-09.png" alt="" onerror="this.style.display='none'" style="position:absolute;left:0;bottom:300px;width:100%;mix-blend-mode:multiply;-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 20%,#000 74%,transparent 97%);mask-image:linear-gradient(to bottom,transparent 0%,#000 20%,#000 74%,transparent 97%);z-index:1;">
    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Suar mais não vai te enriquecer.</div>
        <div class="line red">Arriscar com número na mão, sim.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:150px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro os números que transformam<br>o seu risco em dinheiro no seu bolso.</div>
    </div>
'''

for n in range(1, 10):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
