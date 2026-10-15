#!/usr/bin/env python3
"""Gera os 17 HTMLs do carrossel 120 (editorial-punch, "O último da fila").
Layout do modelo.md (calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {17: "70% bottom", 2: "80% bottom", 8: "35% bottom"}
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

slide(at(1),  st(("Empresário, vou ser direto com você:", B), ("Empresa que não remunera o dono", R), ("não serve pra nada.", R)), top=280, fs=52)
slide(at(2),  st(("Eu sei como é na sua empresa:", B), ("todo mundo recebe antes de você.", R)))
slide(at(3),  st(("Dia 5 a folha. Dia 10 o banco.", B), ("Dia 20 o imposto. Dia 30 o fornecedor.", B))
            + st(("E você?", B), ("Fica com o resto.", R)))
slide(at(4),  st(("E pior: faltou dinheiro,", B), ("o caixa não fechou?", B))
            + st(("Problema teu.", R)))
slide(at(5),  st(("O funcionário não aceita.", B), ("O banco não aceita.", B))
            + st(("O governo?", B), ("Nem te pergunta.", R)))
slide(at(6),  st(("Agora, trabalhar o mês de graça", B), ("você aceita.", R))
            + st(("E tudo certo, afinal você é dono de empresa", B), ("e tem a explicação na ponta da língua:", B)), fs=42)
slide(at(7),  st(("“Estou reinvestindo,", B), ("a empresa está crescendo.", B), ("Quando ela valer mais, eu tiro.”", R)))
slide(at(8),  st(("Amigo, isso é papo de empresa grande,", B), ("de startup.", B))
            + st(("Você é dono", B), ("de pequena e média empresa.", R)))
slide(at(9),  st(("Se a grande falir,", B), ("quem perde são os acionistas.", B))
            + st(("Se a sua falir,", B), ("quem perde é você.", R)))
slide(at(10), st(("Casa, carro, família, o seu CPF.", B), ("Tudo isso está em jogo.", B))
            + st(("Por isso é inadmissível você aceitar", B), ("ser o último da fila", B), ("e ainda ganhar como CLT premium.", R)), fs=42)
slide(at(11), st(("Dono é dono. Dono é soberano.", B))
            + st(("Soberano não fica com o resto.", B), ("Soberano recebe primeiro.", R)))
slide(at(12), st(("Na empresa de um soberano", B), ("DIVIDENDO é a primeira conta.", B))
            + st(("Preço, custo e estrutura", B), ("se ajustam a ela.", R)))
slide(at(13), st(("Valer mais é consequência", B), ("de empresa que paga o dono.", B))
            + st(("O QUE NÃO PAGA HOJE,", A), ("NÃO VALE NADA AMANHÃ.", A)))
slide(at(14), st(("Responde de cabeça:", B))
            + st(("nos últimos 12 meses,", B), ("quanto a sua empresa te pagou pelo risco?", B))
            + st(("E não confunda com pró-labore:", B), ("estou falando de dividendo, a parte do dono.", R)), fs=40)
slide(at(15), st(("Se der errado, o funcionário acha outro emprego", B), ("e o banco executa a garantia.", B))
            + st(("O RISCO É TODO SEU.", A), ("O DINHEIRO NÃO.", A)), fs=40)
slide(at(16), st(("Eu tenho um treinamento pra donos", B), ("onde ensino a desenhar a empresa ao contrário:", B))
            + st(("a parte do dono é a primeira conta,", B), ("e o resto da empresa se ajusta a ela.", R)), fs=40)
slide(at(17), st(("Dono soberano não trabalha de graça.", B), ("Recebe primeiro.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">SOBERANO</span></div>\n'
            + st(("que eu te mando o link no seu direct.", B), mt=18))
