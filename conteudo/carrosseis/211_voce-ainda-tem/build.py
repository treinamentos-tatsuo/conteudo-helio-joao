from PIL import Image, ImageOps, ImageEnhance
import json,sys
b="/Users/pedrohenrique/Desktop/fotos para carrosséis/Hélio/"
# (arquivo, cx, cy, zoom) — centro do recorte em fração e zoom (1 = largura toda)
S=json.load(open('slides.json'))
for i,s in enumerate(S,1):
    im=ImageOps.exif_transpose(Image.open(b+s['f'])).convert('RGB'); W,H=im.size
    cw=W/s['z']; ch=cw*675/1080
    if ch>H: ch=H; cw=ch*1080/675
    x0=min(max(s['cx']*W-cw/2,0),W-cw); y0=min(max(s['cy']*H-ch/2,0),H-ch)
    c=im.crop((round(x0),round(y0),round(x0+cw),round(y0+ch))).resize((1080,675),Image.LANCZOS)
    col=ImageEnhance.Color(c).enhance(1.05)
    g=ImageEnhance.Contrast(ImageOps.grayscale(c)).enhance(1.08).convert('RGB')
    g.save(f'imagens/s{i}-pb.jpg',quality=93); col.save(f'imagens/s{i}-cor.jpg',quality=93)
