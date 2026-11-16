import json,pathlib,subprocess
from PIL import Image
S=pathlib.Path(__file__).parent; I=S.parent/"imagens"
out=subprocess.run(["node","wrapcheck.js"],capture_output=True,text=True,cwd=S).stdout
tb={int(l.split()[0]):json.loads(l.split(' ',1)[1])["textBottom"] for l in out.strip().splitlines()}
json.dump({str(k):v for k,v in tb.items()},open(S/"textbottom.json","w"))
H={}
for n,t in tb.items():
    f=I/f"img-{n:02d}.png"
    if not f.exists(): continue
    im=Image.open(f).convert("L").resize((1080,720)); px=im.load(); row=0
    for y in range(0,720,4):
        if sum(1 for x in range(60,1020,6) if px[x,y]<150)/160>0.06: row=y;break
    fr=row/720; h=int((1350-(t+140))/(1-fr)) if fr<1 else 1150
    H[str(n)]=max(720,min(1150,h))
json.dump(H,open(S/"imgheight.json","w")); print(H)
