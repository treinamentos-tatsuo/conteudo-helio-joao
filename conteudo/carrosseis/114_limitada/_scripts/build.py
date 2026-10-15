#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 114 (editorial-punch, "Limitada").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {7: "left bottom"}
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

slide(at(1),  st(("Sua empresa é limitada?", B), ("O SEU CPF NÃO É.", A)), top=280, fs=48)
slide(at(2),  st(("Te disseram no cartório que era limitada.", B), ("Que se quebrasse, quebrava a empresa.", B))
            + st(("Você assinou e dormiu tranquilo.", B), ("Você é o único que acredita nisso.", R)), fs=42)
slide(at(3),  st(("O banco nunca acreditou.", B), ("Por isso cada contrato que você assinou", B), ("tem o seu nome como avalista.", B))
            + st(("O Ltda ficou na placa.", B), ("O aval ficou no seu CPF.", R)), fs=42)
slide(at(4),  st(("SE O CNPJ CAI,", A), ("A CONTA PULA PRO SEU CPF.", A)))
slide(at(5),  st(("E não é só o banco.", B), ("O juiz do trabalho vai atrás do sócio.", B), ("A Receita vai atrás de quem administra.", B))
            + st(("Os três têm o mesmo endereço:", B), ("o seu.", R)), fs=40)
slide(at(6),  st(("A dívida sobe a escada.", B), ("Vai atrás do que você guardou pra família.", B))
            + st(("O que levou vinte anos pra juntar", B), ("sai num edital de leilão.", R)), fs=42)
slide(at(7),  st(("O LTDA NÃO É MURO.", A), ("É CORTINA.", A)))
slide(at(8),  st(("E o que você tira por correr esse risco?", B), ("Um pró-labore de gerente.", B))
            + st(("Só que o gerente, se a empresa cai,", B), ("perde o emprego.", B), ("Você perde tudo que tem no seu nome.", R)), fs=40)
slide(at(9),  st(("O RISCO É ILIMITADO.", A), ("SÓ O QUE VOCÊ TIRA", A), ("É LIMITADO.", A)))
slide(at(10), st(("Por isso eu defendo que empresa nasceu", B), ("pra botar dinheiro no bolso do dono.", B))
            + st(("Não é ganância. É a única coisa", B), ("que justifica o seu CPF naquele aval.", R)), fs=42)
slide(at(11), st(("Ah, mas eu tô reinvestindo. Tô crescendo.", B), ("Esquece.", B))
            + st(("Se o risco é seu e o dinheiro fica na empresa,", B), ("você não é dono. É fiador.", R)), fs=40)
slide(at(12), st(("Regra número 1 dos negócios:", B))
            + st(("EMPRESA FOI FEITA", A), ("PRA BOTAR DINHEIRO", A), ("NO BOLSO DO DONO.", A)), fs=48)
slide(at(13), st(("Quer saber se a sua empresa te paga", B), ("pelo risco que você corre?", B))
            + st(("Eu ofereço um diagnóstico gratuito", B), ("nos três pilares do MBV.", R), mt=26), fs=42)
slide(at(14), '      <div class="cta-big">Comenta <span class="red">DIAGNÓSTICO</span></div>\n'
            + st(("e eu te mando o link no seu direct", R), ("pra agendar o seu diagnóstico.", R), mt=24))
