#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 41 (porta sem saida)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/41_porta-sem-saida")
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
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,700&family=Anton&family=Caveat:wght@500&display=swap" rel="stylesheet">
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
  .capa{ font-size:48px; line-height:1.3; font-weight:700; color:#1A1A1A; }
  .capa-punch{ font-size:54px; line-height:1.3; font-weight:700; color:#A91C20; margin-top:30px; }
  .hand{ font-family:'Caveat',cursive; font-weight:500; color:#3A3A3A;
    mix-blend-mode:multiply; line-height:1.25; text-align:left; }
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

# 1 — capa-isca (2 setup bold + punch vermelho)
S[1] = photo(1, fade=26) + '''    <div class="top" style="top:300px">
      <div class="capa">Tem um <span class="red">inferno</span> que foi feito<br>sob medida pra empresário.</div>
      <div class="capa-punch">Eu já estive dentro dele.</div>
    </div>
'''

# 2 — tapa (grito puro Anton, 1 linha)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:320px">
      <div class="line anton" style="font-size:{FIT.get("2", 96)}px">RECUPERAÇÃO JUDICIAL.</div>
    </div>
'''

# 3 — a confissão 2+2
S[3] = photo(3, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Eu nunca imaginei que esse nome</div>
        <div class="line">fosse bater na minha porta.</div>
      </div>
      <div class="stanza">
        <div class="line red">Nenhum empresário imagina.</div>
        <div class="line red">Até o dia que bate.</div>
      </div>
    </div>
'''

# 4 — os conselheiros 2+2
S[4] = photo(4, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E eu não estava sozinho.</div>
        <div class="line">Tinha dois conselheiros de peso.</div>
      </div>
      <div class="stanza">
        <div class="line red">Um ex-presidente de multinacional.</div>
        <div class="line red">Um gênio do mercado financeiro.</div>
      </div>
    </div>
'''

# 5 — a quebra 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5, fade=22) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Currículo de dar inveja.</div>
        <div class="line">Experiência de sobra.</div>
      </div>
      <div class="stanza">
        <div class="line red">E nenhum sabia lidar com dívida</div>
        <div class="line red">de pequena e média empresa.</div>
      </div>
    </div>
'''

# 6 — e eu também não (âncora + estrofe)
S[6] = photo(6, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E eu também não sabia.</div>
      </div>
      <div class="stanza">
        <div class="line red">Três homens experientes.</div>
        <div class="line red">Nenhum mapa daquele lugar.</div>
      </div>
    </div>
'''

# 7 — o inferno (2 + âncora)
S[7] = photo(7, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Lá dentro, você acorda todo dia</div>
        <div class="line">procurando a porta de saída.</div>
      </div>
      <div class="stanza">
        <div class="line red">Ela não está em lugar nenhum.</div>
      </div>
    </div>
'''

# 8 — reverbera (2 + âncora)
S[8] = photo(8, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Eu saí daquele inferno.</div>
        <div class="line">Custou anos e custou caro.</div>
      </div>
      <div class="stanza">
        <div class="line red">E tem coisa que reverbera até hoje.</div>
      </div>
    </div>
'''

# 9 — reveal (heroi: 2 serif + 1 Anton)
S[9] = photo(9, fade=22) + f'''    <div class="top" style="top:260px">
      <div class="line">O que me jogou lá dentro</div>
      <div class="line">não foi o mercado nem a crise.</div>
      <div class="line anton" style="font-size:{FIT.get("9", 78)}px;margin-top:22px">FOI O QUE EU NÃO SABIA.</div>
    </div>
'''

# 10 — sócia oculta 2+2
S[10] = photo(10, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A ignorância é uma sócia oculta.</div>
        <div class="line">Não assina contrato, não aparece.</div>
      </div>
      <div class="stanza">
        <div class="line red">Mas a conta dela é sempre</div>
        <div class="line red">a mais cara da empresa.</div>
      </div>
    </div>
'''

# 11 — espelho 2+2 (2a estrofe inteira vermelha) + escrita à mão no envelope
S[11] = photo(11, fade=22) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Agora olha pra sua empresa.</div>
        <div class="line">O que você não sabe hoje?</div>
      </div>
      <div class="stanza">
        <div class="line red">Isso já está te custando.</div>
        <div class="line red">Você só não viu a conta ainda.</div>
      </div>
    </div>
    <div class="hand" style="position:absolute;left:0;right:0;top:944px;font-size:20px;line-height:1.45;text-align:center;opacity:.92;transform:rotate(-1.5deg);z-index:2">Remetente: tio Lu<br>Endereço: quinto dos infernos</div>
'''

# 12 — os dois preços 2+2
S[12] = photo(12, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O conhecimento tem dois preços.</div>
        <div class="line">Antes da crise, custa estudo.</div>
      </div>
      <div class="stanza">
        <div class="line red">Dentro da crise,</div>
        <div class="line red">custa a empresa.</div>
      </div>
    </div>
'''

# 13 — vê o buraco de longe 2+2
S[13] = photo(13, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Quem domina os números</div>
        <div class="line">vê o buraco de longe.</div>
      </div>
      <div class="stanza">
        <div class="line red">E decide cedo, enquanto</div>
        <div class="line red">decidir ainda é barato.</div>
      </div>
    </div>
'''

# 14 — treinamento 2+2
S[14] = photo(14, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Essa aula entrou no meu treinamento</div>
        <div class="line">de gestão pra pequena e média empresa.</div>
      </div>
      <div class="stanza">
        <div class="line red">O que eu paguei caro pra aprender,</div>
        <div class="line red">você aprende antes da conta chegar.</div>
      </div>
    </div>
'''

# 15 — CTA exclusivo (layout padrão: CTA no topo + foto impactante sangrada)
S[15] = photo(15, fade=26) + '''    <div class="top" style="top:236px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro o que eu aprendi<br>enfrentando uma recuperação judicial<br>e onde eu encontrei a porta de saída.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
