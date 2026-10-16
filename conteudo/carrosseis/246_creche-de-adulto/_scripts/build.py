#!/usr/bin/env python3
"""Carrossel 246 (Empresa é creche de adulto), modelo fotos-reais. Base: build do 220 (CSS, pesos 400/600, base a 200 px).
Fotos do Hélio e da imersão CRUAS (só recorte e redimensionamento, como na v4 do 234: "só quando eu pedir").
Imagens geradas em P&B suave (sem curva em S, nitidez nem grão; como na v7 do 234: "cheias de filtro... muito pesada")."""
import pathlib, sys
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
IMG = ROOT/"imagens"; G = IMG/"_src"; OUT = ROOT/"instagram"; OUT.mkdir(exist_ok=True)
F = next(p for p in (pathlib.Path.home()/"Desktop").iterdir() if p.name.startswith("fotos para"))
R = next(d for d in F.iterdir() if d.name.startswith("H")); P = F/"publico"
# n: (fonte, fx, fy, zoom, cru?)  cru = foto real sem tratamento; senão P&B suave
PH = {
 1: (R/"DSCF3116.JPG", .5, .30, 1.0, True),
 2: (G/"gen-02.png", .5, .5, 1.0, False),
 3: (G/"gen-03.png", .5, .5, 1.0, False),
 4: (R/"DSCF3122.JPG", .5, .30, 1.0, True),
 5: (R/"MBV-TATSUOAC-240.jpg", .71, .40, 1.0, True),
 6: (R/"MBV-TATSUOAC-247.jpg", .5, .62, 1.1, True),
 7: (G/"gen-07.png", .5, .5, 1.0, False),
 8: (G/"gen-08.png", .5, .5, 1.0, False),
 9: (G/"gen-09.png", .5, .5, 1.0, False),
 10: (G/"gen-10.png", .5, .5, 1.0, False),
 11: (P/"MBV-TATSUOAC-190.jpg", .5, .0, 1.0, True),
 12: (R/"MBV-TATSUOAC-228.jpg", .45, .64, 1.15, True),
}
OFF = {12: -110}

def soft(im):
    g = ImageOps.grayscale(im)
    g = ImageEnhance.Contrast(g).enhance(0.82)
    a = np.asarray(g).astype(np.float32); a = a*0.92 + 14
    return Image.fromarray(a.clip(0, 255).astype(np.uint8)).convert("RGB")

def photo(n):
    src, fx, fy, z, raw = PH[n]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    W, H = 1080, 1350; sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    im = im.crop((l, t, l+W, t+H))
    (im if raw else soft(im)).save(IMG/f"img-{n:02d}.png")

