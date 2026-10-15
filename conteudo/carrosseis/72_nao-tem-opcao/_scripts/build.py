#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 72 v5 (editorial-punch, "Nao tem opcao")."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# gritos: 1 (capa), 4 (o preco), 8 (o sempre)
DEFAULT_ANTON = {1: 150, 4: 88, 6: 112}
try:
    ANTON = {**DEFAULT_ANTON, **{int(k): v for k, v in json.loads((SCR / "antonfit.json").read_text()).items()}}
except FileNotFoundError:
    ANTON = DEFAULT_ANTON

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
  .stanza + .stanza{ margin-top:52px; }
  .line{ font-size:44px; line-height:1.26; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
</style>
</head>
<body>
"""

def img(n, fade=26):
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')

FADE = {1: 46, 2: 34, 3: 40, 4: 40, 6: 40, 7: 42}   # slides de grito Anton pedem faixa clara atras do texto
current = [0]

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0], 100)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R, A = "", " red", " anton"

def at(n):
    """arma o slide corrente ANTES de st() ser avaliado (args do make sao avaliados da esquerda p/ direita)"""
    current[0] = n
    return n

def make(n, *args, **kw):
    current[0] = n
    slide(n, *args, **kw)

# 1 — CAPA: SO o grito, quebrado em 2 linhas (pedido do user 29/08). Nada de setup, nada embaixo.
make(at(1), st(("DESEJAR É", A), ("DE GRAÇA.", A)), top=196)

# 2 — a conta vem no seu nome
make(at(2), st(("Não tem opção. Isso aqui não é conselho,", B), ("é <b>conta</b>, e ela vem no seu nome.", B))
      + st(("Ou você entrega o prazer de agora,", B), ("ou entrega o que você diz que quer.", R)), fs=42)

# 3 — o prazer de agora, escancarado
make(at(3), st(("O sábado inteiro na frente da televisão.", B), ("A noite que acabou na <b>terceira</b> cerveja.", B))
      + st(("As três horas que somem no celular.", B), ("E você ainda diz que não tem tempo.", R)), fs=41)

# 4 — GRITO: o preco (redacao do user)
make(at(4), st(("Você quer o resultado que quase ninguém tem", B), ("com a rotina que <b>todo mundo</b> tem.", B))
      + st(("UMA VIDA FORA DO NORMAL EXIGE", A), ("ESFORÇO FORA DO NORMAL.", A), cls_extra=' style="margin-top:46px"'),
     top=208, fs=41)

# 5 — cansaco nao e esforco (derruba o alibi do trabalho)
make(at(5), st(("E antes que você diga que trabalha muito:", B), ("trabalhar muito não é mérito, <b>é o mínimo</b>.", B))
      + st(("Quem quebrou também trabalhava muito.", B), ("Cansaço não é a mesma coisa que esforço.", R)), fs=41)

# 6 — GRITO: o sempre
make(at(6), st(("Ser melhor num dia qualquer um é.", B), ("Você já foi. Umas quinze vezes.", B))
      + st(("O DIFÍCIL É O SEMPRE.", A), cls_extra=' style="margin-top:48px"'), top=212, fs=42)

# 7 — cemiterio de comecos; o punch e a palavra sozinha (pedido do user)
make(at(7), st(("Dieta, academia, curso, planilha nova.", B), ("A sua vida é um <b>cemitério de começos</b>.", B))
      + st(("E não faltou vontade em nenhum deles.", B), ("Faltou constância.", R)), fs=42)

# 8 — O ESPELHO: a virada na altura do dono
make(at(8), st(("Agora repara na ironia.", B), ("Você cobra constância do seu time todo dia.", B))
      + st(("Cobra horário, cobra padrão, cobra entrega.", B), ("E não cumpre nem a sua.", R)), fs=41)

# 9 — o defeito que ele esconde (beat quase literal da fala)
make(at(9), st(("E todo dono tem o dele.", B), ("É o que você chama de <b>jeito seu</b>", B), ("pra não ter que chamar de defeito.", B))
      + st(("Você esconde, corre de resolver,", B), ("e finge que não vê.", R)), top=206, fs=42)

# 10 — A DOBRADICA: tira a peca do terreno do coach
make(at(10), st(("Agora a parte que muda o jogo.", B), ("Constância não sai de <b>força de vontade</b>.", B))
       + st(("Vontade é o que te faz começar.", B), ("Método é o que te faz continuar.", R)), fs=42)

# 11 — A ENTREGA: o basico bem feito
make(at(11), st(("E método aqui não é nada complicado.", B), ("É o <b>básico bem feito</b>, todo santo dia.", B))
       + st(("O número na mesma data, a cobrança no mesmo dia,", B), ("o padrão que não depende do seu humor.", R)), top=210, fs=39)

# 12 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">CONSTANCIA</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro, no meu treinamento<br>'
       'de gestão pra pequena e média empresa,<br>'
       'o método que sustenta o básico todo dia.</div>\n')
make(at(12), cta, top=200)
