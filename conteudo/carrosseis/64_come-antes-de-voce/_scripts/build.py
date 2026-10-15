#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 64 (editorial-punch, o que muda na cabeca de quem abre um CNPJ)."""
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


FADE = {4: 34, 11: 46, 12: 32, 14: 40}


def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton):not(.sussurro){{font-size:{fs}px}}</style>\n' if fs else ""
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


# 1 — capa (redacao do user): setup serif + grito Anton em linha unica
make(at(1), st(("Nada muda tanto a cabeça de uma pessoa", B))
      + st(("QUANTO ABRIR UM CNPJ.", " anton"), cls_extra=' style="margin-top:40px"'), top=220, fs=42)

# 2 — o Estado distante x a primeira nota
make(at(2), st(("Enquanto você é só consumidor,", B), ("o governo é <b>uma coisa distante</b>.", B))
      + st(("Aí você abre a empresa e emite nota.", B), ("E o distante senta no seu colo.", R)), top=224, fs=43)

# 3 — a infinidade + a ordem invertida (grito)
make(at(3), st(("Imposto, taxa, guia, obrigação,", B), ("burocracia, regra, custo, multa.", B))
      + st(("TUDO ISSO VEM ANTES", " anton"), ("DO PRIMEIRO LUCRO.", " anton"), cls_extra=' style="margin-top:46px"'),
     top=212, fs=42)

# 4 — os dois folegos
make(at(4), st(("Aí você entende que empreender", B), ("não é ter uma boa <b>ideia</b>.", B))
      + st(("É ter fôlego. E são dois fôlegos:", B), ("o do bolso e o da cabeça.", R)), top=200, fs=44)

# 5 — a casa cai pra voce
make(at(5), st(("E o da cabeça quebra primeiro,", B), ("porque o risco não fica na empresa.", B))
      + st(("Se der errado, não cai só o CNPJ.", B), ("Cai a casa onde a sua família mora.", R)), top=224, fs=43)

# 6 — onde o peso cai (pequeno e medio empresario)
make(at(6), st(("E repara onde esse peso cai.", B), ("Cai em quem ainda <b>não tem patrimônio</b>.", B))
      + st(("No pequeno e no médio empresário,", B), ("que segura este país na linha de frente.", R)), top=222, fs=42)

# 7 — o que sobra pra segurar (grito)
make(at(7), st(("E o que sobra pra segurar essa pessoa de pé?", B))
      + st(("SÓ A FORÇA DE VONTADE.", " anton"), cls_extra=' style="margin-top:44px"'), top=224, fs=42)

# 8 — o guru de internet (recompensa + merito, fundidos)
make(at(8), st(("E é aí que entra o guru de internet,", B), ("prometendo <b>recompensa pelo esforço</b>.", B))
      + st(("Querer muito você já quer.", B), ("Querer nunca foi método.", R)), top=224, fs=43)

# 9 — duas semanas sem dormir
make(at(9), st(("Quem abriu empresa sabe o que é isso:", B), ("duas semanas sem dormir direito.", B))
      + st(("De fora, tudo tem solução simples.", B), ("De dentro, nada é simples.", R)), top=224, fs=43)

# 10 — chacota x apoio
make(at(10), st(("Uns fazem chacota de quem empreende", B), ("e chamam de <b>pequeno burguês</b>.", B))
       + st(("Outros ao menos dizem que apoiam.", B), ("E é aí que muita gente muda de ideia.", R)), top=222, fs=42)

# 11 — nao e egoismo (grito)
make(at(11), st(("E não é que ela ficou egoísta", B), ("ou parou de se importar.", B))
       + st(("ELA PASSOU A ENXERGAR", " anton"), ("O QUE NINGUÉM VÊ.", " anton"), cls_extra=' style="margin-top:46px"'),
     top=198, fs=42)

# 12 — o pedaco invisivel
make(at(12), st(("E o pedaço invisível é esse:", B), ("a sua empresa <b>cobra antes de pagar</b>.", B))
       + st(("Quem nunca abriu uma não sabe", B), ("que o custo chega antes da venda.", R)), top=204, fs=43)

# 13 — o desejo, na experiencia do Helio
make(at(13), st(("Eu demorei anos pra entender isso,", B), ("e aprendi do <b>jeito mais caro</b>.", B))
       + st(("No dia que coloquei método nesse peso,", B), ("o susto virou dinheiro sobrando.", R)), top=224, fs=42)

# 14 — o que e esse metodo (desenvolvimento)
make(at(14), st(("E método aqui não é nada complicado:", B), ("é saber quanto a empresa custa <b>parada</b>.", B))
       + st(("E quanto ela precisa vender pra cobrir", B), ("antes de sobrar um real pra você.", R)), top=200, fs=42)

# 15 — CTA
cta = ('      <div class="cta-big">Comenta <span class="red">DONO</span>,</div>\n'
       '      <div class="cta-sm">que eu te mostro, no meu treinamento<br>'
       'de gestão pra pequena e média empresa,<br>'
       'a conta que põe dinheiro no seu bolso.</div>\n')
make(at(15), cta, top=236)
