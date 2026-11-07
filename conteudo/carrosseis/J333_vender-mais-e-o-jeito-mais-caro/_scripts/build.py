#!/usr/bin/env python3
"""Carrossel J333 (vender mais é o jeito mais caro), formato Notas do iPhone igual ao 245 e ao J301, sem imagem e sem o Hélio.
Fundo branco, texto preto em Montserrat, entrada em serifa itálica, marca-texto carmim #A91C20."""
import pathlib, sys
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
OUT = ROOT/"instagram"; OUT.mkdir(exist_ok=True)
HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;1,600;1,700&family=Montserrat:wght@400;500;600&family=Anton&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden}
.ph{position:absolute;left:0;top:0;width:1080px}.shade{position:absolute;inset:0}.b{position:absolute;z-index:2}
.big{font-family:'Source Serif Pro',serif;font-size:56px;line-height:1.14;font-weight:600;color:#F3F3F3}
.hla{font-family:'Anton',sans-serif;text-transform:uppercase;background:#A91C20;color:#F3F3F3;padding:0 22px;letter-spacing:.5px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
/* Notas */
.note{background:#FFFFFF;font-family:'Montserrat',sans-serif;color:#141414}
.bar{position:absolute;top:44px;left:0;right:0;text-align:center;font:600 30px 'Montserrat',sans-serif;color:#141414}
.nav{position:absolute;top:118px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;color:#A91C20}
.back{font:500 38px 'Montserrat',sans-serif;display:flex;align-items:center;gap:14px}
.icons{display:flex;gap:44px;align-items:center}
.txt{position:absolute;left:110px;right:110px;top:250px;bottom:190px;display:flex;flex-direction:column;justify-content:center}
.p{font-size:56px;line-height:1.3;font-weight:400;letter-spacing:-.3px;text-wrap:pretty}
.p+.p{margin-top:34px}
.i{font-family:'Source Serif Pro',serif;font-style:italic;font-weight:700;font-size:1.1em;letter-spacing:-.5px}
.hl{background:#A91C20;color:#FFFFFF;padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.rule{font-family:'Source Serif Pro',serif;font-style:italic;font-weight:700;font-size:104px;line-height:1.05;color:#A91C20;letter-spacing:-1px}
.kw{font-family:'Anton',sans-serif;background:#A91C20;color:#FFFFFF;padding:0 22px;font-size:104px;line-height:1.25;letter-spacing:1px;display:inline-block}
</style></head><body>'''

ICONS = ('<div class="icons">'
  '<svg width="44" height="54" viewBox="0 0 44 54" fill="none" stroke="#A91C20" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
  '<path d="M14 18H6v32h32V18h-8"/><path d="M22 34V3"/><path d="M12 12 22 3l10 9"/></svg>'
  '<svg width="54" height="54" viewBox="0 0 54 54" fill="none" stroke="#A91C20" stroke-width="4"><circle cx="27" cy="27" r="24"/>'
  '<circle cx="16" cy="27" r="3" fill="#A91C20" stroke="none"/><circle cx="27" cy="27" r="3" fill="#A91C20" stroke="none"/>'
  '<circle cx="38" cy="27" r="3" fill="#A91C20" stroke="none"/></svg></div>')
NAV = ('<div class="bar">12:03</div><div class="nav"><div class="back">'
  '<svg width="24" height="42" viewBox="0 0 24 42" fill="none" stroke="#A91C20" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4 4 21l16 17"/></svg>'
  'Notas</div>' + ICONS + '</div>')

# alças de seleção do iOS no começo e no fim do marca-texto (só no .hl marcado com .sel)
JS = r'''<script>
document.fonts.ready.then(()=>{document.querySelectorAll('.sel').forEach(el=>{
 const rs=[...el.getClientRects()];if(!rs.length)return;const a=rs[0],z=rs[rs.length-1],s=document.querySelector('.slide');
 const mk=(x,y1,y2,top)=>{const d=document.createElement('div');d.style.cssText=`position:absolute;left:${x-2}px;top:${y1}px;width:4px;height:${y2-y1}px;background:#A91C20;z-index:5`;s.appendChild(d);
  const c=document.createElement('div');c.style.cssText=`position:absolute;left:${x-9}px;top:${top?y1-16:y2-2}px;width:18px;height:18px;border-radius:50%;background:#A91C20;z-index:5`;s.appendChild(c);};
 mk(a.left,a.top,a.bottom,true);mk(z.right,z.top,z.bottom,false);});});
</script>'''

def note(body): return f'<div class="slide note">{NAV}<div class="txt">{body}</div></div>'
def P(t, style=""): return f'<div class="p" style="{style}">{t}</div>'
def I(t): return f'<span class="i">{t}</span>'
def HL(t): return f'<span class="hl sel">{t}</span>'

S = {
 1: note(P(I("Outubro foi fraco,") + " e agora você quer correr atrás do prejuízo em novembro. Já mandou o time vender mais.", "font-size:60px;line-height:1.24")
        + P(HL("Vender mais é o jeito<br>mais caro de tirar<br>o prejuízo."), "font-size:76px;line-height:1.3;margin-top:40px;text-wrap:balance")),
 2: note(P(I("Faz essa conta comigo.") + " Num mês normal, a sua empresa fatura 500 mil. Tirando mercadoria, imposto e comissão, sobram 40% de cada venda.")
        + P(HL("São 200 mil pra pagar a estrutura."))),
 3: note(P(I("A estrutura custa 150 mil,") + " vendendo ou não. Num mês normal, sobram 50 mil de resultado.")
        + P(HL("Em outubro a venda caiu 30%.<br>Em vez de sobrar 50 mil,<br>faltaram 10."))),
 4: note(P(I("Agora você quer") + " tirar 20 mil a mais em novembro pra cobrir o buraco. Pelo caminho da venda, precisa faturar 50 mil acima do normal.")
        + P(HL("Mais campanha, mais vendedor, mais cliente pra atender."))),
 5: note(P(I("Pelo outro caminho,") + " você tira 20 mil de um gasto fixo que ninguém questiona há anos.")
        + P(HL("Mesmo resultado. Sem vender um real a mais."))),
 6: note(P(I("E tem uma diferença:") + " a venda a mais você tem que buscar de novo no mês que vem.")
        + '<div class="rule" style="margin-top:40px">O gasto que você cortou continua cortado.</div>'),
 7: note(P(I("Eu entendo.") + " Eu também sempre gostei mais de vender. Olhar gasto é chato pra cacete.")
        + P(HL("Por isso tem empresa que cresce o faturamento e encolhe o resultado."))),
 8: note(P(I("Mas cortar") + " não é sair demitindo. Gente boa você vai precisar pra crescer.")
        + P(HL("Corta o que você paga por costume, não o que traz cliente."))),
 9: note(P(I("Margem, gasto fixo e resultado") + " são gestão. Eu ensino isso no MBV, o meu treinamento pra donos de PME.", "font-size:52px")
        + '<div style="margin-top:44px"><span class="p">Comenta</span><br><span class="kw" style="margin-top:12px">MARGEM</span></div>'
        + P("que eu mando o link no seu direct.", "margin-top:22px")),
}

for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    (OUT/f"slide-{n:02d}.html").write_text(HEAD + S[n] + JS + '</body></html>', encoding="utf-8"); print(f"[{n:02d}] ok")
