// Mede a largura de avanço das aspas em Source Serif Pro (regular e bold), em fração de em.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.setContent(`<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@400;700&display=swap" rel="stylesheet">
    <div style="font-family:'Source Serif Pro',serif;font-weight:400;font-size:200px;white-space:pre" id="a">&ldquo;</div>
    <div style="font-family:'Source Serif Pro',serif;font-weight:700;font-size:200px;white-space:pre" id="b">&rdquo;</div>`);
  await p.waitForTimeout(2000);
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => {
    const w = (id) => { const el = document.getElementById(id); const rg = document.createRange();
      rg.selectNodeContents(el); return rg.getBoundingClientRect().width; };
    return { abre: w('a') / 200, fecha: w('b') / 200 };
  });
  console.log(`abertura(400): ${r.abre.toFixed(4)}em | fechamento(700): ${r.fecha.toFixed(4)}em`);
  await b.close();
})();
