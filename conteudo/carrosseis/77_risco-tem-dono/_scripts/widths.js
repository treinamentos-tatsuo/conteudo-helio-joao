const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/77_risco-tem-dono/instagram';
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let n = 1; n <= 15; n++) {
    const s = String(n).padStart(2,'0');
    await p.goto(`file://${dir}/slide-${s}.html`);
    await p.waitForTimeout(700); await p.evaluate(() => document.fonts.ready);
    const bad = await p.evaluate(() => {
      const out=[];
      document.querySelectorAll('.line,.cta-big').forEach(el=>{
        const lh=parseFloat(getComputedStyle(el).lineHeight);
        const lines=Math.round(el.getBoundingClientRect().height/lh);
        if(lines>1) out.push({t:el.textContent.trim().slice(0,52),lines});
      });
      return out;
    });
    if (bad.length) bad.forEach(x=>console.log(`[${s}] QUEBROU em ${x.lines} linhas: "${x.t}"`));
  }
  await b.close();
})();
