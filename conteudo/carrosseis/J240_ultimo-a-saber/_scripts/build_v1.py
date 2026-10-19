#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 240 (editorial-punch, "O último a saber").
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

slide(at(1),  st(("Você treinou, delegou", B), ("e confiou no gerente.", B))
            + st(("QUEM TE AVISA QUE DEU", A), ("ERRADO É O CLIENTE.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Você paga gerente, paga comissão,", B), ("paga treinamento.", B))
            + st(("E ainda é o último a saber", R), ("o que acontece dentro da sua empresa.", R)), fs=42)
slide(at(3),  st(("Quem te conta que o pedido atrasou é o cliente.", B), ("Quem te conta que a meta furou", B), ("é o extrato do banco, no dia 10.", B))
            + st(("E o seu gerente", R), ("sabia disso três semanas antes.", R)), fs=40)
slide(at(4),  st(("Aí você manda um áudio de quatro minutos", B), ("às onze da noite e marca reunião de emergência.", B))
            + st(("Ele pede desculpa, e no mês seguinte", R), ("acontece tudo de novo.", R)), fs=40)
slide(at(5),  st(("Eu te pergunto: quanto o seu gerente", B), ("vendeu na semana passada?", B), ("Quantos pedidos estão atrasados agora?", B))
            + st(("Se pra saber você precisa ligar pra ele,", R), ("você não delegou. Você largou.", R)), fs=40)
slide(at(6),  st(("E o seu time aprende rápido como funciona:", B), ("o dono só aparece quando pega fogo.", B))
            + st(("Enquanto não pega, ninguém responde", R), ("pelo número, porque ninguém pergunta por ele.", R)), fs=40)
slide(at(7),  st(("E quem paga é você.", B), ("O sábado que era da sua família", B))
            + st(("vira dia de ligar pra cliente", R), ("e refazer pedido.", R)), fs=44)
slide(at(8),  st(("A área que você delegou", B))
            + st(("VOLTA INTEIRINHA", A), ("PRO SEU COLO.", A), mt=22), fs=48)
slide(at(9),  st(("Tem uma frase que eu repito pra todo dono:", B), ("delegai e vigiai.", B))
            + st(("Delegar é só a metade. A outra metade", R), ("é olhar o número antes que ele vire problema.", R)), fs=40)
slide(at(10), st(("Cada área com o número dela: venda da semana,", B), ("pedido no prazo, cliente que reclamou.", B))
            + st(("O gerente preenche, e você olha toda segunda", R), ("de manhã, antes do cliente ligar.", R)), fs=40)
slide(at(11), st(("Uma conversa curta todo dia, uma reunião", B), ("toda segunda e uma avaliação de resultado", B), ("no fim do mês.", B))
            + st(("Aí o atraso aparece na terça,", R), ("quando ainda dá tempo de consertar.", R)), fs=40)
slide(at(12), st(("E a cobrança muda de cara. Sai o áudio", B), ("das onze da noite e entra a pergunta certa", B), ("na reunião de segunda.", B))
            + st(("Dono com o número na mão", R), ("não precisa gritar com ninguém.", R)), fs=40)
slide(at(13), st(("Eu tenho um treinamento de gestão", B), ("pra donos de pequena e média empresa.", B))
            + st(("É lá que eu ensino a comandar a empresa", R), ("pelo número, antes que o susto chegue até você.", R)), fs=40)
slide(at(14), st(("Se você cansou de ser", B), ("o último a saber,", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">COMANDO</span></div>\n'
            + st(("que eu te mando como participar do MBV.", B), mt=18), fs=46)
