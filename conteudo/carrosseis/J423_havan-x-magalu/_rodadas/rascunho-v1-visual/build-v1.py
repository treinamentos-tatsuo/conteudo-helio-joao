"""Monta os 10 HTMLs do J423 (carrossel notícia). Foto no topo, fundo preto embaixo,
título Montserrat 900 com a 2ª linha numa placa carmim, corpo em branco."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "instagram"
OUT.mkdir(exist_ok=True)

# img, posição do foco (background-position), l1, l2, corpo (lista de parágrafos; ** = negrito)
SLIDES = [
    ("img-01.jpg", "50% 0%", "O QUE O DONO DE PEQUENA<br>E MÉDIA EMPRESA<br>PODE APRENDER", "COM HAVAN<br>X MAGALU.",
     ["Não é sobre quem é melhor empresário. É sobre o que cada uma deixou no caixa."], ""),
    ("img-02.jpg", "50% 40%", "O MAGALU VENDEU", "QUASE 3 VEZES MAIS.",
     ["Em 2025, foram R$ 38,7 bilhões de receita no Magalu e R$ 13,7 bilhões na Havan."], ""),
    ("img-03.jpg", "50% 45%", "E A HAVAN LUCROU", "QUASE 17 VEZES MAIS.",
     ["R$ 3,4 bilhões de lucro na Havan. R$ 205 milhões no Magalu."], ""),
    ("img-04.png", "50% 45%", "DE CADA R$ 100 VENDIDOS,", "QUANTO FICOU.",
     ["Na Havan, mais de R$ 20, mesmo tirando o que ela ganhou na Justiça. No Magalu, 53 centavos.",
      "**Guarda esse número.**"], ""),
    ("img-05.png", "50% 40%", "O JURO COMEU", "O LUCRO DE<br>UMA DELAS.",
     ["Com a Selic em 15%, a despesa financeira levou 5,1% da receita do Magalu no fim do ano. A Havan terminou 2025 com dinheiro sobrando no caixa."], ""),
    ("img-06.png", "50% 45%", "E ISSO NÃO É COISA", "SÓ DE EMPRESA GRANDE.",
     ["Tem muita empresa de 20, 30 milhões que vende mais que o concorrente e sobra menos."], ""),
    ("img-07.jpg", "50% 12%", "FATURAMENTO<br>ENCHE O OLHO.", "LUCRO ENCHE<br>O CAIXA.",
     ["Eu já vi muito dono comemorar recorde de venda e pegar empréstimo no mês seguinte.",
      "**Vender mais não quer dizer sobrar mais.**"], "1ª lição"),
    ("img-08.png", "50% 40%", "QUEM CRESCE EMPRESTADO", "DIVIDE O LUCRO<br>COM O BANCO.",
     ["Lembra dos 53 centavos? Com juro de 15%, cada real devido come o pouco que sobra.",
      "**E o banco recebe antes de você.**"], "2ª lição"),
    ("img-09.png", "50% 40%", "MARGEM SE DECIDE", "ANTES DA VENDA.",
     ["No preço, no desconto e no que você aceita vender sem ganhar.",
      "**Quem não olha a margem vende muito e trabalha de graça.**"], "3ª lição"),
    ("img-10.jpg", "50% 36%", "EM 38 ANOS DE EMPRESA,", "EU APRENDI UMA COISA.",
     ["**Empresa boa não é a que vende mais. É a que sobra mais.**"], ""),
    ("img-11c.jpg", "50% 28%", "E NA SUA EMPRESA,<br>DE CADA R$ 100,", "QUANTO FICA?",
     ["Se você não sabe responder de cabeça, está olhando o número errado.",
      "**Comenta RAIOX que eu te mando o link da aula onde você faz o raio-x da sua empresa.**"], ""),
]

# slides comparativos: (img esquerda Havan, img direita Magalu, rótulo, (prefixo, número, unidade) Havan, idem Magalu, vencedor 'L'/'R', foco L, foco R)
CMP = {
    2: ("cmp2L.jpg", "cmp2R.jpg", "Receita líquida 2025", ("R$", "13,7", "bilhões"), ("R$", "38,7", "bilhões"), "R", "50% 50%", "50% 50%"),
    3: ("cmp3L.jpg", "cmp3R.jpg", "Lucro líquido 2025", ("R$", "3,4", "bilhões"), ("R$", "205", "milhões"), "L", "50% 50%", "50% 50%"),
    4: ("cmp4L.jpg", "cmp4R.jpg", "De cada R$ 100 vendidos, ficaram", ("mais de R$", "20", "de lucro"), ("R$", "0,53", "de lucro"), "L", "50% 50%", "50% 50%"),
    5: ("cmp5L.jpg", "cmp5R.jpg", "Fim de 2025", ("R$", "4,3", "bilhões<br>de caixa líquido"), ("", "5,1%", "da receita<br>pro juro (4º tri)"), "L", "50% 50%", "50% 50%"),
}

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
.kk{display:inline-block;font-size:22px;font-weight:800;letter-spacing:0.16em;text-transform:uppercase;color:#fff;border:2px solid #A91C20;padding:6px 14px;margin-bottom:22px}
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
.half{position:absolute;top:0;width:540px;height:900px;background-size:cover;background-repeat:no-repeat}
.half::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,10,.72) 0,rgba(10,10,10,.62) 50%,rgba(10,10,10,.12) 60%,rgba(10,10,10,.12) 76%,rgba(10,10,10,.6) 100%)}
.fade.fc{background:linear-gradient(180deg,rgba(10,10,10,0) 0px,rgba(10,10,10,0) 690px,rgba(10,10,10,.85) 800px,#0A0A0A 870px)}
.hL{left:0}.hR{left:540px}
.sep{position:absolute;left:537px;top:0;width:6px;height:900px;background:#fff}
.tag{position:absolute;left:0;right:0;top:56px;text-align:center}
.tag span{display:inline-block;background:#0A0A0A;border:2px solid #A91C20;color:#fff;font-weight:800;font-size:24px;letter-spacing:.14em;text-transform:uppercase;padding:10px 22px}
.nb{position:absolute;top:150px;width:540px;text-align:center;padding:0 28px}
.nb .br{font-weight:900;font-size:34px;letter-spacing:.22em;color:#fff;text-transform:uppercase;margin-bottom:22px}
.nb .px{font-weight:800;font-size:30px;color:#fff;text-transform:uppercase;letter-spacing:.04em}
.nb .vl{display:inline-block;font-weight:900;font-size:150px;line-height:1;letter-spacing:-0.03em;color:#fff;padding:8px 18px 12px;margin:6px 0}
.nb .vl.win{background:#A91C20}
.nb .vl.lose{color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.8)}
.nb .un{font-weight:800;font-size:26px;color:#fff;text-transform:uppercase;letter-spacing:.08em;line-height:1.25}
"""


