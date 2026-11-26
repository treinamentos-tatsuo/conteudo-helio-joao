"""Monta os 10 HTMLs do J423 (carrossel notícia). Foto no topo, fundo preto embaixo,
título Montserrat 900 com a 2ª linha numa placa carmim, corpo em branco."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "instagram"
OUT.mkdir(exist_ok=True)

# img, posição do foco (background-position), l1, l2, corpo (lista de parágrafos; ** = negrito)
SLIDES = [
    ("img-01.jpg", "50% 0%", "O QUE O DONO DE PEQUENA<br>E MÉDIA EMPRESA<br>PODE APRENDER", "COM HAVAN X MAGALU.",
     ["Não é sobre quem é melhor empresário. É sobre o que cada uma deixou no caixa."], ""),
    ("INFO", "", "", "", [], ""),
    ("img-06.png", "50% 45%", "E ISSO NÃO É COISA", "SÓ DE EMPRESA GRANDE.",
     ["Tem muita empresa de 20, 30 milhões que vende mais que o concorrente e sobra menos."], ""),
    ("img-07.jpg", "50% 12%", "FATURAMENTO<br>ENCHE O OLHO.", "LUCRO ENCHE<br>O CAIXA.",
     ["Eu já vi muito dono comemorar recorde de venda e pegar empréstimo no mês seguinte.",
      "**Vender mais não quer dizer sobrar mais.**"], "1ª lição"),
    ("img-12.png", "50% 45%", "CRESCER A QUALQUER CUSTO", "CUSTA O LUCRO.",
     ["Lembra dos 53 centavos? Quem corre atrás de volume vende mais e fica com menos.",
      "**Eu já vi muito dono dobrar de tamanho<br>e dobrar o problema.**"], "2ª lição"),
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
CMP_V1 = {
    2: ("cmp2L.jpg", "cmp2R.jpg", "Receita líquida 2025", ("R$", "13,7", "bilhões"), ("R$", "38,7", "bilhões"), "R", "50% 50%", "50% 50%"),
    3: ("cmp3L.jpg", "cmp3R.jpg", "Lucro líquido 2025", ("R$", "3,4", "bilhões"), ("R$", "205", "milhões"), "L", "50% 50%", "50% 50%"),
    4: ("cmp4L.jpg", "cmp4R.jpg", "De cada R$ 100 vendidos, ficaram", ("mais de R$", "20", "de lucro"), ("R$", "0,53", "de lucro"), "L", "50% 50%", "50% 50%"),
    5: ("cmp5L.jpg", "cmp5R.jpg", "Fim de 2025", ("R$", "4,3", "bilhões<br>de caixa líquido"), ("", "5,1%", "da receita<br>pro juro (4º tri)"), "L", "50% 50%", "50% 50%"),
}

INFO_ROWS = [
    ("Receita líquida 2025", ("R$ 13,7 bi", ""), ("R$ 38,7 bi", ""), "R"),
    ("Lucro líquido 2025", ("R$ 3,4 bi", ""), ("R$ 205 mi", ""), "L"),
    ("De cada R$ 100 vendidos, ficaram", ("R$ 20+", "mesmo sem o ganho na Justiça"), ("R$ 0,53", ""), "L"),
    ("Juros em 2025", ("+R$ 800 mi", "recebeu de receita financeira"), ("−R$ 2 bi", "pagou de despesa financeira"), "L"),
]
INFO_CSS = """
.ih{position:absolute;left:0;right:0;top:52px;text-align:center}
.ih h2{font-weight:900;font-size:76px;letter-spacing:-0.02em;line-height:1}
.ih p{margin-top:14px;font-weight:700;font-size:26px;letter-spacing:.16em;text-transform:uppercase;color:#BDBDBD}
.cards{position:absolute;top:212px;left:56px;right:56px;display:flex;gap:28px}
.card{flex:1;height:170px;background-size:cover;background-position:center;border:2px solid #2A2A2A;position:relative}
.card span{position:absolute;left:0;right:0;bottom:0;background:rgba(10,10,10,.82);text-align:center;font-weight:900;font-size:28px;letter-spacing:.2em;padding:8px 0}
.rows{position:absolute;top:410px;left:56px;right:56px}
.row{position:relative;height:160px;border-top:1px solid #2A2A2A}
.row .lb{text-align:center;padding-top:16px;font-weight:700;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:#9A9A9A}
.row .c{position:absolute;top:56px;width:440px;text-align:center}
.row .c.l{left:0}.row .c.r{right:0}
.row .v{display:inline-block;font-weight:900;font-size:62px;line-height:1;letter-spacing:-0.02em;padding:6px 14px 8px}
.row .v.win{background:#A91C20}
.row .u{margin-top:6px;font-weight:600;font-size:19px;color:#BDBDBD;text-transform:uppercase;letter-spacing:.06em}
.row .vs{position:absolute;left:50%;top:66px;transform:translateX(-50%);width:54px;height:54px;border-radius:50%;border:2px solid #A91C20;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:20px}
.bar{position:absolute;left:56px;right:56px;top:1066px;background:#A91C20;padding:20px 26px}
.bar b{display:block;font-weight:900;font-size:31px;text-transform:uppercase;letter-spacing:-0.01em}
.bar i{display:block;font-style:normal;margin-top:6px;font-weight:600;font-size:24px}
"""


def info_html(i, n, dots):
    rows = "".join(
        f'<div class="row"><div class="lb">{lb}</div>'
        f'<div class="c l"><div class="v {"win" if w=="L" else ""}">{hl[0]}</div><div class="u">{hl[1]}</div></div>'
        f'<div class="vs">VS</div>'
        f'<div class="c r"><div class="v {"win" if w=="R" else ""}">{hr[0]}</div><div class="u">{hr[1]}</div></div></div>'
        for lb, hl, hr, w in INFO_ROWS)
    return f"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}{INFO_CSS}</style></head><body>
<div class="s">
  <div class="ih"><h2>HAVAN X MAGALU</h2><p>Os números de 2025, lado a lado</p></div>
  <div class="cards"><div class="card" style="background-image:url(../imagens/card-havan.jpg)"></div>
  <div class="card" style="background-image:url(../imagens/card-magalu.jpg)"></div></div>
  <div class="rows">{rows}</div>
  <div class="bar"><b>O Magalu vendeu quase 3x mais. E lucrou 17x menos.</b><i>De cada R$ 100, ficaram 53 centavos. Guarda esse número.</i></div>
  <div class="ft"><div class="h"><span class="dm"></span>@helio.tatsuo · Arraste</div><div class="dots">{dots}</div></div>
</div></body></html>"""

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
    if i not in CMP_V1 or True:
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
    if img == "INFO":
        (OUT / f"slide-{i:02d}.html").write_text(info_html(i, len(SLIDES), dots), encoding="utf-8")
        continue
    html = f"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="s">
  {photo(i, img, pos)}
  <div class="fade"></div>
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
