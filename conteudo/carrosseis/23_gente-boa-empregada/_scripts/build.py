#!/usr/bin/env python3
"""Monta os 12 HTMLs do carrossel 23 (gente boa existe e ja esta empregada / recrutamento)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/23_gente-boa-empregada")
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

# 1 — capa (a dica)
S[1] = photo(1) + '''    <div class="top" style="top:372px">
      <div class="setup">Est&aacute; dif&iacute;cil contratar?</div>
      <div class="impact" style="margin-top:26px">Quer uma dica de como<br>encontrar <span class="red">gente boa</span>?</div>
    </div>
'''

# 2 — ROUBE DOS OUTROS (heroi Anton puro)
S[2] = photo(2) + f'''    <div class="top" style="top:270px">
      <div class="line anton" style="font-size:{FIT.get("2",120)}px">ROUBE DOS OUTROS.</div>
    </div>
'''

# 3 — a verdade 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Gente boa existe aos montes.</div>
        <div class="line">S&oacute; que j&aacute; est&aacute; empregada.</div>
      </div>
      <div class="stanza">
        <div class="line">Sai de um emprego numa sexta</div>
        <div class="line red">e come&ccedil;a outro na segunda.</div>
      </div>
    </div>
'''

# 4 — o mecanismo 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Esse profissional j&aacute; tem sal&aacute;rio,</div>
        <div class="line">j&aacute; tem cargo e j&aacute; tem lugar.</div>
      </div>
      <div class="stanza">
        <div class="line">O seu an&uacute;ncio n&atilde;o chega nele.</div>
        <div class="line red">Chega em quem sobrou no mercado.</div>
      </div>
    </div>
'''

# 5 — a perspectiva 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ent&atilde;o sim, est&aacute; dif&iacute;cil recrutar.</div>
        <div class="line">Mas s&oacute; do jeito que voc&ecirc; recruta.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; espera o bom bater na porta.</div>
        <div class="line red">E o bom n&atilde;o bate. &Eacute; disputado.</div>
      </div>
    </div>
'''

# 6 — a pergunta 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">No pleno emprego, montar time bom</div>
        <div class="line">&eacute; convencer quem j&aacute; est&aacute; bem.</div>
      </div>
      <div class="stanza">
        <div class="line">Por que algu&eacute;m sairia de l&aacute;</div>
        <div class="line red">pra vir trabalhar com voc&ecirc;?</div>
      </div>
    </div>
'''

# 7 — reframe (heroi)
S[7] = photo(7) + f'''    <div class="top" style="top:250px">
      <div class="line">&Eacute; aqui que o jogo muda de nome.</div>
      <div class="line anton" style="font-size:{FIT.get("7",96)}px;margin-top:14px">RECRUTAR &Eacute; VENDA.</div>
    </div>
'''

# 8 — o que se vende 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o vende sal&aacute;rio.</div>
        <div class="line">Ganhar bem, esse cara j&aacute; ganha.</div>
      </div>
      <div class="stanza">
        <div class="line">O que faz ele trocar de lado</div>
        <div class="line red">n&atilde;o est&aacute; no contracheque.</div>
      </div>
    </div>
'''

# 9 — os pilares do clima 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">&Eacute; ele saber que, do seu lado,</div>
        <div class="line">ele vai aprender muito mais.</div>
      </div>
      <div class="stanza">
        <div class="line">Vai se divertir trabalhando.</div>
        <div class="line red">E vai ter orgulho de pertencer.</div>
      </div>
    </div>
'''

# 10 — a abordagem 2+2 (grifo)
S[10] = photo(10) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A conversa &eacute; simples e direta:</div>
        <div class="line">voc&ecirc; tem orgulho de onde trabalha?</div>
      </div>
      <div class="stanza">
        <div class="line">Qual a sua perspectiva a&iacute; dentro?</div>
        <div class="line">{grifo("Vem construir a sua comigo.")}</div>
      </div>
    </div>
'''

# 11 — a regua 2+2
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Mas pra vender essa ideia</div>
        <div class="line">a sua empresa precisa ter uma.</div>
      </div>
      <div class="stanza">
        <div class="line">Ningu&eacute;m sai de um emprego bom</div>
        <div class="line red">por uma empresa sem rumo.</div>
      </div>
    </div>
'''

# 12 — a ponte 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Perspectiva n&atilde;o se promete,</div>
        <div class="line">se mostra com meta, plano e rumo.</div>
      </div>
      <div class="stanza">
        <div class="line">Empresa com gest&atilde;o atrai os bons.</div>
        <div class="line red">Empresa sem gest&atilde;o implora curr&iacute;culo.</div>
      </div>
    </div>
'''

# 13 — fechamento + CTA (foto subida + fade duplo)
S[13] = (f'    <img src="../imagens/img-13.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Esse ambiente n&atilde;o nasce por sorte.</div>
        <div class="line">Ele se constr&oacute;i com m&eacute;todo.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; o que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma empresa<br>que gente boa escolhe e n&atilde;o quer largar.</div>
    </div>
''')

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
