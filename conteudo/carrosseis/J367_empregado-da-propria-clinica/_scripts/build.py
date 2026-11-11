#!/usr/bin/env python3
"""J367 v2 (11/11): formato do J360 (capa com foto + bilhete, slide preto, bloco de notas escuro, foto no meio, pergunta, CTA com foto).
Fotos do João, Congresso Brasileiro de Cirurgia Plástica, Fortaleza, 11/11 (IMG_7414 capa, IMG_7492 slide 8, IMG_7463 CTA com o Dr. Raul).
O CSS e os helpers (HEAD, doc, li, lg) vêm do J360, em _css.py."""
import pathlib, sys
from PIL import Image
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent; IMG = ROOT/"imagens"; OUT = ROOT/"instagram"; FOT = ROOT/"fotos"
IMG.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
exec((SCR/"_css.py").read_text(encoding="utf-8"))

def photo(n, name, fx, fy, z=1.0):
    im = Image.open(FOT/f"{name}.jpg").convert("RGB"); W, H = 1080, 1350
    sc = max(W/im.width, H/im.height)*z; im = im.resize((round(im.width*sc), round(im.height*sc)), Image.LANCZOS)
    l = min(max(0, round(fx*im.width-W/2)), im.width-W); t = min(max(0, round(fy*im.height-H/2)), im.height-H)
    im.crop((l, t, l+W, t+H)).save(IMG/f"img-{n:02d}.png")

S = {
 1: ("photo", ("IMG_7492", .491, .628, 1.3),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 47%", "rgba(11,11,11,.85) 60%", "rgba(11,11,11,.98) 70%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:190px">'
     '<div class="w7" style="font-size:46px;color:#E6E6E6">A faculdade te ensinou</div>'
     '<div class="w9" style="font-size:84px;margin-top:8px">a operar paciente.</div>'
     '<div class="w7" style="font-size:46px;margin-top:30px;color:#E6E6E6">Ninguém te ensinou</div>'
     '<div class="w9" style="font-size:66px;margin-top:14px;line-height:1.35;text-shadow:none"><span class="hl">a operar uma empresa.</span></div></div>'
     '<div class="b" style="right:100px;bottom:62px;width:560px"><div class="note">Médico também<br>é <span class="r">empresário.</span> →</div></div>'),
 2: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:46px">Um cirurgião me disse no MBV,<br>na frente de todo mundo:</div>'
     '<div class="w5" style="font-size:40px;margin-top:40px;font-style:italic">&ldquo;Na medicina a gente não tem formação de gestão.&rdquo;</div>'
     '<div class="w9" style="font-size:66px;margin-top:40px;line-height:1.4"><span class="hl">Essa é a dor</span><br><span class="hl">de todo médico.</span></div></div>'),
 3: ("doc", None, None,
     '<div class="t">Todo mês é a mesma conta.</div>'
     + li("a clínica faturou") + li("pagou aluguel, equipe e insumo") + li("o que sobrou, você chamou de <span class=\"hl\">lucro.</span>") +
     '<div class="ft">Só que dentro dessa sobra tem uma parte que nunca foi lucro.</div>'),
 4: ("doc", None, None,
     '<div class="t">Uma parte dessa sobra <span class="n">é o seu trabalho.</span></div>'
     '<div class="p">Se amanhã outro médico atendesse no seu lugar, a clínica ia ter que pagar ele.</div>'
     '<div class="pk" style="margin-top:40px">Isso é o seu <span class="hl">honorário.</span><br><span class="hl">É salário, não é lucro.</span></div>'
     '<div class="ft">Lucro é o que sobra depois de pagar você.</div>'),
 5: ("doc", None, None,
     '<div class="t">Quando você mistura<br>as duas coisas:</div>'
     + li("acha que a clínica dá lucro, e é só o seu salário") + li("não sabe se pode contratar, crescer ou abrir outra sala") + li("se você para um mês, a clínica para junto") +
     '<div class="ft">Você virou <span class="hl">empregado da própria clínica.</span></div>'),
 6: ("doc", None, None,
     '<div class="t">E enquanto você atende,<br><span class="n">ninguém olha o resto.</span></div>'
     + li("a secretária demora uma hora pra responder o WhatsApp") + li("o paciente pergunta o preço e some") + li("ninguém sabe quantas consultas viraram procedimento") +
     '<div class="ft">Uma das minhas empresas atende 70 clínicas. Só responder o paciente na hora<br><span class="hl">já aumenta a venda.</span></div>'),
 7: ("doc", None, None,
     '<div class="t">O médico é o piloto. Sem ele não tem cirurgia.</div>'
     '<div class="pk" style="font-size:44px;line-height:1.55">Mas quem só pilota</div>'
     '<div class="pk" style="font-size:44px;line-height:1.55;margin-top:4px"><span class="hl">nunca olha o painel do avião.</span></div>'
     '<div class="ft">Dono olha número toda semana: quanto entrou, quanto sobrou depois do seu honorário, quantas consultas viraram tratamento.</div>'),
 8: ("photo", ("IMG_7414", .47, .474, 1.8),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 46%", "rgba(11,11,11,.85) 62%", "rgba(11,11,11,.98) 74%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:150px">'
     '<div class="w9" style="font-size:72px">Clínica é empresa.</div>'
     '<div class="w7" style="font-size:44px;margin-top:26px;color:#E6E6E6">E quem é dono de empresa é</div>'
     '<div class="w9" style="font-size:62px;margin-top:14px;line-height:1.35;text-shadow:none"><span class="hl">empresário,</span><br><span class="hl">de jaleco ou não.</span></div>'
     '<div class="w5" style="font-size:30px;margin-top:30px;color:#CFCFCF">Você estudou anos pra ser bom médico. A clínica precisa que você aprenda a ser dono.</div></div>'),
 9: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:48px">Me responde:</div>'
     '<div class="w5" style="font-size:42px;margin-top:50px">se você parar de atender por 30 dias,</div>'
     '<div class="w9" style="font-size:64px;margin-top:30px;line-height:1.4">a sua clínica<br><span class="hl">paga as contas sozinha?</span></div></div>'),
 10: ("photo", ("IMG_7463", .54, .30, 1.0),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 40%", "rgba(11,11,11,.85) 54%", "rgba(11,11,11,1) 62%"),
     '<div class="b" style="left:110px;right:110px;bottom:150px;text-align:center">'
     '<div class="w7" style="font-size:38px">Se a resposta te incomodou, o problema não é falta de paciente. É falta de gestão.</div>'
     '<div class="w5" style="font-size:30px;margin-top:24px">No MBV eu ensino o médico<br>a ler a clínica como empresa.</div>'
     '<div style="margin-top:46px;font-weight:700;font-size:46px">Comenta <span class="hla" style="font-size:64px;line-height:1.25;vertical-align:middle">LIVRE</span></div>'
     '<div class="w5" style="margin-top:14px;font-size:30px">que eu mando o link no seu direct.</div></div>'),
}
OFF = {}
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
