#!/usr/bin/env python3
"""Monta os 16 HTMLs do carrossel 45 (anda dez, volta oito)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/45_anda-dez-volta-oito")
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

# 1 — capa-grito ludica (Anton vermelho 2 linhas + sussurro)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:200px">
      <div class="line anton" style="font-size:{FIT.get("1", 93)}px">SER DONO É JOGAR<br>JOGO DE TABULEIRO.</div>
      <div class="line" style="font-size:30px;margin-top:30px">E você está perdendo sem perceber.</div>
    </div>
'''

# 2 — o jogo diario (1a estrofe)
S[2] = photo(2, fade=26) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line">Todo dia você joga os dados:</div>
        <div class="line">vende, entrega, apaga incêndio.</div>
      </div>
    </div>
'''

# 3 — a empresa anda no tabuleiro (2a estrofe, imagem do peao no caminho)
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:300px">
      <div class="stanza">
        <div class="line">E a empresa anda no tabuleiro,</div>
        <div class="line red">casa por casa, no seu esforço.</div>
      </div>
    </div>
'''

# 3 — a regra escondida 2+2
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Só que o seu tabuleiro</div>
        <div class="line">tem uma regra escondida:</div>
      </div>
      <div class="stanza">
        <div class="line">a cada dez casas que você anda,</div>
        <div class="line red">ele te manda voltar oito.</div>
      </div>
    </div>
'''

# 4 — saldo x vida 2+2
S[5] = photo(5, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aí o ano fecha no azul</div>
        <div class="line">e você não sai do lugar.</div>
      </div>
      <div class="stanza">
        <div class="line">Tem saldo? Tem.</div>
        <div class="line red">Vida é que não tem.</div>
      </div>
    </div>
'''

# 5 — o preco real 2+2
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">As duas casas que sobram,</div>
        <div class="line">você conta no caixa.</div>
      </div>
      <div class="stanza">
        <div class="line">As oito que voltam,</div>
        <div class="line red">você paga com a sua vida.</div>
      </div>
    </div>
'''

# 6 — ponte 1a pessoa (heroi: setup serif + Anton vermelho)
S[7] = photo(7, fade=26) + f'''    <div class="top" style="top:280px">
      <div class="line">Eu não li isso em livro.</div>
      <div class="line anton" style="font-size:{FIT.get("7", 60)}px;margin-top:24px">EU PAGUEI ESSA CONTA.</div>
    </div>
'''

# 7 — as pescarias canceladas 2+2
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Eu cancelei cinco pescarias</div>
        <div class="line">marcadas com o meu pai.</div>
      </div>
      <div class="stanza">
        <div class="line">Não foi por falta de dinheiro.</div>
        <div class="line red">Foi por andar dez e voltar oito.</div>
      </div>
    </div>
'''

# 8 — 2007 (ancora + estrofe, punch "Nada.")
S[9] = photo(9, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Meu pai foi embora em 2007.</div>
      </div>
      <div class="stanza">
        <div class="line">E agora, o que eu posso fazer?</div>
        <div class="line red">Nada.</div>
      </div>
    </div>
'''

# 9 — espelho (ancora + estrofe)
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O jogo agora é o seu.</div>
      </div>
      <div class="stanza">
        <div class="line">Enquanto você anda dez e volta oito,</div>
        <div class="line red">o que está ficando pra trás?</div>
      </div>
    </div>
'''

# 10 — ilusao 2+2
S[11] = photo(11, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Você jura que é uma fase.</div>
        <div class="line">Que ano que vem alivia.</div>
      </div>
      <div class="stanza">
        <div class="line">Sem gestão, ano que vem</div>
        <div class="line red">é o mesmo tabuleiro.</div>
      </div>
    </div>
'''

# 11 — virada 2+2
S[12] = photo(12, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O teu problema não é esforço.</div>
        <div class="line">Esforço você tem de sobra.</div>
      </div>
      <div class="stanza">
        <div class="line">O que engole os teus passos</div>
        <div class="line red">é o jogo rodando sem gestão.</div>
      </div>
    </div>
'''

# 12 — desejo 2+2
S[13] = photo(13, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Com gestão, o jogo vira:</div>
        <div class="line">você anda cinco e mantém cinco.</div>
      </div>
      <div class="stanza">
        <div class="line">A empresa cresce de verdade.</div>
        <div class="line red">E a pescaria, você faz.</div>
      </div>
    </div>
'''

# 13 — como 2+2
S[14] = photo(14, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Gestão aqui é coisa simples:</div>
        <div class="line">saber o número de cada passo.</div>
      </div>
      <div class="stanza">
        <div class="line">Quanto entra, quanto a empresa come,</div>
        <div class="line red">e quanto sobra pra sua vida.</div>
      </div>
    </div>
'''

# 14 — fechamento 2+2
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Virar esse jogo não é sorte.</div>
        <div class="line">É gestão. E gestão se aprende.</div>
      </div>
      <div class="stanza">
        <div class="line">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (layout padrao: CTA no topo + foto impactante sangrada)
S[16] = photo(16, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir<br>uma empresa que anda pra frente<br>sem cobrar a sua vida de volta.</div>
    </div>
'''

for n in range(1, 17):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
