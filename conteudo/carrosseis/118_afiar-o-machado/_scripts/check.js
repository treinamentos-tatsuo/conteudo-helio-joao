// Mede, por slide, a altura do bloco de texto e a altura que sobra pra gravura.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  console.log('slide  texto   gravura  %gravura  linhas');
  for (let n = 2; n <= 15; n++) {
    const f = path.resolve(__dirname, '..', 'instagram', `slide-${String(n).padStart(2,'0')}.html`);
    await p.goto('file://' + f);
    await p.waitForTimeout(900);
    const r = await p.evaluate(() => {
      const t = document.querySelector('.text').getBoundingClientRect();
      const i = document.querySelector('.ilustra-box').getBoundingClientRect();
      const lh = parseFloat(getComputedStyle(document.querySelector('.text')).lineHeight);
      let lines = 0;
      document.querySelectorAll('.stanza').forEach(s => lines += Math.round(s.getBoundingClientRect().height / lh));
      return { t: Math.round(t.height), i: Math.round(i.height), lines, over: t.bottom > i.top };
    });
    const pct = Math.round(r.i / 1350 * 100);
    console.log(`  ${String(n).padStart(2)}   ${String(r.t).padStart(4)}px  ${String(r.i).padStart(4)}px    ${String(pct).padStart(3)}%     ${r.lines}${r.over ? '   <-- COLISAO' : ''}${r.lines > 5 ? '   <-- >5 LINHAS' : ''}`);
  }
  await b.close();
})();
