"""Post 222 v9 — layout da v7 com ajustes finos de acabamento (07/10). Base: 2 slides no visual do post de referência (grade 2x2 com cruz e losango), texto aprovado em 07/10."""
import pathlib, numpy as np
from PIL import Image
POST = pathlib.Path(__file__).resolve().parents[1]

# fundo: preto liso com leve claridade no centro + granulado (o da referência não tem grade)
H, W = 1350, 1080
rng = np.random.default_rng(7)
yy, xx = np.mgrid[0:H, 0:W]
d = np.hypot((xx - 540) / 700, (yy - 640) / 820)
base = 30 - 20 * np.clip(d, 0, 1)
noise = rng.normal(0, 1, (H, W))
k = np.array([1, 4, 6, 4, 1.]); k /= k.sum()
noise = np.apply_along_axis(lambda r: np.convolve(r, k, 'same'), 1, noise)
noise = np.apply_along_axis(lambda c: np.convolve(c, k, 'same'), 0, noise)
img = np.clip(base + noise / noise.std() * 3.6, 0, 255).astype(np.uint8)
Image.fromarray(np.stack([img] * 3, -1)).save(POST / 'imagens' / 'fundo.png')

CSS = """@import url('https://fonts.googleapis.com/css2?family=Anton&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#111;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;background:url('../imagens/fundo.png');color:#fff;font-family:'Source Serif 4',serif}
.t{position:absolute;left:0;right:0;text-align:center;font-family:'Anton',sans-serif;font-size:92px;line-height:1.02;letter-spacing:.5px}
.t .v{color:#A91C20}
.q{position:absolute;width:440px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;padding-top:30px}
.n{width:78px;height:78px;border-radius:50%;background:#A91C20;display:flex;align-items:center;justify-content:center;font-family:'Anton',sans-serif;font-size:44px}
.q h3{margin-top:16px;font-family:'Anton',sans-serif;font-weight:400;font-size:40px;line-height:1.08;letter-spacing:.3px;text-wrap:balance}
.q p{margin-top:12px;font-size:25px;line-height:1.32;color:#d6d6d6;text-wrap:balance}
.lv{position:absolute;left:539px;width:2px;background:#444}.lh{position:absolute;height:2px;background:#444}
.dia{position:absolute;width:26px;height:26px;background:#A91C20;transform:rotate(45deg)}
.fecho{position:absolute;left:110px;width:860px;text-align:center;font-weight:700;font-size:31px;line-height:1.3;text-wrap:balance}
.intro{position:absolute;left:110px;width:860px;text-align:center;font-size:30px;line-height:1.38;color:#d6d6d6;text-wrap:balance}
.passo{position:absolute;left:110px;width:860px;display:flex;gap:28px;align-items:flex-start}
.passo .n{flex:0 0 78px}
.passo h3{font-family:'Anton',sans-serif;font-weight:400;font-size:40px;line-height:1.1;letter-spacing:.3px}
.passo p{margin-top:6px;font-size:27px;line-height:1.32;color:#d6d6d6;text-wrap:pretty}
.cta{position:absolute;left:90px;width:900px;background:#A91C20;border-radius:14px;padding:30px 44px;text-align:center}
.cta p{font-size:28px;line-height:1.36;font-weight:600;text-wrap:balance}
.cta .bio{margin-top:16px;font-family:'Anton',sans-serif;font-size:54px;letter-spacing:1px}
"""

def page(body):
    return f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s"><div class="conteudo">{body}</div></div></body></html>'

