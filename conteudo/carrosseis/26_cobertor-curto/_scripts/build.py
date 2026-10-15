#!/usr/bin/env python3
"""Monta os 13 HTMLs do carrossel 26 (cobertor curto)."""
import json, pathlib

BASE = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/26_cobertor-curto")
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
  .impact{ font-size:54px; font-weight:700; line-height:1.28; color:#1A1A1A; }
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

# 1 — capa (espelho)
S[1] = photo(1) + '''    <div class="top" style="top:400px">
      <div class="impact" style="font-size:48px">Ser dono de empresa no Brasil<br>&eacute; dormir de <span class="red">cobertor curto.</span></div>
    </div>
'''

# 2 — o tapa (grito puro, Anton fills-column, 2 linhas)
S[2] = photo(2, fade=28) + f'''    <div class="top" style="top:280px">
      <div class="line anton" style="font-size:{FIT.get("2",100)}px">COBRE A CABE&Ccedil;A,</div>
      <div class="line anton" style="font-size:{FIT.get("2",100)}px;margin-top:20px">DESCOBRE O P&Eacute;.</div>
    </div>
'''

# 3 — a cena (puxar o cobertor) 2+2
S[3] = photo(3) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Paga o fornecedor, descobre a folha.</div>
        <div class="line">Segura o pre&ccedil;o, descobre a margem.</div>
      </div>
      <div class="stanza">
        <div class="line red">Cobre um canto da empresa</div>
        <div class="line red">e o frio aparece no outro.</div>
      </div>
    </div>
'''

# 4 — o mes bom 2+2
S[4] = photo(4) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">At&eacute; que chega aquele m&ecirc;s bom.</div>
        <div class="line">A venda anda e o caixa engorda.</div>
      </div>
      <div class="stanza">
        <div class="line">Voc&ecirc; olha o saldo, respira fundo</div>
        <div class="line">e pensa: <span class="red">agora eu tenho caixa.</span></div>
      </div>
    </div>
'''

# 5 — a ilusao (ancora + 2 + 2)
S[5] = photo(5) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line"><b>N&atilde;o tem.</b></div>
      </div>
      <div class="stanza">
        <div class="line">Boa parte daquele dinheiro</div>
        <div class="line">est&aacute; s&oacute; de passagem.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele dorme na sua conta.</div>
        <div class="line red">Mas acorda na conta dos outros.</div>
      </div>
    </div>
'''

# 6 — o mecanismo (imposto embutido) 2+2
S[6] = photo(6) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Em cada venda que voc&ecirc; comemorou,</div>
        <div class="line">o imposto j&aacute; saiu embutido.</div>
      </div>
      <div class="stanza">
        <div class="line">Aquele dinheiro nunca foi seu.</div>
        <div class="line red">Voc&ecirc; n&atilde;o guardou. Voc&ecirc; recolheu.</div>
      </div>
    </div>
'''

# 7 — o grito (heroi: 2 serif + 2 Anton)
S[7] = photo(7) + f'''    <div class="top" style="top:225px">
      <div class="line">O saldo engordou.</div>
      <div class="line">S&oacute; que n&atilde;o foi pra voc&ecirc;.</div>
      <div class="line anton" style="font-size:{FIT.get("7",90)}px;margin-top:18px">VOC&Ecirc; VIROU</div>
      <div class="line anton" style="font-size:{FIT.get("7",90)}px">O COFRE DO GOVERNO.</div>
    </div>
'''

# 8 — a fila do saldo 2+2
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">E n&atilde;o &eacute; s&oacute; o governo esperando.</div>
        <div class="line">Fornecedor, folha, d&eacute;cimo terceiro.</div>
      </div>
      <div class="stanza">
        <div class="line">Caixa cheio, sem gest&atilde;o,</div>
        <div class="line red">&eacute; uma fila que ainda n&atilde;o andou.</div>
      </div>
    </div>
'''

# 9 — o tapa (puxar, nao medir) 2+2
S[9] = photo(9) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Por isso o cobertor nunca estica.</div>
        <div class="line">Voc&ecirc; administra puxando, n&atilde;o medindo.</div>
      </div>
      <div class="stanza">
        <div class="line">E gasta a sua for&ccedil;a escolhendo</div>
        <div class="line red">qual parte vai passar frio no m&ecirc;s.</div>
      </div>
    </div>
'''

# 10 — a anestesia 2+2
S[10] = photo(10) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Tem dono que vive assim h&aacute; dez anos.</div>
        <div class="line">Puxa de um lado, descobre do outro.</div>
      </div>
      <div class="stanza">
        <div class="line">Ele chama isso de rotina.</div>
        <div class="line red">O nome certo &eacute; sobreviv&ecirc;ncia.</div>
      </div>
    </div>
'''

# 11 — a virada (costurar) 2+2 (grifo)
S[11] = photo(11) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Cobertor curto n&atilde;o se resolve</div>
        <div class="line">aprendendo a puxar melhor.</div>
      </div>
      <div class="stanza">
        <div class="line">Se resolve {grifo("costurando um maior.")}</div>
        <div class="line">E quem costura &eacute; a gest&atilde;o.</div>
      </div>
    </div>
'''

# 12 — o metodo 2+2
S[12] = photo(12) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Costurar &eacute; conhecer o n&uacute;mero</div>
        <div class="line">de cada venda que voc&ecirc; faz.</div>
      </div>
      <div class="stanza">
        <div class="line">Quanto &eacute; custo, quanto &eacute; imposto</div>
        <div class="line red">e quanto sobra de verdade pra voc&ecirc;.</div>
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
        <div class="line">Caixa com dono, venda com sobra.</div>
        <div class="line">Isso n&atilde;o &eacute; sorte, &eacute; m&eacute;todo.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; isso que eu ensino no meu treinamento</div>
        <div class="line">de gest&atilde;o pra pequena e m&eacute;dia empresa.</div>
      </div>
    </div>
    <div class="bottom" style="bottom:170px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como construir uma empresa<br>que d&aacute; lucro e te deixa dormir tranquilo.</div>
    </div>
''')

for n in range(1, 14):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
