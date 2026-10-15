# Gera slide-11..16.html no padrão do slide 13 do carrossel 95 (papel granulado + Lora + carmim).
import os
R='#A91C20'
HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700&display=swap" rel="stylesheet">
<style>
html,body{margin:0;padding:0}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;
  background:#F1F1F1 url("../imagens/papel.png") center/cover no-repeat;
  font-family:'Lora',serif;color:#141414}
.wrap{position:absolute;left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:%(gap)dpx}
.p{font-size:%(fs)dpx;line-height:1.36}
.p .r{color:%(R)s;font-weight:700}
.p .sm{font-size:%(sm)dpx;display:block;margin-top:14px}
</style></head><body><div class="slide"><div class="wrap">
'''
def punch(n, blocks, fs=58, gap=70, sm=None):
    sm = sm or int(fs*0.72)
    html=HEAD%dict(gap=gap,fs=fs,sm=sm,R=R)
    for b in blocks: html+='<div class="p">%s</div>\n'%b
    html+='</div></div></body></html>'
    open('instagram/slide-%02d.html'%n,'w').write(html)

punch(11,['Mas aguentar a pressão não é<br>o mesmo que ser <span class="r">pago</span> por ela.',
          'Existem dois donos<br>vivendo a mesma pressão.'])
punch(12,['Um corre o risco todo mês<br>e leva pra casa um <span class="r">salário</span>.<span class="sm">(quando leva)</span>',
          'O outro corre o mesmo risco<br>e leva <span class="r">lucro</span>.<br>Dividendo. Patrimônio.'], gap=90)
punch(13,['A diferença não é coragem.','Não é tamanho de empresa.','É <span class="r">gestão</span>.'], fs=62, gap=60)
punch(14,['<span class="r">Gestão</span> é saber a margem<br>antes de vender.','É número na mesa<br>toda semana.','É time que entrega<br>o combinado.'], fs=56, gap=60)
punch(15,['Sem gestão, o risco é todo seu<br>e o prêmio é de ninguém.','Com gestão,<br>o risco continua seu.<br><span class="r">O prêmio também.</span>'], fs=56, gap=90)

# slide 16: layout do slide 13 do carrossel 95
tick='<svg viewBox="0 0 40 40"><path d="M5 23 L15 33 L35 7" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'%R
s16='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,700&display=swap" rel="stylesheet">
<style>
html,body{margin:0;padding:0}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;
  background:#F1F1F1 url("../imagens/papel.png") center/cover no-repeat;
  font-family:'Lora',serif;color:#141414}
.intro{position:absolute;top:262px;left:0;right:0;text-align:center;font-size:40px;line-height:1.42}
.intro b{font-weight:700}
.list{position:absolute;top:452px;left:0;right:0;display:flex;flex-direction:column;align-items:center;gap:0}
.list .row{width:720px;display:flex;align-items:flex-start;gap:28px;font-size:40px;line-height:1.3;margin-bottom:44px}
.list .row svg{flex:0 0 auto;width:38px;height:38px;margin-top:6px}
.cta{position:absolute;top:846px;left:0;right:0;text-align:center;font-size:52px;line-height:1.2}
.small{position:absolute;top:924px;left:0;right:0;text-align:center;font-size:23px;font-weight:700;line-height:1.3}
.arrow{position:absolute;top:1015px;left:0;right:0;display:flex;justify-content:center}
</style></head><body>
<div class="slide">
  <div class="intro">Eu tenho um treinamento para <b>DONOS</b><br>de pequenas e médias empresas, onde ensino:</div>
  <div class="list">
    <div class="row">%(t)s<div>segurar a pressão sem colapsar</div></div>
    <div class="row">%(t)s<div>montar a gestão que paga o risco</div></div>
    <div class="row">%(t)s<div>e transformar responsabilidade<br>em resultado.</div></div>
  </div>
  <div class="cta">Comente “RECOMPENSA” aqui,</div>
  <div class="small">(e eu te mando o link com todos os detalhes no seu direct.)</div>
  <div class="arrow"><svg width="40" height="200" viewBox="0 0 40 200"><line x1="20" y1="0" x2="20" y2="186" stroke="#111" stroke-width="5"/><path d="M4 172 L20 194 L36 172" fill="none" stroke="#111" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
</div>
</body></html>'''%dict(t=tick)
open('instagram/slide-16.html','w').write(s16)
print('ok')
