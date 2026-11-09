#!/usr/bin/env python3
"""J344 v2 (09/11, correções do João): capa com foto do dia a dia (podcast, polo preta) e texto sem bloco:
uma ideia por linha, tamanhos diferentes, checklist, número grande, menos palavras ("texto blocado dá preguiça de ler").
v1 em build_v1.py e instagram/_v1/. Montserrat (fonte da marca) + Caveat no bilhete. Preto, branco e #A91C20."""
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
.ul{text-decoration:underline;text-decoration-color:#A91C20;text-decoration-thickness:9px;text-underline-offset:12px}
.sh{text-shadow:0 2px 18px rgba(0,0,0,.65)}
.note{font-family:'Caveat',cursive;font-weight:700;font-size:52px;line-height:1.05;color:#F3F3F3;transform:rotate(-6deg);text-align:right}
.lab{font-weight:700;font-size:28px;letter-spacing:6px;color:#9A9A9A;text-transform:uppercase}
.w9{font-weight:900;letter-spacing:-2px;line-height:1.02}.w7{font-weight:700;line-height:1.15;letter-spacing:-.5px}.w5{font-weight:500;line-height:1.3;color:#BDBDBD}
/* bloco de notas escuro */
.doc{background:#141414}
.bar{position:absolute;top:0;left:0;right:0;height:104px;border-bottom:2px solid #262626;display:flex;align-items:center;gap:34px;padding:0 64px;color:#7C7C7C;font-weight:700;font-size:30px}
.bar .sp{flex:1}.bar .dot{width:16px;height:16px;border-radius:50%;background:#A91C20}
.bar .pill{border:2px solid #3A3A3A;border-radius:22px;padding:4px 18px;font-size:22px;letter-spacing:3px;color:#9A9A9A}
.pg{position:absolute;top:160px;left:84px;right:84px;bottom:130px;display:flex;flex-direction:column}
.t{font-weight:800;font-size:66px;line-height:1.08;letter-spacing:-1px;margin-bottom:30px}
.t .n{color:#A91C20}
.p{font-weight:500;font-size:42px;line-height:1.3;color:#BDBDBD}
.pk{font-weight:800;font-size:48px;line-height:1.18;color:#F3F3F3;margin-top:18px}
.sec{font-weight:700;font-size:26px;letter-spacing:5px;color:#8A8A8A;text-transform:uppercase;margin:48px 0 22px}
.ck{display:flex;align-items:center;gap:24px;font-weight:600;font-size:42px;line-height:1.2;margin-bottom:22px}
.ck .bx{width:44px;height:44px;border:4px solid #A91C20;border-radius:8px;flex:none}
.tags{display:flex;flex-wrap:wrap;gap:16px}
.tag{border:3px solid #A91C20;color:#F3F3F3;border-radius:40px;padding:10px 28px;font-weight:700;font-size:40px}
.tag.f{background:#A91C20}
.box{background:#1E1E1E;border-left:8px solid #A91C20;padding:28px 32px;margin-top:auto;font-weight:700;font-size:40px;line-height:1.28;color:#F3F3F3}
.blank{display:inline-block;border-bottom:4px solid #A91C20;width:120px;margin:0 10px;transform:translateY(-6px)}
.go{position:absolute;bottom:56px;right:84px;font-size:46px;font-weight:700;color:#7C7C7C}
.hla{font-weight:900;background:#A91C20;color:#F3F3F3;padding:0 22px;letter-spacing:1px;display:inline-block}
</style></head><body>'''
BAR = ('<div class="bar"><span>B</span><span style="font-style:italic">I</span><span style="text-decoration:underline">U</span>'
       '<span style="text-decoration:line-through">S</span><span>≡</span><span>1.</span><span class="sp"></span>'
       '<span class="pill">NOTAS</span><span class="dot"></span></div>')
def doc(body, arrow=True): return f'<div class="slide doc">{BAR}<div class="pg">{body}</div>' + ('<div class="go">→</div>' if arrow else '') + '</div>'
def ck(t): return f'<div class="ck"><span class="bx"></span><span>{t}</span></div>'
def lg(*s): return "linear-gradient(to bottom," + ",".join(s) + ")"

S = {
 1: ("photo", ("Hé", "MBV-TATSUOAC-227", .47, .62, 1.12),   # v2b: foto 9 (gargalhada apontando), escolha do João
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 40%", "rgba(11,11,11,.82) 56%", "rgba(11,11,11,.97) 70%"),
     '<div class="b sh" style="left:80px;right:80px;bottom:280px">'
     '<div class="w9" style="font-size:132px">Eu DUVIDO</div>'
     '<div class="w7" style="font-size:54px;margin-top:10px">você fazer isso aqui e não<br>descobrir onde a sua empresa</div>'
     '<div class="w9 r ul" style="font-size:100px;margin-top:16px">perde dinheiro.</div></div>'
     '<div class="b" style="right:80px;bottom:80px;width:640px"><div class="note">Só o <span class="r">passo 3</span> já vale<br>o seu tempo aqui. →</div></div>'),
 2: ("plain", None, None,
     '<div class="b" style="left:84px;right:84px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="lab">Apresento:</div>'
     '<div class="w7" style="font-size:64px;margin-top:30px">O plano de</div>'
     '<div class="w9 r" style="font-size:170px">5 passos</div>'
     '<div class="w7" style="font-size:52px;margin-top:20px">pra descobrir, em 30 dias,<br>se a sua empresa<br>está te deixando</div>'
     '<div class="w9 r" style="font-size:84px;margin-top:14px">mais rico<br>ou mais pobre.</div>'
     '<div class="w5" style="font-size:38px;margin-top:50px">Mesmo que você odeie planilha.<br><b style="color:#F3F3F3">Depois você me agradece.</b></div></div>'),
 3: ("doc", None, None,
     '<div class="t"><span class="n">1.</span> Separe o seu bolso do bolso da empresa.</div>'
     '<div class="p">Dono mistura tudo: pessoa física com pessoa jurídica.</div>'
     '<div class="pk">Aí nenhum número que você olha <span class="r">é verdadeiro.</span></div>'
     '<div class="sec">Faça esta semana</div>'
     + ck("Abra uma conta só sua.") + ck("Pró-labore fixo, todo mês no mesmo dia.") + ck("Gasto pessoal sai da sua conta.")
     + '<div class="box">Sem esse passo, <span class="r">os outros 4 não funcionam.</span></div>'),
 4: ("doc", None, None,
     '<div class="t"><span class="n">2.</span> Descubra quanto sobra de cada venda.</div>'
     '<div class="p">Quase todo dono confunde <b style="color:#F3F3F3">margem de contribuição</b> com lucro bruto.</div>'
     '<div class="sec">Pegue os 5 que mais vendem e tire do preço</div>'
     '<div class="tags"><span class="tag">custo</span><span class="tag">imposto</span><span class="tag">comissão</span><span class="tag">frete</span></div>'
     '<div class="pk" style="margin-top:34px">O que sobra = <span class="r">a sua margem.</span></div>'
     '<div class="box">O campeão de vendas, às vezes, é o que menos deixa.</div>'),
 5: ("doc", None, None,
     '<div class="t"><span class="n">3.</span> Quanto você precisa vender só pra empatar?</div>'
     '<div class="p">É o ponto de equilíbrio: onde a empresa dá zero a zero.</div>'
     '<div class="tags" style="margin-top:34px"><span class="tag">custo fixo</span><span style="font-size:48px;font-weight:800;align-self:center">÷</span><span class="tag">margem média</span></div>'
     '<div class="sec" style="margin-top:44px">Exemplo</div>'
     '<div class="w7" style="font-size:48px">R$ 300 mil ÷ 30% =</div>'
     '<div class="w9 r" style="font-size:118px;margin-top:6px">R$ 1 milhão</div>'
     '<div class="w7" style="font-size:42px;margin-top:6px">por mês, só pra empatar.</div>'
     '<div class="box" style="font-size:36px">Abaixo disso, é prejuízo. E o contador não te dá esse número.</div>'),
 6: ("doc", None, None,
     '<div class="t"><span class="n">4.</span> Olhe o caixa, não só o resultado.</div>'
     '<div class="p">A maioria <b style="color:#F3F3F3">paga no curto e recebe no longo.</b></div>'
     '<div class="sec">Anote</div>'
     '<div class="ck">Pago o fornecedor em<span class="blank"></span>dias</div>'
     '<div class="ck">Recebo do cliente em<span class="blank"></span>dias</div>'
     '<div class="ck">O estoque fica parado<span class="blank"></span>dias</div>'
     '<div class="box">Paga em 15 e recebe em 60?<br><span class="r">Você banca o cliente por 45 dias.</span></div>'),
 7: ("doc", None, None,
     '<div class="t"><span class="n">5.</span> Toda segunda, 1 hora com os números.</div>'
     '<div class="p">Sem rito, nada vira hábito.</div>'
     '<div class="tags" style="margin-top:34px"><span class="tag f">SEG · 8H · 1 HORA</span></div>'
     '<div class="sec">Você e 4 números</div>'
     '<div class="tags"><span class="tag">o que entrou</span><span class="tag">o que saiu</span><span class="tag">a margem</span><span class="tag">o caixa</span></div>'
     '<div class="box">No fim dos 30 dias:<br><span class="r">a sua empresa está te deixando mais rico ou mais pobre?</span></div>', False),
 8: ("plain", None, None,
     '<div class="b" style="left:84px;right:84px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:64px">Faça isso por</div>'
     '<div class="w9 r" style="font-size:190px">30 dias</div>'
     '<div class="w7" style="font-size:64px">e volte aqui.</div>'
     '<div class="w9" style="font-size:64px;margin-top:60px;line-height:1.1">Eu duvido você não enxergar a sua empresa de outro jeito.</div>'
     '<div class="w5" style="font-size:38px;margin-top:44px"><b style="color:#F3F3F3">E se quiser fazer isso comigo do lado →</b></div></div>'),
 9: ("photo", ("Hé", "mbv-recebido-2026-11-06_13", .5, .66),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 54%", "rgba(11,11,11,1) 62%"),
     '<div class="b" style="left:84px;right:84px;bottom:140px;text-align:center">'
     '<div class="w7" style="font-size:50px">Eu gravei uma aula de<br>raio-x da sua empresa.</div>'
     '<div class="tags" style="justify-content:center;margin-top:28px"><span class="tag">quanto entra</span><span class="tag">quanto sai</span><span class="tag">onde vaza</span></div>'
     '<div class="w5" style="font-size:36px;margin-top:22px">Com o documento pra preencher.</div>'
     '<div style="margin-top:40px;font-weight:800;font-size:60px">Comenta <span class="hla" style="font-size:84px;line-height:1.2;vertical-align:middle">RAIO-X</span></div>'
     '<div class="w5" style="margin-top:12px;font-size:36px">que eu mando o link da aula no seu direct.</div></div>'),
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
