#!/usr/bin/env python3
"""Gera os 12 HTMLs do carrossel 246 (editorial-punch, "Empresa é creche de adulto"; versão sem rosto, 16/10).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text(encoding='utf-8')).items()}
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
  .line b{ font-weight:700; }
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.12; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
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
def slide(n, body, top=240, fs=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html, encoding='utf-8'); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n
slide(at(1),  st(("Ninguém te avisa quando você abre o CNPJ:", B))
            + st(("EMPRESA É CRECHE DE ADULTO.", A), mt=22), top=280, fs=42)
slide(at(2),  st(("Você treina o vendedor. Ele diz que entendeu", B), ("e repete tudo certinho.", B))
            + st(("No dia seguinte, na frente do cliente,", R), ("faz tudo errado.", R)), fs=42)
slide(at(3),  st(("Aí você reclama com o sócio no almoço", B), ("e manda um áudio de cinco minutos no grupo.", B))
            + st(("E treina de novo,", R), ("pra dar errado de novo.", R)), fs=42)
slide(at(4),  st(("Em 38 anos de empresa, eu tenho", B), ("uma única certeza sobre treinamento:", B))
            + st(("depois dele, ninguém vai fazer", R), ("do jeito que foi ensinado.", R)), fs=44)
slide(at(5),  st(("E não adianta ser reclamão.", B), ("Isso não é defeito do seu time.", B))
            + st(("É a vida como ela é.", R)), fs=44)
slide(at(6),  st(("Por isso eu digo sem vergonha nenhuma:", B))
            + st(("dono de pequena empresa", R), ("é babá de adulto.", R)), fs=44)
slide(at(7),  st(("Antigamente isso tinha nome: pajear.", B), ("Hoje o nome bonito é follow-up.", B))
            + st(("É acompanhar a execução", R), ("até ela virar hábito.", R)), fs=44)
slide(at(8),  st(("E acompanhar não é passar no setor", B), ("quando sobra tempo.", B))
            + st(("Rotina tem dia, hora e assunto.", B), ("Se cada semana é de um jeito,", R), ("não é rotina. É visita.", R)), fs=42)
slide(at(9),  st(("Enquanto você espera o time", B), ("que não precisa ser acompanhado,", B), ("a meta fura, o cliente reclama", B))
            + st(("e quem paga o retrabalho", R), ("é o seu caixa.", R)), fs=42)
slide(at(10), st(("Agora me responde: quantas vezes nesta", B), ("semana você sentou com o seu time", B), ("pra olhar o número?", B))
            + st(("Se a resposta for nenhuma, a creche", R), ("está sem adulto responsável.", R)), fs=42)
slide(at(11), st(("Eu ensino gestão pra donos de PME", B), ("no meu treinamento, o MBV:", B), ("Lucratividade, Crescimento e Cultura.", B))
            + st(("Porque é gestão que faz cada um", R), ("entregar o que foi combinado.", R)), fs=42)
slide(at(12), st(("Quer parar de reclamar do time", B), ("e começar a ter resultado com ele?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">ENTREGA</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
