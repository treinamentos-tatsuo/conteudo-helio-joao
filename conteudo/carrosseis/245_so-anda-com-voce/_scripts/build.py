#!/usr/bin/env python3
"""Carrossel 245 (a empresa que só anda com você), modelo fotos-reais.
Capa com foto real do Hélio (crua, só recorte, como na v4 do 234) e caixa carmim em Anton.
Slides 2 a 9 no estilo Notas do iPhone (referência: Marcos Freitas, DeWoVgSFqaz), adaptado à marca:
fundo branco, texto preto, cabeçalho e marca-texto em carmim #A91C20 no lugar do amarelo e do azul."""
import pathlib, sys
from PIL import Image, ImageOps
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
IMG = ROOT/"imagens"; IMG.mkdir(exist_ok=True); OUT = ROOT/"instagram"; OUT.mkdir(exist_ok=True)
F = next(p for p in (pathlib.Path.home()/"Desktop").iterdir() if p.name.startswith("fotos para"))
R = next(d for d in F.iterdir() if d.name.startswith("H"))
COVER = (R/"DSCF3116.JPG", .5, .40, 1.12)  # fonte, fx, fy, zoom

def cover_photo():
    src, fx, fy, z = COVER
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    W, H = 1080, 1350; sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    im.crop((l, t, l+W, t+H)).save(IMG/"img-01.png")

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
 2: note(P(I("Aí você viaja") + " com a família e o celular não para.")
        + P("O desconto grande espera você autorizar. A briga do gerente com o vendedor espera você voltar.")
        + P(HL("A empresa inteira fica esperando por você."))),
 3: note(P(I("Em casa,") + " ninguém pergunta mais se você vai conseguir desligar.")
        + P(HL("Os seus filhos já sabem que a viagem vai ser com você no telefone."))),
 4: note(P(I("Eu sei como é,") + " porque eu vivi isso.")
        + P("Cresci uma empresa achando que precisava estar em tudo.")
        + P(HL("Virei escravo do meu próprio negócio."))),
 5: note(P(I("E o problema") + " quase nunca é o time.")
        + P("Gente boa sem processo, sem número e sem acompanhamento faz o que dá.")
        + P(HL("O que não dá sobe pra mesa do dono."))),
 6: note(P("Eu aprendi uma regra que levo até hoje:")
        + '<div class="rule" style="margin:30px 0 34px">Delegai e vigiai.</div>'
        + P("Delegar é deixar claro o que fazer, como e quando. Vigiar é acompanhar o número todo dia, e não aparecer só quando o incêndio já começou.", "font-size:48px")),
 7: note(P(I("Agora me responde:") + " se você sumir 30 dias, a sua empresa vende, entrega e cobra sem você?")
        + P(HL("Se a resposta é não, você é o funcionário mais caro e mais preso da sua empresa."))),
 8: note(P(I("Eu juntei") + " o que aprendi em 38 anos num treinamento de 3 dias pra donos de PME: o MBV.")
        + P("Lá eu ensino gestão: " + HL("Lucratividade, Crescimento e Cultura."))),
 9: note(P(I("Quer uma empresa") + " que anda sem você do lado?")
        + '<div style="margin-top:44px"><span class="p">Comenta</span><br><span class="kw" style="margin-top:12px">DELEGAR</span></div>'
        + P("que eu mando o link no seu direct.", "margin-top:22px")),
}

def slide1():
    cover_photo()
    grad = "linear-gradient(to bottom,rgba(11,11,11,0) 0%,rgba(11,11,11,0) 44%,rgba(11,11,11,.88) 60%,rgba(11,11,11,1) 70%)"
    body = ('<div class="b" style="bottom:200px;left:90px;right:90px;text-align:center">'
            '<div class="big">Você tem 40 funcionários na folha</div>'
            '<div style="margin-top:22px;font-size:112px;line-height:1.22"><span class="hla">E NÃO TIRA</span><br><span class="hla">10 DIAS DE FÉRIAS.</span></div></div>')
    return (f'<div class="slide" style="background:#0B0B0B"><img class="ph" src="../imagens/img-01.png">'
            f'<div class="shade" style="background:{grad}"></div>{body}</div>')

# v2 (16/10, pedido do João): capa sem a foto do Hélio, só o texto em destaque, no mesmo estilo Notas.
# A capa com foto (v1) está em build_v1.py e instagram/_v1/.
S[1] = note(P(I("Você tem 40 funcionários") + " na folha", "font-size:76px;line-height:1.24")
            + P(HL("e não tira<br>10 dias de férias."), "font-size:76px;line-height:1.3;margin-top:40px;text-wrap:balance"))

for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    body = S[n]
    (OUT/f"slide-{n:02d}.html").write_text(HEAD + body + JS + '</body></html>', encoding="utf-8"); print(f"[{n:02d}] ok")
