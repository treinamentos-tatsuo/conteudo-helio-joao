const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = __dirname;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 378, height: 567 }, deviceScaleFactor: 3.125 });
  await p.goto(require('url').pathToFileURL(path.join(dir, 'placa-luzes-ar.html')).href);
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: path.join(dir, 'placa-luzes-ar.png') });
  await p.pdf({ path: path.join(dir, 'placa-luzes-ar.pdf'), width: '100mm', height: '150mm', printBackground: true });
  await b.close();
})();
