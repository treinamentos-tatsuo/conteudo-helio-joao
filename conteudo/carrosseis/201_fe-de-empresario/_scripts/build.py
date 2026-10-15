#!/usr/bin/env python3
"""Gera os 13 HTMLs do carrossel 201 (editorial-punch, "Fé de empresário").
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif; Anton só nos gritos)."""
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
  .oq{ margin-left:-0.466em; } .cq{ margin-right:-0.466em; }
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
OQ, CQ = '<span class="oq">&ldquo;</span>', '<span class="cq">&rdquo;</span>'

slide(at(1),  st(("Nenhuma empresa cresce", B))
            + st(("MAIS DO QUE O DONO ACREDITA.", A), mt=22), top=280, fs=48)
slide(at(2),  st(("Todo empresário precisa ter fé.", B), ("E eu não estou falando de reza.", B))
            + st(("Estou falando da fé ao pé da letra:", B), ("acreditar numa coisa", R), ("antes mesmo de ela acontecer.", R)), fs=42)
slide(at(3),  st(("Todo mundo vive mandando o dono", B), ("pôr o pé no chão. O contador, o gerente", B), ("do banco, até o cunhado no churrasco.", B))
            + st(("Só que pé no chão demais vira raiz.", B), ("E raiz não sai do lugar nunca mais.", R)), fs=40)
slide(at(4),  st(("Tem empresa que fatura 20 milhões", B), ("há seis anos seguidos.", B), ("O mesmo galpão, os mesmos clientes,", B), ("o mesmo pró-labore todo mês.", B))
            + st(("O número parou de crescer", B), ("no dia em que o dono parou de acreditar.", R)), fs=40)
slide(at(5),  st(("Ninguém aguenta trabalhar 12 horas por dia", B), ("pra ter a mesma empresa que a do ano passado.", B))
            + st(("Se o prêmio lá na frente não for grande,", B), ("uma hora o dono perde até a vontade", R), ("de levantar da cama.", R)), fs=40)
slide(at(6),  st(("Fé de empresário é enxergar a coisa pronta", B), ("antes de ela existir: a segunda unidade", B), ("aberta, a diretoria tocando o dia a dia,", B), ("o dividendo caindo na conta.", B))
            + st(("Primeiro ela acontece na cabeça do dono.", B), ("Só depois ela acontece no terreno.", R)), fs=39)
slide(at(7),  st(("A empresa funciona igual a uma igreja:", B), ("ela tem um credo. E o time só acredita", B), ("naquilo que o dono prega com convicção.", B))
            + st(("PREGADOR SEM FÉ", A), ("NÃO CONVERTE NINGUÉM.", A), mt=22), fs=40)
slide(at(8),  st(("Outubro é o mês de fechar o orçamento", B), ("de 2027. E muito dono vai pegar", B), ("o deste ano e só colocar 10% em cima.", B))
            + st(("Isso não é ter fé na empresa.", B), ("Isso é torcer pra dar certo.", R)), fs=40)
slide(at(9),  st(("A fé do empresário tem número.", B), ("Ele sabe quanto quer faturar, quanto", B), ("quer que sobre e em quanto tempo.", B))
            + st(("E tem um plano escrito pra cada degrau", B), ("entre onde ele está hoje", R), ("e onde ele quer chegar.", R)), fs=40)
slide(at(10), st(("E esse número grande não fica pendurado", B), ("num quadro na parede. Ele vai pra reunião", B), ("de toda segunda-feira, e alguém olha", B), ("pra ele toda semana.", B))
            + st(("Fé que ninguém acompanha vira promessa", B), ("de Ano-Novo, que em março", R), ("todo mundo já esqueceu.", R)), fs=39)
slide(at(11), st(("Sonho grande sem rotina", B), ("não passa de delírio.", B), ("E rotina sem sonho grande", B), ("vira só repetição.", B))
            + st(("É quando os dois andam juntos", R), ("que a empresa chega no extraordinário.", R)), fs=42)
slide(at(12), st(("Eu tenho um treinamento pra donos", B), ("de pequena e média empresa, o MBV,", B), ("onde eu ensino gestão: como colocar", B), ("número e rito dentro da empresa,", B))
            + st(("pra que aquilo em que o dono acredita", B), ("vire uma empresa grande de verdade.", R)), fs=40)
slide(at(13), st(("Outubro é quando você decide o tamanho", B), ("da sua empresa em 2027.", B), ("Decide com fé, e decide com número.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">GRANDE</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=42)
