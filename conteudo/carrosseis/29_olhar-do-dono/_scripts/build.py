#!/usr/bin/env python3
"""Monta os 13 HTMLs do carrossel 29 (o olhar do dono)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/29_olhar-do-dono")
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
  .bottom{ position:absolute; left:0; right:0; padding:0 70px; text-align:center; z-index:2; }
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

# 1 — capa (a isca)
S[1] = photo(1) + '''    <div class="top" style="top:380px">
      <div class="impact">Quer <span class="red">sair da opera&ccedil;&atilde;o</span><br>da sua empresa de uma vez?</div>
    </div>
'''

# 2 — o tapa (grito puro, Anton, 1 linha)
S[2] = photo(2, fade=26) + f'''    <div class="top" style="top:300px">
      <div class="line anton" style="font-size:{FIT.get("2",100)}px">VENDE A EMPRESA.</div>
    </div>
'''

# 3 — justificativa 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">N&atilde;o &eacute; provoca&ccedil;&atilde;o nenhuma.</div>
        <div class="line">&Eacute; a resposta honesta.</div>
      </div>
      <div class="stanza">
        <div class="line">Porque pequena e m&eacute;dia empresa</div>
        <div class="line red">sobrevive do olhar do dono.</div>
      </div>
    </div>
'''

# 4 — o peso 2+2
S[4] = photo(4, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Eu sei de onde vem essa vontade.</div>
        <div class="line">Voc&ecirc; carrega a empresa nas costas.</div>
      </div>
      <div class="stanza">
        <div class="line">Abre, fecha, apaga inc&ecirc;ndio.</div>
        <div class="line red">E o peso &eacute; sempre seu.</div>
      </div>
    </div>
'''

# 5 — o vendedor de sonho 2+2 (2a estrofe inteira vermelha)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A&iacute; chega algu&eacute;m vendendo o sonho:</div>
        <div class="line">a empresa rodando sem voc&ecirc;.</div>
      </div>
      <div class="stanza">
        <div class="line red">Esse cara n&atilde;o vende liberdade.</div>
        <div class="line red">Ele lucra com o seu cansa&ccedil;o.</div>
      </div>
    </div>
'''

# 6 — o que so o dono percebe 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">S&oacute; que ningu&eacute;m enxerga a empresa</div>
        <div class="line">do jeito que o dono enxerga.</div>
      </div>
      <div class="stanza">
        <div class="line">O pre&ccedil;o errado, o cliente esfriando,</div>
        <div class="line red">s&oacute; o seu olhar percebe a tempo.</div>
      </div>
    </div>
'''

# 7 — o grito (heroi: 1 serif + 1 Anton)
S[7] = photo(7, fade=24) + f'''    <div class="top" style="top:300px">
      <div class="line">O dia que esse olhar sai de vez,</div>
      <div class="line anton" style="font-size:{FIT.get("7",90)}px;margin-top:22px">&Eacute; O IN&Iacute;CIO DO FIM.</div>
    </div>
'''

# 8 — execucao nao e comando 2+2
S[8] = photo(8, fade=34) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Isso n&atilde;o te condena a viver</div>
        <div class="line">atr&aacute;s do balc&atilde;o pra sempre.</div>
      </div>
      <div class="stanza">
        <div class="line">Chamam tudo de opera&ccedil;&atilde;o.</div>
        <div class="line red">Mas execu&ccedil;&atilde;o n&atilde;o &eacute; comando.</div>
      </div>
    </div>
'''

# 9 — a virada 2+2 (2a estrofe inteira vermelha)
S[9] = photo(9, fade=24) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Da execu&ccedil;&atilde;o bra&ccedil;al voc&ecirc; sai, sim.</div>
        <div class="line">Formando gente pra tocar a rotina.</div>
      </div>
      <div class="stanza">
        <div class="line red">Do comando da m&aacute;quina,</div>
        <div class="line red">voc&ecirc; n&atilde;o sai nunca.</div>
      </div>
    </div>
'''

# 10 — comandar e 2+2
S[10] = photo(10, fade=26) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Comandar &eacute; acompanhar o n&uacute;mero,</div>
        <div class="line">cobrar a meta, decidir o pre&ccedil;o.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; o time executando o dia a dia</div>
        <div class="line red">e voc&ecirc; decidindo o jogo.</div>
      </div>
    </div>
'''

# 11 — por escolha 2+2
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O caminho certo &eacute; a empresa parar</div>
        <div class="line">de precisar dos seus bra&ccedil;os.</div>
      </div>
      <div class="stanza">
        <div class="line">E voc&ecirc; ficar porque escolheu.</div>
        <div class="line red">N&atilde;o porque virou ref&eacute;m.</div>
      </div>
    </div>
'''

# 12 — a pedrada 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Tem dono preso no bra&ccedil;al h&aacute; anos,</div>
        <div class="line">e n&atilde;o &eacute; porque ama a opera&ccedil;&atilde;o.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; porque nunca formou gente</div>
        <div class="line red">nem m&eacute;todo pra subir ao comando.</div>
      </div>
    </div>
'''

# 13 — fechamento + CTA (figura flutuante recortada)
S[13] = ('    <img src="../imagens/img-13.png" alt="" onerror="this.style.display=\'none\'" '
         'style="position:absolute;top:585px;left:50%;transform:translateX(-50%);height:440px;'
         'mix-blend-mode:multiply;'
         '-webkit-mask-image:linear-gradient(to bottom,#000 55%,transparent 96%);'
         'mask-image:linear-gradient(to bottom,#000 55%,transparent 96%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Subir do bra&ccedil;al pro comando</div>
        <div class="line">n&atilde;o &eacute; sorte. &Eacute; m&eacute;todo.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; o que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como formar um time que executa<br>e assumir de vez o comando de uma empresa que d&aacute; lucro.</div>
    </div>
''')

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
