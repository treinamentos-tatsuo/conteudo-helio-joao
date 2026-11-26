"""Metades dos slides comparativos: recorta cada fachada com o NOME da loja centrado em (270, 600), em P&B com o azul da marca preservado."""
import pathlib
from PIL import Image
import numpy as np
def brand(im, vmax):
    a = np.asarray(im).astype(np.float32)/255
    hsv = np.asarray(im.convert("HSV")).astype(np.float32)/255
    h,s,v = hsv[...,0]*360, hsv[...,1], hsv[...,2]
    g = (a @ np.array([.299,.587,.114]))[...,None].repeat(3,2); g = np.clip((g-.5)*1.15+.5,0,1)
    hue = np.clip(np.minimum(h-150, 245-h)/12,0,1)
    m = (hue*np.clip((s-.42)/.15,0,1)*np.clip((v-.12)/.2,0,1)*np.clip((vmax-v)/.08,0,1))[...,None]
    return Image.fromarray(((g*(1-m)+a*m)*255).astype(np.uint8))
R = pathlib.Path(__file__).resolve().parent.parent / "imagens"; RAW = R / "_raw"
# nome: (arquivo, centro do letreiro em fração (x, y), largura do letreiro em fração da largura da foto, largura desejada em px)
SPEC = {
    "cmp2L": ("h6", (.59, .47), .17, 360), "cmp2R": ("m5", (.49, .155), .27, 420),
    "cmp3L": ("h5", (.446, .49), .09, 300), "cmp3R": ("m4", (.74, .60), .14, 340),
    "cmp4L": ("h2", (.17, .61), .09, 300), "cmp4R": ("m1", (.40, .22), .12, 130),
    "cmp5L": ("h1", (.54, .463), .10, 300), "cmp5R": ("m5", (.87, .25), .14, 300),
}
for out, (f, (fx, fy), lw, want) in SPEC.items():
    im = Image.open(RAW / f"{f}.jpg").convert("RGB")
    s = want / (lw * im.width)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    cx, cy = fx * im.width, fy * im.height
    x0 = min(max(round(cx - 270), 0), im.width - 540); y0 = round(cy - 600)
    can = Image.new("RGB", (540, 900), (10, 10, 10))
    mk = Image.new("L", im.size, 255)
    if y0 < 0:  # foto não chega no topo: funde a borda de cima no preto
        from PIL import ImageDraw
        dd = ImageDraw.Draw(mk)
        for k in range(160): dd.line((0, k, im.width, k), fill=int(255 * k / 160))
    can.paste(im, (-x0, -y0), mk)
    brand(can, .62 if f.startswith('h') else 1.2).save(R / f"{out}.jpg", quality=92); print(out, f, round(s, 2))
