// Mede a largura real da linha Anton e da linha de referencia, devolve o font-size que casa a margem.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const path = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/9_ninguem-te-contraria/instagram';

// slide -> alvo: 'ref' casa com a linha logo acima; numero = largura alvo em px
const TARGETS = { 3: 'ref', 10: 'ref', 14: 930 };

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = {};
  for (const n of Object.keys(TARGETS)) {
    const f = `${path}/slide-${String(n).padStart(2, '0')}.html`;
    await page.goto('file://' + f, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.evaluate(() => document.fonts.load('100px Anton').then(() => document.fonts.ready));
    await page.waitForTimeout(600);
    const size = await page.evaluate((target) => {
      const w = (el) => { const r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect().width; };
      const antons = [...document.querySelectorAll('.anton')];
      const anton = antons.slice().sort((a, b) => b.textContent.length - a.textContent.length)[0];
      const lines = [...document.querySelectorAll('.line')];
      const idx = lines.indexOf(antons[0]);
      const goal = target === 'ref' ? w(lines[idx - 1]) : target;
      anton.style.whiteSpace = 'nowrap';
      let lo = 40, hi = 260;
      for (let i = 0; i < 26; i++) {
        const mid = (lo + hi) / 2;
        antons.forEach(e => e.style.fontSize = mid + 'px');
        if (w(anton) > goal) hi = mid; else lo = mid;
      }
      return Math.round(lo);
    }, TARGETS[n]);
    out[n] = size;
    console.log(`slide ${n}: anton ${size}px`);
  }
  require('fs').writeFileSync(__dirname + '/antonfit.json', JSON.stringify(out, null, 2));
  await browser.close();
})();
