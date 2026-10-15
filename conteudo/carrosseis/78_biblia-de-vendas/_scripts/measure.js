// Mede as linhas Anton de cada slide e devolve o tamanho ideal pra caber em UMA linha
// com largura-alvo (padrao 900px de 940 uteis). Escreve antonfit.json.
const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const fs = require('fs');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/78_biblia-de-vendas';
const TARGET = 900, MAXW = 940;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  const fit = {}, bottom = {};
  for (let n = 1; n <= 14; n++) {
    const p = String(n).padStart(2, '0');
    await page.goto(`file://${dir}/instagram/slide-${p}.html`);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const r = await page.evaluate(() => {
      const out = [];
      for (const el of document.querySelectorAll('.anton')) {
        const rng = document.createRange();
        rng.selectNodeContents(el);
        out.push({
          text: el.textContent.trim(),
          size: parseFloat(getComputedStyle(el).fontSize),
          textW: rng.getBoundingClientRect().width,
          boxH: el.getBoundingClientRect().height,
        });
      }
      const top = document.querySelector('.top');
      return { lines: out, blockBottom: top.getBoundingClientRect().bottom };
    });
    bottom[n] = Math.round(r.blockBottom);
    if (!r.lines.length) { console.log(`${p}: sem Anton  | bloco termina em ${Math.round(r.blockBottom)}px`); continue; }
    // o tamanho do slide e o menor que serve pra TODAS as linhas Anton dele
    let best = Infinity;
    for (const l of r.lines) {
      const wrapped = l.boxH > l.size * 1.4;      // quebrou em 2+ linhas
      const ideal = Math.floor(l.size * TARGET / l.textW);
      const cap = Math.floor(l.size * MAXW / l.textW);
      best = Math.min(best, wrapped ? cap : ideal);
      console.log(`${p}: "${l.text}" @${l.size}px larg=${Math.round(l.textW)} ${wrapped ? 'QUEBROU ' : ''}-> ideal ${ideal} (teto ${cap})`);
    }
    fit[n] = best;
    console.log(`${p}: => ${best}px  | bloco termina em ${Math.round(r.blockBottom)}px`);
  }
  fs.writeFileSync(`${dir}/_scripts/antonfit.json`, JSON.stringify(fit, null, 2));
  fs.writeFileSync(`${dir}/_scripts/textbottom.json`, JSON.stringify(bottom, null, 2));
  console.log('\nantonfit.json:', JSON.stringify(fit));
  await browser.close();
})();
