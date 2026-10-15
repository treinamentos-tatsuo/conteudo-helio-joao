// Mede a largura de avanço das aspas em Anton, em fração de em (independe do font-size).
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.setContent(`<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
    <div style="font-family:Anton;font-size:200px;letter-spacing:0.5px;white-space:pre" id="a">&ldquo;</div>
    <div style="font-family:Anton;font-size:200px;letter-spacing:0.5px;white-space:pre" id="b">&rdquo;</div>`);
  await p.waitForTimeout(1500);
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => {
    const w = (id) => { const el = document.getElementById(id); const rg = document.createRange();
      rg.selectNodeContents(el); return rg.getBoundingClientRect().width; };
    return { abre: w('a') / 200, fecha: w('b') / 200 };
  });
  console.log(`aspa de abertura: ${r.abre.toFixed(4)}em | aspa de fechamento: ${r.fecha.toFixed(4)}em`);
  await b.close();
})();
