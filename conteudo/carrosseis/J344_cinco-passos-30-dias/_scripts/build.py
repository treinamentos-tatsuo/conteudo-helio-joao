#!/usr/bin/env python3
"""J344 v3 (09/11, correção do João: "o carrossel está muito poluído, fonte menor, trabalhar melhor espaços negativos,
fundo de texto para destaque"). Fonte menor, margens e respiros maiores, um destaque por slide, marca-texto carmim atrás
do texto no lugar das etiquetas e das caixas cinza, nota de rodapé com fio carmim fino. v2 em build_v2.py e instagram/_v2b/.
Montserrat (fonte da marca) + Caveat no bilhete. Preto, branco e #A91C20."""
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

S = {
 1: ("photo", ("Hé", "MBV-TATSUOAC-227", .47, .62, 1.12),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 44%", "rgba(11,11,11,.85) 60%", "rgba(11,11,11,.98) 72%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:290px">'
     '<div class="w9" style="font-size:100px">Eu DUVIDO</div>'
     '<div class="w7" style="font-size:42px;margin-top:16px;color:#E6E6E6">você fazer isso aqui e não descobrir<br>onde a sua empresa</div>'
     '<div class="w9" style="font-size:66px;margin-top:20px;text-shadow:none"><span class="hl">perde dinheiro.</span></div></div>'
     '<div class="b" style="right:100px;bottom:110px;width:560px"><div class="note">Só o <span class="r">passo 3</span> já vale<br>o seu tempo aqui. →</div></div>'),
 2: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="lab">Apresento</div>'
     '<div class="w9" style="font-size:66px;margin-top:34px">O plano de <span class="r">5 passos</span></div>'
     '<div class="w5" style="font-size:36px;margin-top:30px">pra descobrir, em 30 dias,<br>se a sua empresa está te deixando</div>'
     '<div class="w9" style="font-size:56px;margin-top:22px;line-height:1.5"><span class="hl">mais rico ou mais pobre.</span></div>'
     '<div class="w5" style="font-size:30px;margin-top:80px">Mesmo que você odeie planilha.<br><b style="color:#F3F3F3">Depois você me agradece.</b></div></div>'),
 3: ("doc", None, None,
     '<div class="t"><span class="n">1.</span> Separe o seu bolso<br>do bolso da empresa.</div>'
     '<div class="p">Dono mistura tudo: pessoa física com pessoa jurídica.</div>'
     '<div class="pk">Aí <span class="hl">nenhum número que você olha é verdadeiro.</span></div>'
     '<div class="sec">Faça esta semana</div>'
     + ck("Abra uma conta só sua.") + ck("Pró-labore fixo, todo mês no mesmo dia.") + ck("Gasto pessoal sai da sua conta.")),
 4: ("doc", None, None,
     '<div class="t"><span class="n">2.</span> Descubra quanto sobra<br>de cada venda.</div>'
     '<div class="p">Quase todo dono confunde <b>margem de contribuição</b> com lucro bruto.</div>'
     '<div class="sec">Pegue os 5 que mais vendem e tire do preço</div>'
     '<div class="w7" style="font-size:36px;color:#E0E0E0">custo <span class="r">·</span> imposto <span class="r">·</span> comissão <span class="r">·</span> frete</div>'
     '<div class="pk" style="margin-top:34px">O que sobra é <span class="hl">a sua margem.</span></div>'
     '<div class="ft">O campeão de vendas, às vezes, é o que menos deixa.</div>'),
 5: ("doc", None, None,
     '<div class="t"><span class="n">3.</span> Quanto você precisa<br>vender só pra empatar?</div>'
     '<div class="p">É o ponto de equilíbrio: onde a empresa dá zero a zero.</div>'
     '<div class="p" style="margin-top:18px"><b>custo fixo ÷ margem média</b></div>'
     '<div class="sec" style="margin-top:56px">Exemplo</div>'
     '<div class="w5" style="font-size:34px;color:#E0E0E0">R$ 300 mil ÷ 30% =</div>'
     '<div class="w9" style="font-size:76px;margin-top:12px;line-height:1.3"><span class="hl">R$ 1 milhão</span></div>'
     '<div class="w5" style="font-size:32px;margin-top:12px">por mês, só pra empatar.</div>'
     '<div class="ft">Abaixo disso, é prejuízo. E o contador não te dá esse número.</div>'),
 6: ("doc", None, None,
     '<div class="t"><span class="n">4.</span> Olhe o caixa,<br>não só o resultado.</div>'
     '<div class="p">A maioria <b>paga no curto e recebe no longo.</b></div>'
     '<div class="sec">Anote</div>'
     '<div class="ck">Pago o fornecedor em<span class="blank"></span>dias</div>'
     '<div class="ck">Recebo do cliente em<span class="blank"></span>dias</div>'
     '<div class="ck">O estoque fica parado<span class="blank"></span>dias</div>'
     '<div class="ft">Paga em 15 e recebe em 60? <span class="hl">Você banca o cliente por 45 dias.</span></div>'),
 7: ("doc", None, None,
     '<div class="t"><span class="n">5.</span> Toda segunda,<br>1 hora com os números.</div>'
     '<div class="p">Sem rito, nada vira hábito.</div>'
     '<div class="pk" style="margin-top:30px"><span class="hl">segunda · 8h · 1 hora</span></div>'
     '<div class="sec">Você e 4 números</div>'
     '<div class="w7" style="font-size:34px;color:#E0E0E0;line-height:1.6">o que entrou <span class="r">·</span> o que saiu<br>a margem <span class="r">·</span> o caixa</div>'
     '<div class="ft">No fim dos 30 dias: a sua empresa está te deixando mais rico ou mais pobre?</div>', False),
 8: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:46px">Faça isso por</div>'
     '<div class="w9 r" style="font-size:130px;margin-top:6px">30 dias</div>'
     '<div class="w7" style="font-size:46px;margin-top:6px">e volte aqui.</div>'
     '<div class="w7" style="font-size:44px;margin-top:90px;line-height:1.55">Eu duvido você não enxergar<br>a sua empresa <span class="hl">de outro jeito.</span></div>'
     '<div class="w5" style="font-size:30px;margin-top:70px">E se quiser fazer isso comigo do lado →</div></div>'),
 9: ("photo", ("Hé", "mbv-recebido-2026-11-06_13", .5, .66),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 54%", "rgba(11,11,11,1) 62%"),
     '<div class="b" style="left:110px;right:110px;bottom:170px;text-align:center">'
     '<div class="w7" style="font-size:40px">Eu gravei uma aula de raio-x<br>da sua empresa.</div>'
     '<div class="w5" style="font-size:30px;margin-top:20px">quanto entra <span class="r">·</span> quanto sai <span class="r">·</span> onde vaza<br>com o documento pra preencher</div>'
     '<div style="margin-top:50px;font-weight:700;font-size:46px">Comenta <span class="hla" style="font-size:64px;line-height:1.25;vertical-align:middle">RAIO-X</span></div>'
     '<div class="w5" style="margin-top:14px;font-size:30px">que eu mando o link da aula no seu direct.</div></div>'),
}
OFF = {9: -230}
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
