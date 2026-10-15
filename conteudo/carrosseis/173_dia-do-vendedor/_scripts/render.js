const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/173_dia-do-vendedor/instagram';
(async () => {
  const mode = process.argv[2]; // 'measure' ou lista de números
  const list = process.argv.slice(mode === 'measure' ? 3 : 2).map(Number);
  const nums = list.length ? list : Array.from({ length: 16 }, (_, i) => i + 1);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  const tb = {}, wide = {};
  for (const n of nums) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(1100);
    await page.evaluate(() => document.fonts.ready);
    if (mode === 'measure') {
      const r = await page.evaluate(() => { let b = 0, w = 0;
        document.querySelectorAll('.line, .cta-big').forEach(el => { b = Math.max(b, el.getBoundingClientRect().bottom);
          const g = document.createRange(); g.selectNodeContents(el); w = Math.max(w, g.getBoundingClientRect().width); });
        return { b: Math.round(b), w: Math.round(w) }; });
      tb[n] = r.b; if (r.w > 900) wide[n] = r.w;
    } else { await page.screenshot({ path: `${dir}/slide-${p}.png` }); }
  }
  if (mode === 'measure') { const f=__dirname + '/textbottom.json'; let old={}; try{old=JSON.parse(require('fs').readFileSync(f))}catch(e){}; require('fs').writeFileSync(f, JSON.stringify(Object.assign(old,tb), null, 1)); console.log(JSON.stringify(tb)); console.log('LARGO>900', JSON.stringify(wide)); }
  await browser.close();
})();
