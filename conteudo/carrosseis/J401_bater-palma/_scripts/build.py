#!/usr/bin/env python3
"""J401 v1 (17/11): formato do J400/J372 (capa com foto + bilhete, preto, bloco de notas, foto no meio, preto, CTA com foto).
Fotos do acervo `fotos para carrosséis/Hélio/` (lote do MBV de 06/11): _07 (capa), _10 (slide 8), _19 (CTA).
O CSS e os helpers (HEAD, doc, li, lg) vêm do J360, em _css.py."""
import pathlib, sys
from PIL import Image, ImageOps
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent; IMG = ROOT/"imagens"; OUT = ROOT/"instagram"
ACV = pathlib.Path.home()/"Desktop"/"fotos para carrosséis"/"Hélio"
IMG.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
exec((SCR/"_css.py").read_text(encoding="utf-8"))

def photo(n, name, fx, fy, z=1.0):
    src = next(p for p in ACV.iterdir() if p.name.startswith(name))
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB"); W, H = 1080, 1350
    sc = max(W/im.width, H/im.height)*z; im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    im.crop((l, t, l+W, t+H)).save(IMG/f"img-{n:02d}.png")

PRETO = lambda body: ('<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">' + body + '</div>')
S = {
 1: ("photo", ("mbv-recebido-2026-11-06_07", .62, .53, 1.45),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 44%", "rgba(11,11,11,.85) 58%", "rgba(11,11,11,.98) 69%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:240px">'
     '<div class="w7" style="font-size:48px;color:#E6E6E6">Você vê cada erro<br>do seu funcionário.</div>'
     '<div class="w9" style="font-size:58px;margin-top:30px;line-height:1.35;text-shadow:none"><span class="hl">Quando foi a última vez</span><br><span class="hl">que bateu palma pra ele?</span></div></div>'
     '<div class="b" style="right:100px;bottom:80px;width:600px"><div class="note">Liderar também<br>é <span class="r">isso.</span> →</div></div>'),
 2: ("plain", None, None, PRETO(
     '<div class="w7" style="font-size:52px">Líder, muitas vezes, tem que<br>confiar na pessoa</div>'
     '<div class="w9" style="font-size:66px;margin-top:40px;line-height:1.4"><span class="hl">mais do que ela</span><br><span class="hl">mesma confia.</span></div>')),
 3: ("doc", None, None,
     '<div class="t">Liderança é<br><span class="n">80% do seu tempo.</span></div>'
     '<div class="p" style="margin-bottom:26px">Todo dia, o tempo todo, toda hora.</div>'
     + li("alguém chega atrasado e desrespeita o tempo do outro") + li("alguém entrega um trabalho malfeito") + li("alguém deixa de entregar") +
     '<div class="ft">Ninguém entrega o tempo todo.<br>Todo mundo falha um dia.</div>'),
 4: ("doc", None, None,
     '<div class="t">E aí você vai ter que corrigir.</div>'
     '<div class="p">Vai ter que ensinar. Vai ter que cobrar. Faz parte da liderança.</div>'
     '<div class="pk" style="font-size:44px;margin-top:40px">Se você não gosta<br>de fazer isso tudo,<br><span class="hl">você não é líder.</span></div>'),
 5: ("doc", None, None,
     '<div class="t">Mas tem uma parte que <span class="n">quase todo dono esquece.</span></div>'
     '<div class="p" style="margin-bottom:26px">Todo mundo também faz coisa boa.</div>'
     + li("o vendedor que segurou o cliente difícil") + li("quem ficou até mais tarde sem ninguém pedir") + li("quem resolveu um problema sozinho") +
     '<div class="ft"><span class="hl">Você está prestando atenção pra aplaudir?</span></div>'),
 6: ("doc", None, None,
     '<div class="t">Quem só olha o ruim <span class="n">acaba com a autoestima do time.</span></div>'
     '<div class="p">Errou, leva bronca. Acertou, ninguém fala nada.</div>'
     '<div class="pk" style="font-size:44px;margin-top:34px">A pessoa aprende que ali<br><span class="hl">só existe o erro.</span></div>'
     '<div class="ft">E gente que não acredita em si não arrisca, não decide e não cresce.</div>'),
 7: ("doc", None, None,
     '<div class="t">Bater palma não é<br>passar a mão na cabeça.</div>'
     + li("corrige o que está errado") + li("aplaude o que está certo") + li("as duas coisas, toda semana") +
     '<div class="ft">É aí que a pessoa pensa:<br><span class="hl">"cara, eu sou bom? Eu posso?"</span></div>'),
 8: ("photo", ("mbv-recebido-2026-11-06_10", .45, .52, 1.25),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 58%", "rgba(11,11,11,.98) 70%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:160px">'
     '<div class="w7" style="font-size:46px;color:#E6E6E6">Liderança é quase igual a pai e mãe.<br>Está ali pra fazer a pessoa<br>ficar grandona.</div>'
     '<div class="w9" style="font-size:68px;margin-top:34px;line-height:1.3;text-shadow:none"><span class="hl">Ao ponto de não</span><br><span class="hl">precisar mais de você.</span></div></div>'),
 9: ("plain", None, None, PRETO(
     '<div class="w7" style="font-size:50px">Pensa no seu time agora:</div>'
     '<div class="w5" style="font-size:44px;margin-top:40px">quem você corrigiu essa semana?</div>'
     '<div class="w9" style="font-size:72px;margin-top:40px;line-height:1.4"><span class="hl">E quem você aplaudiu?</span></div>')),
 10: ("photo", ("mbv-recebido-2026-11-06_19", .5, .40, 1.5),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 36%", "rgba(11,11,11,.85) 50%", "rgba(11,11,11,1) 58%"),
     '<div class="b" style="left:110px;right:110px;bottom:150px;text-align:center">'
     '<div class="w7" style="font-size:38px">Time grande não nasce pronto.<br>É feito por um líder que corrige e aplaude,<br>toda semana.</div>'
     '<div class="w5" style="font-size:30px;margin-top:24px">No MBV eu ensino gestão pra dono de empresa,<br>inclusive gestão de pessoas, cultura e liderança.</div>'
     '<div style="margin-top:46px;font-weight:700;font-size:46px">Comenta <span class="hla" style="font-size:64px;line-height:1.25;vertical-align:middle">GRANDE</span></div>'
     '<div class="w5" style="margin-top:14px;font-size:30px">que eu mando o link no seu direct.</div></div>'),
}
NOARROW = set()
for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    kind, ph, grad, body = S[n]
    if kind == "doc":
        html = HEAD + doc(body, n not in NOARROW) + '</body></html>'
    elif kind == "plain":
        html = HEAD + f'<div class="slide">{body}</div></body></html>'
    else:
        photo(n, *ph)
        html = HEAD + f'<div class="slide"><img class="ph" style="top:0" src="../imagens/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div></body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
