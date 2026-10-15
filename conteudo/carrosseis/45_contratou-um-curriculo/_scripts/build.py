#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 45 (contratou um currículo) — v3."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/45_contratou-um-curriculo")
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
  .capa{ font-size:50px; line-height:1.3; font-weight:600; }
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

# 1 — capa-grito (Anton vermelho, 1 linha)
S[1] = photo(1, fade=26) + f'''    <div class="top" style="top:300px">
      <div class="line anton" style="font-size:{FIT.get("1", 96)}px">NINGUÉM DEMITE POR TÉCNICA.</div>
    </div>
'''

# 2 — espelho (estrofe única, fonte de capa)
S[2] = photo(2, fade=24) + '''    <div class="top" style="top:400px">
      <div class="stanza">
        <div class="line capa">Você contratou um currículo.</div>
        <div class="line capa red">E demitiu uma pessoa.</div>
      </div>
    </div>
'''

# 3 — a memória 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Lembra do último funcionário</div>
        <div class="line">que você mandou embora?</div>
      </div>
      <div class="stanza">
        <div class="line">Ele sabia fazer o serviço.</div>
        <div class="line red">O serviço nunca foi o problema.</div>
      </div>
    </div>
'''

# 4 — a cena 2+2 (2a estrofe inteira vermelha)
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O problema era a cara fechada.</div>
        <div class="line">A má vontade. A fofoca.</div>
      </div>
      <div class="stanza">
        <div class="line red">O veneno que ele espalhava</div>
        <div class="line red">sem encostar em ferramenta nenhuma.</div>
      </div>
    </div>
'''

# 5 — a lei 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E não foi só com ele.</div>
        <div class="line">Repara nas suas demissões:</div>
      </div>
      <div class="stanza">
        <div class="line red">quase nenhuma foi por técnica.</div>
        <div class="line red">Quase todas foram por atitude.</div>
      </div>
    </div>
'''

# 6 — a entrevista 2+2 (2a estrofe inteira vermelha)
S[6] = photo(6, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Agora volta pro dia</div>
        <div class="line">em que você contratou essa pessoa.</div>
      </div>
      <div class="stanza">
        <div class="line red">O que você avaliou?</div>
        <div class="line red">Currículo, experiência, técnica.</div>
      </div>
    </div>
'''

# 7 — reveal (heroi: 1 serif + 1 Anton)
S[7] = photo(7, fade=28) + f'''    <div class="top" style="top:260px">
      <div class="line">Você testou tudo o que ele sabia.</div>
      <div class="line anton" style="font-size:{FIT.get("7", 78)}px;margin-top:22px">E NADA DO QUE ELE ERA.</div>
    </div>
'''

# 8 — as duas datas 2+2 (2a estrofe inteira vermelha)
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Aquela demissão não foi decidida</div>
        <div class="line">no dia em que você assinou.</div>
      </div>
      <div class="stanza">
        <div class="line red">Foi marcada no dia</div>
        <div class="line red">em que você contratou.</div>
      </div>
    </div>
'''

# 9 — o mecanismo + conta tripla (2 + 2 vermelha + âncora vermelha)
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Técnica você enxerga em uma semana.</div>
        <div class="line">Caráter leva meses pra aparecer.</div>
      </div>
      <div class="stanza">
        <div class="line red">Você pagou pra ele entrar.</div>
        <div class="line red">Pagou enquanto ele envenenava.</div>
      </div>
      <div class="stanza">
        <div class="line red">E pagou de novo pra ele sair.</div>
      </div>
    </div>
'''

# 10 — o custo 2+2
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Técnica ruim custa retrabalho.</div>
        <div class="line">Retrabalho se paga com treino.</div>
      </div>
      <div class="stanza">
        <div class="line red">Atitude ruim apodrece o time.</div>
        <div class="line red">E o time se paga com a empresa.</div>
      </div>
    </div>
'''

# 11 — a distinção 2+2
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Técnica se ensina com treino.</div>
        <div class="line">Motivação se cria com ambiente.</div>
      </div>
      <div class="stanza">
        <div class="line red">Agora, caráter não tem curso.</div>
        <div class="line red">Ou entra pronto, ou não entra.</div>
      </div>
    </div>
'''

# 12 — o filtro 2+2 (v3: entrevista de RH não filtra; cultura filtra)
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Só que caráter não se filtra</div>
        <div class="line">em entrevista de RH.</div>
      </div>
      <div class="stanza">
        <div class="line red">Caráter se filtra com cultura.</div>
        <div class="line red">Quem tem, sabe o que não aceita.</div>
      </div>
    </div>
'''

# 13 — o solo 2+2 (2a estrofe inteira vermelha)
S[13] = photo(13) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Gente errada até passa na porta.</div>
        <div class="line">Mas cultura forte expulsa sozinha.</div>
      </div>
      <div class="stanza">
        <div class="line red">Não é o RH que escolhe a semente.</div>
        <div class="line red">É o solo que decide quem cria raiz.</div>
      </div>
    </div>
'''

# 14 — treinamento 2+2
S[14] = photo(14, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Só que esse solo não nasce sozinho.</div>
        <div class="line">Nasce de método, rito e sistema.</div>
      </div>
      <div class="stanza">
        <div class="line red">É o que eu ensino no meu treinamento</div>
        <div class="line red">de gestão pra pequena e média empresa.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir a cultura<br>onde gente boa cria raiz<br>e joga do seu lado.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
