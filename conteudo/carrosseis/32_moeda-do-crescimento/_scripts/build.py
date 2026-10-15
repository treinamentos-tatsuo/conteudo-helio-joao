#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 32 (a moeda do crescimento)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/32_moeda-do-crescimento")
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


def photo(n, fade=18):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


S = {}

# 1 — capa (a cena que dói)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:220px">
      <div class="impact">Você aumentou o salário.<br><span class="red">E ele foi embora mesmo assim.</span></div>
    </div>
'''

# 2 — a cena 2+2
S[2] = photo(2, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Cobriu a proposta. Prometeu bônus.</div>
        <div class="line">Segurou ele na sala uma hora.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele agradeceu, apertou a sua mão,</div>
        <div class="line red">e pediu as contas do mesmo jeito.</div>
      </div>
    </div>
'''

# 3 — a conclusao errada 2+2
S[3] = photo(3, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aí veio a conclusão de sempre:</div>
        <div class="line">"hoje ninguém tem compromisso".</div>
      </div>
      <div class="stanza">
        <div class="line">Essa desculpa te conforta.</div>
        <div class="line red">Mas a conta não fecha.</div>
      </div>
    </div>
'''

# 4 — virada 2+2 (sangria total, muda regerada baixa no quadro)
S[4] = photo(4, fade=28) + '''    <div class="top" style="top:200px">
      <div class="stanza">
        <div class="line">Ele não saiu por dinheiro.</div>
        <div class="line">Dinheiro você ofereceu.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele saiu porque parou</div>
        <div class="line red">de crescer aí dentro.</div>
      </div>
    </div>
'''

# 5 — o reveal (a moeda) 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5, fade=22) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Salário é só uma das moedas</div>
        <div class="line">que pagam o seu funcionário.</div>
      </div>
      <div class="stanza">
        <div class="line red">Crescimento é outra.</div>
        <div class="line red">E é a que mais vale.</div>
      </div>
    </div>
'''

# 6 — mecanismo 2+2
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Trabalhar com quem sabe mais,</div>
        <div class="line">aprender, sair melhor do que entrou.</div>
      </div>
      <div class="stanza">
        <div class="line">Pra gente boa, isso é pagamento.</div>
        <div class="line red">Não é filantropia. É estratégia.</div>
      </div>
    </div>
'''

# 7 — a pergunta que dói (setup serif + Anton vermelho 2 linhas)
S[7] = photo(7, fade=26) + f'''    <div class="top" style="top:200px">
      <div class="line">Agora a pergunta que dói:</div>
      <div class="line anton" style="font-size:{FIT.get("7",96)}px; margin-top:44px">QUANTO DESSA MOEDA<br>VOCÊ TEM NO CAIXA?</div>
    </div>
'''

# 8 — pedrada 2+2
S[8] = photo(8, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Dono que não estuda nada,</div>
        <div class="line">que não se atualiza nunca,</div>
      </div>
      <div class="stanza">
        <div class="line">quer pagar o próprio time</div>
        <div class="line red">com uma moeda que ele não tem.</div>
      </div>
    </div>
'''

# 9 — pedrada 2 2+2
S[9] = photo(9, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O seu melhor funcionário</div>
        <div class="line">já aprendeu tudo o que você sabia.</div>
      </div>
      <div class="stanza">
        <div class="line">Quando ele chegar amanhã,</div>
        <div class="line red">o que você ensina de novo?</div>
      </div>
    </div>
'''

# 10 — consequencia 2+2 (bloco no topo, pedido do user)
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:180px">
      <div class="stanza">
        <div class="line">Gente boa não espera.</div>
        <div class="line">Ela procura onde cresce.</div>
      </div>
      <div class="stanza">
        <div class="line">Se não cresce com você,</div>
        <div class="line red">cresce no seu concorrente.</div>
      </div>
    </div>
'''

# 11 — regua 2+2 (2a estrofe inteira vermelha)
S[11] = photo(11, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A régua é dura, mas é simples:</div>
        <div class="line">o time cresce até onde o dono foi.</div>
      </div>
      <div class="stanza">
        <div class="line red">A empresa não passa</div>
        <div class="line red">do seu tamanho.</div>
      </div>
    </div>
'''

# 12 — investe em tudo, menos em voce 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você investe em máquina,</div>
        <div class="line">em estoque, em anúncio...</div>
      </div>
      <div class="stanza">
        <div class="line">Mas no seu conhecimento,</div>
        <div class="line red">quando foi a última vez?</div>
      </div>
    </div>
'''

# 13 — curso de cracha (teoria x pratica) 2+2
S[13] = photo(13, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E não é curso pra fazer contato</div>
        <div class="line">e encher caderno de insight.</div>
      </div>
      <div class="stanza">
        <div class="line">Porque na teoria é uma coisa.</div>
        <div class="line red">Na prática, a história é outra.</div>
      </div>
    </div>
'''

# 14 — capacitacao de verdade + treinamento 2+2
S[14] = photo(14, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Capacitação de verdade é a que</div>
        <div class="line red">muda a sua segunda-feira.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 15 — CTA (texto no topo + foto sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma empresa<br>que forma gente boa, segura os melhores<br>e cresce junto com eles.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
