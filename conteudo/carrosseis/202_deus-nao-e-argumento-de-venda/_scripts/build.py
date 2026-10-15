#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 202 (editorial-punch, "Deus não é argumento de venda").
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
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

slide(at(1),  st(("Pode vir o hate.", B))
            + st(("USAR DEUS PRA VENDER", A), ("É ABUSAR DE QUEM", A), ("JÁ ESTÁ DE JOELHOS.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Tem palco de empresário que abre com oração", B), ("e fecha com a maquininha de cartão.", B))
            + st(("Entre uma coisa e outra,", B), ("ninguém mostrou um balanço.", R)), fs=42)
slide(at(3),  st(("“Deus colocou no meu coração te ajudar.”", B), ("“Essa vaga é um propósito na sua vida.”", B))
            + st(("Isso não é pregação.", B), ("É técnica de fechamento.", R)), fs=42)
slide(at(4),  st(("E eles não pescam o dono que está bem.", B), ("Pescam o que está no fundo.", B))
            + st(("Sócio saiu, banco cortou o limite, casa em garantia.", B), ("Esse segura qualquer mão estendida.", R)), fs=38)
slide(at(5),  st(("Dono desesperado não compara preço", B), ("nem pede prova de resultado.", B))
            + st(("Ele quer um milagre.", B), ("E tem gente vendendo.", R)), fs=44)
slide(at(6),  st(("Cobrar 50 mil de quem está afundado", B), ("prometendo que Deus vai prover?", B))
            + st(("ISSO TEM NOME:", A), ("ABUSO.", A), mt=22), fs=44)
slide(at(7),  st(("Vão dizer que eu estou atacando a fé.", B), ("Não estou.", B))
            + st(("Estou atacando quem usa a fé dos outros", B), ("pra fazer caixa.", R)), fs=42)
slide(at(8),  st(("Respeito a fé de qualquer pessoa.", B), ("A sua, a do meu time, a de quem está lendo.", B))
            + st(("E é justamente por respeitar", B), ("que ela não pode virar argumento de venda.", R)), fs=41)
slide(at(9),  st(("Em 38 anos de empresa eu nunca precisei", B), ("pôr Deus numa proposta comercial.", B))
            + st(("Proposta séria", B), ("se defende com número.", R)), fs=42)
slide(at(10), st(("Antes de assinar qualquer mentoria, pergunta:", B), ("quanto a empresa dele fatura? Quanto sobra?", B))
            + st(("Se a resposta vier com versículo,", B), ("levanta e vai embora.", R)), fs=41)
slide(at(11), st(("Empresa não se salva com oração no palco.", B), ("Se salva com margem, caixa e número na mesa.", B))
            + st(("Toda semana,", B), ("olhando de frente.", R)), fs=41)
slide(at(12), st(("Eu tenho um treinamento pra donos de PME, o MBV.", B), ("Não prometo milagre e não uso o nome de Deus.", B))
            + st(("Ensino gestão:", B), ("Lucratividade, Crescimento e Cultura.", R)), fs=38)
slide(at(13), st(("Pode me criticar. Essa é a minha opinião", B), ("e eu assino embaixo.", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">VERDADE</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=44)
