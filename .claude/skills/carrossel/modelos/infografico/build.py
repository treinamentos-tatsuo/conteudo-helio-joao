"""Modelo infografico — gerador de slides (HTML autocontido, 1080x1350).

Uso a partir do _scripts/ de um post (acha a raiz do projeto subindo as pastas, sem caminho fixo de usuario):
    import sys, pathlib
    RAIZ = next(p for p in pathlib.Path(__file__).resolve().parents if (p / '.claude/skills/carrossel').is_dir())
    sys.path.insert(0, str(RAIZ / '.claude/skills/carrossel/modelos/infografico'))
    import build
    build.escrever(POST_DIR, {2: spec_slide2, 3: spec_slide3})
    # depois: node .../infografico/render.js POST_DIR/instagram

Cada spec e um dict com chaves opcionais: titulo, faixa, cards, hub, colunas, fluxo, funil, caixa, logo, css.
Camadas: fundo = arquivo do banco (nunca desenhado aqui) -> elementos (base.css) -> icones do kit -> texto.
"""
import base64
import html
import pathlib
import re

AQUI = pathlib.Path(__file__).parent
FUNDO_REL = '../../_banco-referencias/background infografico escuro.png'   # relativo a <post>/instagram/


def _css():
    return (AQUI / 'base.css').read_text()


def _logo_uri():
    return 'data:image/png;base64,' + base64.b64encode((AQUI / 'logo-simbolo.png').read_bytes()).decode()


def icone(nome, px, traco=1.2):
    svg = (AQUI / 'icones' / f'{nome}.svg').read_text()
    svg = re.sub(r'width="24"', f'width="{px}"', svg, count=1)
    svg = re.sub(r'height="24"', f'height="{px}"', svg, count=1)
    svg = svg.replace('stroke="currentColor"', 'stroke="#ffffff"', 1).replace('stroke-width="2"', f'stroke-width="{traco}"', 1)
    svg = re.sub(r'class="[^"]*"', '', svg, count=1)
    return svg


def _t(s):
    """escapa e permite <br> e <em> vindos do spec."""
    s = html.escape(s, quote=False)
    return s.replace('&lt;br&gt;', '<br>').replace('&lt;em&gt;', '<em>').replace('&lt;/em&gt;', '</em>')


def _titulo(sp):
    t = sp.get('titulo')
    if not t:
        return ''
    top, px = sp.get('titulo_top', 112), sp.get('titulo_px', 93)
    return f'<div class="titulo solo" style="top:{top}px;font-size:{px}px">{_t(t)}</div>'


def _faixa(sp):
    f = sp.get('faixa')
    if not f:
        return ''
    top = sp.get('faixa_top', 238)
    cls = 'faixa solo' + (' forte' if sp.get('faixa_forte') else '')
    px = sp.get('faixa_px')
    st = f'top:{top}px' + (f';font-size:{px}px' if px else '')
    return f'<div class="{cls}" style="{st}">{_t(f)}</div>'


def _cards(c):
    itens = c['itens']            # [(num, titulo, texto)]
    cols = c.get('colunas', 2)
    w, h = c.get('largura', 440), c['altura']
    gx, gy = c.get('gap_x', 40), c.get('gap_y', 72)
    top = c['top']
    total_w = cols * w + (cols - 1) * gx
    x0 = (1080 - total_w) / 2
    out = []
    for i, (n, tit, txt) in enumerate(itens):
        row, col = divmod(i, cols)
        x = x0 + col * (w + gx)
        if c.get('ultimo_centralizado', True) and i == len(itens) - 1 and len(itens) % cols == 1 and cols > 1:
            x = (1080 - w) / 2
        y = top + row * (h + gy)
        longo = ' class="long"' if len(tit) > c.get('limite_titulo_curto', 18) else ''
        ptxt = f'<p style="font-size:{c["corpo_px"]}px">{_t(txt)}</p>' if c.get('corpo_px') else f'<p>{_t(txt)}</p>'
        out.append(f'<div class="card solo" style="left:{x:.0f}px;top:{y:.0f}px;width:{w}px;height:{h}px">'
                   f'<div class="num">{n}</div><h3{longo}>{_t(tit)}</h3>{ptxt}</div>')
    return '\n'.join(out)


