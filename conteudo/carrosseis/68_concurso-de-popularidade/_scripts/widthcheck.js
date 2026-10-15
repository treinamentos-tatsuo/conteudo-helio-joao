// Confere se alguma linha (Anton ou serif) estoura a coluna util de 940px
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/68_concurso-de-popularidade/instagram';
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let n = 1; n <= 12; n++) {
    const f = String(n).padStart(2, '0');
    await p.goto(`file://${dir}/slide-${f}.html`);
    await p.waitForTimeout(700);
    await p.evaluate(() => document.fonts.ready);
    const bad = await p.evaluate(() => {
      const w = (el) => { const r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect().width; };
      return [...document.querySelectorAll('.line,.cta-big,.cta-sm')]
        .map(e => ({ t: e.textContent.slice(0, 34), w: Math.round(w(e)), h: Math.round(e.getBoundingClientRect().height), fs: Math.round(parseFloat(getComputedStyle(e).fontSize)) }))
        .filter(o => o.w > 940 || o.h > 1.9 * o.fs);
    });
    const bottom = await p.evaluate(() => Math.round(document.querySelector('.top').getBoundingClientRect().bottom));
    console.log(`[${f}] texto termina y=${bottom}` + (bad.length ? ` | PROBLEMA: ${JSON.stringify(bad)}` : ' | larguras ok'));
  }
  await b.close();
})();
