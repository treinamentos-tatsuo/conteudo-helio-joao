#!/usr/bin/env python3
"""Monta os 9 HTMLs do carrossel 15 (a margem que vale o risco)."""
import pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/15_margem-que-vale/instagram")
DEST.mkdir(parents=True, exist_ok=True)
EL = "../../_banco-referencias/elementos"

# Anton (grito). Ajustar apos render.
A_CAPA = 66   # capa, 1 linha unica

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
  .setup{ font-size:43px; font-weight:400; line-height:1.3; color:#1A1A1A; }
  .hero{ font-size:49px; line-height:1.28; font-weight:400; color:#1A1A1A; }
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


def grifo(txt):
    return f'<span class="scr">{txt}<img class="u" src="{EL}/sublinhado-rabisco.png" alt=""></span>'


S = {}

# 1 — capa / gancho (paradoxo): setup + Anton punch (2 linhas)
S[1] = photo(1) + f'''    <div class="top" style="top:360px">
      <div class="setup">Voc&ecirc; arrisca tudo. Trabalha dobrado.</div>
      <div class="line anton" style="font-size:{A_CAPA}px;margin-top:24px">E fica com a menor fatia.</div>
    </div>
'''

# 2 — a fila (2+2)
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O fornecedor recebe. O banco recebe.</div>
        <div class="line">O funcion&aacute;rio e o governo recebem.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc;, que arriscou tudo,</div>
        <div class="line red">fica com o que sobrar. Se sobrar.</div>
      </div>
    </div>
'''

# 3 — o preco mais caro (2+2)
S[3] = photo(3) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">O seu risco e o seu suor</div>
        <div class="line">s&atilde;o o pre&ccedil;o mais caro da empresa.</div>
      </div>
      <div class="stanza">
        <div class="line">E pre&ccedil;o t&atilde;o alto</div>
        <div class="line red">exige retorno &agrave; altura.</div>
      </div>
    </div>
'''

# 4 — a armadilha (2+2)
S[4] = photo(4) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">&ldquo;Ent&atilde;o &eacute; s&oacute; vender mais.&rdquo;</div>
        <div class="line">N&atilde;o &eacute;.</div>
      </div>
      <div class="stanza">
        <div class="line">Fazer muito com margem curta</div>
        <div class="line red">&eacute; perder dinheiro mais r&aacute;pido.</div>
      </div>
    </div>
'''

# 5 — o que te paga (lucro) (2+2)
S[5] = photo(5) + '''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">Lucro &eacute; o que sobra</div>
        <div class="line">depois que tudo foi pago.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; o pagamento do dono</div>
        <div class="line red">pelo risco que s&oacute; ele correu.</div>
      </div>
    </div>
'''

# 6 — a tese (heroi): par centrado, punch vermelho
S[6] = photo(6) + '''    <div class="top" style="top:300px">
      <div class="hero">Se &eacute; pra gastar energia e arriscar,</div>
      <div class="hero red" style="margin-top:12px">que seja por uma margem que valha.</div>
    </div>
'''

# 7 — o contraste (2+2)
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Fazer muito e n&atilde;o sobrar nada</div>
        <div class="line">&eacute; trabalhar de gra&ccedil;a em escala.</div>
      </div>
      <div class="stanza">
        <div class="line">Empresa boa n&atilde;o &eacute; a que mais gira.</div>
        <div class="line red">&Eacute; a que mais te sobra.</div>
      </div>
    </div>
'''

# 8 — controla o que conhece (2+2, grifo)
S[8] = photo(8) + f'''    <div class="top" style="top:250px">
      <div class="stanza">
        <div class="line">Voc&ecirc; n&atilde;o defende</div>
        <div class="line">uma margem que n&atilde;o conhece.</div>
      </div>
      <div class="stanza">
        <div class="line">Sem saber {grifo("quanto sobra em cada venda")},</div>
        <div class="line">voc&ecirc; aceita qualquer neg&oacute;cio.</div>
      </div>
    </div>
'''

# 9 — fechamento + CTA (sanduiche: texto topo + figura + CTA rodape)
S[9] = f'''    <div class="top" style="top:206px">
      <div class="stanza">
        <div class="line">Lucro n&atilde;o &eacute; sorte, &eacute; escolha.</div>
        <div class="line red">Toda venda tem que te pagar pelo risco.</div>
      </div>
    </div>
''' + figura(9, 336, 620, "fade") + '''    <div class="bottom" style="bottom:150px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma empresa lucrativa,<br>que te paga pelo risco que s&oacute; voc&ecirc; corre.</div>
    </div>
'''

for n in range(1, 10):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
