const { chromium } = require(__dirname + '/../../../../node_modules/playwright');
const dir = require('path').resolve(__dirname, '../instagram');
(async () => { const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1080,height:1350}});
 for (let n=1;n<=11;n++){ const f=String(n).padStart(2,'0'); await p.goto(require('url').pathToFileURL(`${dir}/slide-${f}.html`).href); await p.waitForTimeout(900);
  const r = await p.evaluate(()=>{const o=[];document.querySelectorAll('.line').forEach(e=>{const lh=parseFloat(getComputedStyle(e).lineHeight);if(e.getBoundingClientRect().height>lh*1.5)o.push(e.innerText)});const t=document.querySelector('.top').getBoundingClientRect().bottom;const i=document.querySelector('img').getBoundingClientRect().top;return {wrap:o,textBottom:Math.round(t),imgTop:Math.round(i)}});
  console.log(n, JSON.stringify(r)); } await b.close(); })();
