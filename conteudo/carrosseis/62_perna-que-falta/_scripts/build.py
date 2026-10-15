#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 62 (editorial-punch, a frase que te entrega)."""
import json, pathlib

SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"
OUT.mkdir(exist_ok=True)

# refrao das 3 desculpas no MESMO tamanho (1, 4, 8); o reveal (10) e o unico vermelho
DEFAULT_ANTON = {1: 128, 4: 128, 8: 128, 10: 100}
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
  .anton.preto{ color:#1A1A1A; }   /* a voz do dono: as 3 desculpas entram em preto */
  /* aspas penduradas: 0.466em e a largura de avanco medida da aspa em Anton.
     Com a margem negativa a aspa ocupa largura ZERO na diagramacao, o texto centraliza
     como se ela nao existisse, e o glifo pende pra fora. Sem isso a 1a linha comeca na
     aspa e a 2a na letra, e o bloco fica torto. */
  .oq{ margin-left:-0.466em; }
  .cq{ margin-right:-0.466em; }
  .sussurro{ font-size:32px; font-weight:400; color:#1A1A1A; }
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

FADE = {1: 43, 4: 34, 8: 46, 9: 36, 12: 52}   # gritos em Anton PRETO exigem faixa clara atras do texto
current = [0]

def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton):not(.sussurro){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html)
    print(f"slide-{n:02d}.html")

def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0], 100)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'

B, R = "", " red"
AP, AV = " anton preto", " anton"   # AP = desculpa do dono (preto) · AV = a nossa resposta (vermelho)

def at(n):
    current[0] = n
    return n

def make(n, *args, **kw):
    current[0] = n
    slide(n, *args, **kw)

# 1 — CAPA: a primeira desculpa, na boca dele (grito preto) + sussurro
make(at(1), st(("<span class='oq'>&ldquo;</span>NINGUÉM QUER", AP), ("TRABALHAR.<span class='cq'>&rdquo;</span>", AP))
      + st(("essa frase te entrega...", " sussurro"), cls_extra=' style="margin-top:46px"'), top=214)

# 2 — o veredito
make(at(2), st(("Parece uma frase sobre o mercado.", B), ("É uma frase sobre <b>a sua empresa</b>.", B))
      + st(("Quem quer trabalhar existe e está rendendo.", B), ("Só não está rendendo aí dentro.", R)), fs=40)

# 3 — a perna que essa frase aponta
make(at(3), st(("Aí dentro <b>nada anda sem você mandar</b>.", B), ("Toda entrega espera o seu empurrão.", B))
      + st(("E o time aprendeu isso com alguém.", B), ("Aprendeu com você.", R)), fs=42)

# 4 — a segunda desculpa (grito preto)
make(at(4), st(("Tem outra, com cara de conta:", B))
      + st(("<span class='oq'>&ldquo;</span>O MEU MERCADO", AP), ("NÃO DÁ MARGEM.<span class='cq'>&rdquo;</span>", AP), cls_extra=' style="margin-top:48px"'),
     top=210, fs=42)

# 5 — o veredito
make(at(5), st(("Se o mercado não desse margem,", B), ("ninguém do seu ramo <b>ganharia dinheiro</b>.", B))
      + st(("Tem gente ganhando na mesma rua,", B), ("com o mesmo custo que o seu.", R)), fs=42)

# 6 — a perna que essa frase aponta
make(at(6), st(("A diferença não está no mercado.", B), ("Está em <b>quem sabe formar preço</b>.", B))
      + st(("Custo, margem, prazo, desconto.", B), ("Você chuta isso e chama de &ldquo;faro&rdquo;.", R)), fs=42)

# 7 — a consequencia
make(at(7), st(("Aí você vende o mês inteiro", B), ("e trabalha <b>todo santo dia</b>.", B))
      + st(("No dia trinta você abre a conta", B), ("e descobre que trabalhou de graça.", R)), fs=42)

# 8 — a terceira desculpa (grito preto)
make(at(8), st(("E tem mais uma, a mais confortável:", B))
      + st(("<span class='oq'>&ldquo;</span>ESSE ANO", AP), ("FOI ATÍPICO.<span class='cq'>&rdquo;</span>", AP), cls_extra=' style="margin-top:48px"'),
     top=210, fs=42)

# 9 — o veredito
make(at(9), st(("Todo ano é atípico.", B), ("Eleição, dólar, chuva, greve.", B))
      + st(("Quem tem método <b>vê o desvio chegar</b>.", B), ("Quem não tem só vê o prejuízo.", R)), fs=43)

# 10 — O REVEAL (unico grito vermelho do carrossel)
make(at(10), st(("São três frases porque são três coisas.", B))
       + st(("LIDERANÇA.", AV), ("CONHECIMENTO TÉCNICO.", AV), ("MÉTODO.", AV), cls_extra=' style="margin-top:44px"'),
     top=206, fs=42)

# 11 — a desculpa aponta pra dentro
make(at(11), st(("A desculpa muda todo ano.", B), ("A perna que falta <b>é a mesma</b>.", B))
       + st(("Você não está explicando o resultado.", B), ("Está apontando o que falta.", R)), fs=42)

# 12 — a parte do dono
make(at(12), st(("E ela não se levanta sozinha.", B), ("Ninguém aí dentro faz isso por você.", B))
       + st(("Não tem funcionário que conserte isso.", B), ("Quem levanta as três é você.", R)), top=208, fs=41)

# 13 — desejo
make(at(13), st(("Com as três de pé,", B), ("o ano <b>para de ser aposta</b>.", B))
       + st(("O resultado vira consequência.", B), ("E a sua empresa para de balançar.", R)), fs=43)

# 14 — primeiro passo
make(at(14), st(("<b>Anota</b> a frase que você mais repete.", B), ("Ela já te disse o que consertar.", B))
       + st(("Ataca essa perna primeiro:", B), ("meta escrita, prazo e dia de cobrar.", R)), fs=42)

# 15 — fechamento
make(at(15), st(("<b>Liderança, conhecimento técnico e método.</b>", B))
       + st(("Nenhuma das três é dom.", B), ("<b>As três se aprendem.</b>", B))
       + st(("Eu criei o MBV pra ensinar isso.", B), ("Dono que aprende firma a empresa.", R)), top=196, fs=42)

# 16 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">FIRME</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro como levantar as três<br>'
       'na sua empresa e parar de fechar<br>'
       'o ano com desculpa.</div>\n')
make(at(16), cta)