def _hub(hb):
    d, cx, cy = hb['d'], hb['cx'], hb['cy']
    out = [f'<div class="hub solo" style="left:{cx-d/2:.0f}px;top:{cy-d/2:.0f}px;width:{d}px;height:{d}px">'
           f'<span style="font-size:{hb.get("fonte", 40)}px">{_t(hb["texto"])}</span></div>']
    for no in hb.get('nos', []):   # dict: icone, rotulo, desc, x (centro), y (topo), w
        w = no.get('w', 270)
        ic = icone(no['icone'], no.get('icone_px', 86)) if no.get('icone') else ''
        desc = f'<div class="desc">{_t(no["desc"])}</div>' if no.get('desc') else ''
        out.append(f'<div class="no solo" style="left:{no["x"]-w/2:.0f}px;top:{no["y"]}px;width:{w}px">{ic}'
                   f'<div class="txt"><div class="rotulo" style="font-size:{no.get("rotulo_px", 27)}px">{_t(no["rotulo"])}</div>{desc}</div></div>')
    return '\n'.join(out)


def _colunas(cl):
    cols = cl['itens']            # dict: titulo, sub, icone, itens(list) | texto
    w, h, top = cl.get('largura', 450), cl['altura'], cl['top']
    gx = cl.get('gap_x', 36)
    x0 = (1080 - (len(cols) * w + (len(cols) - 1) * gx)) / 2
    out = []
    for i, c in enumerate(cols):
        x = x0 + i * (w + gx)
        ic = f'<div style="margin:0 auto 14px;width:{c.get("icone_px", 80)}px">{icone(c["icone"], c.get("icone_px", 80))}</div>' if c.get('icone') else ''
        sub = f'<div class="sub">{_t(c["sub"])}</div>' if c.get('sub') else ''
        corpo = ''
        if c.get('itens'):
            corpo = '<ul>' + ''.join(f'<li>{_t(li)}</li>' for li in c['itens']) + '</ul>'
        elif c.get('texto'):
            corpo = f'<p class="txt" style="margin-top:18px;font-size:{cl.get("texto_px", 25)}px;line-height:1.28;text-align:center">{_t(c["texto"])}</p>'
        out.append(f'<div class="coluna solo" id="col-{i+1}" style="left:{x:.0f}px;top:{top}px;width:{w}px;height:{h}px">{ic}<h3>{_t(c["titulo"])}</h3>{sub}{corpo}</div>')
    if cl.get('meio'):   # simbolo entre as colunas (ex: x)
        out.append(f'<div class="solo" style="position:absolute;left:{540-30}px;top:{top + h/2 - 40:.0f}px;width:60px;text-align:center;'
                   f'font-family:Anton,sans-serif;font-size:64px;color:#fff">{_t(cl["meio"])}</div>')
    return '\n'.join(out)


def _fluxo(fl):
    itens, top = fl['itens'], fl['top']
    w, h, seta = fl.get('largura', 270), fl.get('altura', 86), fl.get('seta', 54)
    total = len(itens) * w + (len(itens) - 1) * seta
    x = (1080 - total) / 2
    out = []
    for i, it in enumerate(itens):
        out.append(f'<div class="solo" style="position:absolute;left:{x:.0f}px;top:{top}px;width:{w}px;height:{h}px;border-radius:12px;'
                   f'background:#141414;border:2px solid #82211f;display:flex;align-items:center;justify-content:center;text-align:center;'
                   f'font-family:Montserrat,sans-serif;font-weight:700;font-size:{fl.get("px", 21)}px;line-height:1.2;text-transform:uppercase;padding:0 12px">{_t(it)}</div>')
        x += w
        if i < len(itens) - 1:
            out.append(f'<div style="position:absolute;left:{x:.0f}px;top:{top}px;width:{seta}px;height:{h}px;display:flex;align-items:center;'
                       f'justify-content:center;font-family:Anton,sans-serif;font-size:40px;color:#d6322c">&rarr;</div>')
            x += seta
    return '\n'.join(out)


