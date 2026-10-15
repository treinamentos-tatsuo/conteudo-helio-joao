#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 198 (editorial-punch, "Remédio pro empresário desmotivado").
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

slide(at(1),  st(("Remédio pro empresário desmotivado:", B))
            + st(("LEVANTA E VAI", A), ("TRABALHAR.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Eu empreendo há 38 anos", B), ("e tem segunda que eu também não quero ir.", B))
            + st(("A diferença é que eu vou.", R)), fs=42)
slide(at(3),  st(("Gostar ou não gostar não entra na conta.", B))
            + st(("QUEM SÓ FAZ O QUE", A), ("GOSTA É CRIANÇA.", A), mt=22), fs=44)
slide(at(4),  st(("Não quer cobrar o cliente que está devendo.", B), ("Não quer demitir o gerente que enrola há dois anos.", B))
            + st(("Não quer abrir o relatório do mês.", B), ("E chama isso de desmotivação.", R)), fs=38)
slide(at(5),  st(("Isso não é desmotivação.", B))
            + st(("É BIRRA DE DONO.", A), mt=22), fs=46)
slide(at(6),  st(("Seu funcionário também acorda sem vontade,", B), ("e você cobra ele igual.", B))
            + st(("Se ele não pode faltar porque não estava a fim,", B), ("você também não pode.", R)), fs=40)
slide(at(7),  st(("Quarenta famílias recebem no dia cinco", B), ("e nenhuma quer saber como você acordou.", B))
            + st(("Então faça tudo", B), ("como se fosse o seu melhor dia.", R)), fs=42)
slide(at(8),  st(("Ninguém botou uma arma na sua cabeça", B), ("pra abrir CNPJ e assinar aval no banco.", B))
            + st(("QUEM ESCOLHEU", A), ("ESSE JOGO FOI VOCÊ.", A), mt=26), fs=42)
slide(at(9),  st(("Quer o bônus de ser dono:", B), ("o carro, a casa, o nome na porta.", B))
            + st(("Então paga o ônus também.", B), ("Inclusive no dia que você não quer.", R)), fs=42)
slide(at(10), st(("Aí você vai atrás de motivação:", B), ("palestra, vídeo de guru, uma semana na praia.", B))
            + st(("Volta pegando fogo na segunda.", B), ("Na quarta, apagou.", R)), fs=42)
slide(at(11), st(("Sabe por que você não tem vontade?", B), ("Porque trabalha no escuro.", B))
            + st(("Fatura 20 milhões por ano", B), ("e não sabe quanto disso fica pra você.", R)), fs=42)
slide(at(12), st(("Dono que sabe quanto entra, quanto sai", B), ("e quanto sobra não precisa de palestra.", B))
            + st(("Ele levanta com gana,", B), ("porque sabe pelo que está jogando.", R)), fs=42)
slide(at(13), st(("No MBV, o meu treinamento pra dono de PME,", B), ("eu ensino gestão:", B))
            + st(("ler a empresa pelo número toda semana,", B), ("com vontade ou sem vontade.", R)), fs=42)
slide(at(14), st(("Assuma o jogo que você escolheu.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">GANA</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
