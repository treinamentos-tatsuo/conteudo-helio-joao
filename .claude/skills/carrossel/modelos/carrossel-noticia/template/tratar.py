"""P&B com o vermelho preservado (puxado pro carmim). Uso: python tratar.py entrada saida"""
import sys
import numpy as np
from PIL import Image, ImageOps
src, dst = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
if max(im.size) > 2400:
    im.thumbnail((2400, 2400))
a = np.asarray(im).astype(np.float32) / 255
hsv = np.asarray(im.convert('HSV')).astype(np.float32) / 255
h, s, v = hsv[..., 0] * 360, hsv[..., 1], hsv[..., 2]
gray = (a @ np.array([0.299, 0.587, 0.114]))[..., None].repeat(3, 2)
gray = np.clip((gray - 0.5) * 1.15 + 0.5, 0, 1)  # um pouco mais de contraste
hue_ok = np.clip(1 - np.minimum(np.abs(h - 360), h) / 14, 0, 1)  # vermelho puro = 1
mask = hue_ok * np.clip((s - 0.35) / 0.25, 0, 1) * np.clip((v - 0.15) / 0.2, 0, 1)
carmim = np.array([0xA9, 0x1C, 0x20]) / 255
lum = gray[..., :1]
red = np.clip(carmim * (0.55 + 0.9 * lum), 0, 1)
out = gray * (1 - mask[..., None]) + red * mask[..., None]
Image.fromarray((out * 255).astype(np.uint8)).save(dst, quality=92)
