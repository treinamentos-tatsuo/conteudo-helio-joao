const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/142_aguentar/instagram';
(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport:{width:1080,height:1350} });
  for (let n=1;n<=12;n++){ const p=String(n).padStart(2,'0');
    await page.goto(`file://${dir}/slide-${p}.html`); await page.waitForTimeout(700); await page.evaluate(()=>document.fonts.ready);
    const r = await page.evaluate(()=>[...document.querySelectorAll('.line')].map(el=>{
      const rg=document.createRange(); rg.selectNodeContents(el);
      const rects=[...rg.getClientRects()].filter(x=>x.width>1);
      return {t:el.textContent.slice(0,50), n:rects.length, w:Math.round(Math.max(...rects.map(x=>x.width)))};
    }));
    r.forEach(x=>{ if(x.n>1||x.w>870) console.log(`[${p}] ${x.n>1?'WRAP '+x.n:'larga'} w=${x.w} | ${x.t}`); });
  }
  await b.close();
})();
