#!/usr/bin/env python3
"""Carrossel J309 (melhor vendedor promovido a gerente), formato Notas do iPhone igual ao 245, sem imagem e sem o Hélio.
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
 1: note(P(I("Você promoveu o seu melhor vendedor") + " a gerente.", "font-size:76px;line-height:1.24")
        + P(HL("E perdeu os dois."), "font-size:76px;line-height:1.3;margin-top:40px;text-wrap:balance")),
 2: note(P(I("Perdeu o vendedor,") + " porque ele saiu da rua. E perdeu o gerente, porque ele nunca foi um.")
        + P(HL("Quem bate a meta não é o mesmo que faz o time bater."))),
 3: note(P(I("Olha o dia dele hoje:") + " atende o cliente grande, fecha a venda que o vendedor travou, resolve o pedido que deu problema.")
        + P(HL("Ele continua vendendo. E o time fica olhando."))),
 4: note(P(I("Me responde:") + " se ele tirar quinze dias de férias, o seu time bate a meta?")
        + P(HL("Se a resposta é não, você não tem um gerente. Tem um vendedor caro."))),
 5: note(P(I("Eu sei disso por mim.") + " Quando eu trabalhava pros outros, eu fui um bom vendedor. Estava entre os melhores.")
        + P(HL("Mas eu nunca fui o melhor."))),
 6: note(P(I("Onde eu fui o melhor") + " foi liderando time de venda. Cheguei a tocar mais de 1.500 vendedores numa empresa só.")
        + P(HL("Vender e fazer o time vender são dois talentos diferentes."))),
 7: note(P(I("E tem uma coisa") + " que quase todo dono esquece:")
        + '<div class="rule" style="margin:30px 0 34px;font-size:86px">O gerente preenche.<br>Quem monta é o dono.</div>'
        + P("Os indicadores, a reunião de segunda, o que cobrar de cada vendedor: isso é você que entrega pra ele. Sem ferramenta, ele faz a única coisa que sabe fazer: vender.", "font-size:48px")),
 8: note(P(I("Eu tenho um treinamento") + " de gestão pra donos de PME: o MBV.")
        + P("Lá eu ensino o dono a montar um time que vende sem depender de uma pessoa só: " + HL("Lucratividade, Crescimento e Cultura."))),
 9: note(P(I("Quer um gerente") + " que faz o time inteiro vender?")
        + '<div style="margin-top:44px"><span class="p">Comenta</span><br><span class="kw" style="margin-top:12px">LIDER</span></div>'
        + P("que eu mando o link no seu direct.", "margin-top:22px")),
}

for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    (OUT/f"slide-{n:02d}.html").write_text(HEAD + S[n] + JS + '</body></html>', encoding="utf-8"); print(f"[{n:02d}] ok")
