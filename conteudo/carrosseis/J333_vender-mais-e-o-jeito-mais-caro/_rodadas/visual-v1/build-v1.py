# Monta os 9 slides do J333 no modelo bloco-de-notas (1080x1350).
# Uso: python build.py
import pathlib, html

OUT = pathlib.Path(__file__).resolve().parent.parent / "instagram"
OUT.mkdir(exist_ok=True)

DATA = "7 de novembro de 2026 às 09:14"

# Cada slide: lista de estrofes; cada estrofe: lista de (texto, bold). "/" quebra linha.
S = [
  [[("Mês fraco, e a primeira coisa / que você faz é mandar o time / vender mais.", 0)],
   [("Vender mais é o jeito / mais caro de ter lucro.", 1)]],
  [[("Faz essa conta comigo. / A sua empresa fatura 500 mil por mês.", 0)],
   [("Tirando mercadoria, imposto e comissão, / sobram 40% de cada venda.", 0),
    ("São 200 mil pra pagar a estrutura.", 1)]],
  [[("A estrutura custa 150 mil. / Aluguel, folha, sistema: / o que você paga vendendo ou não.", 0)],
   [("Sobram 50 mil. / Esse é o seu resultado.", 1)]],
  [[("Agora você quer 20 mil / a mais de resultado. / Pelo caminho da venda, precisa / faturar 50 mil a mais. Todo mês.", 0)],
   [("Mais campanha, mais vendedor, / mais cliente pra atender.", 1)]],
  [[("Pelo outro caminho, você tira 20 mil / de um gasto fixo / que ninguém questiona há anos.", 0)],
   [("Mesmo resultado. / Sem vender um real a mais.", 1)]],
  [[("E tem uma diferença: / a venda a mais você tem que buscar / de novo no mês que vem.", 0)],
   [("O gasto que você cortou / continua cortado.", 1)]],
  [[("Eu entendo. Eu também / sempre gostei mais de vender. / Olhar gasto é chato pra cacete.", 0)],
   [("Por isso tem empresa / que cresce o faturamento / e encolhe o resultado.", 1)]],
  [[("Mas cortar não é sair demitindo. / Gente boa você vai precisar pra crescer.", 0)],
   [("Corta o que você paga por costume, / não o que traz cliente.", 1)]],
  [[("Margem, gasto fixo e resultado / são gestão. Eu ensino isso no MBV, / o meu treinamento pra donos de PME.", 0)],
   [("Comenta <b class='k'>MARGEM</b> / que eu mando o link no seu direct.", 2)]],
]

RED = "#A91C20"
ICON_SHARE = f'<svg width="46" height="54" viewBox="0 0 46 54" fill="none" stroke="{RED}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"><path d="M14 20H8v30h30V20h-6"/><path d="M23 34V3"/><path d="M13 13 23 3l10 10"/></svg>'
ICON_MORE = f'<svg width="54" height="54" viewBox="0 0 54 54" fill="none" stroke="{RED}" stroke-width="3.6"><circle cx="27" cy="27" r="23"/><circle cx="16" cy="27" r="2.6" fill="{RED}" stroke="none"/><circle cx="27" cy="27" r="2.6" fill="{RED}" stroke="none"/><circle cx="38" cy="27" r="2.6" fill="{RED}" stroke="none"/></svg>'
ICON_CHECK = f'<svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="{RED}" stroke-width="3.4" stroke-linecap="round"><circle cx="9" cy="12" r="5"/><circle cx="9" cy="40" r="5"/><path d="M22 12h26M22 40h26M22 26h26"/><circle cx="9" cy="26" r="5"/></svg>'
ICON_CAM = f'<svg width="58" height="50" viewBox="0 0 58 50" fill="none" stroke="{RED}" stroke-width="3.4" stroke-linejoin="round"><path d="M4 14h12l5-8h16l5 8h12v32H4z"/><circle cx="29" cy="29" r="10"/></svg>'
ICON_PEN = f'<svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="{RED}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10 46c8-2 10-10 18-18l12-12-6-6-12 12C14 30 6 32 4 40"/><path d="M34 10l8-6 6 6-6 8"/></svg>'
ICON_NEW = f'<svg width="54" height="54" viewBox="0 0 54 54" fill="none" stroke="{RED}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 30v18H6V10h18"/><path d="M40 4l10 10-22 22H18V26z"/></svg>'

def line(t):
    parts = [p.strip() for p in t.split(" / ")]
    return "<br>".join(parts)

def slide(n, stanzas):
    body = []
    for st in stanzas:
        rows = []
        for t, b in st:
            cls = "p" if b == 0 else ("p hi" if b == 1 else "p cta")
            rows.append(f'<div class="{cls}">{line(t)}</div>')
        body.append('<div class="st">' + "".join(rows) + "</div>")
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;background:#FFFFFF;font-family:'Inter',sans-serif;color:#1C1C1E;overflow:hidden}}
.top{{position:absolute;top:0;left:0;right:0;height:150px;display:flex;align-items:center;justify-content:space-between;padding:40px 56px 0 40px}}
.back{{display:flex;align-items:center;gap:6px;color:{RED};font-size:42px;font-weight:500}}
.back svg{{margin-top:2px}}
.icons{{display:flex;gap:44px;align-items:center}}
.date{{position:absolute;top:172px;left:0;right:0;text-align:center;color:#8E8E93;font-size:28px;font-weight:500}}
.note{{position:absolute;top:268px;left:84px;right:84px}}
.st{{margin-bottom:64px}}
.p{{font-size:46px;line-height:1.38;font-weight:400;letter-spacing:-0.4px}}
.p+.p{{margin-top:6px}}
.hi{{font-weight:800;color:{RED};letter-spacing:-0.6px}}
.cta{{font-weight:500}}
.k{{font-weight:800;color:{RED}}}
.s1 .p{{font-size:48px}}
.s1 .hi{{font-size:76px;line-height:1.18;letter-spacing:-1.4px}}
.bar{{position:absolute;bottom:0;left:0;right:0;height:150px;display:flex;align-items:center;justify-content:space-between;padding:0 70px 24px;border-top:1.5px solid #E5E5EA}}
.home{{position:absolute;bottom:14px;left:50%;width:300px;height:10px;margin-left:-150px;border-radius:6px;background:#1C1C1E}}
</style></head><body class="s{n}">
<div class="top"><div class="back"><svg width="30" height="50" viewBox="0 0 30 50" fill="none" stroke="{RED}" stroke-width="5.4" stroke-linecap="round" stroke-linejoin="round"><path d="M24 4 5 25l19 21"/></svg>Notas</div>
<div class="icons">{ICON_SHARE}{ICON_MORE}</div></div>
<div class="date">{DATA}</div>
<div class="note">{''.join(body)}</div>
<div class="bar">{ICON_CHECK}{ICON_CAM}{ICON_PEN}{ICON_NEW}</div>
<div class="home"></div>
</body></html>"""

for i, st in enumerate(S, 1):
    (OUT / f"slide-{i:02d}.html").write_text(slide(i, st), encoding="utf-8")
    print(f"slide-{i:02d}.html")
