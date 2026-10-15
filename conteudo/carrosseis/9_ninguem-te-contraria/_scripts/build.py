#!/usr/bin/env python3
"""Monta os 15 HTMLs do carrossel 9."""
import json, pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/9_ninguem-te-contraria/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"
FIT = json.loads((pathlib.Path(__file__).parent / "antonfit.json").read_text()) if (pathlib.Path(__file__).parent / "antonfit.json").exists() else {}

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
    -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 50%,transparent 97%),linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%);
    -webkit-mask-composite:source-in;
    mask-image:linear-gradient(to bottom,#000 0%,#000 50%,transparent 97%),linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%);
    mask-composite:intersect; }
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
  .ell{ position:relative; display:inline-block; }
  .ell .e{ position:absolute; left:-9%; width:118%; height:1.78em; top:-0.36em; pointer-events:none; }
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


def photo(n, fade=16):
    return (f'    <img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">\n')


def figura(n, top, height, cls=""):
    return (f'    <img class="figura{(" " + cls) if cls else ""}" src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="top:{top}px;height:{height}px">\n')


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


def elipse(txt):
    return f'<span class="ell">{txt}<img class="e" src="{EL}/elipse-larga-2.png" alt=""></span>'


S = {}

# 1 — capa / gancho
S[1] = photo(1) + '''    <div class="top" style="top:232px">
      <div class="setup">Faz tempo que ningu&eacute;m te contraria numa reuni&atilde;o.</div>
      <div class="impact" style="margin-top:26px">N&atilde;o &eacute; respeito. &Eacute; <span class="red">isolamento</span>.</div>
    </div>
'''

# 2 — a cena (2+2)
S[2] = photo(2) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O problema apareceu h&aacute; tr&ecirc;s semanas.</div>
        <div class="line">Duas pessoas do seu time j&aacute; viram.</div>
      </div>
      <div class="stanza">
        <div class="line">Comentaram no corredor entre elas</div>
        <div class="line red">e decidiram n&atilde;o te falar.</div>
      </div>
    </div>
'''

# 3 — pararam de te falar (heroi)
S[3] = photo(3) + f'''    <div class="top" style="top:232px">
      <div class="line">Voc&ecirc; n&atilde;o parou de ouvir.</div>
      <div class="line anton" style="font-size:{FIT.get("3",96)}px;margin-top:14px">Pararam de te falar.</div>
    </div>
'''

# 4 — a conversa sem voce (2+2, grifo)
S[4] = photo(4) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Todo dia a sua empresa tem uma conversa</div>
        <div class="line">sobre o que est&aacute; errado nela.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o &eacute; convidado</div>
        <div class="line">{grifo("pra essa conversa faz tempo.")}</div>
      </div>
    </div>
'''

# 5 — origem / os acertos (2+2)
S[5] = photo(5) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">E n&atilde;o foi maldade de ningu&eacute;m.</div>
        <div class="line">Voc&ecirc; deu certo uma vez. Deu certo dez.</div>
      </div>
      <div class="stanza">
        <div class="line">E ningu&eacute;m te avisou que acertar demais</div>
        <div class="line red">ensina a parar de perguntar.</div>
      </div>
    </div>
'''

# 6 — par A / o jeito antigo (duas linhas, grifo)
S[6] = photo(6) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A sua empresa dobrou de tamanho.</div>
        <div class="line">{grifo("O seu jeito de decidir, n&atilde;o.")}</div>
      </div>
    </div>
'''

# 7 — par B / o tamanho novo (2+2)
S[7] = photo(7) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Quanto maior ela fica,</div>
        <div class="line">menos coisa cabe na sua vista.</div>
      </div>
      <div class="stanza">
        <div class="line">E mais voc&ecirc; depende de algu&eacute;m</div>
        <div class="line red">disposto a te contar o que voc&ecirc; n&atilde;o viu.</div>
      </div>
    </div>
'''

# 8 — vira numero (2+2, grifo)
S[8] = photo(8) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O aviso que ningu&eacute;m te deu</div>
        <div class="line">volta depois, de outro jeito.</div>
      </div>
      <div class="stanza">
        <div class="line">Vira n&uacute;mero no fim do m&ecirc;s.</div>
        <div class="line">{grifo("E n&uacute;mero &eacute; aviso que j&aacute; custou.")}</div>
      </div>
    </div>
'''

# 9 — a armadilha (2+2, grifo)
S[9] = photo(9) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Humildade aqui n&atilde;o &eacute; baixar a cabe&ccedil;a</div>
        <div class="line">nem falar baixo na sua pr&oacute;pria empresa.</div>
      </div>
      <div class="stanza">
        <div class="line">Muito menos duvidar de voc&ecirc;</div>
        <div class="line">{grifo("e sair pedindo opini&atilde;o pra todo mundo.")}</div>
      </div>
    </div>
'''

# 10 — a virada (heroi)
S[10] = photo(10) + f'''    <div class="top" style="top:232px">
      <div class="line">Voc&ecirc; &eacute; o dono da empresa.</div>
      <div class="line anton" style="font-size:{FIT.get("10",96)}px;margin-top:14px">Mas n&atilde;o o dono</div>
      <div class="line anton" style="font-size:{FIT.get("10",96)}px">da verdade.</div>
    </div>
'''

# 11 — o prumo (2+2)
S[11] = photo(11) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Todo mestre de obra usa prumo.</div>
        <div class="line">N&atilde;o porque duvida do pr&oacute;prio olho.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas porque parede torta</div>
        <div class="line red">n&atilde;o parece torta pra quem levantou.</div>
      </div>
    </div>
'''

# 12 — mecanismo (2+2, grifo)
S[12] = photo(12) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Tenha pessoas do seu lado</div>
        <div class="line">que possam te dizer n&atilde;o sem medo.</div>
      </div>
      <div class="stanza">
        <div class="line">E perguntar antes de decidir,</div>
        <div class="line">{grifo("n&atilde;o depois de j&aacute; ter decidido.")}</div>
      </div>
    </div>
'''

# 13 — sempre comecando (2+2)
S[13] = photo(13) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">O que voc&ecirc; levou dez anos construindo,</div>
        <div class="line">o mercado desmonta em dois.</div>
      </div>
      <div class="stanza">
        <div class="line">No fim, voc&ecirc; n&atilde;o chegou em lugar nenhum.</div>
        <div class="line red">Voc&ecirc; est&aacute; sempre come&ccedil;ando.</div>
      </div>
    </div>
'''

# 14 — o comeco do fim (heroi)
S[14] = photo(14) + f'''    <div class="top" style="top:232px">
      <div class="line">E o dia em que voc&ecirc; achar que chegou l&aacute;...</div>
      <div class="line anton" style="font-size:{FIT.get("14",130)}px;margin-top:10px">&eacute; o come&ccedil;o do fim.</div>
    </div>
'''

# 15 — fechamento + CTA (sanduiche)
S[15] = f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Continue sendo algu&eacute;m</div>
        <div class="line">{grifo("com quem vale a pena falar.")}</div>
      </div>
    </div>
''' + figura(15, 338, 578, "fade") + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como fazer a verdade<br>voltar a chegar em voc&ecirc;.</div>
    </div>
'''

for n in range(1, 16):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
