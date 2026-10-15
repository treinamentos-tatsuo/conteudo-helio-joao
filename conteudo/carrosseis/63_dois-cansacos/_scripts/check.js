// Mede o fundo (bottom) do bloco de texto de cada slide e salva em textbottom.json
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/60_solidao-da-presidencia/instagram';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = {};
  for (let n = 1; n <= 18; n++) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(1100);
    out[n] = await page.evaluate(() => {
      const el = document.querySelector('.top');
      return Math.round(el.getBoundingClientRect().bottom);
    });
  }
  require('fs').writeFileSync(__dirname + '/textbottom.json', JSON.stringify(out, null, 2));
  console.log(JSON.stringify(out));
  await browser.close();
})();
