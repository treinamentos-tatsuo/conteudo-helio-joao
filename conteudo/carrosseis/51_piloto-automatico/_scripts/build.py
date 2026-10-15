#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 51 (editorial-punch, universo aviação)."""
import pathlib

IG = pathlib.Path(__file__).parent.parent / "instagram"
IG.mkdir(exist_ok=True)

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
  .stanza + .stanza{ margin-top:46px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .capa{ font-size:48px; line-height:1.3; font-weight:600; }
  .capa-punch{ font-size:57px; line-height:1.25; font-weight:700; color:#A91C20; }
  .sussurro{ font-size:30px; line-height:1.3; font-weight:400; color:#1A1A1A; margin-top:30px; }
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
</style>
</head>
<body>
  <div class="slide">
    <img src="../imagens/img-{N}.png" alt="" onerror="this.style.display='none'" style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {FADE}%);mask-image:linear-gradient(to bottom,transparent 0%,#000 {FADE}%);z-index:1;">
    <div class="top" style="top:{TOP}px">
{BODY}
    </div>
  </div>
</body>
</html>
"""


def st(lines):
    out = ['      <div class="stanza">']
    for cls, txt in lines:
        out.append(f'        <div class="line {cls}">{txt}</div>' if cls else f'        <div class="line">{txt}</div>')
    out.append("      </div>")
    return "\n".join(out)


SLIDES = {
    1: dict(top=330, fade=26, body="\n".join([
        st([("capa", "A sua empresa roda no piloto automático.")]),
        '      <div class="capa-punch" style="margin-top:34px">E ninguém programou o piloto.</div>',
        '      <div class="sussurro">Por isso ela voa torto.</div>',
    ])),
    2: dict(top=236, fade=24, body="\n".join([
        st([("", "Você já combinou mil vezes. Explicou,"), ("", "desenhou, repetiu. Todo mundo concordou.")]),
        st([("", "Na primeira correria, o time faz"), ("red", "do jeito antigo de novo.")]),
    ])),
    3: dict(top=236, fade=24, body="\n".join([
        st([("", "E você conclui que é má vontade."), ("", "Que ninguém quer nada com nada.")]),
        st([("", "Não é má vontade."), ("red", "É costume.")]),
    ])),
    4: dict(top=236, fade=24, body="\n".join([
        st([("", "Ninguém decide errar."), ("", "Na pressa, ninguém pensa.")]),
        st([("", "O corpo repete o que sempre repetiu."), ("red", "Todo mundo obedece ao automático.")]),
    ])),
    5: dict(top=236, fade=24, body="\n".join([
        st([("", "Cultura não é o que o seu time acredita.")]),
        st([("anton", "É O QUE ELE FAZ SEM PENSAR.")]),
    ])),
    6: dict(top=236, fade=24, body="\n".join([
        st([("", "Por isso quadro na parede não muda ninguém.")]),
        st([("", "Parede não grava costume."), ("red", "Repetição grava.")]),
    ])),
    7: dict(top=236, fade=24, body="\n".join([
        st([("", "E aqui mora o perigo:"), ("", "a sua empresa já tem ritos.")]),
        st([("red", "Você só não escolheu nenhum deles.")]),
    ])),
    8: dict(top=236, fade=24, body="\n".join([
        st([("", "O café que desanda em reclamação."), ("", "A reunião atrasada."), ("", "O erro que passa sem ninguém falar nada.")]),
        st([("red", "Cada um deles treina o automático"), ("red", "do seu time. Contra você.")]),
    ])),
    9: dict(top=236, fade=26, body="\n".join([
        st([("", "Rito não é detalhe."), ("", "Toda empresa tem os seus.")]),
        st([("red", "Se você não escolhe,"), ("red", "a rotina escolhe por você.")]),
    ])),
    10: dict(top=236, fade=24, body="\n".join([
        st([("", "Cultura se instala do jeito"), ("", "menos glamouroso que existe:")]),
        st([("", "rito diário, rito semanal, rito mensal."), ("red", "Repetido até ninguém precisar pensar.")]),
    ])),
    11: dict(top=236, fade=24, body="\n".join([
        st([("", "No começo, o time acha exagero."), ("", "Depois, acha normal.")]),
        st([("red", "No fim, acha que sempre foi assim.")]),
    ])),
    12: dict(top=236, fade=24, body="\n".join([
        st([("", "É assim que nasce gente"), ("", "com o DNA da empresa:")]),
        st([("", "o novato erra, e o próprio time corrige."), ("red", "Antes de você precisar mandar.")]),
    ])),
    13: dict(top=236, fade=24, body="\n".join([
        st([("", "Piloto automático"), ("", "não se desliga. Se reprograma.")]),
        st([("red", "Programar esse piloto é o que eu ensino"), ("red", "no meu treinamento de gestão"), ("red", "pra pequena e média empresa.")]),
    ])),
    14: dict(top=236, fade=26, body="\n".join([
        '      <div class="cta-big">Comenta <span class="red">DNA</span>,</div>',
        '      <div class="cta-sm">que eu te mostro como formar um time<br>com o DNA da sua empresa,<br>que faz o certo sem pensar.</div>',
    ])),
}

for n, cfg in SLIDES.items():
    html = (HEAD.replace("{N}", f"{n:02d}").replace("{FADE}", str(cfg["fade"]))
                .replace("{TOP}", str(cfg["top"])).replace("{BODY}", cfg["body"]))
    (IG / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")