def photo(i, img, pos):
    if i not in CMP:
        return f"<div class=\"ph\" style=\"background-image:url('../imagens/{img}');background-position:{pos}\"></div>"
    l, r, lab, vL, vR, win, pL, pR = CMP[i]
    def nb(side, brand, v, won):
        pre, num, un = v
        return (f'<div class="nb" style="left:{0 if side=="L" else 540}px"><div class="br">{brand}</div>'
                f'<div class="px">{pre}</div><div class="vl {"win" if won else "lose"}">{num}</div><div class="un">{un}</div></div>')
    return (f'<div class="half hL" style="background-image:url(../imagens/{l});background-position:{pL}"></div>'
            f'<div class="half hR" style="background-image:url(../imagens/{r});background-position:{pR}"></div>'
            f'<div class="sep"></div><div class="tag"><span>{lab}</span></div>'
            + nb("L", "Havan", vL, win == "L") + nb("R", "Magalu", vR, win == "R"))


def md(p):
    out, bold = [], False
    for i, part in enumerate(p.split("**")):
        out.append(f"<b>{part}</b>" if i % 2 else part)
    return "".join(out)


for i, (img, pos, l1, l2, body, kick) in enumerate(SLIDES, 1):
    dots = "".join(f'<i class="{"on" if j == i else ""}"></i>' for j in range(1, len(SLIDES) + 1))
    paras = "".join(f"<p>{md(p)}</p>" for p in body)
    seta = " · Arraste" if i < len(SLIDES) else ""
    html = f"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="s">
  {photo(i, img, pos)}
  <div class="fade{' fc' if i in CMP else ''}"></div>
  <div class="txt">
    {f'<div class="kk">{kick}</div>' if kick else ""}
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
