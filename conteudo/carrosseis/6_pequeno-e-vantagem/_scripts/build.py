#!/usr/bin/env python3
"""Monta os 18 HTMLs do carrossel 6."""
import json, pathlib

DEST = pathlib.Path("/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/6_pequeno-e-vantagem/instagram")
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
  .arw{ position:relative; display:inline-block; }
  .arw .a{ position:absolute; left:-2%; width:104%; height:1.05em; bottom:-0.72em; pointer-events:none; }
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


def seta(txt):
    return f'<span class="arw">{txt}<img class="a" src="{EL}/sublinhado-seta.png" alt=""></span>'


def elipse(txt):
    return f'<span class="ell">{txt}<img class="e" src="{EL}/elipse-larga-2.png" alt=""></span>'


S = {}

# 1 — capa
S[1] = photo(1) + f'''    <div class="top" style="top:352px">
      <div class="setup">Enquanto voc&ecirc; tem vergonha de ser pequeno,</div>
      <div class="impact" style="margin-top:26px">o grande <span class="red">inveja o seu tamanho</span>.</div>
    </div>
'''

# 2 — foto sangrando (figura preenche toda a sangria)
S[2] = photo(2) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Ele tem dinheiro que voc&ecirc; n&atilde;o tem.</div>
        <div class="line">Voc&ecirc; tem uma coisa que ele n&atilde;o compra...</div>
      </div>
      <div class="stanza">
        <div class="line red" style="font-style:italic">...nem com o caixa inteiro.</div>
      </div>
    </div>
'''

# 3 — heroi (foto sangrando; a agua saiu escura, nao serve como figura solta)
S[3] = photo(3) + f'''    <div class="top" style="top:232px">
      <div class="line" style="font-size:50px">O nome disso &eacute;:</div>
      <div class="line anton" style="font-size:{FIT.get("3",200)}px;margin-top:2px">Velocidade.</div>
    </div>
'''

# 4
S[4] = photo(4) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Empresa grande &eacute; transatl&acirc;ntico.</div>
        <div class="line">Tem pot&ecirc;ncia, tripula&ccedil;&atilde;o, reserva.</div>
      </div>
      <div class="stanza">
        <div class="line">S&oacute; que pra fazer uma curva</div>
        <div class="line red">ela precisa de quil&ocirc;metros.</div>
      </div>
    </div>
'''

# 5
S[5] = photo(5, fade=26) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">A sua &eacute; uma lancha.</div>
        <div class="line">Cabe pouca gente e gasta pouco.</div>
      </div>
      <div class="stanza">
        <div class="line">Errou a rota &agrave;s tr&ecirc;s,</div>
        <div class="line">{grifo("corrigiu &agrave;s tr&ecirc;s e cinco.")}</div>
      </div>
    </div>
'''

# 6 — duas linhas + anton
S[6] = photo(6) + f'''    <div class="top" style="top:228px">
      <div class="line">Enquanto ele marca a reuni&atilde;o,</div>
      <div class="line anton" style="font-size:{FIT.get("6",80)}px;margin-top:8px">Voc&ecirc; j&aacute; errou e j&aacute; corrigiu.</div>
    </div>
'''

# 7 — cliente A
S[7] = photo(7) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Voc&ecirc; sabe o nome do seu cliente.</div>
        <div class="line">Sabe por que ele reclamou ontem.</div>
      </div>
    </div>
'''

# 8 — cliente B
S[8] = photo(8) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O grande paga uma pesquisa cara</div>
        <div class="line red">pra descobrir o que voc&ecirc; j&aacute; sabe.</div>
      </div>
    </div>
'''

# 9 — comunicacao
S[9] = photo(9) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Sua ordem sai da sua boca</div>
        <div class="line">e chega na ponta no mesmo dia.</div>
      </div>
      <div class="stanza">
        <div class="line red">Na estrutura grande ela passa</div>
        <div class="line red">por quatro andares e chega torta.</div>
      </div>
    </div>
'''

