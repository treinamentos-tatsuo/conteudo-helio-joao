// Gera as placas de comunicação interna (bege, bordô, preto; Montserrat; sem logo).
// Uso: node gerar.js            -> todas
//      node gerar.js copa porta  -> só as que contêm esses trechos no nome
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

const BASE = `
  :root { --bege: #F1E9DC; --bordo: #6C0302; --preto: #0A0A0A; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bege); font-family: 'Montserrat', sans-serif; color: var(--preto); display: flex; flex-direction: column; }
  .fit { display: inline-block; white-space: nowrap; }
  .faixa { flex: none; background: var(--bordo); }
  .faixa.topo { border-bottom: .12rem solid var(--bege); box-shadow: 0 .12rem 0 var(--bordo); }
  .faixa.base { border-top: .12rem solid var(--bege); box-shadow: 0 -.12rem 0 var(--bordo); }
  main { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
`;

// Diminui cada .fit até caber na largura útil do <main> em que está
const FIT = `
document.fonts.ready.then(() => {
  document.querySelectorAll('.fit').forEach(el => {
    const m = el.closest('main'), cs = getComputedStyle(m);
    const max = m.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    let fs = parseFloat(getComputedStyle(el).fontSize);
    while (el.getBoundingClientRect().width > max && fs > 4) { fs *= 0.98; el.style.fontSize = fs + 'px'; }
  });
  document.body.dataset.ok = '1';
});`;

const pagina = (w, h, rem, css, corpo) => `<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,500;0,600;0,800;0,900;1,500&display=swap" rel="stylesheet">
<style>@page { size: ${w}mm ${h}mm; margin: 0; }
html { font-size: ${rem}mm; } html, body { width: ${w}mm; height: ${h}mm; }
${BASE}${css}</style></head>
<body>${corpo}<script>${FIT}</script></body></html>`;

// Aviso em lista (mesmo desenho da placa do banheiro). Unidade = largura/21.
function lista(w, h, { titulo, itens, lembrete }) {
  const css = `
  .faixa { height: 1.6rem; }
  main { padding: 0 1.8rem; }
  h1 { font-weight: 900; font-size: 3rem; letter-spacing: -0.02em; line-height: 1; }
  .fio { width: 4rem; height: .14rem; background: var(--bordo); margin: 1rem 0 1.6rem; }
  ul { list-style: none; width: 100%; padding-left: .6rem; text-align: left; }
  li { font-weight: 500; font-size: .88rem; line-height: 1.25; padding: .42rem 0; display: flex; align-items: flex-start; gap: .7rem; }
  li::before { content: ""; flex: none; width: .42rem; height: .42rem; margin-top: .36em; background: var(--bordo); }
  .lembrete { margin-top: 1.8rem; width: 100%; border: .08rem solid var(--bordo); padding: .8rem .6rem; font-style: italic; font-weight: 500; font-size: .74rem; line-height: 1.35; }`;
  return pagina(w, h, w / 21, css, `
  <div class="faixa topo"></div>
  <main>
    <h1 class="fit">${titulo}</h1>
    <div class="fio"></div>
    <ul>${itens.map(i => `<li>${i}</li>`).join('')}</ul>
    ${lembrete ? `<div class="lembrete">${lembrete}</div>` : ''}
  </main>
  <div class="faixa base"></div>`);
}

// Aviso de destaque (mesmo desenho da placa de luzes e ar). Unidade = largura/10.
function destaque(w, h, { topo, grande, linhas }) {
  const css = `
  .faixa.topo { height: 3.6rem; color: var(--bege); padding: 0 .6rem; }
  .faixa.topo .fit { font-weight: 900; font-size: 1.5rem; letter-spacing: -0.01em; }
  .faixa.base { height: .9rem; }
  main { padding: 0 .6rem; }
  .grande { font-weight: 900; font-size: 1.4rem; letter-spacing: -0.02em; line-height: 1; }
  .fio { width: 2.2rem; height: .1rem; background: var(--bordo); margin: .6rem auto; }
  .item { font-weight: 800; font-size: .72rem; line-height: 1.1; letter-spacing: -0.01em; }
  .e { font-weight: 600; font-size: .55rem; color: var(--bordo); margin: .25rem 0; }`;
  // a faixa do topo também é um <main>, pra o ajuste de largura valer nela
  return pagina(w, h, w / 10, css, `
  <main class="faixa topo" style="flex:none"><span class="fit">${topo}</span></main>
  <main>
    <div><span class="fit grande">${grande}</span></div>
    <div class="fio"></div>
    ${linhas.map(l => l.e ? `<div class="e">${l.e}</div>` : `<div><span class="fit item">${l}</span></div>`).join('')}
  </main>
  <div class="faixa base"></div>`);
}

// Placa de porta (identificação de ambiente). Unidade = largura/20.
function porta(w, h, { nome, sub }) {
  const css = `
  .faixa { height: .7rem; }
  main { padding: 0 1.4rem; }
  .nome { font-weight: 900; font-size: 1.5rem; letter-spacing: -0.01em; line-height: 1; }
  .sub { margin-top: .45rem; font-weight: 600; font-size: .55rem; letter-spacing: .18em; color: var(--bordo); }`;
  return pagina(w, h, w / 20, css, `
  <div class="faixa topo"></div>
  <main>
    <div><span class="fit nome">${nome}</span></div>
    ${sub ? `<div><span class="fit sub">${sub}</span></div>` : ''}
  </main>
  <div class="faixa base"></div>`);
}

