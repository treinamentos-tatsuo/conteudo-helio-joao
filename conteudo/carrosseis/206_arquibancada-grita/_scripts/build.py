#!/usr/bin/env python3
"""Gera os 15 HTMLs do carrossel 206 (editorial-punch, "A arquibancada grita").
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

slide(at(1),  st(("Errar é o risco de quem entra em campo.", B))
            + st(("CRITICAR É O GRITO", A), ("DE QUEM FICOU", A), ("NA ARQUIBANCADA.", A), mt=22), top=280, fs=46)
slide(at(2),  st(("Da arquibancada, todo mundo vê o seu erro.", B), ("Ninguém vê a casa em garantia no banco.", B))
            + st(("Nem a folha de sessenta pessoas", B), ("que vence no dia cinco.", R)), fs=42)
slide(at(3),  st(("O cunhado sabe onde você errou na filial nova.", B), ("O amigo do banco acha o seu preço um absurdo.", B))
            + st(("Nenhum dos dois", B), ("pôs um real nessa empresa.", R)), fs=40)
slide(at(4),  st(("De fora,", B))
            + st(("SEMPRE PARECE", A), ("FÁCIL.", A), mt=22), fs=48)
slide(at(5),  st(("Quem assiste vê o erro.", B), ("Quem está em campo sente o peso.", B))
            + st(("O peso de fechar a unidade que sangra.", B), ("De demitir o gerente de quinze anos.", R)), fs=42)
slide(at(6),  st(("É a decisão que ninguém", B), ("da arquibancada quer tomar.", B))
            + st(("E que você toma sozinho,", B), ("às onze da noite, com o escritório vazio.", R)), fs=42)
slide(at(7),  st(("Eu tenho 38 anos de empresa.", B), ("Toda empresa de pé que eu conheço existe", B))
            + st(("porque alguém apostou", B), ("quando ninguém apostaria.", R)), fs=42)
slide(at(8),  st(("Só que a arquibancada sempre vai existir.", B))
            + st(("O problema é quando o grito dela", B), ("pesa mais do que o placar da sua empresa.", R)), fs=42)
slide(at(9),  st(("Dono que não conhece o placar", B))
            + st(("DECIDE PELO", A), ("BARULHO.", A), mt=22), fs=46)
slide(at(10), st(("Não sobe o preço: o cliente vai reclamar.", B), ("Não fecha a unidade: vão dizer que quebrou.", B))
            + st(("E paga, todo mês,", B), ("o preço de não decidir.", R)), fs=40)
slide(at(11), st(("Tem crítica que ajuda e tem palpite.", B), ("Só o número separa os dois.", B))
            + st(("Crítica que bate com o placar é informação.", B), ("O resto é barulho de arquibancada.", R)), fs=40)
slide(at(12), st(("Quando você sabe o seu placar,", B), ("escuta todo mundo e decide em paz.", B))
            + st(("A arquibancada grita.", B), ("O placar não grita, mas também não mente.", R)), fs=42)
slide(at(13), st(("E placar não é faturamento.", B))
            + st(("É quanto entra, quanto sai", B), ("e quanto sobra pra você.", R)), fs=44)
slide(at(14), st(("Eu gravei uma aula, o RAIO-X da empresa.", B))
            + st(("As perguntas que eu faço pra ler o placar", B), ("de qualquer empresa em poucos minutos.", R)), fs=42)
slide(at(15), st(("Pode errar enquanto joga.", B), ("Só não deixa a arquibancada", R), ("escolher o seu jogo.", R))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">PLACAR</span></div>\n'
            + st(("que eu mando a aula no seu direct.", B), mt=18), fs=44)
