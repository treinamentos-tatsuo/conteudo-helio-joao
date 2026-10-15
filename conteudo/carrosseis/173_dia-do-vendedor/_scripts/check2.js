const { chromium } = require('/Users/pedrohenrique/Documents/tatsuo-carrossel/node_modules/playwright');
const dir = '/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/173_dia-do-vendedor/instagram';
(async () => {
  const nums = process.argv.slice(2).map(Number); const list = nums.length ? nums : [...Array(16).keys()].map(i => i + 1);
  const TT={}; const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const n of list) { const f = String(n).padStart(2, '0');
    await p.goto(`file://${dir}/slide-${f}.html`); await p.waitForTimeout(1100); await p.evaluate(() => document.fonts.ready);
    const r = await p.evaluate(() => { const t = document.querySelector('.txt').getBoundingClientRect().top; const bad = [];
      document.querySelectorAll('.s,.a').forEach(e => { const lh = parseFloat(getComputedStyle(e).lineHeight); const exp = (e.innerHTML.match(/<br>/g) || []).length + 1;
        const got = Math.round(e.getBoundingClientRect().height / lh); if (got > exp) bad.push(e.textContent.slice(0, 30)); });
      return { t: Math.round(t), bad }; });
    await p.screenshot({ path: `${dir}/slide-${f}.png` });
    TT[n]=r.t; console.log(n, 'topo do texto', r.t, r.bad.length ? 'QUEBRA: ' + r.bad.join(' | ') : ''); }
  const fs=require('fs'), jf=__dirname+'/texttop.json'; let o={}; try{o=JSON.parse(fs.readFileSync(jf))}catch(e){}; Object.assign(o,TT); fs.writeFileSync(jf, JSON.stringify(o,null,1));
  await b.close(); })();
