#!/usr/bin/env python3
"""Gera os 17 HTMLs do carrossel 107 (editorial-punch, "Outro bicho").
Layout da skill (calibragem registrada em erros-frequentes 04/09: corpo top 200, capa 240; Source Serif 44; Anton nos gritos)."""
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

slide(at(1),  st(("TE VENDERAM QUE", A), ("SER PEQUENO É DEFEITO.", A)), top=240)
slide(at(2),  st(("E o manual de gestão que veio junto", B), ("FOI ESCRITO PRA OUTRO BICHO.", A)), top=240, fs=48)
slide(at(3),  st(("O outro bicho tem nome: gestor.", B), ("Escola de negócio, passagem por outras grandes.", B))
            + st(("O manual foi escrito pra ele.", B), ("E é com a régua dele que te medem.", R)), fs=40)
slide(at(4),  st(("Empresa de quinhentos milhões tem gestor.", B))
            + st(("Ele toca uma tese de investimento:", B), ("entra um real, sai um e vinte.", R))
            + st(("O dono nem pisa na operação.", B), ("Pra ele, aquilo é <b>dinheiro puro.</b>", B)), fs=40)
slide(at(5),  st(("Na pequena e média eu não encontro gestor.", B), ("Eu encontro você.", R)))
slide(at(6),  st(("A sua não é tese de investimento.", B), ("É o sonho de quem quis mudar de vida.", B))
            + st(("Ela paga a escola do seu filho", B), ("e o fornecedor da mesma conta.", R)), fs=42)
slide(at(7),  st(("Aí vem o curso e o consultor", B), ("e te cobram o que empresa grande faz:", B))
            + st(("Conselho, comitê, plano de cinco anos", B), ("e a ordem de tirar a emoção do negócio.", R)), fs=42)
slide(at(8),  st(("SÃO DOIS BICHOS DIFERENTES.", A), ("O MANUAL DO GRANDE", A), ("NÃO CABE PRA VOCÊ.", A)))
slide(at(9),  st(("O que esse manual não sabe:", B), ("a sua empresa carrega o seu DNA.", B))
            + st(("Ela nasceu de você, e todo risco", B), ("de quebrar ou de lucrar também é seu.", R)), fs=42)
slide(at(10), st(("O gestor que quebra a empresa", B), ("devolve as chaves e vai tocar outra.", B))
            + st(("Você não tem pra quem devolver.", B), ("Cada erro sai do seu bolso.", R)))
slide(at(11), st(("O gestor toca pelo número.", B), ("Você toca pelo bom senso, na tentativa e erro.", B))
            + st(("Por isso ele sabe quanto sobrou no mês.", B), ("E você, depois de tudo pago, sabe?", R)), fs=40)
slide(at(12), st(("BOM SENSO NÃO É GESTÃO.", A), ("É AÍ QUE O BICHO PEGA.", A)))
slide(at(13), st(("Não quero que você vire executivo.", B), ("Quero o básico de gestão dentro do sonho.", B))
            + st(("O arroz com feijão para qualquer empresário:", R)), fs=40)
slide(at(14), st(("A sua empresa dá lucro?", B), ("Qual é a sua margem?", B))
            + st(("Quanto do seu esforço sobra,", B), ("e quanto disso vai pro seu bolso?", R)))
slide(at(15), st(("Gestão feita pro pequeno e médio,", B), ("que faz a sobra mudar de tamanho.", B))
            + st(("Esse é o manual que cabe em você.", R)))
slide(at(16), st(("Eu tenho um treinamento pra donos", B), ("de pequenas e médias empresas, onde ensino:", B))
            + st(("a gestão feita pro seu bicho,", B), ("que faz a empresa sobrar dinheiro", R), ("no bolso do dono.", R), mt=26), fs=40)
slide(at(17), '      <div class="cta-big">Comenta <span class="red">PEQUENO</span></div>\n'
            + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=24))
