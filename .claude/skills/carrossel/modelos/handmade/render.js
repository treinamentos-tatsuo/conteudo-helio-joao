// Modelo handmade — renderiza slide-*.html em PNG 1080x1350 (espera fontes + desenho rough.js).
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), __dirname] }));
const fs = require('fs'), path = require('path'), { pathToFileURL } = require('url');
(async () => {
  const dir = path.resolve(process.argv[2] || '.'); const pick = process.argv.slice(3);
  const files = (pick.length ? pick : fs.readdirSync(dir).filter(f => /^slide-\d+\.html$/.test(f))).sort();
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const f of files) {
    await p.goto(pathToFileURL(path.join(dir, f)).href);
    await p.waitForSelector('body[data-ok="1"]', { timeout: 15000 }); await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(dir, f.replace('.html', '.png')) }); console.log('✓ ' + f.replace('.html', '.png'));
  }
  await b.close();
})();
