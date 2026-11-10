#!/usr/bin/env python3
"""J360 v1 (10/11): modelo do J344 v3 (capa com foto + bilhete, slide preto, bloco de notas escuro, pergunta, CTA com foto)."""
import pathlib, sys
from PIL import Image, ImageOps
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent; IMG = ROOT/"imagens"; OUT = ROOT/"instagram"
IMG.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
F = next(p for p in (pathlib.Path.home()/"Desktop").iterdir() if p.name.startswith("fotos para"))
DIRS = {d.name[:2]: d for d in F.iterdir() if d.is_dir()}

def photo(n, folder, name, fx, fy, z=1.0):
    src = next(p for p in DIRS[folder].iterdir() if p.name.startswith(name))
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB"); W, H = 1080, 1350
    sc = max(W/im.width, H/im.height)*z; im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    im.crop((l, t, l+W, t+H)).save(IMG/f"img-{n:02d}.png")

HEAD = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0B0B0B;font-family:'Montserrat',sans-serif;color:#F3F3F3}
.ph{position:absolute;left:0;top:0;width:1080px}.shade{position:absolute;inset:0}.b{position:absolute;z-index:2}
.r{color:#A91C20}
.hl{background:#A91C20;color:#FFFFFF;padding:2px 12px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.sh{text-shadow:0 2px 16px rgba(0,0,0,.6)}
.note{font-family:'Caveat',cursive;font-weight:700;font-size:42px;line-height:1.05;color:#F3F3F3;transform:rotate(-6deg);text-align:right}
.lab{font-weight:600;font-size:22px;letter-spacing:6px;color:#8A8A8A;text-transform:uppercase}
.w9{font-weight:900;letter-spacing:-1.5px;line-height:1.05}.w7{font-weight:700;line-height:1.22;letter-spacing:-.3px}.w5{font-weight:500;line-height:1.4;color:#A8A8A8}
/* bloco de notas escuro */
.doc{background:#141414}
.bar{position:absolute;top:0;left:0;right:0;height:92px;border-bottom:1px solid #242424;display:flex;align-items:center;gap:30px;padding:0 110px;color:#5E5E5E;font-weight:700;font-size:24px}
.bar .sp{flex:1}.bar .dot{width:12px;height:12px;border-radius:50%;background:#A91C20}
.pg{position:absolute;top:150px;left:110px;right:110px;bottom:150px;display:flex;flex-direction:column;justify-content:center}
.t{font-weight:800;font-size:54px;line-height:1.12;letter-spacing:-.8px;margin-bottom:34px}
.t .n{color:#A91C20}
.p{font-weight:500;font-size:34px;line-height:1.45;color:#A8A8A8}
.p b{color:#F3F3F3;font-weight:700}
.pk{font-weight:700;font-size:38px;line-height:1.5;color:#F3F3F3;margin-top:22px}
.sec{font-weight:600;font-size:22px;letter-spacing:5px;color:#7A7A7A;text-transform:uppercase;margin:64px 0 26px}
.ck{display:flex;align-items:center;gap:22px;font-weight:500;font-size:34px;line-height:1.3;color:#E0E0E0;margin-bottom:22px}
.ck .bx{width:30px;height:30px;border:3px solid #A91C20;border-radius:6px;flex:none}
.ft{margin-top:70px;border-left:4px solid #A91C20;padding:4px 0 4px 26px;font-weight:600;font-size:32px;line-height:1.4;color:#E0E0E0}
.blank{display:inline-block;border-bottom:3px solid #A91C20;width:100px;margin:0 12px;transform:translateY(-6px)}
.go{position:absolute;bottom:70px;right:110px;font-size:36px;font-weight:600;color:#5E5E5E}
.hla{font-weight:900;background:#A91C20;color:#F3F3F3;padding:0 20px;letter-spacing:1px;display:inline-block}
</style></head><body>'''
BAR = ('<div class="bar"><span>B</span><span style="font-style:italic">I</span><span style="text-decoration:underline">U</span>'
       '<span>≡</span><span class="sp"></span><span class="dot"></span></div>')
def doc(body, arrow=True): return f'<div class="slide doc">{BAR}<div class="pg">{body}</div>' + ('<div class="go">→</div>' if arrow else '') + '</div>'
def ck(t): return f'<div class="ck"><span class="bx"></span><span>{t}</span></div>'
def lg(*s): return "linear-gradient(to bottom," + ",".join(s) + ")"

def li(t): return f'<div class="ck"><span style="color:#A91C20;font-weight:900">·</span><span>{t}</span></div>'
S = {
 1: ("photo", ("Hé", "MBV-TATSUOAC-228", .45, .40, 1.15),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 44%", "rgba(11,11,11,.85) 60%", "rgba(11,11,11,.98) 72%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:300px">'
     '<div class="w7" style="font-size:46px;color:#E6E6E6">Eu prefiro quem fala</div>'
     '<div class="w9" style="font-size:100px;margin-top:8px">&ldquo;pobrema&rdquo;</div>'
     '<div class="w7" style="font-size:46px;margin-top:18px;color:#E6E6E6">do que quem</div>'
     '<div class="w9" style="font-size:66px;margin-top:16px;text-shadow:none"><span class="hl">cria problema.</span></div></div>'
     '<div class="b" style="right:100px;bottom:110px;width:560px"><div class="note">Ninguém me <span class="r">enganou</span><br>na entrevista. →</div></div>'),
 2: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:48px">Demorei anos pra entender isso.</div>'
     '<div class="w5" style="font-size:38px;margin-top:40px">E aprendi do jeito mais caro:</div>'
     '<div class="w9" style="font-size:72px;margin-top:26px;line-height:1.4"><span class="hl">errando contratação.</span></div></div>'),
 3: ("doc", None, None,
     '<div class="t">Sempre que eu errava, o motivo era o mesmo.</div>'
     '<div class="pk">Eu tinha me encantado com <span class="hl">a pessoa errada.</span></div>'
     '<div class="sec">O que me encantava</div>'
     + li("fala bonita") + li("segurança na entrevista") + li("currículo bem montado") +
     '<div class="ft">Eu saía achando que tinha resolvido a minha vida.</div>'),
 4: ("doc", None, None,
     '<div class="t">Três meses depois, <span class="n">a conta chegava.</span></div>'
     + li("retrabalho que ninguém assumia") + li("cliente reclamando, e a culpa sempre de outro") + li("equipe incomodada") +
     '<div class="ft">Eu tinha contratado pra tirar peso das costas. E estava carregando <span class="hl">mais um problema.</span></div>'),
 5: ("doc", None, None,
     '<div class="t">Por muito tempo eu culpei a pessoa.</div>'
     '<div class="p" style="font-style:italic">&ldquo;Ela me enganou na entrevista.&rdquo;</div>'
     '<div class="pk" style="margin-top:70px">Ninguém me enganou.</div>'
     '<div class="pk" style="margin-top:10px"><span class="hl">Eu é que olhei pro lado errado.</span></div>'),
 6: ("doc", None, None,
     '<div class="t">Entrevista é o dia em que todo mundo está no seu melhor.</div>'
     '<div class="p">E eu avaliava justamente <b>o que dá pra ensaiar.</b></div>'
     '<div class="sec">Nunca perguntei</div>'
     + ck("como a pessoa reage quando erra") + ck("como trata quem está do lado") + ck("o que faz quando ninguém está olhando")),
 7: ("doc", None, None,
     '<div class="p">Algumas das melhores pessoas das minhas empresas falavam errado, não tinham diploma e tremiam na entrevista.</div>'
     '<div class="pk" style="margin-top:40px">Mas chegavam no horário, avisavam antes do problema estourar e <span class="hl">resolviam sem me chamar.</span></div>'
     '<div class="ft">Eu mesmo não tenho nem ensino médio. Cheguei aqui pelo comportamento, não pelo diploma.</div>'),
 8: ("doc", None, None,
     '<div class="t" style="margin-bottom:12px">Português a gente ensina.</div>'
     '<div class="t">Técnica a gente ensina.</div>'
     '<div class="pk" style="font-size:44px;line-height:1.55;margin-top:20px"><span class="hl">Comportamento, a pessoa traz de casa.</span></div>'
     '<div class="pk" style="font-size:44px;margin-top:4px">Ou não traz.</div>'
     '<div class="ft">O dono que não sabe o que procura contrata pela primeira impressão.</div>'),
 9: ("doc", None, None,
     '<div class="t">Contratação errada não é culpa do funcionário.</div>'
     '<div class="pk" style="margin-top:0"><span class="hl">Foi o dono que abriu a porta.</span></div>'
     '<div class="p" style="margin-top:40px">Se a sua empresa não tem claro o que valoriza, cada contratação vira aposta.</div>'
     '<div class="ft">Hoje eu não decido na entrevista. Eu vejo a pessoa trabalhando: como ela erra, como trata o colega, o que faz sozinha.</div>', False),
 10: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:48px">Olha pra sua equipe hoje.</div>'
     '<div class="w5" style="font-size:40px;margin-top:60px">Quantos estão aí porque</div>'
     '<div class="w9" style="font-size:72px;margin-top:10px">falavam bem,</div>'
     '<div class="w5" style="font-size:40px;margin-top:50px">e quantos porque</div>'
     '<div class="w9" style="font-size:72px;margin-top:10px;line-height:1.4"><span class="hl">resolvem?</span></div></div>'),
 11: ("photo", ("Hé", "mbv-recebido-2026-11-06_18", .5, .40),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 38%", "rgba(11,11,11,.85) 52%", "rgba(11,11,11,1) 60%"),
     '<div class="b" style="left:110px;right:110px;bottom:150px;text-align:center">'
     '<div class="w7" style="font-size:38px">Se essa pergunta te incomodou, o problema não é a equipe. É o que a sua empresa valoriza.</div>'
     '<div class="w5" style="font-size:30px;margin-top:24px">No MBV eu ensino o dono a montar<br>a cultura que escolhe quem entra.</div>'
     '<div style="margin-top:46px;font-weight:700;font-size:46px">Comenta <span class="hla" style="font-size:64px;line-height:1.25;vertical-align:middle">CULTURA</span></div>'
     '<div class="w5" style="margin-top:14px;font-size:30px">que eu mando o link no seu direct.</div></div>'),
}
OFF = {1: -330, 11: -120}
for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    v = S[n]; kind, ph, grad, body = v[:4]; arrow = v[4] if len(v) > 4 else True
    if kind == "doc":
        html = HEAD + doc(body, arrow) + '</body></html>'
    elif kind == "plain":
        html = HEAD + f'<div class="slide">{body}</div></body></html>'
    else:
        photo(n, *ph)
        html = HEAD + f'<div class="slide"><img class="ph" style="top:{OFF.get(n,0)}px" src="../imagens/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div></body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
