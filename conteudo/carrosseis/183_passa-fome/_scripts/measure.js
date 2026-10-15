const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/183_passa-fome/instagram';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = {}; const wide = {};
  for (let n = 1; n <= 13; n++) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(900);
    await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate(() => {
      let b = 0, w = 0;
      document.querySelectorAll('.line, .cta-big, .cta-sm, .anton').forEach(el => {
        b = Math.max(b, el.getBoundingClientRect().bottom);
        const range = document.createRange(); range.selectNodeContents(el);
        w = Math.max(w, range.getBoundingClientRect().width);
      });
      return { b: Math.round(b), w: Math.round(w) };
    });
    out[n] = r.b; if (r.w > 940) wide[n] = r.w;
  }
  require('fs').writeFileSync(__dirname + '/textbottom.json', JSON.stringify(out, null, 2));
  console.log('textbottom', JSON.stringify(out));
  console.log('LARGURA>940:', JSON.stringify(wide));
  await browser.close();
})();
