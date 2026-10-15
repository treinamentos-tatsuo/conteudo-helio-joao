// Modelo handmade — biblioteca de desenho a lapis (rough.js). Inclua depois de rough.js.
// Uso na pagina: <svg id="d"><g id="g" filter="url(#pencil)"></g></svg>, depois H.init(INK).
const H = (() => {
  const RED = '#A91C20';
  let svg, G, rc, INK = '#3a3a3a';
  let seed = 0; // semente sequencial: o mesmo script gera sempre o mesmo traco
  const o = (x = {}) => Object.assign({ stroke: INK, strokeWidth: 3, roughness: 1.5, bowing: 1.5, seed: ++seed }, x);
  const add = n => (G.appendChild(n), n);
  const NS = 'http://www.w3.org/2000/svg';
  const api = {
    RED,
    init(ink) { INK = ink || INK; svg = document.getElementById('d'); G = document.getElementById('g'); rc = rough.svg(svg); },
    line(a, b, c, d, x) { return add(rc.line(a, b, c, d, o(x))); },
    circle(x, y, d, opt) { return add(rc.circle(x, y, d, o(opt))); },
    ellipse(x, y, w, h, opt) { return add(rc.ellipse(x, y, w, h, o(opt))); },
    rect(x, y, w, h, opt) { return add(rc.rectangle(x, y, w, h, o(opt))); },
    path(d, opt) { return add(rc.path(d, o(opt))); },
    poly(pts, opt) { return add(rc.linearPath(pts, o(opt))); },
    curve(pts, opt) { return add(rc.curve(pts, o(opt))); },
    text(s, x, y, size, color, anchor, weight) {
      const t = document.createElementNS(NS, 'text');
      t.setAttribute('x', x); t.setAttribute('y', y); t.setAttribute('text-anchor', anchor || 'middle');
      t.setAttribute('font-family', 'Kalam'); t.setAttribute('font-size', size || 30);
      t.setAttribute('font-weight', weight || 400); t.setAttribute('fill', color || INK); t.textContent = s;
      (document.getElementById('gt') || svg).appendChild(t); return t;
    },
    // seta curva com ponta aberta; bend > 0 curva pra esquerda
    arrow(x1, y1, x2, y2, opt, bend) {
      opt = Object.assign({ stroke: RED, strokeWidth: 4 }, opt || {}); bend = bend === undefined ? .18 : bend;
      const mx = (x1 + x2) / 2 + (y2 - y1) * bend, my = (y1 + y2) / 2 - (x2 - x1) * bend;
      add(rc.curve([[x1, y1], [mx, my], [x2, y2]], o(opt)));
      const ang = Math.atan2(y2 - my, x2 - mx);
      for (const s of [-1, 1]) { const k = ang + Math.PI + s * .45; api.line(x2, y2, x2 + 28 * Math.cos(k), y2 + 28 * Math.sin(k), opt); }
    },
    rabisco(x, y, w, h) { // circulo rabiscado em vermelho, duas voltas
      api.ellipse(x, y, w, h, { stroke: RED, strokeWidth: 4, roughness: 2.2 });
      api.ellipse(x + 4, y - 3, w + 12, h + 8, { stroke: RED, strokeWidth: 3, roughness: 2.6 });
    },
    xis(x, y, s, opt) { s = s || 30; opt = Object.assign({ stroke: RED, strokeWidth: 5 }, opt || {}); api.line(x - s, y - s, x + s, y + s, opt); api.line(x + s, y - s, x - s, y + s, opt); },
    // boneco de palito, traco minimo. (x,y) = centro da cabeca
    boneco(x, y, s, pose, opt) {
      s = s || 1; const h = 30 * s; api.circle(x, y, h * 2, opt);
      const ny = y + h, hy = ny + 72 * s, sh = ny + 22 * s;
      api.line(x, ny, x, hy, opt);
      const A = { neutro: [[-38, 42], [38, 42]], acena: [[-38, 42], [36, -34]], bracos: [[-52, -12], [52, -12]],
        corre: [[-46, 18], [42, 52]], aponta: [[-36, 42], [62, 0]], maos_cabeca: [[-26, -40], [26, -40]],
        segura: [[-30, 46], [44, 20]], apito: [[-36, 42], [10, -28]], relax: [[-26, -40], [26, -40]], carrega: [[-44, -80], [44, -80]] }[pose || 'neutro'] || [[-38, 42], [38, 42]];
      api.line(x, sh, x + A[0][0] * s, sh + A[0][1] * s, opt); api.line(x, sh, x + A[1][0] * s, sh + A[1][1] * s, opt);
      const L = pose === 'corre' ? [[-42, 56], [34, 62]] : (pose === 'sentado' || pose === 'relax') ? [[34, 4], [30, 6]] : [[-24, 70], [24, 70]];
      api.line(x, hy, x + L[0][0] * s, hy + L[0][1] * s, opt); api.line(x, hy, x + L[1][0] * s, hy + L[1][1] * s, opt);
      if (pose === 'sentado' || pose === 'relax') { api.line(x + 34 * s, hy + 4 * s, x + 34 * s, hy + 60 * s, opt); api.line(x + 30 * s, hy + 6 * s, x + 30 * s, hy + 62 * s, opt); }
      return { maoE: [x + A[0][0] * s, sh + A[0][1] * s], maoD: [x + A[1][0] * s, sh + A[1][1] * s], pe: hy + 70 * s };
    },
    // marcacoes a lapis nas palavras do texto: <span class="u"> sublinha, <span class="u2"> sublinha duplo, <span class="o"> circula
    decorar() {
      const D = document.getElementById('gd') || G, prev = G; G = D;
      document.querySelectorAll('.u,.u2').forEach(el => [...el.getClientRects()].forEach(r => {
        const y = r.bottom - 4; api.line(r.left + 2, y, r.right - 2, y - 3, { stroke: RED, strokeWidth: 4, roughness: 1.2, bowing: 2 });
        if (el.classList.contains('u2')) api.line(r.left + 10, y + 10, r.right - 8, y + 8, { stroke: RED, strokeWidth: 3, roughness: 1.2, bowing: 2 });
      }));
      document.querySelectorAll('.o').forEach(el => { const r = el.getBoundingClientRect();
        api.ellipse((r.left + r.right) / 2, (r.top + r.bottom) / 2 + 2, r.width + 22, r.height + 14, { stroke: RED, strokeWidth: 3.5, roughness: 1.4 }); });
      G = prev;
    },
    cone(x, y, s) { s = s || 1; api.path(`M${x - 16 * s},${y} L${x},${y - 34 * s} L${x + 16 * s},${y} Z`, { strokeWidth: 2.5, fill: RED, fillStyle: 'hachure', hachureGap: 6, fillWeight: 1.2, stroke: RED }); },
    bola(x, y, d) { api.circle(x, y, d, { fill: INK, fillStyle: 'hachure', hachureGap: 7, fillWeight: 1.4 }); },
    balao(x, y, w, h, txt, size, cor, rabo) { // balao de fala com rabinho apontando pra (rabo[0], rabo[1])
      api.ellipse(x, y, w, h, { strokeWidth: 3 });
      if (rabo) api.poly([[x - w * .12, y + h * .38], rabo, [x + w * .05, y + h * .45]], { strokeWidth: 3 });
      if (txt) api.text(txt, x, y + (size || 30) * .35, size || 30, cor || INK, 'middle', 700);
    },
    chama(x, y, s) { // foguinho de tres linguas: base larga, lingua do meio mais alta
      s = s || 1; const P = (dx, dy) => `${x + dx * s},${y + dy * s}`;
      api.path(`M${P(-30, 0)} C${P(-44, -26)} ${P(-30, -44)} ${P(-24, -58)} C${P(-16, -42)} ${P(-14, -38)} ${P(-10, -40)} C${P(-12, -64)} ${P(-2, -84)} ${P(6, -100)}`
        + ` C${P(12, -76)} ${P(22, -62)} ${P(16, -46)} C${P(24, -50)} ${P(28, -58)} ${P(30, -66)} C${P(46, -40)} ${P(42, -14)} ${P(30, 0)} Z`,
        { stroke: RED, strokeWidth: 3.5, fill: RED, fillStyle: 'hachure', hachureGap: 8, fillWeight: 1.6 });
      api.path(`M${P(-12, 0)} C${P(-20, -16)} ${P(-8, -30)} ${P(0, -44)} C${P(8, -30)} ${P(18, -16)} ${P(12, 0)}`, { stroke: RED, strokeWidth: 2.5 });
    },
    relogio(x, y, d, hora) { api.circle(x, y, d, { strokeWidth: 3.5 }); api.line(x, y, x, y - d * .34, { strokeWidth: 4 }); api.line(x, y, x + d * .22, y + d * .1, { strokeWidth: 4 });
      for (let i = 0; i < 12; i++) { const a = i * Math.PI / 6; api.line(x + Math.cos(a) * d * .42, y + Math.sin(a) * d * .42, x + Math.cos(a) * d * .47, y + Math.sin(a) * d * .47, { strokeWidth: 2 }); } },
    celular(x, y, w, h) { api.rect(x, y, w, h, { strokeWidth: 3.5 }); api.rect(x + 10, y + 22, w - 20, h - 60, { strokeWidth: 2 }); api.circle(x + w / 2, y + h - 20, 14, { strokeWidth: 2 });
      for (const k of [1, 2, 3]) api.curve([[x + w + 8 * k, y + 20 - 6 * k], [x + w + 16 * k, y + 40], [x + w + 8 * k, y + 60 + 6 * k]], { stroke: RED, strokeWidth: 3 }); },
    campo(x, y, w, h) { api.rect(x, y, w, h, { strokeWidth: 3 }); api.line(x + w / 2, y, x + w / 2, y + h, { strokeWidth: 2.5 }); api.circle(x + w / 2, y + h / 2, h * .32, { strokeWidth: 2.5 });
      api.rect(x, y + h * .3, w * .1, h * .4, { strokeWidth: 2.5 }); api.rect(x + w * .9, y + h * .3, w * .1, h * .4, { strokeWidth: 2.5 }); },
    balcao(x, y, w) { api.rect(x, y, w, 90, { strokeWidth: 3, fill: INK, fillStyle: 'hachure', hachureGap: 14, fillWeight: 1 }); },
  };
  return api;
})();
