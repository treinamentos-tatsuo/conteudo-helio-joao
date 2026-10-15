#!/usr/bin/env python3
"""Monta os 10 HTMLs do carrossel 26 (crescer nao e faturar mais, e aumentar a ultima linha)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/26_crescer-ultima-linha")
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
  .impact{ font-size:52px; font-weight:700; line-height:1.22; color:#1A1A1A; }
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

# 1 — capa (o paradoxo)
S[1] = photo(1) + '''    <div class="top" style="top:260px">
      <div class="setup">A sua empresa cresceu.</div>
      <div class="impact" style="margin-top:26px">E o seu bolso <span class="red">nem ficou sabendo.</span></div>
    </div>
'''

# 2 — a cena (o aplauso) 2+2
S[2] = photo(2) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A empresa vendeu mais esse ano.</div>
        <div class="line">Voc&ecirc; contratou, ampliou, investiu.</div>
      </div>
      <div class="stanza">
        <div class="line">E todo mundo te dando parab&eacute;ns:</div>
        <div class="line red">&ldquo;que orgulho, como voc&ecirc; cresceu.&rdquo;</div>
      </div>
    </div>
'''

# 3 — a dor (o saque parado) 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">S&oacute; que tem uma linha dessa hist&oacute;ria</div>
        <div class="line">que n&atilde;o cresceu junto: o seu saque.</div>
      </div>
      <div class="stanza">
        <div class="line">A empresa dobrou de tamanho.</div>
        <div class="line red">O seu dinheiro continua o mesmo.</div>
      </div>
    </div>
'''

# 4 — o grito (heroi Anton)
S[4] = photo(4) + f'''    <div class="top" style="top:250px">
      <div class="line">Se a sua empresa fatura mais</div>
      <div class="line">e a sobra continua parada,</div>
      <div class="line anton" style="font-size:{FIT.get("4",92)}px;margin-top:14px">ELA N&Atilde;O CRESCEU. ELA INCHOU.</div>
    </div>
'''

# 5 — o mecanismo (no papel x no banco) 2+2
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O faturamento subiu na frente.</div>
        <div class="line">O custo subiu grudado nele.</div>
      </div>
      <div class="stanza">
        <div class="line">No papel, a empresa &eacute; outra.</div>
        <div class="line red">No banco, &eacute; a mesma de sempre.</div>
      </div>
    </div>
'''

# 6 — a definicao (a ultima linha) 2+2 (grifo)
S[6] = photo(6) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">A &uacute;ltima linha &eacute; o fim da conta.</div>
        <div class="line">&Eacute; o que sobra depois de tudo pago.</div>
      </div>
      <div class="stanza">
        <div class="line">Folha, fornecedor, imposto, aluguel.</div>
        <div class="line">{grifo("&Eacute; dali que sai o seu pagamento.")}</div>
      </div>
    </div>
'''

# 7 — a regua (tese) 2+2
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Crescimento de verdade se mede a&iacute;.</div>
        <div class="line">Na &uacute;ltima linha subindo.</div>
      </div>
      <div class="stanza">
        <div class="line">No saque de dividendo aumentando.</div>
        <div class="line red">Na empresa vendendo com resultado.</div>
      </div>
    </div>
'''

# 8 — a pedrada 2+2 (cena escura -> fade maior)
S[8] = photo(8, fade=28) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Tem dono dobrando a empresa</div>
        <div class="line">e empobrecendo dentro dela.</div>
      </div>
      <div class="stanza">
        <div class="line">Mais risco, mais d&iacute;vida, mais peso.</div>
        <div class="line red">Pelo mesmo saque de dois anos atr&aacute;s.</div>
      </div>
    </div>
'''

# 9 — a virada (gestao por dentro) 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O crescimento bom come&ccedil;a por dentro.</div>
        <div class="line">Margem calculada, custo controlado.</div>
      </div>
      <div class="stanza">
        <div class="line">A&iacute; cada venda nova que entra</div>
        <div class="line red">aumenta a linha que paga voc&ecirc;.</div>
      </div>
    </div>
'''

# 10 — fechamento + CTA (foto subida + fade duplo)
S[10] = (f'    <img src="../imagens/img-10.png" alt="" onerror="this.style.display=\'none\'" '
         f'style="position:absolute;bottom:300px;left:0;width:100%;mix-blend-mode:multiply;'
         f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);'
         f'mask-image:linear-gradient(to bottom,transparent 0%,#000 24%,#000 82%,transparent 100%);z-index:1;">\n'
         + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Fazer a &uacute;ltima linha crescer</div>
        <div class="line">&eacute; m&eacute;todo. E m&eacute;todo se aprende.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; isso que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como fazer a sua empresa<br>crescer onde importa: no seu bolso.</div>
    </div>
''')

for n in range(1, 11):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
