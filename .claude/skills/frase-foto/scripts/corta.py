"""Corta a imagem do image-edit (1024x1536) pro post (1080x1350) e salva um zoom do texto pra conferir a grafia.

uso (da raiz do projeto; P = conteudo/carrosseis/N_slug):
  python3 .claude/skills/frase-foto/scripts/corta.py $P/imagens/vidro-v1.png $P/instagram/vidro.png
  python3 .claude/skills/frase-foto/scripts/corta.py $P/imagens/papel-v1.png $P/instagram/papel-mesa.png
opções:
  --top N     onde começa o corte, em px da imagem original (padrão 45, o usado do 210 ao 228)
  --zoom Z    aproxima antes de cortar (o vidro do 210 saiu com --zoom 1.06 --top 160 pra subir o texto)

Além do post, grava <saida>-texto.png: só a área do texto, grande, pra ler letra por letra.
"""
import sys
from PIL import Image

args = sys.argv[1:]
def opt(nome, padrao):
    if nome in args:
        i = args.index(nome); v = float(args[i + 1]); del args[i:i + 2]; return v
    return padrao
top = int(opt('--top', 45)); zoom = opt('--zoom', 1.0)
src, out = args[0], args[1]

im = Image.open(src).convert('RGB'); W, H = im.size
h = round(W * 1350 / 1080)
x0 = 0
if zoom != 1.0:
    im = im.resize((round(W * zoom), round(H * zoom)), Image.LANCZOS)
    x0 = (im.size[0] - W) // 2
post = im.crop((x0, top, x0 + W, top + h)).resize((1080, 1350), Image.LANCZOS)
post.save(out)

# área do texto: no vidro fica à esquerda da emenda, acima do meio; no papel, no centro da folha
caixa = (60, 150, 1000, 980)
post.crop(caixa).resize((1880, 1660), Image.LANCZOS).save(out.rsplit('.', 1)[0] + '-texto.png')
print('OK', out, '+ zoom do texto em', out.rsplit('.', 1)[0] + '-texto.png')
