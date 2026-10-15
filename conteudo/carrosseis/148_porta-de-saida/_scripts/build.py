#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 148 (editorial-punch, "Porta de saida").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
QW = 0.0  # largura da aspa serif (quotewidth.js), em em
try: QW = json.loads((SCR/"quotewidth.json").read_text())["em"]
except Exception: pass
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
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .line b{ font-weight:700; }
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .oq{ margin-left:-QWem; } .cq{ margin-right:-QWem; }
</style>
</head>
<body>
""".replace("QW", f"{QW:.3f}")
def mask(F):
    if F <= 26: return f"linear-gradient(to bottom,transparent 0%,#000 {F}%)"
    return (f"linear-gradient(to bottom,transparent 0%,rgba(0,0,0,0.06) {F*0.25:.1f}%,rgba(0,0,0,0.30) {F*0.55:.1f}%,"
            f"rgba(0,0,0,0.72) {F*0.80:.1f}%,#000 {F:.1f}%)")
def img(n):
    h = HEIGHT.get(n); pos = OBJPOS.get(n, "center bottom")
    box = f'height:{h}px;object-fit:cover;object-position:{pos};' if h else ''
    m = mask(FADE.get(n, 26))
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:{m};mask-image:{m};z-index:1;">')
cur = [0]
def slide(n, body, top=240, fs=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n

slide(at(1),  st(("Setembro de 2020.", B), ("A MINHA EMPRESA ENTROU", A), ("EM RECUPERAÇÃO", A), ("JUDICIAL.", A)), top=280, fs=48)
slide(at(2),  st(("Eu já tinha quebrado.", B), ("Já tinha faltado dinheiro. Já tinha recomeçado.", B))
            + st(("Isso, nunca.", B), ("Ninguém imagina. Até o dia que bate.", R)), fs=40)
slide(at(3),  st(("A pandemia fechou a rede em março.", B), ("A venda caiu. O banco travou.", B))
            + st(("Um modelo lindo no papel,", B), ("alavancado até o pescoço.", R)), fs=42)
slide(at(4),  st(("E eu não estava sozinho.", B), ("Tinha dois conselheiros de peso.", B))
            + st(("Um ex-presidente de multinacional.", B), ("Um gênio do mercado financeiro.", R)), fs=42)
slide(at(5),  st(("Currículo de dar inveja.", B))
            + st(("NENHUM DOS TRÊS", A), ("SABIA LIDAR COM DÍVIDA", A), ("DE PEQUENA EMPRESA.", A)), fs=44)
slide(at(6),  st(("Dívida de multinacional tem manual.", B), ("Dívida de fundo tem estrutura.", B))
            + st(("Dívida de PME tem o dono sozinho", B), ("no telefone com o gerente.", R)), fs=40)
slide(at(7),  st(("Entramos na recuperação judicial.", B), ("Hoje eu sei: era a decisão errada.", B))
            + st(("Tinha outros caminhos.", B), ("Eu não vi nenhum. Não sabia que existiam.", R)), fs=40)
slide(at(8),  st(("Lá dentro você acorda todo dia", B), ("procurando a porta de saída.", B))
            + st(("Custou anos. Custou patrimônio.", B), ("E reverbera até hoje.", R)), fs=42)
slide(at(9),  st(("O que me jogou lá dentro", B), ("não foi a pandemia.", B))
            + st(("FOI O QUE EU NÃO SABIA.", A)), fs=44)
slide(at(10), st(("Eu estava há cinco anos fora do operacional.", B), ("O sonho de todo dono.", B))
            + st(("Fora do operacional", B), ("e sem enxergar a empresa por dentro.", R)), fs=40)
slide(at(11), st(("A ignorância é uma sócia oculta.", B), ("Não assina contrato, não aparece.", B))
            + st(("A conta dela chega no dia", B), ("em que já não dá pra escolher.", R)), fs=42)
slide(at(12), st(("Agora olha pra sua empresa.", B), ("Quanto entra, quanto sai,", B), ("quanto deve, quanto aguenta.", B))
            + st(("O que você não sabe hoje", B), ("já está te custando.", R)), fs=40)
slide(at(13), st(("Conhecimento antes da crise custa estudo.", B), ("Dentro da crise, custa a empresa.", B))
            + st(("Eu paguei o caro.", B), ("Você ainda pode pagar o barato.", R)), fs=40)
slide(at(14), st(("Antes de qualquer decisão,", B), ("um raio-x da sua empresa.", B))
            + st(("É o que eu não tinha em 2020.", B), ("É o que eu ensino a fazer hoje.", R)), fs=42)
slide(at(15), '      <div class="cta-big">Comenta <span class="red">PORTA</span></div>\n'
            + st(("que eu te mando a aula em que você faz", R), ("o raio-x da sua empresa e enxerga", R), ("a saída antes de precisar dela.", R), mt=24), fs=40)
