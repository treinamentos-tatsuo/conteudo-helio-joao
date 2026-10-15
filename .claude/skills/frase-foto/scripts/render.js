// Renderiza o HTML do post em 1080x1350 (PNG) e confere a margem lateral do texto (mínimo 90 px).
//
// uso (da RAIZ do projeto, onde está o node_modules com o playwright):
//   node .claude/skills/frase-foto/scripts/render.js conteudo/carrosseis/N_slug/instagram/slide-01.html
// grava slide-01.png ao lado do HTML (ou no caminho passado como 2º argumento).
//
// Primeira vez na máquina: `npm install` e `npx playwright install chromium` na raiz do projeto.
// Se a margem ficar abaixo de 90 px, o script avisa e sai com erro: diminuir a fonte ou quebrar a linha, nunca a margem.
const path = require('path');
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd()] }));
(async () => {
  const html = path.resolve(process.argv[2]);
  const out = path.resolve(process.argv[3] || html.replace(/\.html$/, '.png'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + html);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(1500);
  const m = await page.evaluate(() => {
    let L = 1e9, R = -1e9;
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (w.nextNode()) {
      const n = w.currentNode;
      const el = n.parentElement;
      if (!n.textContent.trim() || el.closest('script,style') || getComputedStyle(el).visibility === 'hidden') continue;
      const r = document.createRange(); r.selectNodeContents(n);
      for (const b of r.getClientRects()) { if (b.width) { L = Math.min(L, b.left); R = Math.max(R, b.right); } }
    }
    return { esq: Math.round(L), dir: Math.round(1080 - R) };
  });
  await page.screenshot({ path: out });
  await browser.close();
  const ok = m.esq >= 90 && m.dir >= 90;
  console.log(`PNG: ${out}`);
  console.log(`Margem do texto: esquerda ${m.esq} px, direita ${m.dir} px -> ${ok ? 'OK' : 'ABAIXO DE 90 PX: diminuir a fonte ou quebrar a linha (nunca a margem)'}`);
  process.exit(ok ? 0 : 2);
})();
