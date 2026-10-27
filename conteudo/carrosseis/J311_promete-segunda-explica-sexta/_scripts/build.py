#!/usr/bin/env python3
"""Carrossel J311 (segunda promete, sexta explica), formato Notas do iPhone igual ao 245, sem imagem e sem o Hélio.
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
 1: note(P(I("Segunda você promete.") + "", "font-size:76px;line-height:1.24")
        + P(HL("Sexta você explica."), "font-size:76px;line-height:1.3;margin-top:40px;text-wrap:balance")),
 2: note(P(I("Na segunda,") + " a meta da semana está bonita no quadro. Na sexta, chega a lista de motivos: o cliente sumiu, o fornecedor atrasou, choveu.")
        + P(HL("Ninguém mentiu. Só que ninguém olhou no meio da semana."))),
 3: note(P(I("E aí vira o mês.") + " Quatro sextas de explicação viram um mês de meta perdida.")
        + P(HL("E o dono só soma as desculpas no fim."))),
 4: note(P(I("Me responde:") + " hoje, quanto da meta do mês o seu time já fez? Quanto falta? Dá tempo?")
        + P(HL("Se você não sabe, ninguém na sua empresa sabe."))),
 5: note(P(I("Tem uma reunião") + " que eu não abro mão:")
        + '<div class="rule" style="margin:30px 0 34px;font-size:88px">Uma vez por semana, olhar o placar.</div>'
        + P("Quanto da meta já foi feito, se tem negócio suficiente no funil, o que está andando, o que travou, quem está sem retorno.", "font-size:48px")),
 6: note(P(I("É ali que você ajusta") + " antes do mês acabar. Muda o foco, cobra o retorno, ajuda quem travou.")
        + P(HL("No dia 30 não se ajusta nada. Só se conta."))),
 7: note(P(I("E a cobrança") + " acontece ali, com o time inteiro e o número na mesa.")
        + P(HL("Sem amenizar e sem gritar. O número fala sozinho."))),
 8: note(P(I("Eu tenho um treinamento") + " de gestão pra donos de PME: o MBV.")
        + P("Lá eu ensino o dono a montar as reuniões que fazem a meta andar toda semana: " + HL("Lucratividade, Crescimento e Cultura."))),
 9: note(P(I("Quer parar de ouvir") + " explicação toda sexta?")
        + '<div style="margin-top:44px"><span class="p">Comenta</span><br><span class="kw" style="margin-top:12px">SEMANA</span></div>'
        + P("que eu mando o link no seu direct.", "margin-top:22px")),
}

for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    (OUT/f"slide-{n:02d}.html").write_text(HEAD + S[n] + JS + '</body></html>', encoding="utf-8"); print(f"[{n:02d}] ok")
