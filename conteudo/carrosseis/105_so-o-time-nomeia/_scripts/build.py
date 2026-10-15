#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 105 (editorial-punch, "Só o time nomeia").
Layout da skill (calibragem registrada em erros-frequentes 04/09: corpo top 200, capa 240; Source Serif 44; Anton nos gritos).
Aspas na borda de linha penduradas (erros-frequentes 27/08): .oq/.cq com margem negativa medida."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
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
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
  .oq{ margin-left:-0.42em; }
  .cq{ margin-right:-0.43em; }
</style>
</head>
<body>
"""
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
def slide(n, body, top=200, fs=None):
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
OQ, CQ = '<span class="oq">&ldquo;</span>', '<span class="cq">&rdquo;</span>'
def at(n): cur[0] = n; return n

slide(at(1),  st(("Dono, você se nomeou sozinho.", B), ("LÍDER, SÓ O TIME NOMEIA.", A)), top=240, fs=52)
slide(at(2),  st(("O título de dono veio com o CNPJ.", B), ("Está no contrato, no banco, na fachada.", B)) + st(("Ninguém precisou concordar.", B), ("Você assinou e pronto.", R)), fs=42)
slide(at(3),  st(("O de líder não tem papel.", B), ("Nem carimbo, nem assinatura.", B)) + st(("Mora na cabeça de cada um do time.", B), ("E cada um aceita ou nega sozinho.", R)), fs=42)
slide(at(4),  st(("Você fala, o time faz.", B), ("Faz porque é você quem paga a folha.", B)) + st(("Isso é autoridade de cargo.", B), ("Qualquer dono tem.", R)))
slide(at(5),  st(("Aí o dono tenta ganhar o título no discurso.", B), (OQ + "Confia em mim.&rdquo; &ldquo;Veste a camisa." + CQ, B))
            + st(("Só que ele nunca entendeu que", B), ("ninguém veste a camisa", R), ("porque o patrão pediu.", R)), fs=40)
slide(at(6),  st(("LIDERANÇA É IGUAL CONFIANÇA.", A), ("NÃO SE PEDE.", A)))
slide(at(7),  st(("O time te nomeia olhando, não ouvindo.", B)) + st(("A hora que você chega.", B), ("A sua postura sob pressão.", B), ("De quem é a culpa quando dá errado.", R)), fs=42)
slide(at(8),  st(("E, PRINCIPALMENTE,", A), ("SE A REGRA VALE PRA VOCÊ.", A)))
slide(at(9),  st(("Time que só obedece", B), ("está te dizendo, sem falar:", B)) + st((OQ + "Eu faço porque você é o chefe.", R), ("Não porque acredito em você." + CQ, R)), fs=42)
slide(at(10), st(("Quando o time te nomeia, o jogo vira.", B), ("A decisão anda sem você.", B)) + st(("O erro é corrigido antes do prejuízo.", R)), fs=42)
slide(at(11), st(("Aí o time deixa de trabalhar pra você", B), ("e passa a trabalhar com você.", B)) + st(("Não fica pelo salário.", B), ("Fica porque tem orgulho de estar ali.", R)), fs=42)
slide(at(12), st(("Esse título tem nome: Líder.", B), ("Não se compra, não se pede.", B)) + st(("Se constrói todo dia,", B), ("com método, com gestão.", R)))
slide(at(13), st(("Eu tenho um treinamento", B), ("pra donos de empresas, onde ensino:", B))
            + st(("a montar a rotina de liderança e a cultura", B), ("que fazem o time te seguir,", R), ("não só te obedecer.", R), mt=26), fs=40)
slide(at(14), '      <div class="cta-big">Comenta <span class="red">LIDER</span></div>\n'
            + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=24))
