import pathlib, sys
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
def setup(scr):
    SCR = pathlib.Path(scr).parent; ROOT = SCR.parent
    IMG = ROOT/"imagens"; G = IMG/"_src"; OUT = ROOT/"instagram"; OUT.mkdir(exist_ok=True)
    F = next(p for p in (pathlib.Path.home()/"Desktop").iterdir() if p.name.startswith("fotos para"))
    R = next(d for d in F.iterdir() if d.name.startswith("H")); P = F/"publico"
    return IMG, G, OUT, R, P
def soft(im):
    g = ImageEnhance.Contrast(ImageOps.grayscale(im)).enhance(0.82)
    a = np.asarray(g).astype(np.float32)*0.92 + 14
    return Image.fromarray(a.clip(0, 255).astype(np.uint8)).convert("RGB")
def photo(IMG, n, src, fx, fy, z, raw):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    W, H = 1080, 1350; sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    im = im.crop((l, t, l+W, t+H)); (im if raw else soft(im)).save(IMG/f"img-{n:02d}.png")
BK = "11,11,11"
def lg(d, *stops): return f"linear-gradient({d},{','.join(stops)})"
def c(a, p): return f"rgba({BK},{a}) {p}%"
BASE = lg("to bottom", c(0,0), c(0,40), c(.93,56), c(1,64))
DIV = lg("to bottom", c(.96,0), c(.75,16), c(0,28), c(0,54), c(.92,68), c(1,78))
LAT_R = lg("to left", c(1,0), c(.95,40), c(.4,56), c(0,68)) + "," + lg("to bottom", c(0,70), c(.6,100))
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
def run(scr, PH, S, OFF={}):
    IMG, G, OUT, R, P = setup(scr)
    for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
        src = PH[n][0](R, P, G)
        if not src.exists(): print(f"[{n:02d}] falta {src.name}"); continue
        photo(IMG, n, src, *PH[n][1:]); grad, body = S[n]
        html = HEAD + f'<div class="slide"><img class="ph" style="top:{OFF.get(n,0)}px" src="../imagens/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div></body></html>'
        (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
