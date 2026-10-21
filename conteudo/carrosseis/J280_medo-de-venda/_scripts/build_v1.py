#!/usr/bin/env python3
"""J280 (Hoje eu tenho medo de venda), modelo fotos-reais. Base comum em _lib.py (CSS do 220, fotos cruas, gerada em P&B suave)."""
from _lib import run, lg, c, BASE, DIV, LAT_R
H = lambda name: (lambda R, P, G: next(p for p in R.iterdir() if p.name.startswith(name)))
GEN = lambda n: (lambda R, P, G: G/f"gen-{n:02d}.png")
PUB = lambda name: (lambda R, P, G: P/name)
# n: (fonte, fx, fy, zoom, crua?)
PH = {
 1: (H("DSCF3122"), .5, .30, 1.0, True),
 2: (GEN(2), .5, .5, 1.0, False),
 3: (GEN(3), .5, .5, 1.0, False),
 4: (GEN(4), .5, .5, 1.0, False),
 5: (H("MBV-TATSUOAC-240"), .71, .40, 1.0, True),
 6: (GEN(6), .5, .5, 1.0, False),
 7: (GEN(7), .5, .5, 1.0, False),
 8: (H("MBV-TATSUOAC-247"), .5, .62, 1.1, True),
 9: (GEN(9), .5, .5, 1.0, False),
 10: (PUB("MBV-TATSUOAC-190.jpg"), .5, .0, 1.0, True),
 11: (H("MBV-TATSUOAC-228"), .45, .64, 1.15, True),
}
OFF = {11: -110}
S = {
 1: (lg("to bottom", c(0,0), c(0,42), c(.9,58), c(1,68)),
     '<div class="b" style="bottom:200px;left:90px;right:90px;text-align:center">'
     '<div class="big" style="font-size:52px">Eu vendi mais de 9 bilhões<br>em 4 continentes.</div>'
     '<div style="margin-top:22px;font-size:108px;line-height:1.22"><span class="hla">HOJE EU TENHO</span><br><span class="hla">MEDO DE VENDA.</span></div></div>'),
 2: (DIV,
     '<div class="b" style="top:150px;left:110px;right:110px;text-align:center">'
     '<div class="s">Por muito tempo, eu resolvia tudo<br>do mesmo jeito.</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:46px">O caixa apertou? <span class="r">Vende mais.</span></div>'
     '<div class="s" style="font-size:46px;margin-top:10px">A margem caiu? <span class="r">Vende mais.</span></div></div>'),
 3: (BASE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Cheguei a ter um escritório<br>de <b>2 mil metros quadrados.</b></div>'
     '<div class="s" style="font-size:48px;margin-top:28px"><span class="hl">E fretei avião pra levar</span><br><span class="hl">a equipe pra Europa.</span></div></div>'),
 4: (BASE,
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:58px">E o financeiro? <span class="r">Desarrumado.</span></div>'
     '<div class="s" style="margin-top:24px">Eu não sabia quanto sobrava<br>de cada venda.</div></div>'),
 5: (LAT_R,
     '<div class="b" style="top:0;bottom:0;right:100px;width:500px;display:flex;flex-direction:column;justify-content:center;text-align:left">'
     '<div class="s" style="font-size:44px">Aí eu aprendi<br>do jeito mais caro:</div>'
     '<div class="s" style="font-size:44px;margin-top:22px">venda com a casa desarrumada não resolve o problema.</div>'
     '<div class="big" style="font-size:66px;margin-top:30px">Ela acelera<br><span class="r">a merda.</span></div></div>'),
 6: (BASE,
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:left">'
     '<div class="s">Cada venda nova traz mais estoque,<br>mais prazo pro cliente e mais gente na folha.</div>'
     '<div class="s r" style="font-size:52px;line-height:1.15;margin-top:26px">Se a margem já é ruim, você<br>só multiplica o prejuízo.</div></div>'),
 7: (DIV,
     '<div class="b" style="top:150px;left:110px;right:110px;text-align:center">'
     '<div class="s">Conheço dono que comemora<br>recorde de venda em dezembro</div></div>'
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="s" style="font-size:52px;line-height:1.5"><span class="hl">e em março vende o carro</span><br><span class="hl">pra pagar fornecedor.</span></div></div>'),
 8: (lg("to bottom", c(0,0), c(0,50), c(.92,62), c(1,70)),
     '<div class="b" style="bottom:200px;left:100px;right:100px;text-align:center">'
     '<div class="s">Por isso eu digo sem vergonha nenhuma:</div>'
     '<div class="big" style="font-size:62px;margin-top:14px">hoje eu tenho medo de venda.</div>'
     '<div class="s r" style="font-size:46px;margin-top:16px">Medo de vender sem saber quanto sobra.</div></div>'),
 9: (BASE,
     '<div class="b" style="bottom:200px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:56px">Primeiro arruma a casa:</div>'
     '<div class="s" style="font-size:48px;margin-top:10px">margem, custo e caixa.</div>'
     '<div class="s" style="font-size:48px;margin-top:28px"><span class="hl">Depois vai pra rua vender.</span></div></div>'),
 10: (lg("to bottom", c(1,0), c(.95,34), c(.3,42), c(0,48), c(0,82), c(.6,100)),
     '<div class="b" style="top:120px;left:110px;right:110px;text-align:center">'
     '<div class="big" style="font-size:50px">Eu ensino gestão pra donos de PME<br>no meu treinamento, o MBV:</div>'
     '<div class="s" style="font-size:44px;margin-top:16px"><b>Lucratividade, Crescimento e Cultura.</b></div>'
     '<div class="s" style="font-size:42px;margin-top:20px"><span class="hl">Pra você vender sabendo</span><br><span class="hl">o que fica no seu bolso.</span></div></div>'),
 11: (lg("to bottom", c(0,0), c(0,46), c(.92,58), c(1,66)),
     '<div class="b" style="bottom:210px;left:100px;right:100px;text-align:center">'
     '<div class="big" style="font-size:54px">Quer vender mais<br>sem ficar mais pobre?</div>'
     '<div style="color:#F3F3F3;font-size:60px;font-weight:600;line-height:1.1;margin-top:36px">Comenta <span class="hla" style="font-size:86px;line-height:1.15;vertical-align:middle">LUCRO</span></div>'
     '<div class="s" style="font-size:40px;margin-top:8px">que eu mando o link no seu direct.</div></div>'),
}
run(__file__, PH, S, OFF)
