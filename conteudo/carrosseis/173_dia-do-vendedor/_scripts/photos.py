#!/usr/bin/env python3
"""Prepara as fotos reais do Hélio pra faixa de baixo de cada slide: recorte pelo foco, P&B, contraste, grão.
Caixa: começa GAP px abaixo do texto (textbottom.json) e vai até 1350. Grava imagens/img-NN.png e box.json."""
import json, pathlib, random, sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
SCR = pathlib.Path(__file__).parent; IMG = SCR.parent/"imagens"
A = pathlib.Path.home()/"Desktop/fotos_album_2621284"; R = A/"recentes"
TB = {int(k): v for k, v in json.loads((SCR/"textbottom.json").read_text()).items()}
GAP = 30
def rec(p): return next(R.glob(p+"*"))
# n: (fonte, pré-recorte (l,t,r,b) ou None, foco x, foco y, zoom)
SRC = {
 1: (A/"Captura de Tela 2026-10-01 às 19.04.47.png", (0, 0, 690, 385), .5, .4, 1.0),
 2: (IMG/"_src/gen-02.png", None, .5, .75, 1.0),
 3: (A/"noticia_100388.jpg", None, .5, .35, 1.0),
 4: (A/"images.jpeg", None, .5, .45, 1.0),
 5: (IMG/"_src/gen-05.png", None, .5, .75, 1.0),
 6: (A/"helio-tatsuo-yotsui-fundador-da-franquia-hoken-1423773939609_615x300.jpg", None, .5, .3, 1.0),
 7: (rec("ARB0"), None, .72, .5, 1.0),
 8: (rec("0026"), None, .45, .42, 1.0),
 9: (rec("0016"), None, .3, .35, 1.0),
 10: (rec("0004"), None, .5, .6, 1.0),
 11: (rec("0019"), None, .45, .38, 1.0),
 12: (rec("0022"), None, .5, .45, 1.0),
 13: (A/"acqua.jpg", (0, 330, 1080, 1230), .5, .4, 1.0),
 14: (A/"file38168_3738c2c29540.jpeg", None, .45, .3, 1.0),
 15: (rec("0003"), None, .5, .32, 1.0),
 16: (rec("SN-HOKEN"), None, .5, .32, 1.0),
}
def prep(n):
    src, pre, fx, fy, z = SRC[n]
    if not src.exists(): print(f"[{n:02d}] fonte ausente: {src.name}"); return None
    im = Image.open(src).convert("RGB")
    if pre: im = im.crop(pre)
    top = TB[n] + GAP; W, H = 1080, 1350 - top
    s = max(W/im.width, H/im.height) * z
    im = im.resize((round(im.width*s), round(im.height*s)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width - W/2)), im.width - W); t = min(max(0, round(fy*im.height - H/2)), im.height - H)
    im = im.crop((l, t, l+W, t+H))
    g = ImageOps.grayscale(im); g = ImageOps.autocontrast(g, cutoff=1); g = ImageEnhance.Contrast(g).enhance(1.12)
    if s > 1.3: g = g.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))
    random.seed(n); px = g.load()
    for y in range(H):
        for x in range(W):
            v = px[x, y] + random.randint(-9, 9); px[x, y] = 0 if v < 0 else 255 if v > 255 else v
    g.save(IMG/f"img-{n:02d}.png"); print(f"[{n:02d}] {src.name[:30]} escala {s:.2f} caixa top {top} h {H}")
    return {"top": top, "h": H}
box = {}
try: box = {int(k): v for k, v in json.loads((SCR/"box.json").read_text()).items()}
except FileNotFoundError: pass
for n in ([int(a) for a in sys.argv[1:]] or SRC):
    r = prep(n)
    if r: box[n] = r
(SCR/"box.json").write_text(json.dumps(box, indent=1))
