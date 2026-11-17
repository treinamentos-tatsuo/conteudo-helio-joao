const { chromium } = require('playwright');
const path = require('path'); const { pathToFileURL } = require('url');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto(pathToFileURL(path.join(__dirname, 'arte.html')).href);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const h1 = await p.$eval('h1', e => [e.scrollWidth, e.getBoundingClientRect().right]);
  console.log('h1', h1);
  await p.screenshot({ path: path.join(__dirname, 'treinamento-disc-pedro.png') });
  await b.close();
})();
