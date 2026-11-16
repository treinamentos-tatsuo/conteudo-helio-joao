const path = require('path');
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), __dirname] }));
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const n of process.argv.slice(2)) {
    await p.goto('file:///' + path.join(__dirname, '..', 'instagram', 'slide-0' + n + '.html').split(path.sep).join('/'));
    await p.waitForTimeout(900);
    const r = await p.evaluate(() => { const els = [...document.querySelectorAll('.pg > *')]; return Math.round(els[els.length - 1].getBoundingClientRect().bottom); });
    console.log(n, 'fim do texto em y =', r, '(a seta fica em ~1240)'); }
  await b.close(); })();
