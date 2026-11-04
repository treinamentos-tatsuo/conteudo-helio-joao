#!/usr/bin/env python3
"""Gera os 11 HTMLs do carrossel J326 (editorial-punch, "Geração passada e geração atual", 04/11).
Layout da skill (modelo.md, 11/09: corpo top 240, capa 280; Source Serif 44; Anton só nos gritos)."""
import json, pathlib
SCR = pathlib.Path(__file__).parent
OUT = SCR.parent / "instagram"; OUT.mkdir(exist_ok=True)
def _j(name):
    try: return {int(k): v for k, v in json.loads((SCR/name).read_text(encoding='utf-8')).items()}
    except FileNotFoundError: return {}
HEIGHT, FADE, ANTON = _j("imgheight.json"), _j("fade.json"), _j("antonfit.json")
OBJPOS = {}
HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:ital,wght@0,400;0,600;0,700;1,400;1,700&family=Anton&display=swap" rel="stylesheet">
<style>
  *{ margin:0; padding:0; box-sizing:border-box; }
  .slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
    background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
    font-family:'Source Serif Pro',serif; }
  .top{ position:absolute; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
  .stanza + .stanza{ margin-top:34px; }
  .line{ font-size:44px; line-height:1.32; font-weight:600; color:#1A1A1A; }
  .line b{ font-weight:700; }
  .red{ color:#A91C20; font-weight:700; }
  .anton{ font-family:'Anton',sans-serif; font-weight:400; text-transform:uppercase; line-height:1.36; letter-spacing:0.5px; color:#A91C20; }
  .cta-big{ font-size:64px; font-weight:700; line-height:1.2; color:#1A1A1A; }
</style>
</head>
<body>
"""
def mask(F):
    if F <= 26: return f"linear-gradient(to bottom,transparent 0%,#000 {F}%)"
    return (f"linear-gradient(to bottom,transparent 0%,rgba(0,0,0,0.06) {F*0.25:.1f}%,rgba(0,0,0,0.30) {F*0.55:.1f}%,"
            f"rgba(0,0,0,0.72) {F*0.80:.1f}%,#000 {F:.1f}%)")
def img(n):
    h = HEIGHT.get(n); pos = OBJPOS.get(n, "center bottom")
    box = f'height:{h}px;object-fit:cover;object-position:{pos};' if h else ''
    m = mask(FADE.get(n, 26))
    return (f'<img src="../imagens/img-{n:02d}.png" alt="" onerror="this.style.display=\'none\'" '
            f'style="position:absolute;bottom:0;left:0;width:100%;{box}mix-blend-mode:multiply;'
            f'-webkit-mask-image:{m};mask-image:{m};z-index:1;">')
cur = [0]
def slide(n, body, top=240, fs=None):
    override = f'<style>.line:not(.anton){{font-size:{fs}px}}</style>\n' if fs else ""
    html = HEAD + override + f'  <div class="slide">\n    {img(n)}\n    <div class="top" style="top:{top}px">\n{body}    </div>\n  </div>\n</body>\n</html>\n'
    (OUT / f"slide-{n:02d}.html").write_text(html, encoding='utf-8'); print(f"slide-{n:02d}.html")
def st(*lines, mt=None):
    parts = []
    for txt, cls in lines:
        style = f' style="font-size:{ANTON.get(cur[0], 90)}px"' if "anton" in cls else ""
        parts.append(f'        <div class="line{cls}"{style}>{txt}</div>')
    extra = f' style="margin-top:{mt}px"' if mt else ""
    return f'      <div class="stanza"{extra}>\n' + "\n".join(parts) + '\n      </div>\n'
B, R, A = "", " red", " anton"
def at(n): cur[0] = n; return n
slide(at(1),  st(("Você lidera", B)) + st(("GERAÇÃO PASSADA E GERAÇÃO ATUAL", A), mt=4)
            + st(("do mesmo jeito.", B), mt=4) + st(("POR ISSO PERDE OS DOIS.", A), mt=26), top=250, fs=50)
slide(at(2),  st(("Todo dono me conta a mesma briga:", B), ("o gerente diz que o menino novo é fraco.", B), ("O menino diz que o gerente só sabe mandar.", B))
            + st(("E o dono no meio, apagando incêndio,", B), ("achando que o problema é de gente.", R)), fs=42)
slide(at(3),  st(("O seu gerente é da geração passada:", B), ("começou quando emprego bom era raro,", B), ("engoliu chefe ruim e virou noite sem hora extra.", B))
            + st(("Hoje ele quer ser reconhecido", B), ("por tudo que aguentou.", R)), fs=40)
slide(at(4),  st(("O menino é da geração atual:", B), ("chegou com vaga sobrando e não vai", B), ("engolir chefe ruim, porque não precisa.", B))
            + st(("Antes de fazer qualquer coisa,", B), ("ele quer saber pra que serve aquilo.", R)), fs=42)
slide(at(5),  st(("O seu gerente aprendeu a esperar", B), ("a avaliação do fim do ano.", B), ("O menino quer retorno toda semana.", B))
            + st(("Guardou o elogio e a bronca pra dezembro?", B), ("Em agosto ele já pediu as contas.", R)), fs=40)
slide(at(6),  st(("Pro gerente, a ordem bem dada basta.", B), ("Pro menino, ordem sem explicação", B), ("é capricho de chefe.", B))
            + st(("Explicar o porquê não é frescura.", B), ("É o que faz ele acertar sem você olhando.", R)), fs=40)
slide(at(7),  st(("O gerente quer ver o próximo degrau:", B), ("qual cargo, quanto ganha e quando.", B))
            + st(("O menino quer saber o que vai aprender aqui.", B), ("Parou de aprender, vai embora,", R), ("mesmo ganhando bem.", R)), fs=40)
slide(at(8),  st(("E aí vem o erro de quase todo dono:", B), ("liderar todo mundo do mesmo jeito.", B))
            + st(("Normalmente, do jeito que ele foi liderado", B), ("trinta anos atrás.", R)), fs=44)
slide(at(9),  st(("Eu não estou falando pra você amolecer.", B), ("A meta é a mesma pros dois,", B), ("e a cobrança também.", B))
            + st(("O que muda é o caminho", B), ("que você mostra pra cada um chegar nela.", R)), fs=42)
slide(at(10), st(("Eu tenho um treinamento de gestão", B), ("pra donos de pequena e média empresa,", B))
            + st(("onde eu ensino a montar a cultura", B), ("que segura gente boa de qualquer idade.", R)), fs=44)
slide(at(11), st(("Quer o seu gerente e o menino de 22", B), ("batendo a mesma meta?", B))
            + '      <div class="cta-big" style="margin-top:34px">Comenta <span class="red">LIDERAR</span></div>\n'
            + st(("que eu mando o link no seu direct.", B), mt=18), fs=46)
