#!/usr/bin/env python3
"""Monta os 12 HTMLs do carrossel 22 (a torcida que limpa / cultura)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/22_torcida-que-limpa")
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

# 1 — capa / espelho
S[1] = photo(1) + '''    <div class="top" style="top:372px">
      <div class="setup">Quer ver a sua empresa sem maquiagem?</div>
      <div class="impact" style="margin-top:26px">Olha o que ela faz<br>quando voc&ecirc; <span class="red">n&atilde;o est&aacute; l&aacute;</span>.</div>
    </div>
'''

# 2 — promessa (Japao) 2+2
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Tem uma cena que se repete</div>
        <div class="line">em toda Copa do Mundo, no Jap&atilde;o.</div>
      </div>
      <div class="stanza">
        <div class="line">E ela mostra exatamente</div>
        <div class="line red">o que falta na sua empresa.</div>
      </div>
    </div>
'''

# 3 — a cena 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O Jap&atilde;o perde o jogo.</div>
        <div class="line">E a torcida fica pra limpar o est&aacute;dio.</div>
      </div>
      <div class="stanza">
        <div class="line">No vesti&aacute;rio, deixaram tudo limpo,</div>
        <div class="line red">com um bilhete de agradecimento.</div>
      </div>
    </div>
'''

# 4 — ninguem mandou 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Ningu&eacute;m pediu pra fazer aquilo.</div>
        <div class="line">N&atilde;o tinha placa, n&atilde;o tinha fiscal.</div>
      </div>
      <div class="stanza">
        <div class="line">Fizeram no autom&aacute;tico.</div>
        <div class="line red">E o autom&aacute;tico tem nome: cultura.</div>
      </div>
    </div>
'''

# 5 — a prova (heroi)
S[5] = photo(5) + f'''    <div class="top" style="top:210px">
      <div class="line">No Jap&atilde;o, crian&ccedil;a limpa a pr&oacute;pria escola.</div>
      <div class="line">Repete at&eacute; deixar de ser tarefa,</div>
      <div class="line anton" style="font-size:{FIT.get("5",100)}px;margin-top:14px">E VIRAR QUEM ELA &Eacute;.</div>
    </div>
'''

# 6 — traduz 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Na sua empresa funciona igual.</div>
        <div class="line">O time n&atilde;o copia o que voc&ecirc; prega.</div>
      </div>
      <div class="stanza">
        <div class="line">Copia o que voc&ecirc; faz</div>
        <div class="line red">e o que voc&ecirc; deixa acontecer.</div>
      </div>
    </div>
'''

# 7 — voce ensinou 2+2 (triade)
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Todo atraso que passou batido.</div>
        <div class="line">Toda meta que ningu&eacute;m cobrou.</div>
      </div>
      <div class="stanza">
        <div class="line">Isso tamb&eacute;m &eacute; repeti&ccedil;&atilde;o.</div>
        <div class="line red">Voc&ecirc; n&atilde;o tolerou. Voc&ecirc; ensinou.</div>
      </div>
    </div>
'''

# 8 — o teste 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A sua cultura real n&atilde;o est&aacute; no discurso.</div>
        <div class="line">Est&aacute; no que roda quando voc&ecirc; n&atilde;o est&aacute;.</div>
      </div>
      <div class="stanza">
        <div class="line">Aquilo &eacute; a sua cultura.</div>
        <div class="line red">O resto &eacute; decora&ccedil;&atilde;o de parede.</div>
      </div>
    </div>
'''

# 9 — a doutrina (heroi)
S[9] = photo(9) + f'''    <div class="top" style="top:250px">
      <div class="line">Cultura n&atilde;o se exige na reuni&atilde;o.</div>
      <div class="line anton" style="font-size:{FIT.get("9",96)}px;margin-top:14px">Se instala por repeti&ccedil;&atilde;o.</div>
    </div>
'''

# 10 — o caminho 2+2 (grifo)
S[10] = photo(10) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Escolhe UM comportamento</div>
        <div class="line">e transforma em rito toda semana.</div>
      </div>
      <div class="stanza">
        <div class="line">Repete sem falhar</div>
        <div class="line">{grifo("at&eacute; ningu&eacute;m mais precisar mandar.")}</div>
      </div>
    </div>
'''

# 11 — o que trava 2+2
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O que trava a sua empresa</div>
        <div class="line">n&atilde;o &eacute; o mercado, n&atilde;o &eacute; a crise.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; a cultura que, at&eacute; hoje,</div>
        <div class="line red">voc&ecirc; treinou sem perceber.</div>
      </div>
    </div>
'''

# 12 — fechamento + CTA (foto subida + fade duplo)
S[12] = (f'    <img src="../imagens/img-12.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Cultura forte se constr&oacute;i de prop&oacute;sito.</div>
        <div class="line">&Eacute; isso que eu ensino na Imers&atilde;o MBV.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">CULTURA</span>,</div>
      <div class="cta-sm">que eu te mando os detalhes no direct.</div>
    </div>
''')

for n in range(1, 13):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
