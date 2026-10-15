#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 106 (editorial-punch, "Foi pra fechar o mês").
Layout da skill (calibragem registrada em erros-frequentes 04/09: corpo top 200, capa 240; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {4: "75% bottom"}
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
def at(n): cur[0] = n; return n

slide(at(1),  st(("O BANCO NÃO QUEBRA SUA EMPRESA.", A), ("ELE SÓ FINANCIA A QUEBRA.", A)), top=240)
slide(at(2),  st(("Você abre às sete e fecha às nove.", B), ("Trabalha mais que qualquer funcionário.", B)) + st(("E o único que tira lucro", B), ("da sua empresa é o banco.", R)), fs=42)
slide(at(3),  st(("Você não tem mais uma empresa.", B), ("Tem uma dívida com placa na porta.", B)) + st(("O lucro que era pra ir pro seu bolso", B), ("vai pro banco no dia 10.", R)), fs=42)
slide(at(4),  st(("VOCÊ VIROU FUNCIONÁRIO DO BANCO.", A), ("E AINDA AGRADECE O GERENTE.", A)))
slide(at(5),  st(("Aí entra o cheque especial.", B), ("Depois antecipa o cartão.", B)) + st(("Empréstimo pagando empréstimo,", B), ("e a operação continua no vermelho.", R)), fs=42)
slide(at(6),  st(("O gerente liga oferecendo mais.", B), ("Agora com o carro de garantia.", B)) + st(("Você assina, o mês não espera.", B), ("E chama isso de capital de giro.", R)), fs=42)
slide(at(7),  st(("Primeiro foi o limite.", B), ("Depois o carro. Depois o rancho.", B)) + st(("Quando a casa entra de garantia,", B), ("a dívida já é da sua família.", R)), fs=42)
slide(at(8),  st(("Ninguém nunca sentou pra ver", B), ("quanto entra e quanto sai por mês.", B)) + st(("Você sabe a parcela de cor.", B), ("Mas não sabe se a empresa dá lucro.", R)), fs=42)
slide(at(9),  st(("Essa conta é do dono.", B), ("Não do gerente do banco.", B)) + st(("O gerente vende dinheiro.", B), ("Ganha quando o seu caixa não fecha.", R)), fs=42)
slide(at(10), st(("Clareza é saber, antes do dia 10,", B), ("quanto entra, quanto sai, quanto sobra.", B)) + st(("Se falta, o conserto é na operação.", B), ("Não no limite do banco.", R)), fs=41)
slide(at(11), st(("CONTA QUE FECHA", A), ("NÃO PRECISA DE BANCO.", A)) + st(("E conta que não fecha,", B), ("banco nenhum salva.", B), mt=30))
slide(at(12), st(("Quer saber se o seu caixa fecha", B), ("antes do próximo empréstimo?", B))
            + st(("Eu ofereço um diagnóstico gratuito,", B), ("com um especialista da minha equipe,", B), ("nos três pilares do MBV.", R), mt=26), fs=40)
slide(at(13), '      <div class="cta-big">Comenta <span class="red">DIAGNÓSTICO</span></div>\n'
            + st(("e eu te mando o link no seu direct", R), ("pra agendar o seu diagnóstico.", R), mt=24))
