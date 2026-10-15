#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 173 (Dia do Vendedor; editorial-punch com fotos reais do Hélio).
Layout da skill: corpo top 240 / capa 280, Source Serif 44 (capa 46), Anton só no grito da capa.
A foto entra na faixa de baixo, começando GAP px abaixo do texto (box.json gerado por photos.py)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
try: BOX = {int(k): v for k, v in json.loads((SCR/"box.json").read_text()).items()}
except FileNotFoundError: BOX = {}
FADE = {6: 7}
HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&family=Anton&display=swap" rel="stylesheet">
<style>
  *{ margin:0; padding:0; box-sizing:border-box; }
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; }
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  i{ font-style:italic; }
</style>
</head>
<body>
"""
def img(n):
    b = BOX.get(n)
    if not b: return ""
    F = FADE.get(n, 20)
    m = f"linear-gradient(to bottom,transparent 0%,rgba(0,0,0,0.35) {F*0.45:.1f}%,#000 {F}%)"
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" style="position:absolute;top:{b["top"]}px;left:0;'
            f'width:1080px;height:{b["h"]}px;mix-blend-mode:multiply;-webkit-mask-image:{m};mask-image:{m};z-index:1;">')

def st(*lines):
    out = '      <div class="stanza">\n'
    for l in lines:
        cls = "line"
        if l.startswith("R:"): cls, l = "line red", l[2:]
        elif l.startswith("A:"): cls, l = "line anton", l[2:]
        out += f'        <div class="{cls}">{l}</div>\n'
    return out + '      </div>\n'

S = {
 1: (280, st("Hoje é o Dia do Vendedor,", "e isso faz passar um filme", "na minha cabeça,") +
          st("R:porque foi através das vendas", "R:que eu saí da feira e me tornei", "R:um empresário que vendeu") +
          '      <div class="stanza" style="margin-top:14px">\n        <div class="line anton" style="font-size:88px">MAIS DE 7 BILHÕES</div>\n        <div class="line anton" style="font-size:88px">DE REAIS.</div>\n      </div>\n'),
 2: (240, st("Tudo isso me lembra", "o início da minha carreira,", "antes de ser empresário.") +
          st("Vendedor <i>only commission</i>,", "R:de porta em porta,", "R:vendendo Barsa e Mirador.")),
 3: (240, st("Fiz mais de dez mil demonstrações,", "anotadas cliente por cliente.") +
          st("Chegou um ponto em que,", "só no aperto de mão do bom dia,", "R:eu já sabia se ia vender ou não.")),
 4: (240, st("Tudo o que eu aprendi nessas portas", "virou livro: <i>Você Nasceu Para Vender Muito</i>,", "best-seller da Veja e da PublishNews.") +
          st("Escrevi pra mostrar que venda não é dom.", "R:É técnica, e técnica se aprende.")),
 5: (240, st("Em 1997 eu abri o meu escritório", "em São José do Rio Preto", "pra vender purificador de água.", "Seiscentos reais de aluguel.") +
          st("Quem vendia era eu.", "R:Quem atendia o telefone e cuidava", "R:de todo o resto era a Regina,", "R:minha esposa.")),
 6: (240, st("E por muito tempo eu achei", "que era isso que fazia a empresa crescer:") +
          st("vender cada vez mais,", "R:aumentar o faturamento.")),
 7: (240, st("Eu era um vendedor excepcional.", "Por isso a minha empresa", "sempre faturou muito.") +
          st("E por isso mesmo", "R:sempre perdeu muito dinheiro.")),
 8: (240, st("R:Porque eu era um analfabeto empresarial.") +
          st("Um vendedor que virou dono de empresa", "R:sem nunca ter aprendido a ser empresário.")),
 9: (240, st("Todo problema de gestão", "eu resolvia do mesmo jeito:", "vendendo mais.") +
          st("Tomava dois gols?", "R:Saía pra fazer dois.")),
 10: (240, st("E é o que a maioria dos donos faz até hoje.", "Em vez de aprender gestão,", "pensa em vender mais.") +
           st("Só que venda em cima", "de empresa desarrumada", "R:não resolve o problema. Acelera.")),
 11: (240, st("Se eu soubesse lá atrás", "o que eu ensino hoje,") +
           st("eu teria acumulado", "dez, talvez cem vezes mais", "R:do que eu acumulei.")),
 12: (240, st("Levei anos pra entender", "que vendedor e empresário", "são profissões diferentes.") +
           st("O vendedor resolve tudo vendendo.", "R:O empresário cuida do lucro,", "R:do crescimento e da cultura.")),
 13: (240, st("Quando eu aprendi, a empresa que começou", "num escritório de seiscentos reais", "passou a vender sem depender de mim.") +
           st("O último presidente que eu contratei", "R:pra tocar ela ganhava 1,2 milhão por ano.")),
 14: (240, st("O moleque que saiu da feira", "e estudou até os quinze", "fez MBA na FGV", "e hoje ensina dono de empresa.") +
           st("E eu continuo vendedor.", "R:Só que hoje eu vendo", "R:pensando como empresário.")),
 15: (240, st("Tudo o que eu levei", "vinte e nove anos pra aprender", "está no MBV,", "o meu treinamento pra dono de PME:") +
           st("Lucratividade, Crescimento e Cultura.", "R:A parte que a venda não resolve.")),
 16: (240, st("Feliz Dia do Vendedor.", "R:Principalmente pra você, dono,", "R:que ainda resolve tudo vendendo mais.") +
           st("Quer aprender a parte", "que a venda não resolve?") +
           '      <div class="cta-big" style="margin-top:22px">Comenta <span class="red">MBV</span></div>\n' +
           '      <div class="stanza" style="margin-top:14px">\n        <div class="line">que eu te mando no direct</div>\n        <div class="line">o link da próxima turma.</div>\n      </div>\n'),
}
for n, (top, body) in S.items():
    html = HEAD + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
print("ok", len(S))
