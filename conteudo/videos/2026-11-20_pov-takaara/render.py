import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

FF = r"C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v9.0.2.exe"
SRC = r"C:\Users\DELL\Desktop\takaara"
OUT = sys.argv[1]
FONT_XB = r"C:\Users\DELL\AppData\Local\Microsoft\Windows\Fonts\Montserrat-ExtraBold.otf"
FONT_B = r"C:\Users\DELL\AppData\Local\Microsoft\Windows\Fonts\Montserrat-Bold.otf"
W, H = 1080, 1920
RED = (169, 28, 32, 255)
BLACK = (0, 0, 0, 235)
os.makedirs(os.path.join(OUT, "png"), exist_ok=True)
os.makedirs(os.path.join(OUT, "clips"), exist_ok=True)

TONE = ("zscale=w={w}:h={h}:t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
        "tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p")


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    return lines


def text_png(name, text, y, size=62, bg=BLACK, font=FONT_XB):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(font, size)
    lines = wrap(d, text, f, W - 160)
    lh = int(size * 1.32)
    for i, ln in enumerate(lines):
        tw = d.textlength(ln, font=f)
        x = (W - tw) / 2
        yy = y + i * lh
        d.rectangle([x - 22, yy - 10, x + tw + 22, yy + lh - 4], fill=bg)
        d.text((x, yy), ln, font=f, fill=(255, 255, 255, 255))
    p = os.path.join(OUT, "png", name + ".png")
    img.save(p)
    return p


# texto: (texto, y, inicio, fim, estilo)  estilo: "h" titulo preto, "r" titulo vermelho, "s" legenda, "sr" legenda vermelha
TOP, TOP2, SUB = 300, 470, 1330
# modo: fill = 9:16 cheio; band = quadrado no centro com fundo preto; wide = 16:9 no centro
CLIPS = [
    dict(f="9764", ss=1.5, to=6.2, cx=.38, mode="fill", vol=1.0, txt=[
        ("POV: seu mentor foi visitar a sua empresa", TOP, 0, 9, "h"),
        ("...e voltou com a feira da semana", TOP2, 2.2, 9, "r"),
        ("\"Minha feirinha é maior!\"", SUB, 2.7, 9, "s")]),
    dict(f="9759", ss=0, to=1.37, cx=.45, mode="fill", vol=.5, txt=[
        ("Mas antes da feira...", TOP, 0, 9, "h")]),
    dict(f="9757", ss=2.5, to=7.0, cx=.52, mode="fill", vol=.4, txt=[
        ("...teve número na mesa", TOP, 0, 9, "r")]),
    dict(f="9760", ss=13.6, to=16.9, cx=.55, mode="fill", vol=.6, txt=[]),
    dict(f="9761", ss=8.0, to=11.8, cx=.45, mode="band", vol=.6, txt=[
        ("Augusto, dono da Takaara", 270, 0, 9, "h")]),
    dict(f="9760", ss=46.0, to=49.3, cx=.50, mode="band", vol=.6, txt=[]),
    dict(f="9761", ss=45.0, to=47.5, cx=.55, mode="band", vol=.6, txt=[]),
    dict(f="9762", ss=2.3, to=7.0, cx=.55, mode="band", vol=1.0, txt=[
        ("Bastante sucesso.", 1440, 1.5, 3.3, "s"),
        ("Mais uma vez, parabéns!", 1440, 3.3, 9, "s")]),
    dict(f="9767", ss=16.5, to=22.8, cx=.40, mode="fill", vol=1.0, txt=[
        ("Vê o brilho nos olhos deles,", SUB, 0, 2.7, "s"),
        ("vê a expectativa de futuro.", SUB, 2.7, 5.3, "s"),
        ("É isso que paga tudo.", SUB, 5.3, 9, "sr")]),
    dict(f="9767", ss=40.6, to=42.9, cx=.42, mode="fill", vol=1.0, txt=[
        ("Na visita anterior...", TOP, 0, 9, "h"),
        ("...ele disse que não via mais solução.", SUB, 0, 9, "s")]),
    dict(f="9767", ss=45.5, to=48.4, cx=.42, mode="fill", vol=1.0, txt=[
        ("Agora o cara enxergando...", SUB, 0, 9, "sr")]),
    dict(f="9766", ss=4.3, to=8.3, cx=.33, mode="fill", vol=1.0, txt=[
        ("Mais um cliente satisfeito aqui, ó.", SUB, 0, 2.6, "s"),
        ("Takaara Hortifruti!", SUB, 2.6, 9, "s")]),
    dict(f="9766", ss=18.2, to=21.9, cx=.33, mode="fill", vol=1.0, txt=[
        ("Vai explodir de resultado o caixa dele.", SUB, 0, 9, "sr")]),
    dict(f="9764", ss=12.8, to=15.7, cx=.5, mode="wide", vol=.6, txt=[
        ("Takaara Frutas e Legumes", 440, 0, 9, "h"),
        ("Mentorado do MBV", 1330, 0.6, 9, "r")]),
]

STY = {"h": dict(size=62, bg=BLACK), "r": dict(size=62, bg=RED),
       "s": dict(size=50, bg=BLACK, font=FONT_B), "sr": dict(size=50, bg=RED, font=FONT_B)}

files = []
for i, c in enumerate(CLIPS):
    dur = round(c["to"] - c["ss"], 3)
    if c["mode"] == "fill":
        cw, ow, oh, oy = 1216, 1080, 1920, 0
    elif c["mode"] == "band":
        cw, ow, oh, oy = 2160, 1080, 1080, 420
    else:
        cw, ow, oh, oy = 3840, 1080, 608, 656
    x = int(min(max(c["cx"] * 3840 - cw / 2, 0), 3840 - cw)) // 2 * 2
    inputs = ["-ss", str(c["ss"]), "-t", str(dur), "-i", os.path.join(SRC, f"IMG_{c['f']}.MOV")]
    fc = [f"[0:v]crop={cw}:2160:{x}:0,{TONE.format(w=ow, h=oh)},fps=30,setsar=1[v]",
          f"color=black:s={W}x{H}:r=30:d={dur}[bg]",
          f"[bg][v]overlay=0:{oy}:shortest=1[b0]"]
    last = "b0"
    for j, (t, y, a, b, s) in enumerate(c["txt"]):
        p = text_png(f"c{i:02d}_{j}", t, y, **STY[s])
        inputs += ["-loop", "1", "-t", str(dur), "-i", p]
        fc.append(f"[{last}][{j+1}:v]overlay=0:0:enable='between(t,{a},{min(b, dur)})'[b{j+1}]")
        last = f"b{j+1}"
    fc.append(f"[0:a]volume={c['vol']},afade=t=in:d=0.05,afade=t=out:st={max(dur-0.08,0)}:d=0.08[a]")
    out = os.path.join(OUT, "clips", f"{i:02d}.mp4")
    cmd = [FF, "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", f"[{last}]", "-map", "[a]",
           "-t", str(dur), "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(i, c["f"], dur, "OK" if r.returncode == 0 else r.stderr[-800:], flush=True)
    files.append(out)

lst = os.path.join(OUT, "list.txt")
with open(lst, "w") as fh:
    for f in files:
        fh.write(f"file '{f}'\n")
final = os.path.join(OUT, "pov-takaara-v1.mp4")
r = subprocess.run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                    "-movflags", "+faststart", final], capture_output=True, text=True)
print("FINAL", "OK" if r.returncode == 0 else r.stderr[-800:])
