"""Recorta uma foto do acervo no tamanho da faixa (ou do post inteiro), sem mexer no Hélio.

uso (da raiz do projeto; P = conteudo/carrosseis/N_slug):
  python3 .claude/skills/frase-foto/scripts/prepara_foto.py "$HOME/Desktop/fotos para carrosséis/Hélio/<foto>" $P/imagens/foto-cima.jpg --tam 1080x675
opções:
  --tam LxA      tamanho final (1080x675 = meia altura; 1080x610 / 1080x740 = faixas do 185; 1080x450 = 3 faixas; 1080x1350 = foto única)
  --cx 0.5       centro do recorte na horizontal (0 = borda esquerda da foto, 1 = direita)
  --cy 0.4       centro do recorte na vertical (0 = topo, 1 = pé)
  --zoom 1.0     aproxima (2 = recorte com metade da largura da foto)
  --pb           converte pra preto e branco
  --contraste C  só com --pb (o 221 usou 1.15)
  --brilho B     padrão 0.93 (os finais usaram 0.92 a 0.95)

É o mesmo tratamento dos posts 217, 221 e 232: girar pelo EXIF, recortar, reduzir e escurecer um pouco.
Nada de IA aqui: o Hélio sai exatamente como o fotógrafo registrou.
"""
import sys
from PIL import Image, ImageOps, ImageEnhance

args = sys.argv[1:]
def opt(nome, padrao, tipo=float):
    if nome in args:
        i = args.index(nome); v = args[i + 1]; del args[i:i + 2]; return tipo(v)
    return padrao
pb = '--pb' in args
if pb: args.remove('--pb')
tam = opt('--tam', '1080x675', str); tw, th = map(int, tam.split('x'))
cx, cy, zoom = opt('--cx', 0.5), opt('--cy', 0.4), opt('--zoom', 1.0)
contraste, brilho = opt('--contraste', 1.0), opt('--brilho', 0.93)
src, out = args[0], args[1]

im = ImageOps.exif_transpose(Image.open(src)).convert('RGB'); W, H = im.size
cw = W / zoom; ch = cw * th / tw
if ch > H:
    ch = H; cw = ch * tw / th
x0 = min(max(cx * W - cw / 2, 0), W - cw); y0 = min(max(cy * H - ch / 2, 0), H - ch)
im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((tw, th), Image.LANCZOS)
if pb:
    im = ImageEnhance.Contrast(im.convert('L')).enhance(contraste).convert('RGB')
im = ImageEnhance.Brightness(im).enhance(brilho)
im.save(out, quality=93)
print('OK', out, f'{tw}x{th}')
