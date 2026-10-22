const path = require('path');
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), path.resolve(__dirname, '../../../..')] }));
const dir = path.resolve(__dirname, '../instagram');
(async () => { const nums = process.argv.slice(2).map(Number);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const n of nums) { const f = String(n).padStart(2, '0');
    await p.goto('file:///' + path.join(dir, `slide-${f}.html`).split(path.sep).join('/')); await p.waitForTimeout(1100); await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => [...document.querySelectorAll('.b')].some(e => { const r = e.getBoundingClientRect(); return r.top < 60 || r.bottom > 1300 || r.left < 40 || r.right > 1040; }));
    await p.screenshot({ path: path.join(dir, `slide-${f}.png`) }); if (over) console.log(n, 'FORA DA MARGEM'); }
  await b.close(); })();