def _funil(fn):
    degraus, top = fn['degraus'], fn['top']      # (rotulo, qtd, taxa|None)
    h, gap = fn.get('altura', 118), fn.get('gap', 14)
    wmax, wmin = fn.get('wmax', 820), fn.get('wmin', 380)
    n = len(degraus)
    out = []
    for i, (rot, qtd, taxa) in enumerate(degraus):
        wt = wmax - (wmax - wmin) * i / n
        wb = wmax - (wmax - wmin) * (i + 1) / n
        y = top + i * (h + gap)
        x = (1080 - wt) / 2
        ins = (wt - wb) / 2 / wt * 100
        cor = fn.get('cores', ['#6e1d22', '#651b1f', '#5c181b', '#531518', '#8e1f1f'])[i % 5]
        tx = f'<span style="font-weight:700;font-size:23px;text-transform:uppercase">{_t(rot)}</span>' \
             f'<span style="font-family:Anton,sans-serif;font-size:44px;margin-left:18px">{_t(qtd)}</span>'
        out.append(f'<div class="solo" style="position:absolute;left:{x:.0f}px;top:{y}px;width:{wt:.0f}px;height:{h}px;background:{cor};'
                   f'clip-path:polygon(0 0,100% 0,{100-ins:.2f}% 100%,{ins:.2f}% 100%);display:flex;align-items:center;justify-content:center">{tx}</div>')
        if taxa:
            out.append(f'<div style="position:absolute;left:{x + wt + 16:.0f}px;top:{y - gap/2 - 18:.0f}px;font-family:Montserrat,sans-serif;'
                       f'font-weight:800;font-size:26px;color:#d6322c">{_t(taxa)}</div>')
    return '\n'.join(out)


def _caixa(cx):
    cls = 'caixa solo' + (' preta' if cx.get('estilo') == 'preta' else '')
    st = f'top:{cx["top"]}px;width:{cx.get("largura", 880)}px' + (f';font-size:{cx["px"]}px' if cx.get('px') else '')
    return f'<div class="{cls}" style="{st}">{_t(cx["texto"])}</div>'


def slide_html(sp):
    partes = [_titulo(sp), _faixa(sp)]
    for chave, fn in (('cards', _cards), ('hub', _hub), ('colunas', _colunas), ('fluxo', _fluxo), ('funil', _funil)):
        if sp.get(chave):
            blocos = sp[chave] if isinstance(sp[chave], list) else [sp[chave]]
            partes += [fn(b) for b in blocos]
    if sp.get('caixa'):
        partes.append(_caixa(sp['caixa']))
    if sp.get('logo', True):
        partes.append(f'<img class="logo solo" src="{_logo_uri()}" style="top:{sp.get("logo_top", 1226)}px" alt="">')
    corpo = '\n'.join(p for p in partes if p)
    return (f'<!doctype html><html lang="pt-br"><head><meta charset="utf-8"><style>{_css()}\n{sp.get("css", "")}</style></head>'
            f'<body><div class="slide"><img class="fundo" src="{FUNDO_REL}" alt="">'
            f'<div class="conteudo">{corpo}</div></div></body></html>')


def escrever(post_dir, slides):
    """slides: {numero_do_slide_no_carrossel: spec}. Grava instagram/slide-NN.html."""
    d = pathlib.Path(post_dir) / 'instagram'
    d.mkdir(parents=True, exist_ok=True)
    for n, sp in slides.items():
        (d / f'slide-{n:02d}.html').write_text(slide_html(sp))
    return d
