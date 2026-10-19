#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 244 (editorial-punch, "Vendeu mais e foi no banco").
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


slide(at(1),  st(("Você vendeu mais do que nunca", B))
            + st(("E NUNCA DEVEU", A), ("TANTO PRO BANCO.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Contratou gente, comprou mais mercadoria", B), ("e abriu cliente novo.", B))
            + st(("E no dia 10 estava ligando pro gerente", R), ("do banco pra conseguir fechar a folha.", R)), fs=40)
slide(at(3),  st(("Conheço dono que fatura 30 milhões por ano", B), ("e passa dezembro inteiro pedindo prazo", B), ("pra fornecedor.", B))
            + st(("Não falta venda. Falta o dinheiro", R), ("chegar antes do boleto.", R)), fs=40)
slide(at(4),  st(("A mercadoria fica 20 dias no estoque,", B), ("o cliente te paga em 30", B), ("e o fornecedor cobra em 15.", B))
            + st(("Nesses 35 dias,", R), ("quem banca o seu cliente é você.", R)), fs=42)
slide(at(5),  st(("E quanto mais você vende,", B), ("maior fica esse buraco.", B))
            + st(("Cada venda nova é mais boleto de fornecedor", R), ("vencendo antes do cliente pagar.", R)), fs=42)
slide(at(6),  st(("Aí entra o banco: capital de giro,", B), ("conta garantida, antecipação de cartão.", B))
            + st(("Dá alívio por dois meses, e depois", R), ("aperta de novo, com juro em cima.", R)), fs=42)
slide(at(7),  st(("E pra liberar o dinheiro, o banco pede", B), ("o seu aval e a casa da família de garantia.", B))
            + st(("Você trabalha pra crescer", R), ("e cresce pra dever mais.", R)), fs=42)
slide(at(8),  st(("Outubro é quando todo dono monta", B), ("o orçamento do ano que vem.", B))
            + st(("Se a conta do prazo não mudar, 2027", R), ("vai ser 2026 com uma dívida maior.", R)), fs=42)
slide(at(9),  st(("Eu te pergunto: quantos dias a sua", B), ("empresa fica bancando o cliente?", B))
            + st(("Se você não sabe responder,", R), ("quem sabe é o gerente do banco.", R)), fs=44)
slide(at(10), st(("Em 38 anos de empresa, eu aprendi", B), ("que crescer sem olhar o prazo", B), ("é cavar o buraco mais rápido.", B))
            + st(("A velocidade do crescimento tem", R), ("que caber no caixa que a empresa gera.", R)), fs=40)
slide(at(11), st(("O lucro de 2027 começa no prazo que você", B), ("negocia agora: com o fornecedor, com", B), ("o cliente e com o estoque parado.", B))
            + st(("Cada dia que você encurta é dinheiro", R), ("que não precisa vir do banco.", R)), fs=40)
slide(at(12), st(("Eu tenho um treinamento de gestão", B), ("pra donos de pequena e média empresa.", B))
            + st(("É lá que eu ensino o dono a crescer", R), ("sem entregar a casa pro banco.", R)), fs=42)
slide(at(13), st(("Se você quer crescer em 2027", B), ("com fôlego no caixa,", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">FOLEGO</span></div>\n'
            + st(("que eu te mando como participar do MBV.", B), mt=18), fs=46)
