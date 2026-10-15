#!/usr/bin/env python3
"""Gera os 16 HTMLs do carrossel 119 (editorial-punch, "Cansei de demitir vendedor").
Layout da skill (modelo.md, calibragem de 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
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

slide(at(1),  st(("CANSEI DE DEMITIR", A), ("VENDEDOR.", A)), top=280)
slide(at(2),  st(("Terceiro nome no mesmo crachá.", B), ("Mesma vaga, mesmo erro, mesma bronca.", B))
            + st(("E você já sabe o final:", B), ("daqui a três meses, troca de novo.", R)))
slide(at(3),  st(("O primeiro saiu por preguiça.", B), ("O segundo, por falta de atenção.", B))
            + st(("O terceiro erra igualzinho aos dois.", B), ("E hoje é mais um dia", R), ("com você lendo currículo.", R)), fs=42)
slide(at(4),  st(("VOCÊ NÃO DEMITIU O PROBLEMA.", A), ("DEMITIU QUEM ESTAVA", A), ("SENTADO EM CIMA DELE.", A)))
slide(at(5),  st(("A vaga tem um erro que já é dela.", B), ("E quem senta ali herda ele no primeiro dia.", B))
            + st(("Ninguém escreveu o que tem que fazer.", B), ("Cada um aprende olhando como o outro faz.", R)), fs=40)
slide(at(6),  st(("Demitir dá a sensação de que você agiu.", B), ("É o remédio mais caro que existe:", B))
            + st(("aviso prévio, salário novo, três meses", B), ("pra chegar no mesmo erro de sempre.", R)), fs=42)
slide(at(7),  st(("OUTRO ELENCO.", A), ("MESMO ROTEIRO.", A), ("MESMO FINAL.", A)))
slide(at(8),  st(("É mais fácil ensinar quem está dentro", B), ("do que contratar achando que vem pronto.", B))
            + st(("Do mercado vem gente.", B), ("Agora gente pronta, quem forma é você.", R)), fs=42)
slide(at(9),  st(("Antes de abrir a próxima vaga,", B), ("conserta a que você já tem:", B))
            + st(("o que ela faz, no papel. Quem ensina.", B), ("E cobrança igual toda semana.", R)))
slide(at(10), st(("Treinou o vendedor e achou que resolveu?", B), ("Ninguém sai de um treinamento fazendo certo.", B))
            + st(("Treinar sem acompanhar não adianta nada.", B), ("É dinheiro jogado no pátio.", R)), fs=40)
slide(at(11), st(("A PARTE MAIS DIFÍCIL", A), ("NÃO É TREINAR.", A), ("É ACOMPANHAR TODO SANTO DIA.", A)))
slide(at(12), st(("Rito diário, mesma hora, três perguntas:", B), ("o que vendeu ontem, o que faz hoje,", B), ("o que te trava.", B))
            + st(("Amanhã você pergunta de novo.", B), ("E depois de amanhã também.", R)), fs=40)
slide(at(13), st(("Vendedor bom não precisa de herói.", B))
            + st(("Precisa de dono normal,", R), ("que faça o básico bem feito sempre.", R)))
slide(at(14), st(("Aí a próxima troca não é por erro.", B), ("É por crescimento.", B))
            + st(("E quem entra erra menos que quem saiu,", B), ("porque a vaga já sabe o que fazer.", R)), fs=42)
slide(at(15), st(("Eu tenho um treinamento pra donos", B), ("de pequenas e médias empresas, onde ensino:", B))
            + st(("a montar a vaga antes do vendedor,", B), ("com padrão escrito, ensinado", B), ("e acompanhado todo dia.", R), mt=26), fs=42)
slide(at(16), '      <div class="cta-big">Comenta <span class="red">RAIZ</span></div>\n'
            + st(("e eu te mando o link com todos", R), ("os detalhes no seu direct.", R), mt=24))
