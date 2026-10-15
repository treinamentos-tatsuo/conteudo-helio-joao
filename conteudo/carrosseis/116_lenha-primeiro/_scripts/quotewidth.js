// Mede a largura de avanço das aspas em Source Serif Pro 600, em fração de em (independe do font-size).
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.setContent(`<link href="https://fonts.googleapis.com/css2?family=Source+Serif+Pro:wght@600&display=swap" rel="stylesheet">
    <div style="font-family:Source Serif Pro;font-weight:600;font-size:200px;white-space:pre" id="a">&ldquo;</div>
    <div style="font-family:Source Serif Pro;font-weight:600;font-size:200px;white-space:pre" id="b">&rdquo;</div>`);
  await p.waitForTimeout(1500);
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => {
    const w = (id) => { const el = document.getElementById(id); const rg = document.createRange();
      rg.selectNodeContents(el); return rg.getBoundingClientRect().width; };
    return { abre: w('a') / 200, fecha: w('b') / 200 };
  });
  require("fs").writeFileSync(__dirname+"/quotewidth.json", JSON.stringify({em:+r.abre.toFixed(3)}));console.log(`aspa de abertura: ${r.abre.toFixed(4)}em | aspa de fechamento: ${r.fecha.toFixed(4)}em`);
  await b.close();
})();