# 10 — custo fixo A
S[10] = photo(10) + f'''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">Um m&ecirc;s ruim n&atilde;o te mata.</div>
        <div class="line">{grifo("Custo fixo baixo &eacute; f&ocirc;lego.")}</div>
      </div>
    </div>
'''

# 11 — custo fixo B
S[11] = photo(11) + '''    <div class="top" style="top:236px">
      <div class="stanza">
        <div class="line">O grande n&atilde;o tem esse conforto.</div>
        <div class="line red">A m&aacute;quina dele come todo m&ecirc;s.</div>
      </div>
    </div>
'''

# 12 — cultura
S[12] = photo(12) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Numa empresa de dez pessoas,</div>
        <div class="line">cultura &eacute; o que voc&ecirc; faz na frente delas.</div>
      </div>
      <div class="stanza">
        <div class="line">Numa de mil, cultura vira cartaz</div>
        <div class="line">{elipse("que ningu&eacute;m l&ecirc; na parede.")}</div>
      </div>
    </div>
'''

# 13 — copia o transatlantico
S[13] = photo(13) + f'''    <div class="top" style="top:228px">
      <div class="line">E o que voc&ecirc; faz com tudo isso?</div>
      <div class="line anton" style="font-size:{FIT.get("13",96)}px;margin-top:8px">Copia o transatl&acirc;ntico.</div>
    </div>
'''

# 14 — camada e processo
S[14] = photo(14) + '''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Cria camada, cria comit&ecirc;,</div>
        <div class="line">cria processo que ningu&eacute;m pediu.</div>
      </div>
      <div class="stanza">
        <div class="line">Fica lento igual empresa de mil</div>
        <div class="line red">sem ter o caixa de uma.</div>
      </div>
    </div>
'''

# 15 — pior dos dois mundos
S[15] = photo(15) + f'''    <div class="top" style="top:228px">
      <div class="line">Perdeu a vantagem do pequeno.</div>
      <div class="line anton" style="font-size:{FIT.get("15",118)}px;margin-top:10px">E n&atilde;o ganhou</div>
      <div class="line anton" style="font-size:{FIT.get("15",118)}px">a for&ccedil;a do grande.</div>
    </div>
'''

# 16 — pequeno nao e destino
S[16] = photo(16) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Isso n&atilde;o &eacute; pra voc&ecirc; ficar pequeno.</div>
        <div class="line">Pequeno n&atilde;o &eacute; destino nem virtude.</div>
      </div>
      <div class="stanza">
        <div class="line">&Eacute; pra voc&ecirc; usar a vantagem</div>
        <div class="line">{grifo("enquanto ela ainda &eacute; sua.")}</div>
      </div>
    </div>
'''

# 17 — rumo / metodo
S[17] = photo(17) + f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Lancha r&aacute;pida sem rumo n&atilde;o chega antes.</div>
        <div class="line red">Ela se perde antes.</div>
      </div>
      <div class="stanza">
        <div class="line">Velocidade s&oacute; vira vantagem</div>
        <div class="line">{grifo("com n&uacute;mero na m&atilde;o e rota definida.")}</div>
      </div>
    </div>
'''

# 18 — fechamento + CTA
S[18] = f'''    <div class="top" style="top:212px">
      <div class="stanza">
        <div class="line">Pare de querer o tamanho dele.</div>
        <div class="line">{grifo("Use o que ele n&atilde;o tem.")}</div>
      </div>
    </div>
''' + figura(18, 338, 578, "fade") + '''    <div class="bottom" style="bottom:168px">
      <div class="cta-big">Comenta <span class="red">307</span>,</div>
      <div class="cta-sm">que eu te mostro como virar<br>o seu tamanho a favor.</div>
    </div>
'''

for n in range(1, 19):
    (DEST / f"slide-{n:02d}.html").write_text(HEAD + S[n] + FOOT, encoding="utf-8")
print(f"OK: {len(S)} slides em {DEST}")
