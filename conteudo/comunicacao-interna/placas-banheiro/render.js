const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 3.125 });
  await p.goto(require('url').pathToFileURL(path.join(dir, 'placa-banheiro.html')).href);
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(dir, 'placa-banheiro.png') });
  await p.pdf({ path: path.join(dir, 'placa-banheiro.pdf'), width: '210mm', height: '297mm', printBackground: true });
  await b.close();
})();
