#!/usr/bin/env python3
"""J344 (Eu duvido você fazer isso aqui: plano de 5 passos em 30 dias). Formato do carrossel do Pedro Sobral (DfZyjLPkVHH) na identidade da marca:
capa com foto real do Hélio descontraído + gancho e bilhete à mão; slide 2 e 8 em fundo preto com texto grande; passos num bloco de notas
em modo escuro (diferente do Notas branco do 245). Montserrat (fonte da marca) + Caveat no bilhete. Preto, branco e #A91C20."""
import pathlib, sys
from PIL import Image, ImageOps
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent; IMG = ROOT/"imagens"; OUT = ROOT/"instagram"
IMG.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
F = next(p for p in (pathlib.Path.home()/"Desktop").iterdir() if p.name.startswith("fotos para"))
R = next(d for d in F.iterdir() if d.name.startswith("H"))

def photo(n, name, fx, fy, z=1.0):
    src = next(p for p in R.iterdir() if p.name.startswith(name))
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
.ul{text-decoration:underline;text-decoration-color:#A91C20;text-decoration-thickness:8px;text-underline-offset:10px}
.hook{font-weight:800;font-size:76px;line-height:1.08;letter-spacing:-1.5px;text-shadow:0 2px 18px rgba(0,0,0,.6)}
.hook .cap{font-weight:900}
.note{font-family:'Caveat',cursive;font-weight:700;font-size:50px;line-height:1.05;color:#F3F3F3;transform:rotate(-6deg);text-align:right}
.lab{font-weight:700;font-size:30px;letter-spacing:6px;color:#9A9A9A;text-transform:uppercase}
.mega{font-weight:900;font-size:88px;line-height:1.04;letter-spacing:-2px}
.sub{font-weight:500;font-size:40px;line-height:1.35;color:#BDBDBD}
.sub b{color:#F3F3F3;font-weight:700}
/* bloco de notas escuro */
.doc{background:#141414}
.bar{position:absolute;top:0;left:0;right:0;height:104px;border-bottom:2px solid #262626;display:flex;align-items:center;gap:34px;padding:0 64px;color:#7C7C7C;font-weight:700;font-size:30px}
.bar .sp{flex:1}.bar .dot{width:16px;height:16px;border-radius:50%;background:#A91C20}
.bar .pill{border:2px solid #3A3A3A;border-radius:22px;padding:4px 18px;font-size:22px;letter-spacing:3px;color:#9A9A9A}
.pg{position:absolute;top:150px;left:84px;right:84px;bottom:110px}
.t{font-weight:800;font-size:68px;line-height:1.08;letter-spacing:-1px;color:#F3F3F3;margin-bottom:34px}
.t .n{color:#A91C20}
.p{font-weight:500;font-size:40px;line-height:1.34;color:#CFCFCF;margin-bottom:24px}
.p b{color:#F3F3F3;font-weight:700}
.li{font-weight:500;font-size:40px;line-height:1.3;color:#CFCFCF;margin:0 0 12px 0;display:flex;gap:20px}
.li .k{color:#A91C20;font-weight:800;min-width:40px}
.kw{color:#A91C20;font-weight:700}
.box{background:#1E1E1E;border-left:8px solid #A91C20;padding:28px 32px;margin-top:26px;font-weight:600;font-size:37px;line-height:1.34;color:#E6E6E6}
.box b{color:#FFFFFF;font-weight:800}
.go{position:absolute;bottom:60px;left:84px;font-size:46px;font-weight:700;color:#7C7C7C}
.hla{font-weight:900;background:#A91C20;color:#F3F3F3;padding:0 22px;letter-spacing:1px;display:inline-block}
</style></head><body>'''
BAR = ('<div class="bar"><span>B</span><span style="font-style:italic">I</span><span style="text-decoration:underline">U</span>'
       '<span style="text-decoration:line-through">S</span><span>≡</span><span>1.</span><span class="sp"></span>'
       '<span class="pill">NOTAS</span><span class="dot"></span></div>')
def doc(body): return f'<div class="slide doc">{BAR}<div class="pg">{body}</div><div class="go">→</div></div>'
def li(k, t): return f'<div class="li"><span class="k">{k}</span><span>{t}</span></div>'

def lg(*s): return "linear-gradient(to bottom," + ",".join(s) + ")"
S = {
 1: ("photo", ("mbv-recebido-2026-11-06_19", .5, .42),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 38%", "rgba(11,11,11,.85) 58%", "rgba(11,11,11,.97) 72%"),
     '<div class="b" style="left:80px;right:80px;bottom:300px">'
     '<div class="hook">Eu <span class="cap">DUVIDO</span> você fazer isso aqui e não descobrir onde a sua empresa <span class="r ul">perde dinheiro.</span></div></div>'
     '<div class="b" style="right:80px;bottom:90px;width:620px"><div class="note">Só o <span class="r">passo 3</span> já vale<br>o seu tempo aqui. →</div></div>'),
 2: ("plain", None, None,
     '<div class="b" style="left:84px;right:84px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="lab">Apresento:</div>'
     '<div class="mega" style="margin-top:26px">O plano de 5 passos pra descobrir, em 30 dias, se a sua empresa está te deixando <span class="r">mais rico ou mais pobre.</span></div>'
     '<div class="sub" style="margin-top:44px">Mesmo que você odeie planilha e nunca tenha aberto um balanço. <b>Depois você me agradece.</b></div></div>'),
 3: ("doc", None, None,
     '<div class="t"><span class="n">1.</span> Separe o seu bolso do bolso da empresa.</div>'
     '<div class="p">Dono de pequena e média empresa mistura tudo: pessoa física com pessoa jurídica.</div>'
     '<div class="p">Enquanto a sua conta e a da empresa forem uma só, <b>nenhum número que você olhar é verdadeiro.</b></div>'
     '<div class="p" style="margin-top:34px"><b>Faça esta semana:</b></div>'
     + li("1.", "Abra uma conta só sua.") + li("2.", "Defina um <span class=\"kw\">pró-labore fixo</span>, todo mês no mesmo dia.") + li("3.", "Gasto pessoal sai da sua conta. Nunca da empresa.")),
 4: ("doc", None, None,
     '<div class="t"><span class="n">2.</span> Descubra quanto sobra de cada venda.</div>'
     '<div class="p">Quase todo dono que eu conheço confunde <span class="kw">margem de contribuição</span> com lucro bruto.</div>'
     '<div class="p">Pegue os 5 produtos ou serviços que mais vendem. De cada preço, tire <span class="kw">o custo do produto, o imposto, a comissão e o frete.</span></div>'
     '<div class="p">O que sobra é a sua <b>margem de contribuição.</b></div>'
     '<div class="box">Tem produto que vende muito e quase não deixa nada. <b>Às vezes é o seu campeão de vendas.</b></div>'),
 5: ("doc", None, None,
     '<div class="t" style="font-size:60px"><span class="n">3.</span> Calcule quanto você precisa vender só pra empatar.</div>'
     '<div class="p">É o ponto de equilíbrio: onde a empresa dá <b>zero a zero.</b></div>'
     '<div class="p">A conta: <b>custo fixo do mês ÷ margem de contribuição média.</b></div>'
     '<div class="p" style="margin-top:6px;margin-bottom:14px;color:#9A9A9A;font-weight:700">Exemplo:</div>'
     + li("•", "Custo fixo: R$ 300 mil por mês.") + li("•", "Margem média: 30%.") + li("•", "Ponto de equilíbrio: <span class=\"kw\">R$ 1 milhão por mês.</span>")
     + '<div class="box">Tudo o que você vende abaixo disso é prejuízo. <b>E não adianta pedir pro contador: a contabilidade fiscal não te dá esse número.</b></div>'),
 6: ("doc", None, None,
     '<div class="t"><span class="n">4.</span> Olhe o caixa, não só o resultado.</div>'
     '<div class="p">A maioria das empresas <b>paga no curto e recebe no longo.</b></div>'
     '<div class="p" style="margin-top:28px"><b>Anote:</b></div>'
     + li("1.", "Em quantos dias você paga o fornecedor?") + li("2.", "Em quantos dias o cliente te paga?") + li("3.", "Quantos dias a mercadoria fica parada no estoque?")
     + '<div class="box">Se você paga em 15 e recebe em 60, a sua empresa banca o cliente por <span class="kw">45 dias.</span> <b>E quanto mais você vende, mais dinheiro isso consome.</b></div>'),
 7: ("doc", None, None,
     '<div class="t"><span class="n">5.</span> Toda segunda-feira, 1 hora com esses números.</div>'
     '<div class="p">Sem rito, nada disso vira hábito.</div>'
     '<div class="p">Coloque na agenda: <b>segunda, 8h,</b> você e 4 números:</div>'
     + li("1.", "o que entrou;") + li("2.", "o que saiu;") + li("3.", "a margem;") + li("4.", "o caixa.")
     + '<div class="box">No fim dos 30 dias, responda a única pergunta que importa: <b>a sua empresa está te deixando mais rico ou mais pobre?</b></div>'),
 8: ("plain", None, None,
     '<div class="b" style="left:84px;right:84px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="mega">Faça isso durante <span class="r">30 dias</span> e volte aqui.</div>'
     '<div class="mega r" style="margin-top:34px">Eu duvido você não enxergar a sua empresa de outro jeito.</div>'
     '<div class="sub" style="margin-top:50px"><b>E se quiser fazer isso comigo do lado →</b></div></div>'),
 9: ("photo", ("mbv-recebido-2026-11-06_13", .5, .66),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 54%", "rgba(11,11,11,1) 62%"),
     '<div class="b" style="left:84px;right:84px;bottom:150px;text-align:center">'
     '<div class="sub" style="color:#E6E6E6;font-size:40px">Eu gravei uma aula em que eu faço o raio-x da empresa com você, com o documento pra preencher: <b>quanto entra, quanto sai e onde vaza.</b></div>'
     '<div style="margin-top:40px;font-weight:800;font-size:60px">Comenta <span class="hla" style="font-size:84px;line-height:1.2;vertical-align:middle">RAIO-X</span></div>'
     '<div class="sub" style="margin-top:12px;font-size:38px">que eu mando o link da aula no seu direct.</div></div>'),
}
OFF = {9: -230}   # v1b (pedido do João): o rosto do CTA subiu pra não ficar atrás do texto
for n in ([int(x) for x in sys.argv[1:]] or sorted(S)):
    kind, ph, grad, body = S[n]
    if kind == "doc":
        html = HEAD + doc(body) + '</body></html>'
    elif kind == "plain":
        html = HEAD + f'<div class="slide">{body}</div></body></html>'
    else:
        photo(n, *ph)
        html = HEAD + f'<div class="slide"><img class="ph" style="top:{OFF.get(n,0)}px" src="../imagens/img-{n:02d}.png"><div class="shade" style="background:{grad}"></div>{body}</div></body></html>'
    (OUT/f"slide-{n:02d}.html").write_text(html, encoding="utf-8"); print(f"[{n:02d}] ok")
