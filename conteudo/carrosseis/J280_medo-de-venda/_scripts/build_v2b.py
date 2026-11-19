#!/usr/bin/env python3
"""J280 v2 (21/10, correções do João): o Hélio recortado sobre o fundo preto liso (sem nada atrás) em todo slide em que ele fala;
imagens geradas minimalistas nos outros (6, 7, 9); sombra leve no texto. v1 em build_v1.py e instagram/_v1/."""
import pathlib, sys
from PIL import Image
from _lib import lg, c, HEAD, soft
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
IMG = ROOT/"imagens"; CUT = IMG/"_cut"; G = IMG/"_src"; OUT = ROOT/"instagram"
W, H = 1080, 1350; BG = (11, 11, 11)

def figure(n, name, height, cx, top):
    """Cola o recorte do Hélio no fundo preto: altura do recorte em px, centro x, topo y (a cabeça)."""
    im = Image.open(CUT/f"{name}.png").convert("RGBA"); im = im.crop(im.getchannel("A").point(lambda a: 255 if a > 20 else 0).getbbox())
    sc = height/im.height; im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), BG); canvas.paste(im, (round(cx-im.width/2), top), im); canvas.save(IMG/f"img-{n:02d}.png")

PLACE = {7: (540, 640), 9: (540, 470)}   # v2b (pedido do João): o objeto centralizado nesses slides (centro x, centro y)

def gen(n):
    im = Image.open(G/f"gen-{n:02d}.png").convert("RGB"); sc = max(W/im.width, H/im.height)
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    if n in PLACE:
        import numpy as np
        from PIL import ImageFilter
        import json                                                  # centro do objeto achado pelo recorte (isnet-general-use), em obj_center.json
        fx, fy = json.load(open(SCR/"obj_center.json"))[str(n)]
        cx, cy = fx*im.width, fy*im.height; tx, ty = PLACE[n]
        mask = Image.new("L", im.size, 0); mask.paste(255, (120, 120, im.width-120, im.height-120)); mask = mask.filter(ImageFilter.GaussianBlur(90))
        canvas = Image.new("RGB", (W, H), BG); canvas.paste(im, (round(tx-cx), round(ty-cy)), mask)
        soft(canvas).save(IMG/f"img-{n:02d}.png"); return
    l = (im.width-W)//2; t = max(0, (im.height-H)//2); soft(im.crop((l, t, l+W, t+H))).save(IMG/f"img-{n:02d}.png")

