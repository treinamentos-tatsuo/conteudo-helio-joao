// Autofit da Anton do slide 3: casa a margem da linha serif de referência.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const path = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/33_decidir-no-escuro/instagram';
const TARGETS = { 3: 'ref' };
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const n of Object.keys(TARGETS)) {
    const f = `${path}/slide-${String(n).padStart(2, '0')}.html`;
    await page.goto('file://' + f);
    await page.waitForTimeout(1200);
    const size = await page.evaluate((target) => {
      const w = (el) => { const r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect().width; };
      const antons = [...document.querySelectorAll('.anton')];
      const anton = antons[0];
      const lines = [...document.querySelectorAll('.line')];
      const idx = lines.indexOf(anton);
      const goal = target === 'ref' ? w(lines[idx - 1]) : target;
      anton.style.whiteSpace = 'nowrap';
      let lo = 40, hi = 260;
      for (let i = 0; i < 26; i++) {
        const mid = (lo + hi) / 2;
        anton.style.fontSize = mid + 'px';
        if (w(anton) > goal) hi = mid; else lo = mid;
      }
      return Math.round(lo);
    }, TARGETS[n]);
    console.log(`slide ${n}: anton ${Math.min(size,110)}px (medido ${size})`);
  }
  await browser.close();
})();
