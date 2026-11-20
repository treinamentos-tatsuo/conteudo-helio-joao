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
HD, HD2, SUB = 1020, 1190, 1400
# modo: fill = 9:16 cheio (cx fixo, ou pan de cx a cx2); wide = 16:9 sobre o proprio video desfocado
# vss = inicio do VIDEO quando a imagem vem de outro trecho que o audio (ss = inicio do audio)
CLIPS = [
    dict(f="9764", ss=1.5, to=6.2, cx=.38, vol=1.0, txt=[
        ("POV: você foi visitar o seu mentorado", 960, 0, 9, "h"),
        ("...e voltou com a feira da semana", 1150, 2.2, 9, "r")]),
    dict(f="9760", ss=3.3, to=6.6, cx=.50, vol=.6, txt=[
        ("Mas antes da feira...", HD, 0, 9, "h")]),
    dict(f="9757", ss=0.0, to=1.9, cx=.52, vol=.5, txt=[
        ("...teve número na mesa", HD, 0, 9, "r")]),
    dict(f="9765", ss=23.2, to=25.25, cx=.74, vol=.5, txt=[
        ("...teve número na mesa", HD, 0, 9, "r")]),
    dict(f="9760", ss=13.6, to=16.9, cx=.55, vol=.6, txt=[]),
    dict(f="9761", ss=70.0, to=73.6, cx=.60, vol=.6, txt=[
        ("Augusto, dono da Takaara", HD, 0.3, 9, "h")]),
    dict(f="9761", ss=74.6, to=76.6, cx=.30, cx2=.58, vol=.6, txt=[]),
    dict(f="9762", ss=2.3, to=7.0, cx=.40, cx2=.60, vol=1.0, txt=[
        ("Bastante sucesso.", SUB, 1.5, 3.3, "s"),
        ("Mais uma vez, parabéns!", SUB, 3.3, 9, "s")]),
    dict(f="9767", ss=16.5, to=22.8, cx=.40, vol=1.0, txt=[
        ("Vê o brilho nos olhos deles,", SUB, 0, 2.7, "s"),
        ("vê a expectativa de futuro.", SUB, 2.7, 5.3, "s"),
        ("É isso que paga tudo.", SUB, 5.3, 9, "sr")]),
    dict(f="9767", ss=38.0, to=43.6, vss=24.0, cx=.27, vol=1.0, txt=[
        ("Na visita anterior...", HD, 0, 9, "h"),
        ("Você lembra da última que ele estava?", SUB, 0, 2.5, "s"),
        ("Ele citou até que não via mais solução.", SUB, 2.5, 9, "s")]),
    dict(f="9767", ss=45.5, to=48.4, cx=.42, vol=1.0, txt=[
        ("Agora o cara enxergando...", SUB, 0, 9, "sr")]),
    dict(f="9766", ss=18.2, to=21.9, cx=.33, vol=1.0, txt=[
        ("Vai explodir de resultado o caixa dele.", SUB, 0, 9, "sr")]),
    dict(f="9764", ss=12.8, to=15.7, cx=.5, mode="wide", vol=.6, txt=[
        ("Takaara Frutas e Legumes", 480, 0, 9, "h"),
        ("Mentorado do MBV", 1330, 0.6, 9, "r")]),
]

STY = {"h": dict(size=62, bg=BLACK), "r": dict(size=62, bg=RED),
       "s": dict(size=50, bg=BLACK, font=FONT_B), "sr": dict(size=50, bg=RED, font=FONT_B)}

files = []
for i, c in enumerate(CLIPS):
    dur = round(c["to"] - c["ss"], 3)
    mov = os.path.join(SRC, f"IMG_{c['f']}.MOV")
    vss = c.get("vss", c["ss"])
    inputs = ["-ss", str(vss), "-t", str(dur), "-i", mov, "-ss", str(c["ss"]), "-t", str(dur), "-i", mov]
    if c.get("mode") == "wide":
        fc = [f"[0:v]split[a1][a2]",
              f"[a1]crop=1216:2160:1312:0,{TONE.format(w=1080, h=1920)},boxblur=40:2,eq=brightness=-0.12,fps=30,setsar=1[bg]",
              f"[a2]{TONE.format(w=1080, h=608)},fps=30,setsar=1[fg]",
              f"[bg][fg]overlay=0:656:shortest=1[b0]"]
    else:
        cx0, cx1 = c["cx"], c.get("cx2", c["cx"])
        xe = rf"clip(({cx0}+({cx1}-{cx0})*t/{dur})*3840-608\,0\,2624)"
        fc = [f"[0:v]crop=1216:2160:'{xe}':0,{TONE.format(w=1080, h=1920)},fps=30,setsar=1[b0]"]
    last = "b0"
    for j, (t, y, a, b, st) in enumerate(c["txt"]):
        p = text_png(f"c{i:02d}_{j}", t, y, **STY[st])
        inputs += ["-loop", "1", "-t", str(dur), "-i", p]
        fc.append(f"[{last}][{j+2}:v]overlay=0:0:enable='between(t,{a},{min(b - 0.04, dur)})'[b{j+1}]")
        last = f"b{j+1}"
    fc.append(f"[1:a]volume={c['vol']},afade=t=in:d=0.05,afade=t=out:st={max(dur-0.08,0)}:d=0.08[a]")
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
final = os.path.join(OUT, "pov-takaara-v2.mp4")
r = subprocess.run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                    "-movflags", "+faststart", final], capture_output=True, text=True)
print("FINAL", "OK" if r.returncode == 0 else r.stderr[-800:])