// Placa de direção (aponta pra outro andar ou ambiente). Unidade = largura/20.
function direcao(w, h, { seta, nomes, onde }) {
  const css = `
  .faixa { height: 1.2rem; }
  main { padding: 0 1.6rem; }
  .seta { width: 5.2rem; height: 5.2rem; margin-bottom: 1.6rem; }
  .nome { font-weight: 900; font-size: 3.4rem; letter-spacing: -0.02em; line-height: 1; }
  .e { font-weight: 600; font-size: 1.3rem; color: var(--bordo); margin: .5rem 0; }
  .fio { width: 4rem; height: .2rem; background: var(--bordo); margin: 1.6rem auto; }
  .onde { font-weight: 600; font-size: 1.1rem; letter-spacing: .18em; color: var(--bordo); }`;
  const giro = { cima: 0, direita: 90, baixo: 180, esquerda: 270 }[seta];
  return pagina(w, h, w / 20, css, `
  <div class="faixa topo"></div>
  <main>
    <svg class="seta" viewBox="0 0 100 100" style="transform:rotate(${giro}deg)"><path d="M50 4 L94 50 L66 50 L66 96 L34 96 L34 50 L6 50 Z" fill="#6C0302"/></svg>
    ${nomes.map((n, i) => (i ? '<div class="e">e</div>' : '') + `<div><span class="fit nome">${n}</span></div>`).join('')}
    <div class="fio"></div>
    <div><span class="fit onde">${onde}</span></div>
  </main>
  <div class="faixa base"></div>`);
}

const NBH = '&#8209;'; // hífen que não quebra linha

const PLACAS = [
  // Avisos em lista
  ['placa-banheiro-masculino', 210, 297, lista, {
    titulo: 'ATENÇÃO',
    itens: ['Não suba no vaso sanitário', 'Não urine no chão', 'Levante a tampa antes de usar', 'Jogue o papel higiênico no lixo', 'Após o uso, dê a descarga'],
    lembrete: 'Lembre-se: depois de você,<br>outras pessoas vão usar este banheiro.' }],
  ['placa-copa', 200, 300, lista, {
    titulo: 'COPA',
    itens: ['Lave, seque e guarde a sua louça', 'Identifique seus alimentos com nome e data', 'Não deixe comida vencida na geladeira', 'Limpe o que sujar: pia, mesa e micro-ondas', 'Jogue o lixo no lugar certo'],
    lembrete: 'A copa é de todos.<br>Deixe como você gostaria de encontrar.' }],
  ['placa-sala-reuniao', 200, 300, lista, {
    titulo: 'AO SAIR',
    itens: ['Coloque as cadeiras no lugar', 'Deixe a mesa limpa', 'Apague o quadro', `Desligue luzes, TV e ar${NBH}condicionado`, 'Feche a porta'],
    lembrete: 'A próxima reunião começa<br>do jeito que você deixar a sala.' }],
  // Destaque
  ['placa-sala-aula', 150, 200, destaque, {
    topo: 'SILÊNCIO', grande: 'EM AULA',
    linhas: ['CELULAR NO SILENCIOSO', { e: 'e' }, 'ENTRE SEM INTERROMPER'] }],
  // Direção
  ['placa-buffet-banheiros', 600, 800, direcao, {
    seta: 'cima', nomes: ['BUFFET', 'BANHEIROS'], onde: 'NO ANDAR DE CIMA' }, 150],
  // Portas
  ...[
    ['banheiro-masculino', 'BANHEIRO', 'MASCULINO'],
    ['banheiro-feminino', 'BANHEIRO', 'FEMININO'],
    ['sala-de-aula', 'SALA DE AULA'],
    ['sala-de-reuniao', 'SALA DE REUNIÃO'],
    ['copa', 'COPA'],
    ['recepcao', 'RECEPÇÃO'],
    ['restrito', 'RESTRITO', 'SOMENTE FUNCIONÁRIOS'],
  ].map(([slug, nome, sub]) => [`placas-porta/porta-${slug}`, 200, 80, porta, { nome, sub }]),
];

(async () => {
  const filtro = process.argv.slice(2);
  const b = await chromium.launch();
  for (const [nome, w, h, modelo, dados, dpi = 300] of PLACAS) {
    if (filtro.length && !filtro.some(f => nome.includes(f))) continue;
    const dir = path.join(__dirname, nome.includes('/') ? path.dirname(nome) : nome);
    const base = path.join(dir, path.basename(nome));
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(base + '.html', modelo(w, h, dados));
    const px = mm => Math.round(mm * 96 / 25.4);
    const p = await b.newPage({ viewport: { width: px(w), height: px(h) }, deviceScaleFactor: dpi / 96 });
    await p.goto(pathToFileURL(base + '.html').href);
    await p.waitForSelector('body[data-ok]', { state: 'attached' });
    await p.screenshot({ path: base + '.png' });
    await p.pdf({ path: base + '.pdf', width: w + 'mm', height: h + 'mm', printBackground: true });
    await p.close();
    console.log('ok', nome, `${w / 10}x${h / 10} cm`);
  }
  await b.close();
})();