EXTRA = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
.passo p{text-wrap:balance}
.q{padding-top:0}
.q .n{width:96px;height:96px;font-size:54px}
.q h3{margin-top:22px;font-size:48px;line-height:1.08}
.bloco{position:absolute;left:130px;width:820px;text-align:center;display:flex;flex-direction:column;align-items:center}
.bloco .n{width:96px;height:96px;font-size:54px}
.bloco h3{margin-top:22px;font-family:'Anton',sans-serif;font-weight:400;font-size:56px;line-height:1.08;letter-spacing:.3px}
.bloco p{margin-top:16px;font-size:33px;line-height:1.38;color:#d6d6d6;text-wrap:balance}
.dest{margin-top:22px;background:#A91C20;border-radius:10px;padding:12px 28px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:27px;line-height:1.3;color:#fff;width:fit-content;max-width:820px}
.bola{flex:0 0 22px;width:22px;height:22px;border-radius:50%;background:#A91C20;margin-top:14px}
/* v9 — ajustes finos de acabamento sobre o layout aprovado (sem mudar a diagramacao) */
.s::after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 58%,rgba(0,0,0,.42) 100%);pointer-events:none}
.conteudo{position:absolute;inset:0;z-index:2}
.lv{width:1px;background:#3a3a3a}.lh{height:1px;background:#3a3a3a}
.dia{width:18px;height:18px;margin:4px 0 0 4px}
.n{box-shadow:0 0 0 7px rgba(169,28,32,.16)}
.q .n,.bloco .n{width:86px;height:86px;font-size:48px}
.t{letter-spacing:.8px}
.q h3{font-size:46px;letter-spacing:.6px;margin-top:26px}
.bloco h3{font-size:54px;letter-spacing:.6px;margin-top:26px}
.bloco p{font-size:32px;line-height:1.42;color:#c9c9c9}
.dest{max-width:900px;white-space:nowrap;border-radius:6px;padding:14px 30px;font-size:25px;letter-spacing:.2px;box-shadow:0 8px 24px rgba(0,0,0,.35)}
.intro{color:#c9c9c9}
.passo h3{letter-spacing:.6px}
.passo p{color:#c9c9c9;line-height:1.42}
.bola{flex:0 0 16px;width:16px;height:16px;margin-top:17px;box-shadow:0 0 0 5px rgba(169,28,32,.16)}
.cta{border-radius:6px;box-shadow:0 10px 30px rgba(0,0,0,.4)}
.cta .bio{letter-spacing:2px}
"""

def pg(body):
    return page(body).replace('<style>', '<style>' + EXTRA.split(chr(10),2)[1] + chr(10)).replace('</style>', EXTRA + '</style>')


EXTRA += """
.ttl{position:absolute;left:130px;width:820px;text-align:center;font-family:'Anton',sans-serif;font-size:76px;line-height:1.04;letter-spacing:.8px}
.ttl .v{color:#A91C20}
.txt{position:absolute;left:130px;width:820px;text-align:center;font-size:32px;line-height:1.42;color:#c9c9c9;text-wrap:balance}
.dest2{position:absolute;left:50%;transform:translateX(-50%);background:#A91C20;border-radius:6px;padding:14px 30px;font-family:'Montserrat',sans-serif;font-weight:700;font-size:26px;line-height:1.3;color:#fff;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.35)}
.g{position:absolute;width:400px;text-align:center;display:flex;flex-direction:column;align-items:center}
.g .n{width:70px;height:70px;font-size:40px}
.g h3{margin-top:16px;font-family:'Anton',sans-serif;font-weight:400;font-size:40px;letter-spacing:.6px}
.g p{margin-top:8px;font-size:26px;line-height:1.36;color:#c9c9c9;text-wrap:balance}
.eng{position:absolute;left:150px;width:780px;display:flex;gap:24px}
.eng h3{font-family:'Anton',sans-serif;font-weight:400;font-size:40px;letter-spacing:.6px}
.eng p{margin-top:6px;font-size:28px;line-height:1.42;color:#c9c9c9;text-wrap:balance}
"""
import base64
LOGO = base64.b64encode(open('/Users/pedrohenrique/Documents/tatsuo-carrossel/.claude/skills/carrossel/modelos/infografico/logo-simbolo.png','rb').read()).decode()
def w(n, b): (POST / 'instagram' / f'slide-{n:02d}.html').write_text(pg(b))

# 1 capa
b = '<div class="ttl solo" style="top:330px;font-size:104px">ESTOU FICANDO<br>MAIS RICO<br><span class="v">OU MAIS POBRE?</span></div>'
b += '<div class="lh" style="top:720px;left:390px;width:300px"></div><div class="dia" style="left:527px;top:708px"></div>'
b += '<div class="txt solo" style="top:770px;width:760px;left:160px">A maioria dos donos não sabe responder, mesmo com a empresa dando lucro.</div>'
w(1, b)

# 2 o lucro muda de forma
b = '<div class="ttl solo" style="top:150px">O LUCRO NÃO SOME.<br><span class="v">MUDA DE FORMA.</span></div>'
b += '<div class="txt solo" style="top:340px">O lucro aparece na DRE, mas nem sempre aparece na conta. Antes de virar dinheiro disponível, ele pode ter ido para quatro lugares:</div>'
b += '<div class="lv" style="top:560px;height:620px"></div><div class="lh" style="top:869px;left:150px;width:780px"></div><div class="dia" style="left:527px;top:857px"></div>'
G = [('1','ESTOQUE','Comprou mercadoria que ainda não vendeu.'),('2','RECEBÍVEL','Vendeu, mas o cliente ainda não pagou.'),
     ('3','DÍVIDA','O resultado foi usado para abater empréstimo.'),('4','RETIRADA','O sócio tirou para si.')]
for (x,y),(n,t,p) in zip([(120,590),(560,590),(120,905),(560,905)],G):
    b += f'<div class="g solo" style="left:{x}px;top:{y}px"><div class="n">{n}</div><h3>{t}</h3><p>{p}</p></div>'
w(2, b)

# 3 a DRE nao responde
b = '<div class="ttl solo" style="top:290px">A DRE NÃO RESPONDE<br><span class="v">ESSA PERGUNTA</span></div>'
b += '<div class="txt solo" style="top:500px">A DRE mostra se a empresa deu lucro no mês. Ela não mostra se esse lucro virou riqueza ou se escorreu pelo caminho.</div>'
b += '<div class="txt solo" style="top:690px">Para isso, o dono precisa olhar para o patrimônio da empresa, e não só para o resultado.</div>'
b += '<div class="dest2 solo" style="top:880px">Lucro é o que a empresa gerou. Riqueza é o que ficou.</div>'
w(3, b)

# 4 por que o dono se acha mais rico
b = '<div class="ttl solo" style="top:180px">POR QUE O DONO SE ACHA<br><span class="v">MAIS RICO DO QUE É</span></div>'
b += '<div class="txt solo" style="top:390px">Quem tenta responder de cabeça costuma cair em três enganos:</div>'
E = [('O SALDO DO BANCO','Conta o saldo inteiro, mas parte dele já tem dono.'),
     ('O RECEBÍVEL','Conta como dinheiro, mas ele tem prazo e inadimplência.'),
     ('O ESTOQUE','Conta tudo, mas mercadoria que não vende não vira dinheiro.')]
y = 530
for i,(t,p) in enumerate(E):
    b += f'<div class="eng solo" style="top:{y}px"><div class="bola"></div><div><h3>{t}</h3><p>{p}</p></div></div>'
    if i < 2: b += f'<div class="lh" style="top:{y+168}px;left:150px;width:780px"></div>'
    y += 200
w(4, b)

# 5 CTA
b = '<div class="ttl solo" style="top:290px;font-size:84px">QUER A RESPOSTA<br><span class="v">DE VERDADE, TODO MÊS?</span></div>'
b += '<div class="txt solo" style="top:510px;width:780px;left:150px;font-size:33px;color:#e6e6e6">O Balanço Japonês mostra, com número, se a empresa está ficando mais rica ou mais pobre. No MBV, o dono de pequena e média empresa aprende a montar e a ler essa ferramenta na própria empresa.</div>'
b += '<div class="cta solo" style="top:840px;left:290px;width:500px;padding:22px 30px;text-align:center"><div class="bio" style="margin-top:0;font-size:56px">LINK NA BIO</div></div>'
b += f'<img class="solo" src="data:image/png;base64,{LOGO}" style="position:absolute;left:504px;top:1120px;width:72px;height:72px" alt="">'
w(5, b)
print('ok')
