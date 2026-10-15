const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/125_nada-pessoal/instagram';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = {}; const wide = {}; const wrap = {};
  for (let n = 1; n <= 14; n++) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(900);
    await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate(() => {
      let b = 0, w = 0; const wr = [];
      document.querySelectorAll('.line, .cta-big, .cta-sm, .anton').forEach(el => {
        const rc = el.getBoundingClientRect(); b = Math.max(b, rc.bottom);
        const range = document.createRange(); range.selectNodeContents(el);
        w = Math.max(w, range.getBoundingClientRect().width);
        const cs = getComputedStyle(el); const lh = parseFloat(cs.fontSize) * (el.classList.contains('anton') ? 1.12 : 1.32);
        if (rc.height > lh * 1.6) wr.push(el.textContent.trim().slice(0, 40));
      });
      return { b: Math.round(b), w: Math.round(w), wr };
    });
    out[n] = r.b; if (r.w > 900) wide[n] = r.w; if (r.wr.length) wrap[n] = r.wr;
  }
  require('fs').writeFileSync(__dirname + '/textbottom.json', JSON.stringify(out, null, 2));
  console.log('textbottom', JSON.stringify(out));
  console.log('LARGURA>900:', JSON.stringify(wide));
  console.log('WRAP:', JSON.stringify(wrap));
  await browser.close();
})();
