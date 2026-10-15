// Modelo infografico — renderiza os slide-*.html de uma pasta em PNG 1080x1350 e roda a regua.
// Uso: node .claude/skills/carrossel/modelos/infografico/render.js <pasta-instagram> [slide-01.html ...]
// Regua (falha = corrigir antes de mostrar):
//   1) nenhum texto estoura o proprio conteiner (scrollHeight/scrollWidth > client + 1);
//   2) nenhum elemento de conteudo sai da pagina;
//   3) nenhum titulo de card encosta no circulo do numero;
//   4) elementos marcados .solo nao se sobrepoem entre si.
// Playwright vem do node_modules do projeto: procura a partir da pasta atual e da pasta deste arquivo (sem caminho fixo de usuario).
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), __dirname] }));
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = path.resolve(process.argv[2] || '.');
  const pick = process.argv.slice(3);
  const files = (pick.length ? pick : fs.readdirSync(dir).filter(f => /^slide-\d+\.html$/.test(f))).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  let falhas = 0;
  for (const f of files) {
    await page.goto(`file://${path.join(dir, f)}`);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(900);
    const problemas = await page.evaluate(() => {
      const out = [];
      const r = el => el.getBoundingClientRect();
      const nome = el => (el.className || el.tagName) + ' "' + (el.textContent || '').trim().slice(0, 40) + '"';
      document.querySelectorAll('.conteudo *').forEach(el => {
        const cs = getComputedStyle(el);
        if (cs.overflow !== 'visible' || ['P', 'H3', 'LI', 'SPAN', 'DIV'].includes(el.tagName)) {
          if (el.scrollHeight > el.clientHeight + 1 && el.clientHeight > 0 && cs.overflowY !== 'visible')
            out.push('estoura (altura): ' + nome(el));
        }
        const b = r(el);
        if (b.width && (b.left < -1 || b.top < -1 || b.right > 1081 || b.bottom > 1351))
          out.push('sai da pagina: ' + nome(el));
      });
      document.querySelectorAll('.card, .coluna, .caixa').forEach(box => {
        const bb = r(box);
        box.querySelectorAll('h3, p, li, .sub').forEach(t => {
          const tb = r(t);
          if (tb.bottom > bb.bottom - 6 || tb.right > bb.right + 1) out.push('texto encosta/estoura o card: ' + nome(t));
        });
        const num = box.querySelector('.num');
        const h3 = box.querySelector('h3');
        if (num && h3) {
          const nb = r(num), hb = r(h3);
          // mede a largura real do texto do titulo (linha a linha)
          const range = document.createRange(); range.selectNodeContents(h3);
          for (const lr of range.getClientRects()) {
            if (lr.top < nb.bottom - 2 && lr.bottom > nb.top && lr.right > nb.left - 4 && lr.left < nb.right + 4)
              out.push('titulo bate no circulo do numero: ' + nome(h3));
          }
        }
      });
      document.querySelectorAll('.hub').forEach(h => {
        const hb = r(h), sp = h.querySelector('span');
        if (!sp) return;
        const range = document.createRange(); range.selectNodeContents(sp);
        const cx = hb.left + hb.width / 2, cy = hb.top + hb.height / 2, raio = hb.width / 2 - 14;
        for (const lr of range.getClientRects()) {
          for (const [px, py] of [[lr.left, lr.top], [lr.right, lr.top], [lr.left, lr.bottom], [lr.right, lr.bottom]])
            if (Math.hypot(px - cx, py - cy) > raio) { out.push('texto do hub encosta na borda do circulo: ' + nome(sp)); return; }
        }
      });
      // area de seguranca (regra do user, 07/10): 90 px nas laterais, 110 px em cima e embaixo; o logo pode ficar na faixa de baixo, a 60 px da borda
      document.querySelectorAll('.solo').forEach(el => {
        const b = r(el); if (!b.width) return;
        if (el.classList.contains('logo')) { if (b.bottom > 1290 || b.left < 90 || b.right > 990) out.push('logo fora da margem: ' + nome(el)); return; }
        let box = b;
        const range = document.createRange(); range.selectNodeContents(el);
        const tr = [...range.getClientRects()].filter(x => x.width);
        if (getComputedStyle(el).backgroundColor === 'rgba(0, 0, 0, 0)' && !el.querySelector('img,svg') && tr.length)
          box = { left: Math.min(...tr.map(x => x.left)), right: Math.max(...tr.map(x => x.right)), top: b.top, bottom: b.bottom };   // horizontal pelo texto real; vertical pela caixa (a caixa da fonte Anton passa da linha)
        if (box.left < 89 || box.right > 991 || box.top < 109 || box.bottom > 1241) out.push('fora da area de seguranca (90/110 px): ' + nome(el));
      });
      const solos = [...document.querySelectorAll('.solo')];
      for (let i = 0; i < solos.length; i++) for (let j = i + 1; j < solos.length; j++) {
        const a = r(solos[i]), b = r(solos[j]);
        if (a.left < b.right && b.left < a.right && a.top < b.bottom && b.top < a.bottom)
          out.push('sobreposicao: ' + nome(solos[i]) + ' x ' + nome(solos[j]));
      }
      return [...new Set(out)];
    });
    const png = path.join(dir, f.replace(/\.html$/, '.png'));
    await page.screenshot({ path: png });
    if (problemas.length) { falhas++; console.log(`✗ ${path.basename(png)}\n   - ` + problemas.join('\n   - ')); }
    else console.log(`✓ ${path.basename(png)}`);
  }
  await browser.close();
  if (falhas) { console.log(`\n${falhas} slide(s) com problema na regua.`); process.exitCode = 1; }
})();
