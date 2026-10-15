const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.setContent(`<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@600;700&display=swap" rel="stylesheet">
    <div style="font-family:'Source Serif Pro';font-weight:700;font-size:200px;white-space:pre" id="a">&ldquo;</div>
    <div style="font-family:'Source Serif Pro';font-weight:700;font-size:200px;white-space:pre" id="b">&rdquo;</div>
    <div style="font-family:'Source Serif Pro';font-weight:600;font-size:200px;white-space:pre" id="c">&ldquo;</div>`);
  await p.waitForTimeout(1500); await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => { const w = id => { const el=document.getElementById(id); const rg=document.createRange(); rg.selectNodeContents(el); return rg.getBoundingClientRect().width; }; return { abre700: w('a')/200, fecha700: w('b')/200, abre600: w('c')/200 }; });
  console.log(JSON.stringify(r)); await b.close();
})();
