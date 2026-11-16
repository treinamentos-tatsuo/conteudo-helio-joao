#!/usr/bin/env python3
"""J400 (16/11): escada do "1 hora ruim" (07/10). 5 slides, 2 faixas de foto real do Hélio (P&B em cima, cor embaixo)."""
import pathlib, sys, subprocess
SCR = pathlib.Path(__file__).parent; ROOT = SCR.parent; IMG = ROOT/"imagens"; OUT = ROOT/"instagram"
ACV = pathlib.Path.home()/"Desktop"/"fotos para carrosséis"/"Hélio"
PREP = ROOT.parents[2]/".claude"/"skills"/"frase-foto"/"scripts"/"prepara_foto.py"
def src(pref): return str(next(p for p in ACV.iterdir() if p.name.startswith(pref)))
# (slide, faixa, foto, cx, cy, zoom, pb)
F = [
 (1,"cima","DSCF3105",.5,.30,1.0,True), (1,"baixo","MBV-TATSUOAC-206",.5,.40,1.5,False),
 (2,"cima","DSCF3116",.5,.30,1.0,True),  (2,"baixo","MBV-TATSUOAC-207",.5,.40,1.5,False),
 (3,"cima","DSCF3115",.5,.30,1.0,True), (3,"baixo","MBV-TATSUOAC-227",.48,.45,1.3,False),
 (4,"cima","DSCF3122",.5,.30,1.0,True),  (4,"baixo","MBV-TATSUOAC-230",.5,.42,1.3,False),
 (5,"cima","DSCF3076",.5,.30,1.0,True), (5,"baixo","SN-HOKEN-E-4",.5,.42,1.0,False),
]
T = {1:("1 cliente perdido.","Você ainda tem todos os outros."),
     2:("1 funcionário que<br>pediu as contas.","Você ainda tem o time que ficou."),
     3:("1 mês no vermelho.","Você ainda tem 11 pra virar o jogo."),
     4:("1 ano difícil.","Você ainda tem a empresa de pé."),
     5:("1 recuperação judicial.","A minha empresa<br>fez 29 anos.")}
ns = [int(x) for x in sys.argv[1:]] or [1,2,3,4,5]
for n,f,p,cx,cy,z,pb in F:
    if n not in ns: continue
    cmd=[sys.executable,str(PREP),src(p),str(IMG/f"s{n:02d}-{f}.jpg"),"--tam","1080x675","--cx",str(cx),"--cy",str(cy),"--zoom",str(z)]
    if pb: cmd+=["--pb","--contraste","1.1"]
    subprocess.run(cmd,check=True,capture_output=True)
HEAD='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
<style>*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#000;overflow:hidden;font-family:'Montserrat',sans-serif;color:#fff}
.p{position:absolute;left:0;width:1080px;height:675px;overflow:hidden}.p img{position:absolute;left:0;top:0;width:1080px;height:675px}
.g{position:absolute;inset:0}
.t{position:absolute;left:70px;right:70px;bottom:62px;text-align:center;font-weight:800;line-height:1.12;letter-spacing:-.5px;text-shadow:0 2px 18px rgba(0,0,0,.7)}
</style></head><body>'''
for n in ns:
    a,b=T[n]; fa=66 if len(a)<=30 else 58; fb=60 if len(b)<=30 else 52
    html=HEAD+f'''
<div class="p" style="top:0"><img src="../imagens/s{n:02d}-cima.jpg"><div class="g" style="background:linear-gradient(to bottom,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 78%,rgba(0,0,0,.85) 100%)"></div><div class="t" style="font-size:{fa}px">{a}</div></div>
<div class="p" style="top:675px"><img src="../imagens/s{n:02d}-baixo.jpg"><div class="g" style="background:linear-gradient(to bottom,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 14%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 78%,rgba(0,0,0,.85) 100%)"></div><div class="t" style="font-size:{fb}px">{b}</div></div>
</body></html>'''
    (OUT/f"slide-{n:02d}.html").write_text(html,encoding="utf-8"); print(f"[{n:02d}] ok")
