#!/usr/bin/env python3
"""J282 (Parabellum: cadê o dinheiro?), modelo fotos-reais. Fotos do próprio evento (22/10/2026),
salvas no acervo como Hélio/parabellum-2026-10-22_IMG_*.jpg. Tratamento, HEAD e JS do 220 (lib220.py).
Tudo em cor: o vermelho do telão do evento conversa com o carmim da marca."""
import pathlib, sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
exec((SCR/"lib220.py").read_text(encoding="utf-8"))
IMG = ROOT/"imagens/v1"; IMG.mkdir(parents=True, exist_ok=True); OUT = ROOT/"instagram"
F = pathlib.Path.home()/"Desktop/fotos para carrosséis"; R = F/"Hélio"
def ev(i): return R/f"parabellum-2026-10-22_IMG_{i}.jpg"
BK = "11,11,11"
def lg(d, *stops): return f"linear-gradient({d},{','.join(stops)})"
def c(a, p): return f"rgba({BK},{a}) {p}%"
# n: (foto, fx, fy, zoom)
PH = {
 1: (ev(5663), .45, .42, 1.0),
 2: (ev(5673), .45, .40, 1.0),
 3: (ev(5674), .50, .62, 1.0),
 4: (ev(5653), .50, .55, 1.0),
 5: (ev(5679), .50, .80, 1.35),
 6: (ev(5680), .45, .45, 1.0),
 7: (ev(5658), .50, .40, 1.0),
 8: (ev(5662), .50, .62, 1.0),
 9: (ev(5654), .55, .50, 1.0),
 10: (ev(5536), .50, .40, 1.0),
 11: (ev(5659), .50, .38, 1.0),
}
SHRINK = {10: .78}
def photo(n):
    src, fx, fy, z = PH[n]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    W, H = 1080, 1350
    sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    g = grade_color(im.crop((l, t, l+W, t+H)), n)
    if n in SHRINK:
        f = SHRINK[n]; sm = g.resize((round(W*f), round(H*f)), Image.LANCZOS)
        mask = Image.new("L", sm.size, 0); mk = Image.new("L", (sm.width-80, sm.height-80), 255)
        mask.paste(mk, (40, 40)); mask = mask.filter(ImageFilter.GaussianBlur(30))
        canvas = Image.new("RGB", (W, H), (11, 11, 11))
        canvas.paste(sm, ((W-sm.width)//2, H-sm.height-40), mask); g = canvas
    g.save(IMG/f"img-{n:02d}.png")
BASE = lambda a=34, b=50, d=58: lg("to bottom", c(0,0), c(0,a), c(.93,b), c(1,d))
TOP = lambda a=26, b=38, d=48: lg("to bottom", c(1,0), c(.93,a), c(.35,b), c(0,d), c(0,80), c(.5,100))
S = {
 1: (BASE(40, 56, 64),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="s fit" style="font-size:40px">Hoje eu estou no Parabellum, do Pedro Sobral,<br>numa sala cheia de empresário que fatura milhões.</div>'
     '<div class="big fit" style="font-size:52px;margin-top:28px">E a minha primeira pergunta vai ser:</div>'
     '<div style="margin-top:20px"><span class="hla" style="font-size:118px;line-height:1.1">CADÊ O DINHEIRO?</span></div></div>'),
 2: (BASE(36, 52, 60),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Eu saí da feira, onde limpava peixe,<br>e construí uma empresa que vendeu</div>'
     '<div class="s r" style="font-size:52px;line-height:1.15;margin-top:6px">mais de 9 bilhões em 4 continentes.</div>'
     '<div class="big" style="font-size:50px;margin-top:34px">Hoje eu levo pra esse palco o que<br>eu levei 38 anos pra aprender.</div></div>'),
 3: (TOP(30, 42, 52),
     '<div class="b" style="top:130px;left:100px;right:100px;text-align:center">'
     '<div class="lab">A regra nº 1</div>'
     '<div class="big" style="font-size:56px">Empresa foi feita pra colocar<br>dinheiro no bolso do dono.</div>'
     '<div class="s" style="margin-top:24px">Você arriscou tudo pra empreender no Brasil.</div>'
     '<div class="s" style="margin-top:18px"><span class="hl">A empresa existe pra te pagar por esse risco.</span><br><span class="hl">Não pra consumir a sua vida.</span></div></div>'),
 4: (BASE(36, 52, 60),
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s fit">Só que eu conheço muito dono que fatura milhões<br>e vive do mesmo pró-labore há dez anos.</div>'
     '<div class="s" style="margin-top:22px">A empresa cresceu, mudou de endereço,<br>dobrou o time.</div>'
     '<div class="a" style="font-size:74px;line-height:1.08;margin-top:26px">E o dono continua<br>ganhando a mesma coisa.</div></div>'),
 5: (TOP(44, 58, 68),
     '<div class="b" style="top:130px;left:110px;right:110px;text-align:center">'
     '<div class="s fit" style="font-size:42px">Você chega primeiro, sai por último<br>e perde o jantar com os seus filhos<br>pra apagar incêndio na empresa.</div>'
     '<div class="s" style="font-size:42px;margin-top:24px">No fim do ano, o contador<br>diz que deu lucro.</div>'
     '<div style="margin-top:26px"><span class="hla" style="font-size:66px;line-height:1.2">Mas o dinheiro não está</span><br><span class="hla" style="font-size:66px;line-height:1.2;margin-top:8px">na sua conta.</span></div></div>'),
 6: (BASE(42, 56, 64),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="big" style="font-size:56px">Eu sei como é,<br>porque eu já fui esse dono.</div>'
     '<div class="s" style="margin-top:24px">Durante anos eu resolvia tudo vendendo mais.</div>'
     '<div class="s r" style="font-size:50px;line-height:1.16;margin-top:18px">E vender mais nunca<br>foi o meu problema.</div></div>'),
 7: (BASE(40, 55, 62),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="big" style="font-size:66px">O problema é que<br>venda nenhuma conserta<br>uma empresa que o dono<br><span class="ul">não sabe ler.</span></div></div>'),
 8: (TOP(44, 56, 64),
     '<div class="b" style="top:130px;left:110px;right:110px;text-align:center">'
     '<div class="s">Enquanto entra muito dinheiro,<br>ninguém pergunta pra onde ele está indo.</div>'
     '<div class="big" style="font-size:58px;margin-top:22px">Até o dia em que entra menos.</div>'
     '<div class="s" style="margin-top:22px"><span class="hl">E aí o dono descobre que nunca soube</span><br><span class="hl">onde estava o dinheiro.</span></div></div>'),
 9: (BASE(38, 54, 62),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Então eu te faço a pergunta<br>que vou fazer pra eles hoje:</div>'
     '<div class="big" style="font-size:56px;margin-top:20px">você está mais rico<br>do que há cinco anos?</div>'
     '<div class="a" style="font-size:72px;line-height:1.08;margin-top:20px">Ou a empresa só<br>te deu mais trabalho?</div></div>'),
 10: (lg("to bottom", c(1,0), c(1,24), c(.6,34), c(0,44)),
     '<div class="b" style="top:120px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:46px">É isso que eu ensino pros empresários:</div>'
     '<div class="big" style="font-size:54px;margin-top:18px">ler a própria empresa, pra que o<br>dinheiro que ela gera <span class="r">chegue<br>no bolso do dono.</span></div></div>'),
 11: (BASE(42, 56, 64),
     '<div class="b" style="bottom:230px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:54px">Quer descobrir onde está<br>o dinheiro da sua empresa?</div>'
     '<div style="color:#F3F3F3;font-size:60px;font-weight:600;line-height:1.1;margin-top:36px">Comenta <span class="hla" style="font-size:96px;line-height:1.15;vertical-align:middle">SOBRAL</span></div>'
     '<div class="s" style="font-size:42px;margin-top:10px">que eu te mostro, no direct, como fazer isso.</div></div>'),
}
for n in ([int(x) for x in sys.argv[1:]] or S):
    photo(n); grad, body = S[n]
    html = HEAD + f'<div class="slide"><img class="ph" src="../imagens/v1/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div>' + JS + '</body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
