#!/usr/bin/env python3
"""Gera os 18 HTMLs do carrossel 60 (editorial-punch, a solidao da presidencia)."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

try:
    ANTON = {int(k): v for k, v in json.loads((SCR / "antonfit.json").read_text()).items()}
except FileNotFoundError:
    ANTON = {}

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
  .capa{ font-size:40px; line-height:1.28; font-weight:700; }
  .sussurro{ font-size:30px; font-weight:400; color:#1A1A1A; }
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

FADE = {1: 20}

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton):not(.capa):not(.sussurro){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = ""
        if "anton" in cls:
            style = f' style="font-size:{ANTON.get(current[0], 84)}px"'
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R = "", " red"
current = [0]

def at(n):
    """Fixa o slide atual ANTES de st() ser avaliado (args sao avaliados antes da chamada)."""
    current[0] = n
    return n


def make(n, *args, **kw):
    current[0] = n
    slide(n, *args, **kw)

# 1 — capa v2 (27/08, decisao do user): grito puro, uma linha so
make(at(1), st(("A COROA PESA.", " anton")), top=240)

# 2 — a cena do jantar (reconhecimento)
make(at(2), st(("Você está no jantar com os amigos.", B), ("Todo mundo rindo, <b>todo mundo leve</b>.", B))
      + st(("Você está na cadeira, mas não está na mesa.", B), ("A sua cabeça está no pagamento de sexta.", R)), fs=41)

# 3 — o vao
make(at(3), st(("E não tem nada de errado com eles.", B), ("Eles só não carregam <b>o que você carrega</b>.", B))
      + st(("Eles dormem às dez. Você apaga a luz", B), ("e o seu cérebro continua ligado.", R)), top=224, fs=41)

# 4 — a pergunta que doi
make(at(4), st(("Aí vem a pergunta que você nunca fez em voz alta:", B), ("<b>será que o problema sou eu?</b>", B))
      + st(("Não é você e não é eles.", B), ("É a cadeira.", R)), fs=40)

# 5 — o batismo (grito)
make(at(5), st(("Isso tem nome, e não é papo de empresa grande:", B))
      + st(("A SOLIDÃO", " anton"), ("DA PRESIDÊNCIA.", " anton"), cls_extra=' style="margin-top:44px"'),
     top=218, fs=41)

# 6 — o que e a cadeira
make(at(6), st(("Presidente não é cargo de prédio de vidro.", B), ("Presidente é quem <b>assina</b>.", B))
      + st(("Na sua empresa, quem assina é você.", B), ("E essa cadeira não tem revezamento.", R)), top=212, fs=42)

# 7 — a virada (grito)
make(at(7), st(("Essa conta não cobra em choro.", B), ("<b>Ela cobra em decisão.</b>", B))
      + st(("NÃO É TRISTEZA.", " anton"), ("É PREJUÍZO.", " anton"), cls_extra=' style="margin-top:46px"'),
     top=214, fs=42)

# 8 — o caso
make(at(8), st(("Eu já vi dono decidir de madrugada, sozinho,", B), ("vender o terreno da empresa pra pagar todo mundo.", B))
      + st(("Devia três. Tinha trinta em patrimônio.", B), ("Ia torrar trinta pra resolver três.", R)), fs=39)

# 9 — por que ele ia fazer isso
make(at(9), st(("E não era burrice. <b>Era vergonha.</b>", B), ("Ele nunca tinha devido nada a ninguém.", B))
      + st(("Se achava um picareta por procurar saída.", B), ("E vergonha sozinha decide péssimo.", R)), fs=41)

# 10 — a regra (grito)
make(at(10), st(("Repara que não faltou coragem naquele homem.", B))
       + st(("CORAGEM VOCÊ TEM DE SOBRA.", " anton"), ("O QUE FALTA É REPERTÓRIO.", " anton"), cls_extra=' style="margin-top:44px"'),
     top=218, fs=41)

# 11 — com quem voce fala
make(at(11), st(("E quando o peso passa do limite, você fala.", B), ("<b>Mas fala com quem?</b>", B))
       + st(("Com o guru da internet, com o amigo", B), ("que nunca fez uma folha de pagamento.", R)), fs=41)

# 12 — a parte do dono
make(at(12), st(("E tem uma parte que é sua.", B), ("<b>Ninguém te mandou ficar calado.</b>", B))
       + st(("Você calou achando que pedir ajuda ia te fazer menor.", B), ("Menor foi o que o silêncio te fez.", R)), fs=38)

# 13 — doutrina (a caneta)
make(at(13), st(("E não confunde as duas coisas: dividir o peso", B), ("não é dividir a <b>responsabilidade</b>.", B))
       + st(("A caneta continua na sua mão.", B), ("Quem assina é você. Isso não muda.", R)), fs=41)

# 14 — desejo
make(at(14), st(("Ninguém tira de você o peso de assinar.", B), ("Você vai continuar sendo <b>o único que assina</b>.", B))
       + st(("Mas você deixa de ser o único que enxerga.", B), ("E dono leve decide melhor.", R)), fs=40)

# 15 — o como
make(at(15), st(("E não é sala de network, não é troca de cartão,", B), ("<b>não é foto em cima de palco.</b>", B))
       + st(("É um lugar onde dá pra chegar e dizer:", B), ("estou fraco aqui, me ajuda.", R)), fs=40)

# 16 — primeiro passo
make(at(16), st(("Começa amanhã. Pega a decisão que está travada", B), ("há mais tempo e escreve numa folha, <b>com o número</b>.", B))
       + st(("Leva pra alguém que já decidiu essa mesma coisa.", B), ("Não pro amigo que vai te dar razão.", R)), fs=38)

# 17 — fechamento
make(at(17), st(("Se não tem pra quem levar essa folha,", B), ("esse é o seu problema mais urgente.", R))
       + st(("Foi pra isso que eu criei a Tatsuo Academy.", B), ("Dono aprende gestão, e aprende <b>no meio de dono</b>.", B)), fs=40)

# 18 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">LEVE</span>,</div>\n'
       '      <div class="cta-sm">que eu te chamo pra dentro da nossa<br>'
       'comunidade de donos: lá você aprende gestão<br>'
       'e para de decidir sozinho.</div>\n')
make(at(18), cta)
