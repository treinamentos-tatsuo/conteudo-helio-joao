"""Monta os 7 HTMLs do J406 (carrossel notícia). Foto no topo, fundo preto embaixo,
título Montserrat 900 com a 2ª linha numa placa carmim, corpo em branco."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "instagram"
OUT.mkdir(exist_ok=True)

# img, posição do foco (background-position), l1, l2, corpo (lista de parágrafos; ** = negrito)
SLIDES = [
    ("img-01.jpg", "50% 30%", "CHILLI BEANS DEVE<br>R$ 340 MILHÕES", "PRO BANCO E FOI RENEGOCIAR.",
     ["No fim de outubro, a rede de óculos do Caito Maia pediu recuperação extrajudicial. E ela não está sozinha nessa fila."]),
    ("img-02.jpg", "50% 35%", "A SUA OPERAÇÃO", "PAGA OS JUROS DO BANCO?",
     ["Antes de achar que isso é problema de empresa grande, arrasta e vê quem está nessa fila."]),
    ("img-03.png", "50% 45%", "14.510 EMPRESAS", "EM RECUPERAÇÃO OU FALÊNCIA.",
     ["É o maior número da série da PreservaCred, no fim do 3º trimestre de 2026. Foram quase nove empresas a mais por dia no último ano."]),
    ("img-04.png", "50% 45%", "NÃO É EMPRESA NOVA.", "NEM É EMPRESA PEQUENA.",
     ["A empresa típica que pede recuperação tem 12 anos e meio de estrada. Quase seis em cada dez não são micro nem pequena.",
      "**Ou seja: é a empresa que deu certo.**"]),
    ("img-05.png", "50% 40%", "NOVE EM CADA DEZ", "CULPAM A DÍVIDA E O CAIXA.",
     ["Sete em cada dez falam de custo alto e margem apertada. Seis em cada dez, dos juros. Foi o que as próprias empresas escreveram no pedido."]),
    ("img-06.jpg", "50% 22%", "ALONGAR A DÍVIDA", "NÃO CONSERTA A EMPRESA.",
     ["Em 38 anos de empresa, eu aprendi: juro se paga com o que a operação sobra. Se não sobra, renegociar só compra tempo.",
      "**E o banco cobra por esse tempo também.**"]),
    ("img-07.jpg", "50% 60%;background-size:100%", "QUANTO A SUA<br>EMPRESA SOBRA", "DEPOIS DE PAGAR O BANCO?",
     ["Se você não sabe responder de cabeça, eu me preocuparia seriamente.",
      "**Comenta RAIOX que eu te mando o link da aula onde você faz o raio-x da sua empresa.**"]),
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#0A0A0A;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;background:#0A0A0A;font-family:'Montserrat',sans-serif;color:#fff}
.ph{position:absolute;left:0;top:0;width:1080px;height:900px;background-size:cover;background-repeat:no-repeat}
.fade{position:absolute;left:0;top:0;width:1080px;height:1350px;
  background:linear-gradient(180deg,rgba(10,10,10,0) 0px,rgba(10,10,10,0) 430px,rgba(10,10,10,.55) 620px,rgba(10,10,10,.93) 760px,#0A0A0A 860px)}
.txt{position:absolute;left:72px;right:72px;bottom:128px}
h1{font-weight:900;text-transform:uppercase;letter-spacing:-0.02em;line-height:1.06;font-size:64px}
h1 .l1{display:block}
h1 .l2{display:inline;background:#A91C20;color:#fff;padding:2px 14px 4px;line-height:1.32;
  -webkit-box-decoration-break:clone;box-decoration-break:clone;margin-left:-14px}
.body{margin-top:34px}
.body p{font-weight:500;font-size:33px;line-height:1.38;color:#E6E6E6}
.body p+p{margin-top:20px}
.body b{font-weight:800;color:#fff}
.ft{position:absolute;left:72px;right:72px;bottom:56px;display:flex;align-items:center;justify-content:space-between;
  font-size:21px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#6B6B6B}
.ft .h{display:flex;align-items:center;gap:14px}
.ft .dm{width:14px;height:14px;background:#A91C20;transform:rotate(45deg)}
.dots{display:flex;gap:10px}
.dots i{width:10px;height:10px;border-radius:50%;background:#3A3A3A;display:block}
.dots i.on{background:#A91C20}
"""


def md(p):
    out, bold = [], False
    for i, part in enumerate(p.split("**")):
        out.append(f"<b>{part}</b>" if i % 2 else part)
    return "".join(out)


for i, (img, pos, l1, l2, body) in enumerate(SLIDES, 1):
    dots = "".join(f'<i class="{"on" if j == i else ""}"></i>' for j in range(1, len(SLIDES) + 1))
    paras = "".join(f"<p>{md(p)}</p>" for p in body)
    seta = " · Arraste" if i < len(SLIDES) else ""
    html = f"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="s">
  <div class="ph" style="background-image:url('../imagens/{img}');background-position:{pos}"></div>
  <div class="fade"></div>
  <div class="txt">
    <h1><span class="l1">{l1}</span><span class="l2">{l2}</span></h1>
    <div class="body">{paras}</div>
  </div>
  <div class="ft"><div class="h"><span class="dm"></span>@helio.tatsuo{seta}</div><div class="dots">{dots}</div></div>
</div>
<script>document.fonts.ready.then(()=>{{const h=document.querySelector('h1'),l=h.querySelector('.l1');let f=64;const n=l.querySelectorAll('br').length+1;
while(l.getBoundingClientRect().height>n*f*1.2&&f>54){{f--;h.style.fontSize=f+'px'}}}});</script>
</body></html>"""
    (OUT / f"slide-{i:02d}.html").write_text(html, encoding="utf-8")
print("ok", len(SLIDES))
