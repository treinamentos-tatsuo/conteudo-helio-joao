# Fatia a arte em 9 posts 4:5 (1080x1350). A grade do perfil mostra cada post
# recortado em 3:4 (1012x1350, tira ~34 px de cada lado): a área visível de cada
# post na grade é 1/9 da arte e as bordas de 34 px trazem a continuação do vizinho.
# Nas bordas externas do mural não há vizinho: a arte é ampliada até cobrir também
# essas faixas (só aparecem no feed), sem esticar nem espelhar pixel nenhum.
from pathlib import Path
from PIL import Image

base = Path(__file__).resolve().parent
im = Image.open(base / "arte-original.webp").convert("RGB")
# a arte vem com um fio claro de 1 px nas bordas: corta antes de ampliar
TRIM = 2
im = im.crop((TRIM, TRIM, im.width - TRIM, im.height - TRIM))

W, H = 3106, 3 * 1350  # 3 colunas 3:4 de 1012,5 px + as duas faixas externas de 34 px
esc = max(W / im.width, H / im.height)
im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
x0, y0 = (im.width - W) // 2, (im.height - H) // 2
canvas = im.crop((x0, y0, x0 + W, y0 + H))

out = base.parent / "instagram"
PAD = 34
col_w = (W - 2 * PAD) / 3
for r in range(3):
    for c in range(3):
        x = round(PAD + c * col_w + col_w / 2 - 540)
        tile = canvas.crop((x, r * 1350, x + 1080, (r + 1) * 1350))
        peca = r * 3 + c + 1
        post = 10 - peca  # posta de trás pra frente: a peça 9 (canto inferior direito) sai primeiro
        tile.save(out / f"post-{post}_peca-{peca}.png")
canvas.save(out / "mural-completo.png")
