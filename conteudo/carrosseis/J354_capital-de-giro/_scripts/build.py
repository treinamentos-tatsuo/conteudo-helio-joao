#!/usr/bin/env python3
"""Carrossel J354 (capital de giro), formato Notas do iPhone igual ao 245 e ao J301, sem imagem e sem o Hélio.
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
 1: note(P(I("A empresa fatura 300 mil por mês.") + " E precisa ter 400 mil parados só pra continuar funcionando.", "font-size:60px;line-height:1.24")
        + P(HL("Você sabe quanto<br>a sua precisa?"), "font-size:76px;line-height:1.3;margin-top:40px")),
 2: note(P(I("Faz a conta comigo.") + " Essa empresa gasta 250 mil no mês e trabalha 25 dias.")
        + P(HL("Saem 10 mil do caixa todo dia."))),
 3: note(P(I("E cada real que sai hoje") + " só volta daqui a 40 dias, que é o ciclo financeiro dela.")
        + P(HL("40 dias vezes 10 mil dá 400 mil."))),
 4: note(P(I("Hoje saem 10 mil") + " que voltam daqui a 40 dias. Amanhã saem mais 10 mil, que voltam 40 dias depois.")
        + P(HL("E todo dia é assim."))),
 5: note(P(I("Então, em qualquer dia que você olhar,") + " tem 40 dias de gasto na rua esperando voltar.")
        + '<div class="rule" style="margin-top:40px">Esse dinheiro nunca fica livre.</div>'),
 6: note(P(I("Isso tem nome:") + " necessidade de capital de giro. É o dinheiro que precisa ficar parado pra operação girar.")
        + P(HL("Enquanto a empresa funcionar, ele não cai."))),
 7: note(P(I("Ele só muda") + " se mudar o ciclo ou se mudar o gasto.")
        + P(HL("Vender mais não diminui esse número."))),
 8: note(P(I("Por isso o dono que não sabe esse número") + " acha que o aperto é falta de venda.")
        + P(HL("É falta de capital de giro."))),
 9: note(P(I("Eu ensino essa conta no MBV,") + " o meu treinamento de gestão pra donos de PME.")
        + '<div style="margin-top:44px"><span class="p">Comenta</span><br><span class="kw" style="margin-top:12px">GIRO</span></div>'
        + P("que eu mando o link no seu direct.", "margin-top:22px")),
}

for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    (OUT/f"slide-{n:02d}.html").write_text(HEAD + S[n] + JS + '</body></html>', encoding="utf-8"); print(f"[{n:02d}] ok")
