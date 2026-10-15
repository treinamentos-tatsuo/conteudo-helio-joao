#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 45 (vontade propria)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/45_vontade-propria")
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


def photo(n, fade=26):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


S = {}

# 1 — capa (o punch em grito Anton vermelho)
S[1] = photo(1) + f'''    <div class="top" style="top:200px">
      <div class="line anton" style="font-size:{FIT.get("1", 100)}px">VONTADE<br>NÃO ESTÁ À VENDA.</div>
    </div>
'''

# 2 — a promessa da definicao 1+1 vermelha
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Todo dono quer um time engajado.</div>
      </div>
      <div class="stanza">
        <div class="line red">Quase nenhum sabe o que isso significa.</div>
      </div>
    </div>
'''

# 3 — a cena (tentou de tudo) 2+2
S[3] = photo(3) + '''    <div class="top" style="top:220px">
      <div class="stanza">
        <div class="line">Você já tentou de tudo:</div>
        <div class="line" style="font-style:italic;font-weight:700">aumentou, bonificou, motivou.</div>
      </div>
      <div class="stanza">
        <div class="line">Funciona uma semana.</div>
        <div class="line">Depois tudo volta ao lugar.</div>
      </div>
    </div>
'''

# 4 — a conclusao errada 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aí vem a conclusão de sempre:</div>
        <div class="line">ninguém quer nada com nada.</div>
      </div>
      <div class="stanza">
        <div class="line">A geração é fraca.</div>
        <div class="line">O mercado não ajuda.</div>
      </div>
    </div>
'''

# 5 — a virada de leitura 2+1 vermelha
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Só que você trata engajamento</div>
        <div class="line">como cobrança: apertou, saiu.</div>
      </div>
      <div class="stanza">
        <div class="line red">E aperto nunca criou vontade.</div>
      </div>
    </div>
'''

# 6 — a definicao (serif + grito Anton) — texto maior, gap curto (menos espaco negativo)
S[6] = photo(6) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line" style="font-size:52px">Engajamento é fazer o outro</div>
      </div>
      <div class="stanza" style="margin-top:26px">
        <div class="line anton" style="font-size:{FIT.get("6", 86)}px">TER VONTADE PRÓPRIA.</div>
      </div>
    </div>
'''

# 7 — a triade em estrofe unica (mesma estrutura, tudo junto)
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Vem porque quer.</div>
        <div class="line">Fica porque quer.</div>
        <div class="line red">Faz porque quer.</div>
      </div>
    </div>
'''

# 8 — o que se compra 2+2 (2a estrofe vermelha)
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A cobrança compra presença.</div>
        <div class="line">O salário compra tarefa.</div>
      </div>
      <div class="stanza">
        <div class="line red">Mas querer não entra</div>
        <div class="line red">na folha de pagamento.</div>
      </div>
    </div>
'''

# 9 — o tapa (serif + grito Anton) — close, sujeito grande; bloco maior e gap curto
S[9] = photo(9) + f'''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line" style="font-size:50px">Só líder entende isso.</div>
      </div>
      <div class="stanza" style="margin-top:24px">
        <div class="line anton" style="font-size:{FIT.get("9", 110)}px">DONO NÃO.</div>
      </div>
    </div>
'''

# 10 — a pedrada 2+2 (2a estrofe vermelha)
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Se ninguém no seu time tem vontade,</div>
        <div class="line">não é porque gente boa acabou.</div>
      </div>
      <div class="stanza">
        <div class="line red">É porque ali não existe</div>
        <div class="line red">motivo pra querer.</div>
      </div>
    </div>
'''

# 11 — o reposicionamento 2+1 vermelha
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Vontade nasce de um lugar</div>
        <div class="line">onde se aprende, onde se joga junto</div>
      </div>
      <div class="stanza">
        <div class="line red">e onde dá orgulho de estar.</div>
      </div>
    </div>
'''

# 12 — a reflexao-espelho 2+2 (2a estrofe vermelha)
S[12] = photo(12, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E se você quer um teste honesto,</div>
        <div class="line">responde pra você mesmo:</div>
      </div>
      <div class="stanza">
        <div class="line red">Se você não fosse o dono,</div>
        <div class="line red">trabalharia aí por vontade própria?</div>
      </div>
    </div>
'''

# 13 — fechamento (treinamento nomeado) 1+2
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Essa resposta se muda com cultura.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 14 — CTA exclusivo (layout padrao: CTA no topo + foto impactante sangrada)
S[14] = photo(14) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como formar um time<br>que trabalha com vontade própria.</div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
