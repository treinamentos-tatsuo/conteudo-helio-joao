const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/73_fechamento-do-mes/instagram';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = {};
  for (let n = 1; n <= 10; n++) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(900);
    await page.evaluate(() => document.fonts.ready);
    out[n] = await page.evaluate(() => {
      let b = 0;
      document.querySelectorAll('.line, .cta-big, .cta-sm').forEach(el => { b = Math.max(b, el.getBoundingClientRect().bottom); });
      return Math.round(b);
    });
  }
  require('fs').writeFileSync(__dirname + '/textbottom.json', JSON.stringify(out, null, 2));
  console.log(JSON.stringify(out));
  await browser.close();
})();
