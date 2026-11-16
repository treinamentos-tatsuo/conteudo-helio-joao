#!/usr/bin/env python3
"""J400 v2 (16/11): formato do J372/J367 (capa com foto + bilhete, preto, bloco de notas, foto no meio, preto, CTA com foto).
Fotos do acervo `fotos para carrosséis/Hélio/`: DSCF3076 (capa), SN-HOKEN-E-4 (slide 8), MBV-TATSUOAC-207 (CTA).
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
 1: ("photo", ("DSCF3076", .5, .40, 1.15),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 44%", "rgba(11,11,11,.85) 58%", "rgba(11,11,11,.98) 69%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:250px">'
     '<div class="w9" style="font-size:84px">1 cliente perdido.</div>'
     '<div class="w7" style="font-size:46px;margin-top:30px;color:#E6E6E6">Você ainda tem</div>'
     '<div class="w9" style="font-size:72px;margin-top:12px;line-height:1.3;text-shadow:none"><span class="hl">todos os outros.</span></div></div>'
     '<div class="b" style="right:100px;bottom:80px;width:600px"><div class="note">A perda fala mais alto<br>que o <span class="r">resto.</span> →</div></div>'),
 2: ("plain", None, None, PRETO(
     '<div class="w7" style="font-size:52px">Perda tem um defeito:</div>'
     '<div class="w9" style="font-size:66px;margin-top:40px;line-height:1.4"><span class="hl">ela fala mais alto que</span><br><span class="hl">tudo o que ficou.</span></div>')),
 3: ("doc", None, None,
     '<div class="t">O cliente que cancelou ocupa <span class="n">a semana inteira.</span></div>'
     + li("o dono liga, se explica, perde o sono") + li("ninguém lembra de quem continua comprando") + li("quem ficou é atendido no automático") +
     '<div class="ft"><span class="hl">Você ainda tem a carteira inteira.</span></div>'),
 4: ("doc", None, None,
     '<div class="t">1 funcionário pediu as contas.</div>'
     '<div class="p">Vira o assunto do mês. O time que ficou trabalhando quase não aparece.</div>'
     '<div class="pk" style="font-size:44px;margin-top:34px"><span class="hl">Você ainda tem o time</span><br><span class="hl">que ficou.</span></div>'
     '<div class="ft">E é esse time que está olhando como você reage.</div>'),
 5: ("doc", None, None,
     '<div class="t">1 mês no vermelho.</div>'
     + li("o dono corta o que não devia") + li("desiste do que estava dando certo") + li("trata um mês como se fosse o ano") +
     '<div class="ft"><span class="hl">Você ainda tem 11 pra virar o jogo.</span></div>'),
 6: ("doc", None, None,
     '<div class="t">No calor da perda, o dono toma <span class="n">as piores decisões.</span></div>'
     '<div class="p">Porque decide olhando pra um pedaço ruim como se fosse a empresa inteira.</div>'
     '<div class="pk" style="font-size:42px;margin-top:40px">O problema não é a perda.<br><span class="hl">É o tamanho que você dá pra ela.</span></div>'),
 7: ("doc", None, None,
     '<div class="t">Eu já passei por isso<br>muitas vezes.</div>'
     + li("faltou dinheiro") + li("faltou cliente") + li("faltou gente") +
     '<div class="ft">Quebra eu já tinha vivido.<br>Recuperação judicial, eu nunca imaginei viver.</div>'),
 8: ("photo", ("SN-HOKEN-E-4", .42, .45, 1.0),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 58%", "rgba(11,11,11,.98) 70%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:170px">'
     '<div class="w7" style="font-size:48px;color:#E6E6E6">Em 2020, a minha empresa entrou<br>em recuperação judicial.</div>'
     '<div class="w9" style="font-size:74px;margin-top:34px;line-height:1.3;text-shadow:none"><span class="hl">Em outubro,</span><br><span class="hl">ela fez 29 anos.</span></div></div>'),
 9: ("plain", None, None, PRETO(
     '<div class="w7" style="font-size:48px">O que separa quem atravessa<br>de quem para</div>'
     '<div class="w5" style="font-size:42px;margin-top:40px">não é sofrer menos.</div>'
     '<div class="w9" style="font-size:62px;margin-top:40px;line-height:1.4"><span class="hl">É enxergar o tamanho</span><br><span class="hl">real do problema.</span></div>')),
 10: ("doc", None, None,
     '<div class="t">E isso só dá pra fazer <span class="n">com número na mão.</span></div>'
     + li("quanto entrou") + li("quanto saiu") + li("quanto ainda tem") +
     '<div class="ft">Quem não sabe o tamanho do buraco<br><span class="hl">acha que todo buraco é o fim.</span></div>'),
 11: ("photo", ("MBV-TATSUOAC-207", .5, .463, 1.6),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 36%", "rgba(11,11,11,.85) 50%", "rgba(11,11,11,1) 58%"),
     '<div class="b" style="left:110px;right:110px;bottom:150px;text-align:center">'
     '<div class="w7" style="font-size:38px">Se hoje foi um dia ruim na sua empresa,<br>olha o que ainda está de pé<br>antes de decidir.</div>'
     '<div class="w5" style="font-size:30px;margin-top:24px">No MBV eu ensino o dono a ler a empresa<br>com número na mão.</div>'
     '<div style="margin-top:46px;font-weight:700;font-size:46px">Comenta <span class="hla" style="font-size:64px;line-height:1.25;vertical-align:middle">VIRADA</span></div>'
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
