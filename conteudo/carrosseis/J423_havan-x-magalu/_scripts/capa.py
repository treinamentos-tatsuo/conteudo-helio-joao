"""Capa J423: fachada Havan | fachada Magalu, com o azul das marcas preservado, e os donos em recorte P&B."""
import numpy as np, pathlib
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter
R = pathlib.Path(__file__).resolve().parent.parent / "imagens"
RAW = R / "_raw"
def brand(im, lo=150, hi=245):
    a = np.asarray(im.convert("RGB")).astype(np.float32)/255
    hsv = np.asarray(im.convert("HSV")).astype(np.float32)/255
    h,s,v = hsv[...,0]*360, hsv[...,1], hsv[...,2]
    g = (a @ np.array([.299,.587,.114]))[...,None].repeat(3,2); g = np.clip((g-.5)*1.15+.5,0,1)
    hue = np.clip(np.minimum(h-lo, hi-h)/12,0,1)
    m = (hue*np.clip((s-.42)/.15,0,1)*np.clip((v-.12)/.2,0,1))[...,None]
    return Image.fromarray(((g*(1-m)+a*m)*255).astype(np.uint8))
def bw(im):
    rgb, al = im.convert("RGB"), im.getchannel("A").point(lambda a: 255 if a>140 else 0).filter(ImageFilter.GaussianBlur(1.2))
    g = ImageOps.grayscale(rgb); g = g.point(lambda x: max(0,min(255,(x-128)*1.15+128)))
    out = Image.merge("RGBA",(g,g,g,al)); return out
def fit(im, w, h, cx=.5, cy=.5, z=1):
    s = max(w/im.width, h/im.height)*z; im = im.resize((round(im.width*s), round(im.height*s)), Image.LANCZOS)
    x = int((im.width-w)*cx); y = int((im.height-h)*cy); return im.crop((x,y,x+w,y+h))
W,H = 1080,900
c = Image.new("RGB",(W,H))
c.paste(brand(fit(Image.open(RAW/"h1.jpg"),540,H,.47,.95,1.45)),(0,0))
c.paste(brand(fit(Image.open(RAW/"m1.jpg"),540,H,1.0,.2,1.0)),(540,0))
c = c.convert("RGBA")
def put(cut, height, x_center, top):
    cut = cut.crop(cut.getbbox()); s = height/cut.height
    cut = bw(cut.resize((round(cut.width*s), height), Image.LANCZOS))
    sh = Image.new("RGBA", cut.size, (0,0,0,0)); sh.putalpha(cut.getchannel("A").point(lambda a: int(a*.55)))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    x = 12 if x_center is None else int(x_center - cut.width/2); c.alpha_composite(sh,(x+10,top+10)); c.alpha_composite(cut,(x,top))
put(Image.open(RAW/"v2_cut.png"), 500, 205, 200)
put(Image.open(RAW/"q1_cut.png"), 620, 915, 230)
d = ImageDraw.Draw(c)
d.rectangle((537,0,543,H), fill=(255,255,255,255))
cy, r = 110, 52
d.ellipse((540-r,cy-r,540+r,cy+r), fill=(0xA9,0x1C,0x20,255), outline=(255,255,255,255), width=5)
f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 54)
d.text((540,cy), "X", font=f, fill="white", anchor="mm")
c.convert("RGB").save(R/"img-01.jpg", quality=92); print("ok")
