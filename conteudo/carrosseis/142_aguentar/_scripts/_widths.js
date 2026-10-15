const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/142_aguentar/instagram';
(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport:{width:1080,height:1350} });
  for (const n of [6,8,10,11]){ const p=String(n).padStart(2,'0');
    await page.goto(`file://${dir}/slide-${p}.html`); await page.waitForTimeout(700); await page.evaluate(()=>document.fonts.ready);
    const r = await page.evaluate(()=>{ const o=[];
      document.querySelectorAll('.line').forEach(el=>{ el.style.whiteSpace='nowrap';
        const rg=document.createRange(); rg.selectNodeContents(el);
        o.push({t:el.textContent.slice(0,52), w:Math.round(rg.getBoundingClientRect().width), fs:parseFloat(getComputedStyle(el).fontSize)}); });
      return o; });
    console.log(`--- slide ${p} ---`); r.forEach(x=>console.log(`  ${x.w}px @${x.fs} | ${x.t}`));
  }
  await b.close();
})();
