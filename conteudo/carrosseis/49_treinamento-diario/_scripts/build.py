#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 49 (editorial-punch, v2 pós-revisão do user)."""
import pathlib

OUT = pathlib.Path(__file__).parent.parent / "instagram"
OUT.mkdir(exist_ok=True)

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
  .capa{ font-size:50px; line-height:1.3; font-weight:600; }
  .cta-big{ font-size:66px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .cta-sm{ font-size:36px; font-weight:400; line-height:1.34; color:#1A1A1A; margin-top:20px; }
</style>
</head>
<body>
"""

def img(n, fade=26, bottom=0, fade_bottom=None):
    if fade_bottom:
        mask = f"linear-gradient(to bottom,transparent 0%,#000 {fade}%,#000 {fade_bottom}%,transparent 100%)"
    else:
        mask = f"linear-gradient(to bottom,transparent 0%,#000 {fade}%)"
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:{bottom}px;left:0;width:100%;mix-blend-mode:multiply;'
            f'-webkit-mask-image:{mask};mask-image:{mask};z-index:1;">')

def slide(n, body, fade=26, top=236, fs=None, bottom=0, fade_bottom=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade, bottom, fade_bottom)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines):
    parts = []
    for txt, cls in lines:
        style = ""
        if "anton92" in cls:
            cls, style = cls.replace("anton92", "anton"), ' style="font-size:92px"'
        elif "anton98" in cls:
            cls, style = cls.replace("anton98", "anton"), ' style="font-size:98px"'
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return '      <div class="stanza">\n' + "\n".join(parts) + '\n      </div>\n'

B, R = "", " red"

# 1 — capa (bloco mais alto; imagem nova: prancheta + apito em primeiro plano)
slide(1, st(("Você já pagou curso,", " capa"), ("palestra, treinamento.", " capa"))
        + st(("E o seu time continua o mesmo.", " capa red")), top=200)

# 2 — o dia bonito (imagem nova: plateia empolgada) + vermelho no fecho
slide(2, st(("O dia do treinamento é bonito.", B))
        + st(("Caderno cheio, time empolgado,", B), ("promessa de mudança.", R)))

# 3 — uma semana depois + a conclusão errada (ex-cadeiras vazias)
slide(3, st(("Uma semana depois, está tudo", B), ("do jeito que sempre foi.", B))
        + st(("Aí você conclui que gente não muda.", B), ("Que treinamento é dinheiro jogado fora.", B)), fs=42)

# 4 — o punch sozinho (imagem nova: o evento varrido)
slide(4, st(("Quase.", B))
        + st(("O que você pagou não foi", R), ("treinamento. Foi um evento.", R)))

# 5 — evento x repetição (Anton) — boxer no saco
slide(5, st(("Evento emociona. E emoção passa.", B))
        + st(("O QUE FICA É O QUE REPETE.", " anton92")))

# 6 — piloto automático — pulando corda
slide(6, st(("Ninguém muda de comportamento ouvindo uma vez.", B), ("Comportamento mora no piloto automático.", B))
        + st(("E piloto automático", R), ("se constrói com repetição.", R)), fs=39)

# 7 — amanhã erra de novo — córner
slide(7, st(("Quer a única certeza que existe", B), ("depois de um treinamento?", B))
        + st(("Amanhã alguém faz errado de novo.", B))
        + st(("Isso não é defeito do seu time.", R), ("É a vida como ela é.", R)))

# 8 — o playbook — caderno nas mãos
slide(8, st(("Por isso existe manual,", B), ("padrão, combinado escrito.", B))
        + st(("Não é enfeite de gaveta.", B), ("É ferramenta de cobrança:", B))
        + st(("“Nós combinamos.", R), ("Olha a página quatro.”", R)))

# 9 — a volta diária, só o texto (imagem nova: flexões + cobrança)
slide(9, st(("Corrigiu hoje? Amanhã você", B), ("volta e cobra de novo.", B))
        + st(("E depois de amanhã também.", B)))

# 10 — o grito sozinho (imagem do sino, subida com fade duplo)
slide(10, st(("O ÚNICO TREINAMENTO", " anton98"), ("QUE FUNCIONA É O DIÁRIO.", " anton98")), fade=30)

# 11 — rotina vira cultura — luvas (imagem levemente subida)
slide(11, st(("Treinamento anual não prepara ninguém.", B), ("Manual guardado não muda comportamento.", B))
         + st(("Rotina é o que transforma", R), ("o combinado em cultura.", R)), fs=42)

# 12 — a constância é sua — manhã
slide(12, st(("O seu time não é desinteressado.", B))
         + st(("Ele só nunca teve alguém", B), ("com disciplina de repetir.", B))
         + st(("A constância que falta", R), ("no time é a sua.", R)))

# 13 — fechamento — sincronia
slide(13, st(("Time bom não nasce num evento.", B))
         + st(("É formado numa rotina", B), ("de repetição e cobrança.", B))
         + st(("É isso que eu ensino no meu treinamento", R), ("de gestão pra pequena e média empresa.", R)), fs=42)

# 14 — CTA — treinador de costas
cta = ('      <div class="cta-big">Comenta <span class="red">ROTINA</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como construir um time<br>'
       'que executa o combinado<br>sem depender do seu grito.</div>\n')
slide(14, cta)
