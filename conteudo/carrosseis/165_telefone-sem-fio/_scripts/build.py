#!/usr/bin/env python3
"""Gera os 14 HTMLs do carrossel 165 (editorial-punch, "Telefone sem fio").
Layout da skill (modelo.md, calibragem 11/09: corpo top 240, capa 280; Source Serif 44; Anton nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text()).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {14: "80% bottom"}
QW = 0.0  # largura da aspa serif (quotewidth.js), em em
try: QW = json.loads((SCR/"quotewidth.json").read_text())["em"]
except Exception: pass
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
  .oq{ margin-left:-QWem; } .cq{ margin-right:-QWem; }
  .anton .oq{ margin-left:-0.466em; } .anton .cq{ margin-right:-0.466em; }
</style>
</head>
<body>
""".replace("QW", f"{QW:.3f}")
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

Q1, Q2 = '<span class="oq">&ldquo;</span>', '<span class="cq">&rdquo;</span>'
slide(at(1),  st(("Você explicou direitinho.", B)) + st(("E FIZERAM TUDO", A), ("DIFERENTE.", A), mt=10), top=280, fs=48)
slide(at(2),  st(("O desconto que ninguém autorizou.", B), ("A medida que saiu errada.", B), ("O prazo que não existe.", B))
            + st(("E todo mundo jura que fez", R), ("do jeito que você falou.", R)))
slide(at(3),  st(("Todo dono me diz a mesma coisa:", B), (f"{Q1}essa geração não quer nada com nada.{Q2}", B))
            + st((f"{Q1}Eu explico mil vezes", R), (f"e ninguém faz do jeito que eu falei.{Q2}", R)), fs=42)
slide(at(4),  st(("Pode reclamar, eu também já reclamei.", B), ("Mas presta atenção:", B))
            + st(("ninguém faz do jeito que você falou.", B), ("Cada um faz do jeito que entendeu.", R)), fs=42)
slide(at(5),  st(("Empresa que roda no boca a boca", B)) + st(("VIRA TELEFONE SEM FIO.", A), mt=14))
slide(at(6),  st(("Você fala pro gerente.", B), ("O gerente conta pro vendedor.", B))
            + st(("O vendedor passa pro novato como entendeu.", B), ("No cliente, a história já é outra.", R)), fs=42)
slide(at(7),  st(("Entregar a tarefa e sair andando tem nome.", B)) + st(("CHAMA DELARGAR.", A), mt=14), fs=42)
slide(at(8),  st(("Delargar é dar a tarefa sem dizer o quê,", B), ("sem mostrar como e sem marcar quando.", B))
            + st(("Aí cada um tapa o buraco", B), ("com o que acha que você quis dizer.", R)), fs=42)
slide(at(9),  st(("Gente não lê pensamento.", B), ("Gente cumpre o que está escrito.", R))
            + st(("Quando não tem nada escrito,", B), ("cumpre o que lembra.", B)))
slide(at(10), st(("Lembra da cartilha Caminho Suave?", B), ("Abelha, barriga, cachorro.", B))
            + st(("Ninguém aprendeu a ler de ouvido.", B), ("Aprendeu com a mesma página pra sala inteira.", R)), fs=40)
slide(at(11), st(("Empresa também precisa de cartilha:", B), ("o quê, como e quando, por escrito.", B))
            + st(("Na empresa, essa cartilha se chama", B)) + st(("SCRIPT,", A), mt=4)
            + st(("com processo, com passo a passo.", R), mt=22), fs=42)
slide(at(12), st(("Aí o novato aprende igual ao antigo,", B), ("o vendedor fala igual ao gerente", B))
            + st(("e o cliente ouve a mesma história", R), ("que saiu da sua boca.", R)), fs=42)
slide(at(13), st(("Agora vem a parte que quase todo dono pula.", B))
            + st(("O funcionário lê a cartilha no primeiro dia", B), ("e na segunda semana já faz do jeito dele.", R)), fs=42)
slide(at(14), st(("Pode ter script, pode ter manual.", B)) + st(("SEM ACOMPANHAMENTO,", A), ("NADA FUNCIONA.", A), mt=14))
slide(at(15), st(("Sem cartilha, você não tem o que cobrar.", B), ("Sem acompanhamento, a cartilha vira papel.", R))
            + st(("Treinar uma vez não resolve.", B), ("O que resolve é o rito de acompanhar.", R)), fs=42)
slide(at(16), st(("Eu tenho um treinamento de gestão", B), ("pra pequena e média empresa,", B))
            + st(("inclusive gestão de pessoas,", B), ("cultura e liderança.", R)))
slide(at(17), st(("Ou você acompanha o que escreveu,", B), ("ou cada um faz do seu jeito.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PADRÃO</span></div>\n'
            + st(("que eu te mando o link no direct.", B), mt=6))
