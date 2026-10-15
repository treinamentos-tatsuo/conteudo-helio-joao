// Ajusta a Anton pela régua da skill: casa a largura da linha de referência (serif mais larga do slide);
// grito puro (sem serif) mira 640px; teto 110px (capa 118). Grava antonfit.json.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const fs = require('fs');
const dir = __dirname + '/../instagram';
const slides = [2, 9];
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = {};
  for (const n of slides) {
    await page.goto(`file://${dir}/slide-${String(n).padStart(2,'0')}.html`);
    await page.waitForTimeout(900); await page.evaluate(() => document.fonts.ready);
    const r = await page.evaluate(() => {
      const w = el => { const rg = document.createRange(); rg.selectNodeContents(el); return rg.getBoundingClientRect().width; };
      let ref = 0; document.querySelectorAll('.line:not(.anton)').forEach(el => ref = Math.max(ref, w(el)));
      const antons = [...document.querySelectorAll('.anton')];
      antons.forEach(el => el.style.whiteSpace = 'nowrap');
      let aw = 0, fsz = 0; antons.forEach(el => { aw = Math.max(aw, w(el)); fsz = parseFloat(getComputedStyle(el).fontSize); });
      return { ref, aw, fsz };
    });
    const target = Math.min(r.ref > 0 ? r.ref : 895, 895);
    const teto = n === 2 ? 118 : 110;
    let size = Math.round(r.fsz * target / r.aw);
    size = Math.min(size, teto); size = Math.max(size, 66);
    out[n] = size;
    console.log(`slide ${n}: ref ${Math.round(r.ref)} | anton ${Math.round(r.aw)}@${r.fsz} -> ${size}px`);
  }
  fs.writeFileSync(__dirname + '/antonfit.json', JSON.stringify(out));
  await browser.close();
})();
