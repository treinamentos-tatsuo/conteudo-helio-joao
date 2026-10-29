# Fatia a arte em 9 posts 4:5 (1080x1350). A grade do perfil mostra cada post
# recortado em 3:4 (1012x1350, tira ~34 px de cada lado): a arte ocupa exatamente
# essas áreas visíveis e as bordas de 34 px trazem a continuação do vizinho.
import sys
from pathlib import Path
from PIL import Image

base = Path(__file__).resolve().parent
im = Image.open(base / "arte-original.webp").convert("RGB")
H, VIS = 4050, 3038  # 3 linhas x 1350; 3 colunas x 1012,67 (3:4)
im = im.resize((VIS, H), Image.LANCZOS)
PAD = 34
canvas = Image.new("RGB", (VIS + 2 * PAD, H))
canvas.paste(im, (PAD, 0))
# bordas externas: estica a última coluna de pixels (só aparece no feed, não na grade)
canvas.paste(im.crop((0, 0, 1, H)).resize((PAD, H)), (0, 0))
canvas.paste(im.crop((VIS - 1, 0, VIS, H)).resize((PAD, H)), (PAD + VIS, 0))
out = base.parent / "instagram"
col_w = VIS / 3
for r in range(3):
    for c in range(3):
        x = round(PAD + c * col_w + col_w / 2 - 540)
        tile = canvas.crop((x, r * 1350, x + 1080, (r + 1) * 1350))
        peca = r * 3 + c + 1
        post = 10 - peca  # posta de trás pra frente: a peça 9 (canto inferior direito) sai primeiro
        tile.save(out / f"post-{post}_peca-{peca}.png")
canvas.save(out / "mural-completo.png")
