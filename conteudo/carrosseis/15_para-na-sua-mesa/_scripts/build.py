#!/usr/bin/env python3
"""Monta os 14 HTMLs do carrossel 15 (o problema para na sua mesa)."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/15_para-na-sua-mesa/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"

# Anton (grito). Ajustar apos render.
A_CAPA = 62    # capa, punch 2 palavras a mais
A_RESP = 72    # slide 5, "E RESPONDER QUANDO DA ERRADO" (1 linha)
A_NIN = 70     # slide 7, "NINGUEM VAI RESOLVER POR VOCE" (1 linha)
A_CPF = 74     # slide 11, "O CPF DA CULPA JA TA DEFINIDO"
H_MENOS = 100  # slide 3, heroi vermelho serif "Menos voce."

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
  .scr{ position:relative; display:inline-block; }
  .scr .u{ position:absolute; left:-3%; width:106%; height:0.5em; bottom:-0.26em; pointer-events:none; }
  .impact{ font-size:50px; font-weight:700; line-height:1.22; color:#1A1A1A; }
  .setup{ font-size:35px; font-weight:400; line-height:1.3; color:#1A1A1A; }
  .hero{ font-weight:700; line-height:1.08; color:#A91C20; }
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

# 1 — capa / gancho (reconhecimento): setup + Anton punch
S[1] = photo(1) + f'''    <div class="top" style="top:352px">
      <div class="setup" style="font-size:43px">O funcion&aacute;rio vai. O cliente vai.</div>
      <div class="line anton" style="font-size:{A_CAPA}px;margin-top:22px">O problema fica. E fica seu.</div>
    </div>
'''

# 2 — as saidas (2+2)
S[2] = photo(2) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Numa empresa, todo mundo tem uma sa&iacute;da.</div>
        <div class="line">O funcion&aacute;rio pede demiss&atilde;o.</div>
      </div>
      <div class="stanza">
        <div class="line">O cliente procura outro fornecedor.</div>
        <div class="line red">O s&oacute;cio cai fora. O parceiro desiste.</div>
      </div>
    </div>
'''

# 3 — menos voce (heroi vermelho serif)
S[3] = photo(3) + f'''    <div class="top" style="top:214px">
      <div class="stanza">
        <div class="line">Todo mundo pode virar as costas pro problema.</div>
      </div>
      <div class="hero" style="font-size:{H_MENOS}px;margin-top:30px">Menos voc&ecirc;.</div>
      <div class="stanza" style="margin-top:36px">
        <div class="line">Voc&ecirc; acorda no dia seguinte</div>
        <div class="line">e ele continua ali. Esperando por voc&ecirc;.</div>
      </div>
    </div>
'''

# 4 — romantizam (1+2)
S[4] = photo(4) + '''    <div class="top" style="top:262px">
      <div class="stanza">
        <div class="line">Muita gente romantiza o resultado.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas n&atilde;o aguentaria uma semana</div>
        <div class="line red">com o peso que vem junto.</div>
      </div>
    </div>
'''

# 5 — responder quando da errado (2 + Anton heroi)
S[5] = photo(5) + f'''    <div class="top" style="top:224px">
      <div class="stanza">
        <div class="line">Empreender n&atilde;o &eacute; ganhar</div>
        <div class="line">quando t&aacute; dando tudo certo.</div>
      </div>
      <div class="line anton" style="font-size:{A_RESP}px;margin-top:40px">&Eacute; responder quando d&aacute; errado.</div>
    </div>
'''

# 6 — a pilha na mesa (2+2)
S[6] = photo(6) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">A conta venceu. O funcion&aacute;rio saiu.</div>
        <div class="line">A m&aacute;quina quebrou. O caixa apertou.</div>
      </div>
      <div class="stanza">
        <div class="line">O governo inventou mais um imposto.</div>
        <div class="line red">E tudo para na mesma mesa. A sua.</div>
      </div>
    </div>
'''

# 7 — ninguem resolve (2 + Anton heroi)
S[7] = photo(7) + f'''    <div class="top" style="top:224px">
      <div class="stanza">
        <div class="line">N&atilde;o importa de quem &eacute; a culpa.</div>
        <div class="line">O problema &eacute; seu pra resolver.</div>
      </div>
      <div class="line anton" style="font-size:{A_NIN}px;margin-top:40px">Ningu&eacute;m vai resolver por voc&ecirc;.</div>
    </div>
'''

# 8 — capitao do navio (1+1)
S[8] = photo(8) + '''    <div class="top" style="top:288px">
      <div class="stanza">
        <div class="line">Todo mundo quer ser o capit&atilde;o do navio.</div>
      </div>
      <div class="stanza">
        <div class="line red">At&eacute; o navio come&ccedil;ar a afundar.</div>
      </div>
    </div>
'''

# 9 — titulo x responsabilidade (2+1)
S[9] = photo(9) + '''    <div class="top" style="top:252px">
      <div class="stanza">
        <div class="line">&Eacute; a&iacute; que voc&ecirc; descobre</div>
        <div class="line">quem queria mesmo a responsabilidade.</div>
      </div>
      <div class="stanza">
        <div class="line red">E quem s&oacute; queria o t&iacute;tulo.</div>
      </div>
    </div>
'''

# 10 — por que cansa (1+2)
S[10] = photo(10) + '''    <div class="top" style="top:252px">
      <div class="stanza">
        <div class="line">Empreender cansa. Mas n&atilde;o &eacute; o trabalho.</div>
      </div>
      <div class="stanza">
        <div class="line">Cansa o problema que n&atilde;o &eacute; seu</div>
        <div class="line red">e mesmo assim vira seu pra resolver.</div>
      </div>
    </div>
'''

# 11 — vitoria x culpa (2 + linha + Anton heroi)
S[11] = photo(11) + f'''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Quando d&aacute; certo, todo mundo participa.</div>
        <div class="line">Bate palma, sente inveja, colhe o que &eacute; seu.</div>
      </div>
      <div class="line" style="margin-top:44px">Quando d&aacute; errado?</div>
      <div class="line anton" style="font-size:{A_CPF}px;margin-top:26px">O CPF da culpa j&aacute; t&aacute; definido.</div>
    </div>
'''

# 12 — risco x recompensa (2+2)
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O problema vai continuar chegando.</div>
        <div class="line red">Isso &eacute; o cargo, n&atilde;o &eacute; castigo.</div>
      </div>
      <div class="stanza">
        <div class="line">Mas j&aacute; que voc&ecirc; vai correr o risco,</div>
        <div class="line">que seja por uma recompensa &agrave; altura.</div>
      </div>
    </div>
'''

# 13 — a verdade (dinheiro no bolso) (2 + 1 + red 2 linhas)
S[13] = photo(13) + '''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">O problema nunca foi o risco que voc&ecirc; corre.</div>
        <div class="line">Foi correr o risco e n&atilde;o ser recompensado.</div>
      </div>
      <div class="stanza">
        <div class="line">No fim das contas, a verdade &eacute; uma s&oacute;:</div>
        <div class="line red">Empresa nasceu pra botar<br>dinheiro no bolso do dono.</div>
      </div>
    </div>
'''

# 14 — fechamento + CTA (sanduiche: texto topo + figura + CTA rodape)
S[14] = f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Voc&ecirc; j&aacute; paga o pre&ccedil;o de ser dono.</div>
        <div class="line">Est&aacute; na hora de receber por ele.</div>
      </div>
    </div>
''' + figura(14, 384, 600, "fade") + '''    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como fazer esse peso todo<br>virar mais dinheiro l&iacute;quido no seu bolso.</div>
    </div>
'''

for n in range(1, 15):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
