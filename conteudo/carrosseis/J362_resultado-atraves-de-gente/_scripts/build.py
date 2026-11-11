#!/usr/bin/env python3
"""J362 (resultado através de gente): Notas do iPhone em modo escuro, igual ao post de 01/11 (DfNMSaAETtG).
Fundo preto, texto branco em Montserrat, entrada em negrito itálico, marca-texto carmim #A91C20 com alças,
desenho de traço branco (SVG) na metade de baixo."""
import pathlib, sys
SCR = pathlib.Path(__file__).parent; OUT = SCR.parent/"instagram"; OUT.mkdir(exist_ok=True)
HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,700;0,800;1,700;1,800&family=Anton&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#000;font-family:'Montserrat',sans-serif;color:#F2F2F2}
.bar{position:absolute;top:44px;left:0;right:0;text-align:center;font:600 30px 'Montserrat',sans-serif;color:#F2F2F2}
.nav{position:absolute;top:118px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;color:#A91C20}
.back{font:500 38px 'Montserrat',sans-serif;display:flex;align-items:center;gap:14px}
.icons{display:flex;gap:44px;align-items:center}
.txt{position:absolute;left:100px;right:100px;top:270px}
.p{font-size:50px;line-height:1.32;font-weight:400;letter-spacing:-.2px}
.p+.p{margin-top:26px}
.i{font-weight:800;font-style:italic}
.hl{background:#A91C20;color:#FFF;padding:0 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.cap{font-weight:800;text-transform:uppercase}
.kw{font-family:'Anton',sans-serif;background:#A91C20;color:#FFF;padding:0 26px;font-size:104px;line-height:1.25;letter-spacing:1px;display:inline-block}
.draw{position:absolute;left:90px;right:90px;bottom:110px;height:470px}
.draw svg{width:100%;height:100%}
</style></head><body>'''
ICONS = ('<div class="icons">'
  '<svg width="44" height="54" viewBox="0 0 44 54" fill="none" stroke="#A91C20" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
  '<path d="M14 18H6v32h32V18h-8"/><path d="M22 34V3"/><path d="M12 12 22 3l10 9"/></svg>'
  '<svg width="54" height="54" viewBox="0 0 54 54" fill="none" stroke="#A91C20" stroke-width="4"><circle cx="27" cy="27" r="24"/>'
  '<circle cx="16" cy="27" r="3" fill="#A91C20" stroke="none"/><circle cx="27" cy="27" r="3" fill="#A91C20" stroke="none"/>'
  '<circle cx="38" cy="27" r="3" fill="#A91C20" stroke="none"/></svg></div>')
NAV = ('<div class="bar">13:45</div><div class="nav"><div class="back">'
  '<svg width="24" height="42" viewBox="0 0 24 42" fill="none" stroke="#A91C20" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4 4 21l16 17"/></svg>'
  'Notas</div>' + ICONS + '</div>')
JS = r'''<script>
document.fonts.ready.then(()=>{document.querySelectorAll('.sel').forEach(el=>{
 const rs=[...el.getClientRects()];if(!rs.length)return;const a=rs[0],z=rs[rs.length-1],s=document.querySelector('.slide');
 const mk=(x,y1,y2,top)=>{const d=document.createElement('div');d.style.cssText=`position:absolute;left:${x-2}px;top:${y1}px;width:4px;height:${y2-y1}px;background:#A91C20;z-index:5`;s.appendChild(d);
  const c=document.createElement('div');c.style.cssText=`position:absolute;left:${x-9}px;top:${top?y1-16:y2-2}px;width:18px;height:18px;border-radius:50%;background:#A91C20;z-index:5`;s.appendChild(c);};
 mk(a.left,a.top,a.bottom,true);mk(z.right,z.top,z.bottom,false);});});
</script>'''

# ---------- desenho (viewBox 900 x 470, traço branco) ----------
ST = 'stroke="#F2F2F2" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
def T(x, y, t, s=26, w=700, anchor="middle"):
    return f'<text x="{x}" y="{y}" fill="#F2F2F2" font-family="Montserrat" font-weight="{w}" font-size="{s}" text-anchor="{anchor}">{t}</text>'
def fig(x, g, label=None, flag=False):
    hy = g - 250
    s = (f'<circle cx="{x}" cy="{hy}" r="30" {ST}/>'
         f'<circle cx="{x-10}" cy="{hy-4}" r="5" {ST}/><circle cx="{x+10}" cy="{hy-4}" r="5" {ST}/>'
         f'<path d="M{x} {hy+30}V{g-100} M{x} {hy+60}L{x-50} {hy+115} M{x} {hy+60}L{x+50} {hy+115} '
         f'M{x} {g-100}L{x-38} {g} M{x} {g-100}L{x+38} {g}" {ST}/>')
    if flag:
        s += f'<path d="M{x+50} {hy+115}V{hy-110}" {ST}/><path d="M{x+50} {hy-110}h90l-20 28 20 28h-90" {ST}/>'
    if label: s += T(x, g + 40, label, 24)
    return s
def balloon(x, y, w, t, tx, ty):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="62" rx="4" {ST}/>' + T(x + w/2, y + 41, t, 25)
            + f'<path d="M{tx} {y+62}L{tx} {ty}" {ST}/>')
def box(x, y, w, h): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {ST}/>'
def check(x, y, sz=110, mark=True):
    s = box(x, y, sz, sz)
    if mark: s += f'<path d="M{x+20} {y+sz*.55}L{x+sz*.42} {y+sz-22}L{x+sz-14} {y+18}" {ST} stroke-width="7"/>'
    return s
def svg(inner): return f'<div class="draw"><svg viewBox="0 0 900 470">{inner}</svg></div>'

D = {}
# 1 tabela QUEM FAZ O QUÊ
rows = [("VENDA", "TIME"), ("ENTREGA", "TIME"), ("ATENDIMENTO", "TIME"), ("COBRAR O NÚMERO", "DONO")]
t = box(130, 20, 640, 430) + T(450, 78, "QUEM FAZ O QUÊ", 32, 800) + f'<path d="M130 105H770" {ST}/>'
for k, (a, b) in enumerate(rows):
    y = 170 + k * 72
    t += T(165, y, a, 27, 600, "start") + T(735, y, b, 27, 600, "end")
t += box(150, 170 + 3*72 - 44, 600, 64)
D[1] = svg(t)
# 2 dono olhando a planilha
pl = box(470, 130, 230, 170) + ''.join(f'<path d="M470 {130+34*i}H700" {ST} stroke-width="3"/>' for i in range(1, 5)) + f'<path d="M560 130V300" {ST} stroke-width="3"/>'
D[2] = svg(fig(330, 420, "DONO") + balloon(170, 20, 330, "BATEU A META?", 330, 135) + pl + T(585, 335, "PLANILHA", 22))
# 3 três bonecos
D[3] = svg(fig(200, 410, "VENDE") + fig(450, 410, "ENTREGA") + fig(700, 410, "ATENDE") + f'<path d="M90 412H810" {ST}/>')
# 4 relógio 8H
ticks = ''.join(f'<path d="M450 {60}V{85}" {ST} transform="rotate({a} 450 235)"/>' for a in range(0, 360, 30))
D[4] = svg(f'<circle cx="450" cy="235" r="175" {ST}/>' + ticks + f'<path d="M450 235V120 M450 235L355 290" {ST} stroke-width="7"/>' + T(450, 350, "8H", 54, 800))
# 5 EMPRESA x CASA
emp = box(110, 150, 240, 230) + ''.join(box(140 + 70*c, 185 + 70*r, 40, 40) for r in range(2) for c in range(3)) + T(230, 430, "EMPRESA", 28)
casa = f'<path d="M560 230L680 130L800 230V380H560Z" {ST}/>' + box(650, 300, 60, 80) + T(680, 430, "CASA", 28)
D[5] = svg(emp + T(455, 300, "×", 90, 800) + casa)
# 6 saindo pela porta
porta = box(560, 120, 170, 300) + f'<circle cx="710" cy="275" r="6" {ST}/>' + box(510, 30, 270, 62) + T(645, 71, "PROPOSTA NOVA", 24)
D[6] = svg(fig(420, 420) + porta + f'<path d="M480 300h55m-18-16 18 16-18 16" {ST}/>' + f'<path d="M300 422H800" {ST}/>')
# 7 três caixinhas marcadas
lbl = [("FESTA", "JUNINA"), ("FUTEBOL", "DE TERÇA"), ("ALUNO", "NOVO")]
t = ''
for k, (a, b) in enumerate(lbl):
    x = 130 + k * 250
    t += check(x, 90, 140) + T(x + 70, 290, a, 26) + T(x + 70, 325, b, 26)
D[7] = svg(t)
# 8 time em fila, um com bandeira
D[8] = svg(''.join(fig(x, 430, flag=(x == 450)) for x in (130, 290, 450, 610, 770)) + f'<path d="M60 432H840" {ST}/>')
# 9 duas caixinhas vazias
D[9] = svg(check(190, 70, 120, False) + T(350, 150, "SÓ O NÚMERO", 40, 800, "start")
           + check(190, 250, 120, False) + T(350, 330, "QUEM FAZ O NÚMERO", 40, 800, "start"))

def note(body, n=None):
    return f'<div class="slide">{NAV}<div class="txt">{body}</div>{D.get(n, "")}</div>'
def P(t, style=""): return f'<div class="p" style="{style}">{t}</div>'
def I(t): return f'<span class="i">{t}</span>'
def HL(t, cap=False): return f'<span class="hl sel{" cap" if cap else ""}">{t}</span>'

S = {
 1: note(P(I("Você cobra o resultado<br>todo mês."), "font-size:76px;line-height:1.18")
        + P(HL("Mas quem faz o resultado não é você.", True), "font-size:54px;line-height:1.38;margin-top:34px"), 1),
 2: note(P(HL("Muito dono olha a<br>planilha todo dia.")) + P("Sabe a meta, o faturamento e a margem.<br>E não sabe o que o time pensa da empresa."), 2),
 3: note(P(HL("Só que número não bate meta sozinho.")) + P("Quem vende é o vendedor. Quem entrega é a operação. Quem atende é quem está no balcão.", "font-size:46px")
        + P(I("Eu só faço resultado através de gente."), "font-size:46px"), 3),
 4: note(P(I("O seu funcionário passa oito horas por dia") + " na sua empresa. Às vezes, mais do que na própria casa.") + P(HL("O que ele encontra nessas oito horas?")), 4),
 5: note(P(I("O clima da sua empresa tem um concorrente.") + "<br>E não é a empresa da esquina.") + P(HL("É a casa do seu funcionário.")), 5),
 6: note(P(I("Se lá dentro é pior do que em casa,") + " ele vem pelo salário e vai embora na primeira proposta.") + P(HL("Ninguém fica onde não tem orgulho de estar.")), 6),
 7: note(P(I("Por isso festa não é besteira.") + " Na minha empresa tem festa junina, futebol toda terça e comemoração a cada aluno novo.", "font-size:46px")
        + P(HL("É assim que se constrói orgulho."), "font-size:46px"), 7),
 8: note(P(I("E time com orgulho") + " não trabalha só quando o dono está olhando.") + P(HL("Ele defende o resultado como se fosse dele.")), 8),
 9: note(P(I("Então me responde:")) + P(HL("na sua empresa, você cuida só do número ou também de quem faz o número?"), "margin-top:10px"), 9),
 10: note(P(I("Eu ensino a fazer resultado através de gente") + " no MBV, o meu treinamento de gestão pra donos de PME.")
        + '<div style="margin-top:50px"><span class="p">Comenta</span><br><span class="kw" style="margin-top:14px">ORGULHO</span></div>'
        + P("que eu mando o link no seu direct.", "margin-top:24px")
        + '<svg style="position:absolute;left:-30px;top:-95px" width="130" height="90" viewBox="0 0 130 90"><path d="M115 82L18 12m0 0v40m0-40h40" stroke="#F2F2F2" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'),
}
for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    (OUT/f"slide-{n:02d}.html").write_text(HEAD + S[n] + JS + '</body></html>', encoding="utf-8"); print(f"[{n:02d}] ok")
