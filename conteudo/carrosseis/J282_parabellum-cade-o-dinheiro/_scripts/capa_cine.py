"""Capa J282: IMG_5663 com fundo escurecido, Hélio mais claro e grade cinematográfica (pedido do João, 22/10).
Máscara: imagens/_src/mask-5663.png (rembg u2net_human_seg). Saída: imagens/_src/capa-5663-cine.jpg"""
from PIL import Image, ImageOps, ImageFilter
import pathlib, numpy as np
ROOT=pathlib.Path(__file__).parent.parent
src=pathlib.Path.home()/"Desktop/fotos para carrosséis/Hélio/parabellum-2026-10-22_IMG_5663.jpg"
im=ImageOps.exif_transpose(Image.open(src)).convert("RGB")
m0=Image.open(ROOT/"imagens/_src/mask-5663.png").convert("L").point(lambda v:255 if v>128 else 0)
m=m0.filter(ImageFilter.MinFilter(17)).filter(ImageFilter.GaussianBlur(9))
core=np.asarray(m0.filter(ImageFilter.MinFilter(71))).astype(np.float32)[...,None]/255
k=np.asarray(m).astype(np.float32)[...,None]/255
a=np.asarray(im).astype(np.float32)/255
# vermelho saturado do telão perto da borda (fora do miolo do corpo) sai da máscara
red=((a[...,0]>.55)&(a[...,1]<.33)&(a[...,2]<.42)).astype(np.uint8)*255
red=np.asarray(Image.fromarray(red).filter(ImageFilter.MaxFilter(11)).filter(ImageFilter.GaussianBlur(5))).astype(np.float32)[...,None]/255
k=k*(1-red*(1-core))
bgi=np.asarray(im.filter(ImageFilter.GaussianBlur(16))).astype(np.float32)/255
g=bgi.mean(2,keepdims=True); bgi=(g+(bgi-g)*0.45)*0.16
h,w=a.shape[:2]; yy,xx=np.mgrid[0:h,0:w]
spot=np.exp(-(((xx-w*.45)/(w*.22))**2+((yy-h*.27)/(h*.16))**2))[...,None]
fg=np.clip(a*(1.18+0.18*spot)+0.02,0,1)
x=fg*k+bgi*(1-k)
x=0.5+0.5*np.tanh(2.1*(x-0.5))/np.tanh(1.05)
lum=x.mean(2,keepdims=True)
x=x+(1-lum)*np.array([-0.02,0.01,0.04])+lum*np.array([0.04,0.015,-0.03])
r=np.sqrt(((xx-w*.45)/(w*.6))**2+((yy-h*.32)/(h*.6))**2)
x*=(1-0.55*np.clip(r-0.45,0,1)**1.3)[...,None]
x+=np.random.default_rng(7).normal(0,0.012,x.shape)
Image.fromarray((np.clip(x,0,1)*255).astype('uint8')).save(ROOT/"imagens/_src/capa-5663-cine.jpg",quality=95)
