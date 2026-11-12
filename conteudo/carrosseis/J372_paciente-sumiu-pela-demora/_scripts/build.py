#!/usr/bin/env python3
"""J372 v1 (12/11): formato do J367 (capa com foto + bilhete, slide preto, bloco de notas escuro, foto no meio, desafio, CTA com foto).
Fotos do João no 62º Congresso Brasileiro de Cirurgia Plástica (Fortaleza, 11/11): IMG_7414 na capa e no CTA (recorte fechado), IMG_7492 no slide 8.
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
 1: ("photo", ("IMG_7414", .47, .522, 1.35),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 56%", "rgba(11,11,11,.98) 67%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:220px">'
     '<div class="w7" style="font-size:46px;color:#E6E6E6">Se eu pudesse te ensinar</div>'
     '<div class="w9" style="font-size:92px;margin-top:6px">1 só coisa</div>'
     '<div class="w7" style="font-size:46px;margin-top:14px;color:#E6E6E6">pra vender mais cirurgias,</div>'
     '<div class="w9" style="font-size:72px;margin-top:18px;line-height:1.3;text-shadow:none"><span class="hl">sabe qual seria?</span></div></div>'
     '<div class="b" style="right:100px;bottom:70px;width:600px"><div class="note">E não tem nada a ver<br>com <span class="r">medicina.</span> →</div></div>'),
 2: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w9" style="font-size:76px">Responda o paciente</div>'
     '<div class="w9" style="font-size:64px;margin-top:14px;line-height:1.35"><span class="hl">em menos de 1 minuto.</span></div>'
     '<div class="w5" style="font-size:40px;margin-top:50px">Parece simples demais.<br>Quase nenhuma clínica faz.</div></div>'),
 3: ("doc", None, None,
     '<div class="t">A gente testa isso<br><span class="n">se passando por paciente.</span></div>'
     '<div class="p" style="margin-bottom:26px">Uma das minhas empresas atende clínicas médicas. É o primeiro teste que a gente faz.</div>'
     + li("resposta em 5, 10 minutos") + li("resposta em 2, 3 horas") + li("clínica que só responde no dia seguinte") +
     '<div class="ft" style="margin-top:50px">Dos consultórios que a gente testou,<br><span class="hl">nenhum respondeu em menos de um minuto.</span></div>'),
 4: ("doc", None, None,
     '<div class="t">No telefone, 1 minuto esperando é uma eternidade.</div>'
     '<div class="p">No WhatsApp, ninguém liga. Mandou de manhã, a clínica responde depois do almoço.</div>'
     '<div class="pk" style="font-size:46px;margin-top:34px">Uai, aí o paciente<br><span class="hl">já até sarou.</span></div>'
     '<div class="ft">Já passou a dor de cabeça dele. Ou ele já marcou com outro médico.</div>'),
 5: ("doc", None, None,
     '<div class="t">E quando responde, é assim:</div>'
     '<div class="p" style="font-style:italic;color:#E0E0E0;font-size:40px">&ldquo;A consulta custa 700 reais.&rdquo;</div>'
     '<div class="p" style="margin-top:30px">Sem perguntar o nome, o caso, o que ele está sentindo.</div>'
     '<div class="pk" style="margin-top:30px">Isso não é atendimento.<br><span class="hl">É tabela de preço.</span></div>'
     '<div class="ft">Aí o paciente compara preço. Foi a única coisa que a clínica deu pra ele comparar.</div>'),
 6: ("doc", None, None,
     '<div class="t">A consulta é<br><span class="n">a porta de entrada.</span></div>'
     + li("o paciente entra pela consulta") + li("na consulta, ele conhece o procedimento") + li("é o procedimento que sustenta a clínica") +
     '<div class="ft">Quem perde a consulta no WhatsApp<br><span class="hl">perde a cirurgia junto.</span></div>'),
 7: ("doc", None, None,
     '<div class="t">E o médico não vê nada disso.</div>'
     '<div class="p">Ninguém mede quanto tempo a clínica leva pra responder, nem quantas mensagens viram consulta.</div>'
     '<div class="pk" style="font-size:44px;margin-top:34px"><span class="hl">O que ninguém mede,</span><br><span class="hl">ninguém cobra.</span></div>'
     '<div class="ft">Nas clínicas que a gente atende, só acompanhar o tempo de resposta já aumentou o faturamento.</div>'),
 8: ("photo", ("IMG_7492", .70, .58, 2.0),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 42%", "rgba(11,11,11,.85) 56%", "rgba(11,11,11,.98) 68%"),
     '<div class="b sh" style="left:100px;right:100px;bottom:150px">'
     '<div class="w9" style="font-size:72px">Clínica tem meta.</div>'
     '<div class="w9" style="font-size:72px;margin-top:8px">Tem funil.</div>'
     '<div class="w9" style="font-size:72px;margin-top:14px;line-height:1.3;text-shadow:none"><span class="hl">Tem venda.</span></div>'
     '<div class="w5" style="font-size:30px;margin-top:34px;color:#CFCFCF">Médico que acha que venda é coisa de comerciante deixa o paciente pro concorrente que respondeu primeiro.</div></div>'),
 9: ("plain", None, None,
     '<div class="b" style="left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">'
     '<div class="w7" style="font-size:48px">Faz o teste hoje:</div>'
     '<div class="w5" style="font-size:40px;margin-top:40px">manda uma mensagem pra sua clínica como se fosse paciente.</div>'
     '<div class="w9" style="font-size:62px;margin-top:40px;line-height:1.4">Quanto tempo ela levou<br><span class="hl">pra responder?</span></div></div>'),
 10: ("photo", ("IMG_7414", .47, .462, 2.6),
     lg("rgba(11,11,11,0) 0%", "rgba(11,11,11,0) 36%", "rgba(11,11,11,.85) 50%", "rgba(11,11,11,1) 58%"),
     '<div class="b" style="left:110px;right:110px;bottom:150px;text-align:center">'
     '<div class="w7" style="font-size:38px">Se a resposta te incomodou, a sua clínica está perdendo paciente no caminho.</div>'
     '<div class="w5" style="font-size:30px;margin-top:24px">A Alta Escala, uma das minhas empresas,<br>faz o Mapa de Oportunidades da sua clínica:<br>mostra onde o paciente desiste.</div>'
     '<div style="margin-top:46px;font-weight:700;font-size:46px">Comenta <span class="hla" style="font-size:64px;line-height:1.25;vertical-align:middle">MOP</span></div>'
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
