#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 111 (editorial-punch, "Quebra por falta de caixa").
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

slide(at(1),  st(("Empresa não quebra por falta de venda.", B), ("QUEBRA POR FALTA DE CAIXA.", A)), top=280, fs=48)
slide(at(2),  st(("Essa é a lição mais simples que existe,", B), ("mas que salva pequena e média empresa", B), ("de quebrar todo santo dia.", R)))
slide(at(3),  st(("Te ensinaram que venda resolve tudo.", B), ("Mas olha a sua empresa:", B))
            + st(("vendeu como nunca, e continuou", B), ("pegando empréstimo como nunca.", R)), fs=42)
slide(at(4),  st(("Onde realmente está o dinheiro?", R), ("Na rua. No cartão, no carnê do cliente,", B), ("dividido em dez vezes.", B))
            + st(("Enquanto o seu fornecedor, que entregou", B), ("a mercadoria, quer o dele em trinta dias.", R)), fs=40)
slide(at(5),  st(("Ou seja: você vende hoje,", B), ("paga em trinta e recebe em noventa.", B))
            + st(("Nesses sessenta dias quem banca o cliente é você.", B), ("E nem juros cobra.", R)), fs=40)
slide(at(6),  st(("Isso tem nome: Fluxo de Caixa.", B))
            + st(("O DINHEIRO QUE ENTRA", A), ("NO CAIXA NÃO É SEU.", A), ("ESTÁ SÓ EMPRESTADO.", A)), fs=48)
slide(at(7),  st(("E cada venda nova é mais dinheiro seu na rua.", B), ("Por isso a conta não fecha.", B))
            + st(("Quanto mais você vende assim,", B), ("mais falta pra folha no dia 5.", R)), fs=42)
slide(at(8),  st(("Aí, quando falta, você faz o quê?", B), ("Vende mais. E pega mais no banco.", B))
            + st(("E o buraco que você tentou tapar", B), ("ficou maior. Agora com juros.", R)))
slide(at(9),  st(("CRESCER SEM CAIXA É", A), ("ACELERAR RUMO AO ABISMO.", A)))
slide(at(10), st(("Não é falta de venda.", B), ("É uma conta que ninguém fez com você.", B))
            + st(("Quantos dias pra receber, quantos pra pagar.", B), ("A diferença é onde você quebra.", R)), fs=42)
slide(at(11), st(("Quem faz essa conta cresce vendendo.", B), ("Quem não faz, quebra vendendo.", B))
            + st(("E quase sempre", B), ("com a loja cheia.", R)))
slide(at(12), st(("Quer saber em quantos dias", B), ("a sua venda vira dinheiro?", B))
            + st(("Eu ofereço um diagnóstico gratuito,", B), ("com um especialista da minha equipe,", B), ("nos três pilares do MBV.", R), mt=26), fs=42)
slide(at(13), '      <div class="cta-big">Comenta <span class="red">DIAGNÓSTICO</span></div>\n'
            + st(("e eu te mando o link no seu direct", R), ("pra agendar o seu diagnóstico.", R), mt=24))
