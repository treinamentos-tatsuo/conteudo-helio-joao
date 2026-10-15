#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 87 (editorial-punch, "time que você não prepara")."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
DEFAULT_ANTON = {1: 104, 3: 96, 6: 120, 7: 110, 8: 118, 10: 84, 11: 104}
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
FADE = {}
current = [0]
def img(n, fade=26):
    h = HEIGHT.get(n)
    box = f'height:{h}px;object-fit:cover;object-position:center bottom;' if h else ''
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);'
            f'mask-image:linear-gradient(to bottom,transparent 0%,#000 {fade}%);z-index:1;">')
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

make(at(1), st(("Você cobra resultado", B)) + st(("DE UM TIME QUE", A), ("VOCÊ NÃO PREPARA.", A), cls_extra=MT(10)), top=236, fs=52)
make(at(2), st(("Contrata alguém “bom”. Joga no fogo.", B), ("E espera que ele resolva tudo sozinho.", R)), top=320, fs=44)
make(at(3), st(("Não acompanha.", B), ("Não corrige.", B)) + st(("Não direciona.", B), ("NÃO ENSINA.", A), cls_extra=MT(40)), top=250, fs=46)
make(at(4), st(("Mas quer que ele “pense como dono”.", R)) + st(("Quer iniciativa. Quer entrega.", B)), top=330, fs=44)
make(at(5), st(("E quando não vem o resultado...", B), ("você culpa o time.", B)) + st(("Troca a pessoa.", B), ("Reclama da geração.", R)), top=262, fs=44)
make(at(6), st(("MAS A REAL É DURA:", AB)), top=330)
make(at(7), st(("Se o time falha,", B)) + st(("O COMANDO", A), ("FALHOU ANTES.", A), cls_extra=MT(30)), top=300, fs=48)
make(at(8), st(("VOCÊ É O LÍDER.", A)) + st(("E a responsabilidade de formar,", B), ("desenvolver e cobrar é sua.", B), cls_extra=MT(40)), top=310, fs=44)
make(at(9), st(("Não existe time forte", B), ("com liderança fraca.", B)) + st(("E não existe crescimento", B), ("com comando ausente.", R)), top=262, fs=44)
make(at(10), st(("Liderar não é mandar.", B)) + st(("É GERAR RESULTADO", A), ("ATRAVÉS DAS PESSOAS.", A), cls_extra=MT(30)) + st(("Com cultura. Com padrão. Com presença.", B), cls_extra=MT(40)), top=210, fs=44)
make(at(11), st(("Um empresário não cresce sozinho.", B), ("Mas também não cresce", B), ("com gente fraca, sem direção.", B)) + st(("Time forte não se acha.", B), ("SE FORMA. POR VOCÊ.", A), cls_extra=MT(40)), top=280, fs=42)
cta = (st(("Eu tenho um treinamento que ensina o dono", B), ("a formar, desenvolver e cobrar o time.", B))
       + st(("Sem teoria. De empresário pra empresário.", R), cls_extra=MT(40))
       + '      <div class="cta-big" style="margin-top:54px">Comenta <span class="red">PREPARO</span></div>\n'
       + st(("e eu te mando o link com tudo no seu direct.", R), cls_extra=MT(24)))
make(at(12), cta, top=220, fs=42)
