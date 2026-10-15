#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 83 (editorial-punch, "Ritual de comando")."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
DEFAULT_ANTON = {1: 158, 4: 78, 5: 110, 8: 118, 10: 78, 11: 96, 14: 80, 15: 92}
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
FADE = {1: 12, 16: 10}
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

make(at(1), st(("Empresa boa não tem reunião.", B)) + st(("TEM RITUAL.", A), cls_extra=' style="margin-top:8px"'), top=236, fs=52)
make(at(2), st(("Porque reunião por reunião", B), ("qualquer empresa faz.", B)) + st(("Agora ritual...", B), ("Ritual é outra coisa.", R)), top=305, fs=44)
make(at(3), st(("Ritual é o que acontece com", B), ("frequência, método e objetivo claro.", R)), top=300, fs=44)
make(at(4), st(("E a reunião semanal precisa acontecer.", B), ("Não porque é bonito na agenda.", B)) + st(("MAS PORQUE RESULTADO", A), ("PRECISA DE ACOMPANHAMENTO.", A), cls_extra=' style="margin-top:40px"'), top=236, fs=42)
make(at(5), st(("No final das contas, o seu resultado", B), ("no ano é a soma do que aconteceu", B)) + st(("NOS 365 DIAS DELE.", A), cls_extra=' style="margin-top:40px"'), top=250, fs=44)
make(at(6), st(("Se você corrige a rota", B), ("toda semana...", B)) + st(("Você tem de 48 a 52 chances", B), ("no ano de ajustar o problema.", R)), top=262, fs=44)
make(at(7), st(("Se você corrige", B), ("só uma vez por mês...", B)) + st(("Você tem 12 chances.", R)), top=370, fs=46)
make(at(8), st(("Se você não corrige nunca...", B)) + st(("VOCÊ TEM ZERO.", A), cls_extra=' style="margin-top:34px"'), top=330, fs=48)
make(at(9), st(("E aí não adianta reclamar do time,", B), ("da operação ou do resultado.", R)), top=330, fs=44)
make(at(10), st(("Porque reunião de gestão", B), ("não é para passar recado.", B)) + st(("É PARA COBRAR RESULTADO", A), ("E AJUSTAR PLANO.", A), cls_extra=' style="margin-top:40px"'), top=240, fs=44)
make(at(11), st(("É O FAMOSO FOLLOW-UP.", AB)) + st(("O combinado foi feito? Foi entregue?", B), ("Saiu do jeito certo?", B), cls_extra=' style="margin-top:40px"') + st(("Se não saiu...", B), ("o que vai ser ajustado?", R)), top=200, fs=42)
make(at(12), st(("É isso que garante", B), ("o resultado do funcionário.", B)) + st(("Não é motivação.", B), ("É acompanhamento.", R)), top=262, fs=44)
make(at(13), st(("Combinado sem follow-up", B), ("vira sugestão.", B)) + st(("E sugestão não fecha a conta.", R)), top=320, fs=46)
make(at(14), st(("Empresa desorganizada", B), ("faz reunião para falar.", B)) + st(("EMPRESA BOA FAZ RITUAL", A), ("PARA CORRIGIR.", A), cls_extra=' style="margin-top:40px"'), top=240, fs=44)
make(at(15), st(("Se você quer resultado,", B), ("pare de fazer reunião solta.", B)) + st(("CRIE RITUAL DE COMANDO.", A), cls_extra=' style="margin-top:40px"'), top=290, fs=44)
cta = (st(("É isso que eu ensino para donos", B), ("de pequena e média empresa.", B))
       + '      <div class="cta-big" style="margin-top:54px">Comenta <span class="red">RITUAL</span></div>\n'
       + st(("E eu te mostro como montar o seu.", R), cls_extra=' style="margin-top:30px"'))
make(at(16), cta, top=280, fs=43)