# n: ("fig", recorte, altura, centro x, topo) ou ("gen",)
PH = {
 1: ("fig", "DSCF3122", 1650, 560, 110),
 2: ("fig", "0027", 1250, 820, 150),
 3: ("fig", "MBV-TATSUOAC-227", 1150, 500, 130),
 4: ("fig", "MBV-TATSUOAC-240", 1200, 110, 160),
 5: ("fig", "DSCF3116", 1600, 540, 110),
 6: ("gen",), 7: ("gen",),
 8: ("fig", "MBV-TATSUOAC-247", 1000, 540, 130),
 9: ("gen",),
 10: ("fig", "0009", 1450, 760, 120),
 11: ("fig", "MBV-TATSUOAC-228", 1150, 560, 150),
}
FADE = lg("to bottom", c(0,0), c(0,48), c(.88,62), c(1,70))
SIDE_L = lg("to right", c(1,0), c(.85,34), c(0,52)) + "," + lg("to bottom", c(0,70), c(.8,100))   # texto à esquerda
SIDE_R = lg("to left", c(1,0), c(.85,34), c(0,52)) + "," + lg("to bottom", c(0,70), c(.8,100))    # texto à direita
GENFADE = lg("to bottom", c(0,0), c(0,46), c(.9,60), c(1,68))
S = {
 1: (FADE,
     '<div class="b" style="bottom:200px;left:90px;right:90px;text-align:center">'
     '<div class="big" style="font-size:54px">Eu vendi mais de 9 bilhões<br>em 4 continentes.</div>'
     '<div style="margin-top:24px;font-size:112px;line-height:1.22"><span class="hla">HOJE EU TENHO</span><br><span class="hla">MEDO DE VENDA.</span></div></div>'),
 2: (SIDE_L,
     '<div class="b" style="top:0;bottom:0;left:90px;width:470px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="s" style="font-size:46px">Por muito tempo, eu resolvia tudo do mesmo jeito.</div>'
     '<div class="s" style="font-size:50px;margin-top:30px">O caixa apertou?<br><span class="r">Vende mais.</span></div>'
     '<div class="s" style="font-size:50px;margin-top:20px">A margem caiu?<br><span class="r">Vende mais.</span></div></div>'),
 3: (FADE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="s" style="font-size:46px">Cheguei a ter um escritório<br>de <b>2 mil metros quadrados.</b></div>'
     '<div class="s" style="font-size:48px;margin-top:26px"><span class="hl">E fretei avião pra levar</span><br><span class="hl">a equipe pra Europa.</span></div></div>'),
 4: (SIDE_R,
     '<div class="b" style="top:0;bottom:0;right:100px;width:480px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="big" style="font-size:56px">E o financeiro?</div>'
     '<div class="big r" style="font-size:66px;margin-top:6px">Desarrumado.</div>'
     '<div class="s" style="font-size:44px;margin-top:30px">Eu não sabia quanto sobrava de cada venda.</div></div>'),
 5: (FADE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="s" style="font-size:44px">Aí eu aprendi do jeito mais caro:<br>venda com a casa desarrumada<br>não resolve o problema.</div>'
     '<div class="big" style="font-size:72px;margin-top:20px">Ela acelera <span class="r">a merda.</span></div></div>'),
 6: (GENFADE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s" style="font-size:46px">Cada venda nova traz mais estoque,<br>mais prazo pro cliente<br>e mais gente na folha.</div>'
     '<div class="s r" style="font-size:54px;line-height:1.15;margin-top:26px">Se a margem já é ruim, você<br>só multiplica o prejuízo.</div></div>'),
 7: (lg("to bottom", c(.9,0), c(.6,16), c(0,26), c(0,50), c(.9,64), c(1,74)),
     '<div class="b" style="top:150px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:46px">Conheço dono que comemora<br>recorde de venda em dezembro</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:54px;line-height:1.5"><span class="hl">e em março vende o carro</span><br><span class="hl">pra pagar fornecedor.</span></div></div>'),
 8: (FADE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="s" style="font-size:44px">Por isso eu digo sem vergonha nenhuma:</div>'
     '<div class="big" style="font-size:60px;margin-top:14px">hoje eu tenho medo de venda.</div>'
     '<div class="s r" style="font-size:42px;margin-top:16px">Medo de vender sem saber quanto sobra.</div></div>'),
 9: (GENFADE,
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:62px">Primeiro arruma a casa:</div>'
     '<div class="s" style="font-size:52px;margin-top:10px">margem, custo e caixa.</div>'
     '<div class="s" style="font-size:52px;margin-top:30px"><span class="hl">Depois vai pra rua vender.</span></div></div>'),
 10: (SIDE_L,
     '<div class="b" style="top:0;bottom:0;left:100px;width:520px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="s" style="font-size:44px">Eu ensino gestão pra donos de PME no meu treinamento, o MBV:</div>'
     '<div class="big" style="font-size:50px;margin-top:20px">Lucratividade, Crescimento e Cultura.</div>'
     '<div class="s" style="font-size:44px;margin-top:26px"><span class="hl">Pra você vender sabendo o que fica no seu bolso.</span></div></div>'),
 11: (FADE,
     '<div class="b" style="bottom:210px;left:100px;right:100px;text-align:center">'
     '<div class="big" style="font-size:56px">Quer vender mais<br>sem ficar mais pobre?</div>'
     '<div style="color:#F3F3F3;font-size:62px;font-weight:600;line-height:1.1;margin-top:36px">Comenta <span class="hla" style="font-size:90px;line-height:1.15;vertical-align:middle">LUCRO</span></div>'
     '<div class="s" style="font-size:42px;margin-top:8px">que eu mando o link no seu direct.</div></div>'),
}
SHADOW = '<style>.b{text-shadow:0 2px 14px rgba(0,0,0,.85),0 0 3px rgba(0,0,0,.6)}</style>'
for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    k = PH[n]
    if k[0] == "fig":
        if not (CUT/f"{k[1]}.png").exists(): print(f"[{n:02d}] falta o recorte {k[1]}"); continue
        figure(n, *k[1:])
    else:
        if not (G/f"gen-{n:02d}.png").exists(): print(f"[{n:02d}] falta gen-{n:02d}"); continue
        gen(n)
    grad, body = S[n]
    html = HEAD.replace('</style>', '</style>'+SHADOW, 1) + f'<div class="slide"><img class="ph" src="../imagens/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div></body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
