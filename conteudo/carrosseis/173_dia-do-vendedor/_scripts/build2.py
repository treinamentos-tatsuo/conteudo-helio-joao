#!/usr/bin/env python3
"""v2 do 173 (layout da referência do user, 01/10): foto P&B em tela cheia (ou no alto, quando a original é pequena),
escurecimento embaixo, texto centralizado nos 40% de baixo: serifa branca 44 + UM destaque em Anton carmim por slide.
Uso: python3 build2.py [n ...]  (processa foto + HTML)."""
import pathlib, sys
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent
IMG = ROOT/"imagens/v2"; IMG.mkdir(parents=True, exist_ok=True); OUT = ROOT/"instagram"
A = pathlib.Path.home()/"Desktop/fotos_album_2621284"; R = A/"recentes"
def rec(p): return next(R.glob(p+"*"))
G = ROOT/"imagens/_src"
# n: fonte, pré-recorte, modo ('full' tela cheia | 'top' largura cheia no alto), foco x, foco y, zoom, escurecimento (início, quase, total %)
P = {
 1: (A/"Captura de Tela 2026-10-01 às 19.04.47.png", (0,0,690,385), 'top', .5,.4,1, (18,38,44)),
 2: (G/"gen-02-v2.png", None, 'full', .5,.4,1, (40,58,70)),
 3: (A/"noticia_100388.jpg", None, 'top', .5,.4,1, (38,56,62)),
 4: (A/"images.jpeg", None, 'top', .5,.45,1, (30,46,52)),
 5: (G/"gen-05-v2.png", None, 'full', .5,.4,1, (38,56,68)),
 6: (A/"helio-tatsuo-yotsui-fundador-da-franquia-hoken-1423773939609_615x300.jpg", None, 'top', .5,.4,1, (20,36,42)),
 7: (rec("ARB0"), None, 'full', .7,.72,1.3, (40,58,70)),
 8: (rec("0026"), None, 'full', .5,.62,1.35, (40,62,74)),
 9: (rec("0016"), None, 'full', .32,.45,1.1, (40,60,72)),
 10: (rec("0028"), None, 'full', .74,.85,1.25, (40,58,70)),
 11: (rec("0019"), None, 'full', .45,.42,1.1, (40,60,72)),
 12: (rec("0022"), None, 'full', .5,.5,1, (40,58,70)),
 13: (A/"acqua.jpg", (0,40,1080,1350), 'full', .45,.66,1.4, (40,56,66)),
 14: (A/"file38168_3738c2c29540.jpeg", None, 'full', .45,.3,1, (40,58,70)),
 15: (rec("0003"), None, 'full', .5,.5,1.25, (42,60,72)),
 16: (rec("SN-HOKEN"), None, 'full', .5,.4,1, (40,56,66)),
}
def s(*l): return f'<div class="s">{"<br>".join(l)}</div>'
def a(*l, size=128): return f'<div class="a" style="font-size:{size}px">{"<br>".join(l)}</div>'
T = {
 1: s("Hoje é o Dia do Vendedor, e isso faz passar","um filme na minha cabeça, porque foi através","das vendas que eu saí da feira e me tornei","um empresário que vendeu") + a("MAIS DE 7 BILHÕES","DE REAIS.", size=118),
 2: s("Tudo isso me lembra o início da minha","carreira, antes de ser empresário.","Vendedor <i>only commission</i>,") + a("DE PORTA","EM PORTA,", size=140) + s("vendendo Barsa e Mirador."),
 3: s("Fiz mais de") + a("DEZ MIL","DEMONSTRAÇÕES,", size=132) + s("anotadas cliente por cliente.","Chegou um ponto em que, só no aperto","de mão do bom dia, eu já sabia","se ia vender ou não."),
 4: s("Tudo o que eu aprendi nessas portas","virou livro:") + a("VOCÊ NASCEU PARA","VENDER MUITO,", size=112) + s("best-seller da Veja e da PublishNews.","Escrevi pra mostrar que venda não é dom.","É técnica, e técnica se aprende."),
 5: s("Em") + a("1997", size=170) + s("eu abri o meu escritório em São José","do Rio Preto pra vender purificador","de água. Seiscentos reais de aluguel.","Quem vendia era eu. Quem atendia o telefone","e cuidava de todo o resto era a Regina,","minha esposa."),
 6: s("E por muito tempo eu achei que era isso","que fazia a empresa crescer:") + a("VENDER CADA","VEZ MAIS,", size=140) + s("aumentar o faturamento."),
 7: s("Eu era um vendedor excepcional.","Por isso a minha empresa","sempre faturou muito. E por isso mesmo") + a("SEMPRE PERDEU","MUITO DINHEIRO.", size=126),
 8: s("Porque eu era um") + a("ANALFABETO","EMPRESARIAL.", size=136) + s("Um vendedor que virou dono de empresa","sem nunca ter aprendido a ser empresário."),
 9: s("Todo problema de gestão","eu resolvia do mesmo jeito:") + a("VENDENDO MAIS.", size=130) + s("Tomava dois gols? Saía pra fazer dois."),
 10: s("E é o que a maioria dos donos","faz até hoje. Em vez de aprender gestão,","pensa em vender mais. Só que venda em cima","de empresa desarrumada","não resolve o problema.") + a("ACELERA.", size=170),
 11: s("Se eu soubesse lá atrás o que eu ensino hoje,","eu teria acumulado") + a("DEZ, TALVEZ","CEM VEZES MAIS", size=136) + s("do que eu acumulei."),
 12: s("Levei anos pra entender que vendedor","e empresário são") + a("PROFISSÕES","DIFERENTES.", size=140) + s("O vendedor resolve tudo vendendo.","O empresário cuida do lucro,","do crescimento e da cultura."),
 13: s("Quando eu aprendi, a empresa que começou","num escritório de seiscentos reais","passou a vender sem depender de mim.","O último presidente que eu contratei","pra tocar ela ganhava") + a("1,2 MILHÃO","POR ANO.", size=140),
 14: s("O moleque que saiu da feira e estudou","até os quinze fez MBA na FGV e hoje","ensina dono de empresa. E eu continuo","vendedor. Só que hoje eu vendo") + a("PENSANDO COMO","EMPRESÁRIO.", size=128),
 15: s("Tudo o que eu levei vinte e nove anos","pra aprender está no") + a("MBV,", size=190) + s("o meu treinamento pra dono de PME:","Lucratividade, Crescimento e Cultura.","A parte que a venda não resolve."),
 16: s("Feliz Dia do Vendedor.","Principalmente pra você, dono,","que ainda resolve tudo vendendo mais.","Quer aprender a parte","que a venda não resolve?") + a("COMENTA MBV", size=150) + s("que eu te mando no direct","o link da próxima turma."),
}
HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,600&family=Anton&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0B0B0B;font-family:'Source Serif Pro',serif}
.ph{position:absolute;left:0;top:0;width:1080px}
.shade{position:absolute;inset:0}
.txt{position:absolute;left:0;right:0;bottom:110px;padding:0 70px;text-align:center}
.s{font-size:44px;line-height:1.28;font-weight:600;color:#F3F3F3}
.a{font-family:'Anton',sans-serif;color:#A91C20;text-transform:uppercase;line-height:1.02;letter-spacing:.5px;margin:12px 0 16px}
.a:last-child{margin-bottom:0}.a:first-child{margin-top:0}
</style></head><body>'''
LIFT = {}
def photo(n):
    src, pre, mode, fx, fy, z, _ = P[n]
    im = Image.open(src).convert("RGB")
    if pre: im = im.crop(pre)
    W = 1080; H = 1350 if mode == 'full' else round(im.height*W/im.width)
    sc = max(W/im.width, H/im.height)*z
    im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    g = ImageOps.grayscale(im.crop((l, t, l+W, t+H))); g = ImageOps.autocontrast(g, cutoff=1); g = ImageEnhance.Contrast(g).enhance(1.1)
    if n in LIFT: g = g.point(lambda v: round(255*((v/255)**LIFT[n])))
    if sc > 1.3: g = g.filter(ImageFilter.UnsharpMask(radius=2, percent=50, threshold=3))
    g.save(IMG/f"img-{n:02d}.png"); return sc
import json
try: TOP = {int(k): v for k, v in json.loads((SCR/"texttop.json").read_text()).items()}
except FileNotFoundError: TOP = {}
for n in ([int(x) for x in sys.argv[1:]] or P):
    if not P[n][0].exists(): print(f"[{n:02d}] sem fonte ainda"); continue
    sc = photo(n); a0, a1, a2 = P[n][6]
    if n in TOP:  # escurecimento ancorado no topo real do texto
        tt = TOP[n]; a0, a1, a2 = [round(v/13.5, 1) for v in (tt-320, tt-70, tt+30)]
        if P[n][2] == 'top':  # foto no alto: nunca deixar a borda de baixo da foto aparecer
            hb = Image.open(IMG/f"img-{n:02d}.png").height/13.5; a2 = min(a2, round(hb-1, 1)); a1 = min(a1, a2-4); a0 = min(a0, a1-14)
    shade = f"background:linear-gradient(to bottom,rgba(11,11,11,0) 0%,rgba(11,11,11,0) {a0}%,rgba(11,11,11,.9) {a1}%,#0B0B0B {a2}%)"
    html = HEAD + f'<div class="slide"><img class="ph" src="../imagens/v2/img-{n:02d}.png"><div class="shade" style="{shade}"></div><div class="txt">{T[n]}</div></div></body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html); print(f"[{n:02d}] escala {sc:.2f}")