BK = "11,11,11"
def lg(d, *stops): return f"linear-gradient({d},{','.join(stops)})"
def c(a, p): return f"rgba({BK},{a}) {p}%"
BASE = lg("to bottom", c(0,0), c(0,40), c(.93,56), c(1,64))
S = {
 1: (lg("to bottom", c(0,0), c(0,42), c(.9,58), c(1,68)),
     '<div class="b" style="bottom:200px;left:90px;right:90px;text-align:center">'
     '<div class="big" style="font-size:54px">Ninguém te avisa<br>quando você abre o CNPJ:</div>'
     '<div style="margin-top:22px;font-size:112px;line-height:1.22"><span class="hla">EMPRESA É</span><br><span class="hla">CRECHE DE ADULTO.</span></div></div>'),
 2: (lg("to bottom", c(.96,0), c(.75,16), c(0,28), c(0,54), c(.92,68), c(1,78)),
     '<div class="b" style="top:150px;left:110px;right:110px;text-align:center">'
     '<div class="s">Você treina o vendedor. Ele diz que entendeu<br>e repete tudo certinho.</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s r" style="font-size:52px;line-height:1.15">No dia seguinte, na frente do cliente,<br>faz tudo errado.</div></div>'),
 3: (BASE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Aí você reclama com o sócio no almoço<br>e manda um áudio de cinco minutos no grupo.</div>'
     '<div class="s" style="font-size:48px;margin-top:30px"><span class="hl">E treina de novo,</span><br><span class="hl">pra dar errado de novo.</span></div></div>'),
 4: (lg("to bottom", c(0,0), c(0,40), c(.9,55), c(1,63)),
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:46px">Em 38 anos de empresa, eu tenho<br>uma única certeza sobre treinamento:</div>'
     '<div class="s r" style="font-size:60px;line-height:1.14;margin-top:24px">depois dele, ninguém vai fazer<br>do jeito que foi ensinado.</div></div>'),
 5: (lg("to left", c(1,0), c(.95,40), c(.4,56), c(0,68)) + "," + lg("to bottom", c(0,70), c(.6,100)),
     '<div class="b" style="top:0;bottom:0;right:100px;width:500px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="s" style="font-size:46px">E não adianta<br>ser reclamão.</div>'
     '<div class="s" style="font-size:46px;margin-top:22px">Isso não é defeito<br>do seu time.</div>'
     '<div class="big" style="font-size:68px;margin-top:30px">É a vida<br>como ela é.</div></div>'),
 6: (lg("to bottom", c(0,0), c(0,50), c(.92,62), c(1,70)),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="s">Por isso eu digo sem vergonha nenhuma:</div>'
     '<div class="s" style="font-size:58px;line-height:1.5;margin-top:18px">dono de pequena empresa é<br><span class="hl">babá de adulto.</span></div></div>'),
 7: (BASE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Antigamente isso tinha nome: <b>pajear.</b><br>Hoje o nome bonito é <b>follow-up.</b></div>'
     '<div class="s r" style="font-size:52px;line-height:1.16;margin-top:30px">É acompanhar a execução<br>até ela virar hábito.</div></div>'),
 8: (lg("to bottom", c(.96,0), c(.75,18), c(0,30), c(0,52), c(.92,66), c(1,76)),
     '<div class="b" style="top:150px;left:110px;right:110px;text-align:center">'
     '<div class="s">E acompanhar não é passar no setor<br>quando sobra tempo.</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:56px">Rotina tem dia, hora e assunto.</div>'
     '<div class="s" style="font-size:44px;margin-top:26px">Se cada semana é de um jeito, não é rotina.<br><span class="hl">É visita.</span></div></div>'),
 9: (BASE,
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s">Enquanto você espera o time<br>que não precisa ser acompanhado,<br>a meta fura, o cliente reclama</div>'
     '<div class="s r" style="font-size:56px;line-height:1.15;margin-top:18px">e quem paga o retrabalho<br>é o seu caixa.</div></div>'),
 10: (lg("to bottom", c(.96,0), c(.8,22), c(0,34), c(0,54), c(.92,68), c(1,78)),
     '<div class="b" style="top:130px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:42px">Agora me responde:<br>quantas vezes nesta semana você sentou<br>com o seu time pra olhar o número?</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:44px">Se a resposta for nenhuma,</div>'
     '<div class="big" style="font-size:60px;margin-top:10px">a creche está sem<br><span class="r">adulto responsável.</span></div></div>'),
 11: (lg("to bottom", c(1,0), c(.95,34), c(.3,42), c(0,48), c(0,82), c(.6,100)),
     '<div class="b" style="top:120px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:52px">Eu ensino gestão pra donos de PME<br>no meu treinamento, o MBV:</div>'
     '<div class="s" style="font-size:46px;margin-top:18px"><b>Lucratividade, Crescimento e Cultura.</b></div>'
     '<div class="s" style="font-size:42px;margin-top:22px"><span class="hl">Porque é gestão que faz cada um</span><br><span class="hl">entregar o que foi combinado.</span></div></div>'),
 12: (lg("to bottom", c(0,0), c(0,46), c(.92,58), c(1,66)),
     '<div class="b" style="bottom:210px;left:100px;right:100px;text-align:center">'
     '<div class="big" style="font-size:52px">Quer parar de reclamar do time<br>e começar a ter resultado com ele?</div>'
     '<div style="color:#F3F3F3;font-size:60px;font-weight:600;line-height:1.1;margin-top:36px">Comenta <span class="hla" style="font-size:86px;line-height:1.15;vertical-align:middle">ENTREGA</span></div>'
     '<div class="s" style="font-size:40px;margin-top:8px">que eu mando o link no seu direct.</div></div>'),
}
HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,600;1,700&family=Anton&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0B0B0B;font-family:'Source Serif Pro',serif}
.ph{position:absolute;left:0;top:0;width:1080px}.shade{position:absolute;inset:0}.b{position:absolute;z-index:2}
.s{font-size:42px;line-height:1.32;font-weight:400;color:#F3F3F3}.s b{font-weight:600}
.big{font-size:64px;line-height:1.12;font-weight:600;color:#F3F3F3}
.r{color:#A91C20;font-weight:600}
.hla{font-family:'Anton',sans-serif;text-transform:uppercase;background:#A91C20;color:#F3F3F3;padding:0 22px;letter-spacing:.5px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hl{background:#A91C20;color:#F3F3F3;padding:2px 14px;-webkit-box-decoration-break:clone;box-decoration-break:clone;line-height:1.62}
</style></head><body>'''

for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    if not PH[n][0].exists(): print(f"[{n:02d}] falta a imagem {PH[n][0].name}"); continue
    photo(n); grad, body = S[n]
    html = HEAD + f'<div class="slide"><img class="ph" style="top:{OFF.get(n,0)}px" src="../imagens/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div></body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
