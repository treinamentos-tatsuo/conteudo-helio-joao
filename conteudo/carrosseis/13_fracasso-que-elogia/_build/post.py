#!/usr/bin/env python3
# post.py <raw> <dst>  — P&B garantido no pós + corta o quadrado inferior (sujeito baixo, topo pálido)
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("L").convert("RGB")   # dessatura sempre (gotcha do gpt-image-2)
w, h = im.size
side = min(w, h)
left = (w - side) // 2
top = h - side                                      # ancora no rodapé -> mantem topo palido, sujeito baixo
im = im.crop((left, top, left + side, top + side))
im.save(dst)
print("post", dst, im.size)
