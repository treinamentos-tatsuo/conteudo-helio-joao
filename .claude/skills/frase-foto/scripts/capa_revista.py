"""Monta as duas camadas da "capa de revista" (191, feira): fundo escurecido + Hélio recortado por cima do texto.

É o código que gerou o 191 final (06/10), só com nomes de arquivo genéricos. Não gera nada por IA:
a foto é a real; o fundo continua lá (escurecido, com luz vinda de cima), nunca vira preto chapado.

comandos da raiz do projeto (F = .claude/skills/frase-foto, P = conteudo/carrosseis/N_slug):
passo 1 (máscara do Hélio, Vision do macOS):
  swift $F/scripts/lift.swift $P/imagens/foto.jpg $P/imagens/recorte.png
passo 2:
  python3 $F/scripts/capa_revista.py $P/imagens/foto.jpg $P/imagens/recorte.png $P/imagens
  opcional: --objeto $P/imagens/mascara-objeto.png  (máscara branca do objeto que fica em vermelho #A91C20; no 191 foi o peixe)
saída: $P/imagens/base.jpg (vai atrás do texto) e $P/imagens/sujeito.png (vai na frente), usadas no templates/a-capa-revista.html

Precisa de Pillow, numpy e opencv-python.
"""
import sys
import numpy as np, cv2
from PIL import Image, ImageFilter

args = sys.argv[1:]
obj = None
if '--objeto' in args:
    i = args.index('--objeto'); obj = args[i + 1]; del args[i:i + 2]
foto, recorte, pasta = args[0], args[1], args[2].rstrip('/')

np.random.seed(11)
rgb = np.array(Image.open(foto).convert('RGB')).astype(float); Hh, Ww = rgb.shape[:2]
L = 0.15 * rgb[..., 0] + 0.55 * rgb[..., 1] + 0.30 * rgb[..., 2]
pm = Image.open(recorte).split()[3]
person = np.array(pm.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(2.5))).astype(float) / 255
g = np.clip((L - 10) * 1.08, 0, 255)                      # preto e branco com contraste
subj = np.repeat(g[..., None], 3, 2)
if obj:                                                    # cor seletiva só no objeto, no vermelho da marca
    mm = (cv2.imread(obj, 0) > 128).astype(float)
    fish = cv2.GaussianBlur(mm, (0, 0), 2)
    car = np.array([169, 28, 32]) / 255.0; t = (g / 255)[..., None]
    col = np.where(t < 0.5, 2 * t * car, 1 - 2 * (1 - t) * (1 - car)); col = (col * 0.8 + t * 0.2) * 255
    subj = subj * (1 - fish[..., None]) + col * fish[..., None]
yy, xx = np.mgrid[0:Hh, 0:Ww]                              # luz direcional de cima-esquerda
light = np.clip(1.0 - 0.75 * np.sqrt(((xx - Ww * 0.35) / (Ww * 0.9)) ** 2 + ((yy - Hh * 0.2) / (Hh * 0.8)) ** 2), 0.15, 1)
bg = np.repeat((g * 0.30)[..., None], 3, 2) * light[..., None]   # ambiente original a ~30%
a = person[..., None]; noise = np.random.normal(0, 4, subj.shape)  # grão une as camadas
Image.fromarray((subj * a + bg * (1 - a) + noise).clip(0, 255).astype('uint8')).save(f'{pasta}/base.jpg', quality=94)
Image.fromarray(np.dstack([subj + noise, person * 255]).clip(0, 255).astype('uint8')).save(f'{pasta}/sujeito.png')
print('OK', f'{pasta}/base.jpg', f'{pasta}/sujeito.png')
