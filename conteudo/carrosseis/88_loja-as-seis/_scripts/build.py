#!/usr/bin/env python3
"""Gera os 9 HTMLs do carrossel 88 (editorial-punch, "a loja às seis")."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
DEFAULT_ANTON = {1: 104, 4: 112, 7: 64, 8: 84}
try: ANTON = {**DEFAULT_ANTON, **{int(k): v for k, v in json.loads((SCR/"antonfit.json").read_text()).items()}}
except FileNotFoundError: ANTON = DEFAULT_ANTON
try: HEIGHT = {int(k): v for k, v in json.loads((SCR/"imgheight.json").read_text()).items()}
except FileNotFoundError: HEIGHT = {}
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
  .stanza + .stanza{ margin-top:50px; }
  .line{ font-size:44px; line-height:1.28; font-weight:400; color:#1A1A1A; }
  .red{ color:#A91C20; font-weight:700; }
  b{ font-weight:700; }
  .anton.blk{ color:#1A1A1A; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase;
    line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""
try: FADE = {int(k): v for k, v in json.loads((SCR/"fade.json").read_text()).items()}
except FileNotFoundError: FADE = {}
current = [0]
OBJPOS = {3: "right bottom"}   # object-position por slide (default "center bottom")
def mask(F):
    # curva suave: ramp longo que so chega a 100% no inicio do assunto (F = % da altura da imagem)
    return (f"linear-gradient(to bottom,transparent 0%,rgba(0,0,0,0.06) {F*0.25:.1f}%,rgba(0,0,0,0.30) {F*0.55:.1f}%,"
            f"rgba(0,0,0,0.72) {F*0.80:.1f}%,#000 {F:.1f}%)")
def img(n, fade=26):
    h = HEIGHT.get(n)
    pos = OBJPOS.get(n, "center bottom")
    box = f'height:{h}px;object-fit:cover;object-position:{pos};' if h else ''
    m = mask(fade)
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:{m};mask-image:{m};z-index:1;">')
def slide(n, body, fade=26, top=236, fs=None):
    fade = FADE.get(n, fade)
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n, fade)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html); print(f"slide-{n:02d}.html")
def st(*lines, cls_extra=""):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(current[0],90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    return f'      <div class="stanza"{cls_extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A, AB = "", " red", " anton", " anton blk"
def at(n): current[0] = n; return n
def make(n, *a, **k): slide(n, *a, **k)
MT = lambda px: f' style="margin-top:{px}px"'

# Slide 1 — capa: tudo Source Serif; so "talento" e "vontade" em vermelho negrito (user 04/09)
make(at(1), st(('O <span class="red">talento</span> acorda às nove.', B), ('A <span class="red">vontade</span> abriu a loja às seis.', B)), top=240, fs=52)
# Slide 2
make(at(2), st(("Todo mundo conhece um talentoso.", B), ("Fala bonito. Pensa rápido. Tem ideia pra tudo.", B)) + st(("E a ideia está lá até hoje. <b>Guardada.</b>", R)), top=200, fs=44)
# Slide 3 — anáfora 2+2
make(at(3), st(("Ele espera o momento certo.", B), ("Espera o sócio certo. Espera o dinheiro certo.", B)) + st(("Enquanto ele espera,", B), ("o portão da esquina já subiu.", R)), top=200, fs=44)
# Slide 4 — grito (hora em numero: user 04/09)
make(at(4), st(("Talento é dom.", B)) + st(("VONTADE É DECISÃO.", A), cls_extra=MT(20)) + st(("E se toma todo dia, às 5h30.", R), cls_extra=MT(30)), top=200, fs=46)
# Slide 5
make(at(5), st(("A vontade não escolhe dia bom.", B)) + st(("Abre no frio. Abre na chuva.", R), ("Abre sem ninguém na porta.", R)), top=200, fs=46)
# Slide 6
make(at(6), st(("Quem abre às seis não é", B), ("o mais brilhante da rua.", B)) + st(("É o que ainda vai estar lá", R), ("daqui a dez anos.", R)), top=200, fs=44)
# Slide 7 — 2+1 (a cutucada)
make(at(7), st(("Só que vontade sozinha também cansa.", B), ("Abre às seis, fecha às nove. E o mês termina igual.", B)) + st(("VONTADE SEM MÉTODO", A), ("É CANSAÇO COM HORA MARCADA.", A), cls_extra=MT(40)), top=200, fs=42)
# Slide 8 — 2+2
make(at(8), st(("Direção diz pra onde.", B), ("Método diz como, todo dia.", B)) + st(("Talento com vontade abre a loja.", B), ("VONTADE COM MÉTODO", A), ("FAZ ELA CRESCER.", A), cls_extra=MT(40)), top=200, fs=44)
# Slide 9 — CTA: 2 linhas balanceadas + chamada grande + linha de fecho
cta = (st(("Eu tenho um treinamento que ensina o dono", B), ("a botar direção e método na vontade que ele já tem.", B))
       + '      <div class="cta-big" style="margin-top:60px">Comenta <span class="red">METODO</span></div>\n'
       + st(("e eu te mando o link no seu direct.", R), cls_extra=MT(26)))
make(at(9), cta, top=200, fs=40)
