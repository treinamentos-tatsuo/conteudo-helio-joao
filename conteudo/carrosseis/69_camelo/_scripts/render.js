// Renderiza todos os slides do carrossel 69 em 1080x1350.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const only = process.argv.slice(2).map(Number);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  const dir = path.resolve(__dirname, '..', 'instagram');
  for (let n = 1; n <= 19; n++) {
    if (only.length && !only.includes(n)) continue;
    const id = String(n).padStart(2, '0');
    const img = path.resolve(__dirname, '..', 'imagens', n === 10 ? 'img-10a.png' : `img-${id}.png`);
    if (!fs.existsSync(img)) { console.log(`  ${id} SEM IMAGEM, pulando`); continue; }
    await p.goto('file://' + path.join(dir, `slide-${id}.html`));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(1200);
    await p.screenshot({ path: path.join(dir, `slide-${id}.png`) });
    console.log(`  ${id} OK`);
  }
  await b.close();
})();
