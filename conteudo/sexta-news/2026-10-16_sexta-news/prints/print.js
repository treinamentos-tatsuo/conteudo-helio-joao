// Print 4:5 (1080x1350) das matérias reais, em tela de celular. Uso: node prints/print.js [num]
const { chromium, devices } = require(require.resolve('playwright', { paths: [process.cwd(), __dirname] }));
const path = require('path');
const M = {
  '01': 'https://g1.globo.com/politica/noticia/2026/10/14/senado-aprova-pec-do-fim-da-escala-6x1.ghtml',
  '02': 'https://www.jornaldocomercio.com/economia/2026/10/1266556-debate-do-split-payment-traz-a-tona-receio-do-comercio-com-reducao-do-capital-de-giro.html',
  '03': 'https://www.estadao.com.br/economia/brasileiros-se-endividam-ou-gastam-a-poupanca-para-pagar-contas-basicas-como-agua-e-luz/',
  '04': 'https://g1.globo.com/economia/noticia/2026/10/09/ipca-setembro.ghtml',
  '05': 'https://www.uol.com.br/tilt/colunas/helton-simoes-gomes/2026/10/12/whatsapp-mata-era-da-mensagem-gratuita-e-dispara-alerta-para-boleto-inedito.htm',
};
(async () => {
  const pick = process.argv.slice(2); const nums = pick.length ? pick : Object.keys(M);
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ ...devices['iPhone 13'], viewport: { width: 432, height: 540 + Number(process.env.CORTE || 0) }, deviceScaleFactor: 2.5, locale: 'pt-BR',
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1' });
  for (const n of nums) {
    const page = await ctx.newPage();
    try {
      await page.goto(M[n], { waitUntil: 'domcontentloaded', timeout: 60000 });
      await page.waitForTimeout(Number(process.env.ESPERA || 6000));
      // limpeza só visual: some com anúncio, banner de app, aviso de cookie e paywall (nada é aceito nem clicado)
      await page.evaluate(() => {
        const sel = 'iframe,ins,[id*="banner" i],[class*="banner" i],[class*="publicidade" i],[id*="publicidade" i],[class*="cookie" i],[id*="cookie" i],[class*="consent" i],[id*="consent" i],[class*="paywall" i],[id*="paywall" i],[class*="ads-" i],[class*="-ads" i],[id^="ad-" i],[class^="ad-" i],[id*="google_ads" i],[data-ad],[class*="smartbanner" i],[class*="advert" i],[class*="taboola" i],[class*="sponsor" i],[class*="oferecido" i]';
        document.querySelectorAll(sel).forEach(e => { if (!e.querySelector('h1')) e.remove(); });
        document.querySelectorAll('body *').forEach(e => { const cs = getComputedStyle(e); if ((cs.position === 'fixed' || cs.position === 'sticky') && !e.querySelector('h1')) {
          const b = e.getBoundingClientRect(); const cabecalho = b.top < 300 && b.height > 30 && b.height < 260 && b.width > 380 && /header|cabecalho|topo|navbar|menu/i.test(e.outerHTML.slice(0, 300));
          if (cabecalho) { e.style.position = 'relative'; e.style.top = '0'; } else e.remove(); } });
        document.querySelectorAll('body *').forEach(e => { const b = e.getBoundingClientRect(); if (b.top < 200 && b.height > 60 && !e.textContent.trim() && !e.querySelector('img,svg,picture,video')) e.style.display = 'none'; });
        // blocos de assinatura, cotação e patrocínio: some com o maior bloco que tem o texto e não tem a manchete
        ['Assine e tenha acesso', 'OFERTA ESPECIAL', 'Ibovespa', 'Valor PRO', 'Oferecido por', 'OFERECIDO POR', 'Baixe agora'].forEach(t => {
          const alvo = [...document.querySelectorAll('body *')].filter(e => e.children.length === 0 && e.textContent.includes(t));
          alvo.forEach(e => { let x = e; while (x.parentElement && x.parentElement !== document.body && !x.parentElement.querySelector('h1')) x = x.parentElement; if (!x.querySelector('h1')) x.remove(); });
        });
        document.documentElement.style.overflow = 'auto'; document.body.style.overflow = 'auto';
        window.scrollTo(0, 0);
      });
      await page.waitForTimeout(Number(process.env.POS || 1500));
      const h = await page.evaluate(() => { const e = document.querySelector('h1'); if (!e) return null; const b = e.getBoundingClientRect(); return [Math.round(b.top), Math.round(b.bottom)]; });
      console.log(n, page.url(), 'h1', h);
      await page.screenshot({ path: path.join(__dirname, `bruto-${n}.png`), clip: { x: 0, y: Number(process.env.CORTE || 0), width: 432, height: 540 } });
    } catch (e) { console.log(n, 'ERRO', e.message.split('\n')[0]); }
    await page.close();
  }
  await browser.close();
})();
