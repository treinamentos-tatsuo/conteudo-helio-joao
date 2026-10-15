const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/64_come-antes-de-voce/instagram';
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let n = 1; n <= 15; n++) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/slide-${p}.html`);
    await page.waitForTimeout(900);
    const rows = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('.line, .cta-big, .cta-sm').forEach(el => {
        const cs = getComputedStyle(el);
        const lh = parseFloat(cs.lineHeight);
        const h = el.getBoundingClientRect().height;
        const w = el.getBoundingClientRect().width;
        out.push({ t: el.textContent.trim().slice(0, 34), lines: Math.round(h / lh), w: Math.round(w) });
      });
      return out;
    });
    rows.forEach(r => {
      const expected = r.t.includes('que eu te mostro') ? 3 : 1;
      if (r.lines > expected) console.log(`S${p} QUEBROU x${r.lines} :: ${r.t}`);
    });
  }
  await browser.close();
  console.log('WIDTHCHECK FIM');
})();
