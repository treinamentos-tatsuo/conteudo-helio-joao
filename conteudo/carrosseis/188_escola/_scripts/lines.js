const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir=__dirname+'/../instagram'; const N=parseInt(process.argv[2]||'11');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let n=1;n<=N;n++){await p.goto(`file://${dir}/slide-${String(n).padStart(2,'0')}.html`);await p.waitForTimeout(700);await p.evaluate(()=>document.fonts.ready);
const w=await p.evaluate(()=>[...document.querySelectorAll('.line')].filter(e=>{const lh=parseFloat(getComputedStyle(e).lineHeight);return e.getBoundingClientRect().height>lh*1.5}).map(e=>e.textContent));
if(w.length)console.log(n,'QUEBRA:',w);}
await b.close();})();
