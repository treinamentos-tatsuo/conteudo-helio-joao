// Acusa .line que quebrou sozinha (mais de uma linha visual) — palavra órfã / quebra não controlada.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = __dirname + '/../instagram';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let n = 1; n <= 14; n++) {
    await page.goto(`file://${dir}/slide-${String(n).padStart(2,'0')}.html`);
    await page.waitForTimeout(700); await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate(() => [...document.querySelectorAll('.line,.cta-big')].map(el => {
      const lh = parseFloat(getComputedStyle(el).lineHeight); return { t: el.textContent.slice(0, 40), rows: Math.round(el.getBoundingClientRect().height / lh) };
    }).filter(x => x.rows > 1));
    if (r.length) console.log(n, JSON.stringify(r));
  }
  console.log('wrapchk fim');
  await browser.close();
})();
