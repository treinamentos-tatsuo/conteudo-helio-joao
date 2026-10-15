const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir='/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/142_aguentar/instagram';
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1350}});
for(const n of [1,5,7]){await pg.goto(`file://${dir}/slide-0${n}.html`);await pg.waitForTimeout(700);await pg.evaluate(()=>document.fonts.ready);
const r=await pg.evaluate(()=>[...document.querySelectorAll('.anton')].map(el=>{const rg=document.createRange();rg.selectNodeContents(el);
const rects=[...rg.getClientRects()].filter(x=>x.width>1);return {t:el.textContent,w:Math.round(Math.max(...rects.map(x=>x.width))),n:rects.length,fs:getComputedStyle(el).fontSize};}));
console.log(n,JSON.stringify(r));}await b.close();})();
