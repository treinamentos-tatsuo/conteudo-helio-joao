// Renderiza os slides do carrossel 72 (1080x1350).
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/72_nao-tem-opcao/instagram';

(async () => {
  const list = process.argv.slice(2).map(Number);
  const nums = list.length ? list : Array.from({ length: 12 }, (_, i) => i + 1);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const n of nums) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(1100);
    await page.screenshot({ path: `${dir}/slide-${p}.png` });
    console.log(`slide-${p}.png`);
  }
  await browser.close();
})();
