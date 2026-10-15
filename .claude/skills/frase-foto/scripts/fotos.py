"""Lista as fotos do acervo em ordem de horário (EXIF) e gera uma folha de miniaturas numeradas.

uso:
  python3 .claude/skills/frase-foto/scripts/fotos.py                      # pasta Hélio/ do acervo (folha vai pra pasta temporária)
  python3 .claude/skills/frase-foto/scripts/fotos.py "<pasta>" folha.jpg   # outra pasta / outro nome de saída

Serve pra achar fotos do MESMO MOMENTO: na lista, fotos com segundos a poucos minutos de
diferença, no mesmo cenário, são da mesma sequência. A miniatura só serve pra achar a foto:
a escolha final é sempre olhando o arquivo em tamanho grande (careta e rosto cortado não aparecem na miniatura).
"""
import os, sys, tempfile
from PIL import Image, ImageOps, ImageDraw, ImageFont

ACERVO = os.path.expanduser('~/Desktop/fotos para carrosséis/Hélio')
VETADAS = {f'DSCF{n}' for n in range(3322, 3328)}  # quadro com os nomes antigos dos pilares (05/10)

pasta = sys.argv[1] if len(sys.argv) > 1 else ACERVO
saida = sys.argv[2] if len(sys.argv) > 2 else os.path.join(tempfile.gettempdir(), 'folha-fotos.jpg')
if not os.path.isdir(pasta):
    sys.exit(f'Pasta não encontrada: {pasta}\nO acervo de fotos não está no Git: copiar pra ~/Desktop/fotos para carrosséis/ antes de usar.')

fotos = []
for nome in os.listdir(pasta):
    if not nome.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue
    p = os.path.join(pasta, nome)
    try:
        im = Image.open(p)
        ex = im.getexif()
        dt = ex.get_ifd(0x8769).get(36867) or ex.get(306) or ''
        w, h = im.size
        if ex.get(274) in (5, 6, 7, 8):
            w, h = h, w
        fotos.append((dt or '9999', nome, p, w, h))
    except Exception as e:
        print('não abriu:', nome, e)
fotos.sort()

for i, (dt, nome, p, w, h) in enumerate(fotos, 1):
    forma = 'horizontal' if w > h else 'vertical'
    aviso = '  VETADA (pilares antigos)' if os.path.splitext(nome)[0].upper() in VETADAS else ''
    print(f'{i:3d}  {dt if dt != "9999" else "sem data":19s}  {forma:10s}  {nome}{aviso}')

# folha de miniaturas
T, COL = 260, 6
lin = (len(fotos) + COL - 1) // COL
folha = Image.new('RGB', (COL * T, lin * (T + 30)), 'white')
d = ImageDraw.Draw(folha)
try:
    fonte = ImageFont.load_default(size=18)
except TypeError:
    fonte = ImageFont.load_default()
for i, (dt, nome, p, w, h) in enumerate(fotos):
    im = Image.open(p); im.draft('RGB', (T * 2, T * 2))
    im = ImageOps.exif_transpose(im).convert('RGB'); im.thumbnail((T - 8, T - 8))
    x, y = (i % COL) * T, (i // COL) * (T + 30)
    folha.paste(im, (x + 4, y + 4))
    d.text((x + 6, y + T + 2), f'{i + 1}  {nome[:20]}', fill='black', font=fonte)
folha.save(saida, quality=85)
print(f'\nFolha de miniaturas: {saida} ({len(fotos)} fotos)')
