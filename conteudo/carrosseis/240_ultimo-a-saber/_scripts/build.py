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

slide(at(1),  st(("Conheço dono que fatura", B), ("20 milhões por ano", B))
            + st(("E FICA SABENDO DO", A), ("ERRO PELO CLIENTE.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Ele tem gerente, tem supervisor,", B), ("tem folha de 40 funcionários.", B))
            + st(("E é o último a saber o que acontece", R), ("dentro da empresa que leva o nome dele.", R)), fs=42)
slide(at(3),  st(("O pedido atrasou três semanas e ninguém", B), ("falou nada. Quem contou foi o cliente,", B), ("puto da vida, no celular do dono.", B))
            + st(("E o gerente sabia", R), ("desde o primeiro dia.", R)), fs=40)
slide(at(4),  st(("Aí ele faz o que todo dono faz: manda áudio", B), ("de quatro minutos às onze da noite", B), ("e ameaça demitir todo mundo.", B))
            + st(("E no mês seguinte", R), ("acontece tudo de novo.", R)), fs=40)
slide(at(5),  st(("Eu te pergunto: quanto a sua empresa", B), ("vendeu na semana passada?", B), ("Quantos pedidos estão atrasados agora?", B))
            + st(("Se pra responder você precisa ligar pro", R), ("gerente, você não delegou. Você largou.", R)), fs=40)
slide(at(6),  st(("Pode reclamar, eu também já reclamei:", B), ("aqui ninguém tem compromisso.", B))
            + st(("Só que ninguém tem compromisso", R), ("com um número que o dono nunca pergunta.", R)), fs=42)
slide(at(7),  st(("E quem paga a conta é você.", B))
            + st(("O sábado que era do seu filho", R), ("vira dia de ligar pra cliente e pedir desculpa.", R)), fs=42)
slide(at(8),  st(("A área que você delegou", B))
            + st(("VOLTA INTEIRINHA", A), ("PRO SEU COLO.", A), mt=22), fs=48)
slide(at(9),  st(("Em 38 anos de empresa, eu aprendi uma frase", B), ("que repito pra todo dono: delegai e vigiai.", B))
            + st(("Delegar sem vigiar", R), ("é entregar a chave e torcer.", R)), fs=40)
slide(at(10), st(("Vigiar é o gerente sentar com você toda", B), ("segunda com o número na mão: quanto vendeu,", B), ("quanto atrasou, quem reclamou.", B))
            + st(("Se o número não veio,", R), ("você já sabe onde está o problema.", R)), fs=40)
slide(at(11), st(("Dez minutos todo dia, uma hora", B), ("toda segunda e uma tarde no fim do mês.", B))
            + st(("É pouco tempo perto do sábado", R), ("que você está perdendo hoje.", R)), fs=42)
slide(at(12), st(("E a cobrança muda de cara. Você para de", B), ("gritar às onze da noite e começa a perguntar", B), ("na segunda de manhã.", B))
            + st(("Dono com o número na mão", R), ("não precisa gritar com ninguém.", R)), fs=40)
slide(at(13), st(("Eu tenho um treinamento de gestão", B), ("pra donos de pequena e média empresa.", B))
            + st(("É lá que eu ensino a comandar a empresa", R), ("pelo número, antes que o susto chegue até você.", R)), fs=40)
slide(at(14), st(("Se você cansou de ser", B), ("o último a saber,", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">COMANDO</span></div>\n'
            + st(("que eu te mando como participar do MBV.", B), mt=18), fs=46)
