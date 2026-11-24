// Gera as placas de comunicação interna na identidade visual interna da Tatsuo Academy
// (a mesma dos playbooks de cultura: branco, vermelho escuro, Lora nos títulos,
// Poppins nos rótulos, Lato no texto, fio vermelho curto, diagonais finas no canto,
// "TATSUO ACADEMY" escrito no rodapé).
// Uso: node gerar.js            -> todas
//      node gerar.js copa porta  -> só as que contêm esses trechos no nome
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

const BASE = `
  :root { --verm: #A00F0F; --capa: #8C1C1C; --tinta: #1E1E1E; --cinza: #6E6E6E;
          --fio: #E4E4DF; --card: #F6F2F2; --papel: #FFFFFF; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { position: relative; overflow: hidden; background: var(--papel); color: var(--tinta);
         font-family: 'Lato', sans-serif; display: flex; flex-direction: column; }
  .fit { display: inline-block; white-space: nowrap; }
  .kicker { font-family: 'Poppins', sans-serif; font-weight: 600; text-transform: uppercase; color: var(--verm); }
  .titulo { font-family: 'Lora', serif; font-weight: 600; line-height: 1.05; letter-spacing: -0.01em; }
  .regua { background: var(--verm); }
  .diag { position: absolute; top: 0; right: 0; pointer-events: none; }
  .diag line { stroke: var(--verm); stroke-opacity: .28; }
  .rodape { flex: none; display: flex; justify-content: space-between; align-items: baseline; border-top: .04rem solid var(--fio); }
  .marca { font-family: 'Poppins', sans-serif; font-weight: 700; letter-spacing: .06em; }
  .rodape .apoio { color: var(--cinza); }
  main { display: flex; flex-direction: column; }
`;

// Linhas diagonais finas no canto superior direito (assinatura da capa dos playbooks)
const DIAG = (tam, traco) => `<svg class="diag" style="width:${tam}rem;height:${tam}rem" viewBox="0 0 100 100">
  ${[34, 48, 62, 76, 90].map(a => `<line x1="${a}" y1="0" x2="100" y2="${100 - a}" stroke-width="${traco}"/>`).join('')}</svg>`;

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
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Lato:ital,wght@0,400;0,700;1,400&family=Lora:ital,wght@0,600;1,500&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
<style>@page { size: ${w}mm ${h}mm; margin: 0; }
html { font-size: ${rem}mm; } html, body { width: ${w}mm; height: ${h}mm; }
${BASE}${css}</style></head>
<body>${corpo}<script>${FIT}</script></body></html>`;

const rodape = (apoio = 'Comunicação interna') =>
  `<div class="rodape"><span class="marca">TATSUO ACADEMY</span><span class="apoio">${apoio}</span></div>`;

// Ícones de linha das placas (viewBox 64x64): traço preto, detalhe vermelho. Divertidos, nada vulgar.
const VASO = `<path d="M17 10h13v19H17z" rx="2"/><path d="M12 30h40c0 9-7 15-17 16l2 8H22l2-9c-7-2-12-8-12-15z"/>`;
const PROIBIDO = `<circle cx="32" cy="32" r="27" class="v"/><path d="M13 13l38 38" class="v"/>`;
const LIXEIRA = `<path d="M36 32h20l-3 24H39z"/><path d="M34 32h24M42 32v-3h8v3M43 38v13M49 38v13"/>`;
const ICONES = {
  'nao-subir': `${VASO}${PROIBIDO}`,
  'limpo': `<path d="M27 5l5.5 16.5L49 27l-16.5 5.5L27 49l-5.5-16.5L5 27l16.5-5.5z"/><path d="M49 39l2.5 7 7 2.5-7 2.5-2.5 7-2.5-7-7-2.5 7-2.5z" class="v f"/><path d="M52 6l1.8 4.2L58 12l-4.2 1.8L52 18l-1.8-4.2L46 12l4.2-1.8z" class="v f"/><path d="M8 50l1.5 3.5L13 55l-3.5 1.5L8 60l-1.5-3.5L3 55l3.5-1.5z" class="v f"/>`,
  'tampa': `<path d="M6 14h12v20H6z"/><path d="M21 4h7v30h-7z" class="v"/><path d="M4 35h42c0 10-7 15-17 16l2 9H16l2-10C10 48 4 43 4 35z"/><path d="M54 36V8M46 16l8-8 8 8" class="v"/>`,
  'papel': `<circle cx="16" cy="22" r="9"/><circle cx="16" cy="22" r="3"/><path d="M25 22v16H13"/><path d="M20 10c10-8 24-6 29 12" class="v"/><path d="M43 18l6 5 3-7" class="v"/>${LIXEIRA}`,
  'descarga': `<path d="M32 7s-16 19-16 30a16 16 0 0 0 32 0C48 26 32 7 32 7z"/><path d="M25 39a7 7 0 0 0 11 5" class="v"/><path d="M52 12a5 5 0 0 1 0 7M56 8a10 10 0 0 1 0 15" class="v"/>`,
  'nao-chao': `<path d="M32 9s-11 13-11 21a11 11 0 0 0 22 0c0-8-11-21-11-21z"/><path d="M10 50h44M16 56h32"/>${PROIBIDO}`,
  'absorvente': `<rect x="4" y="6" width="24" height="15" rx="4"/><path d="M10 13.5h12"/><path d="M14 25c1 9 9 12 17 8" class="v"/><path d="M27 30l5 3-3 5" class="v"/>${LIXEIRA}`,
};
const icone = k => `<svg viewBox="0 0 64 64" fill="none" stroke="#1E1E1E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">${ICONES[k]}</svg>`;

// Aviso em lista: rótulo, título em serifa, itens numerados entre fios, lembrete em card. Unidade = largura/21.
function lista(w, h, { kicker, titulo, itens, lembrete, anton }) {
  // itens: texto, ou [texto, ícone] para a versão com ícones; anton: título e destaques na fonte Anton
  const css = `
  body { padding: 2.2rem 1.9rem 1.3rem; }
  .kicker { font-size: .5rem; letter-spacing: .22em; }
  .titulo { font-size: 2.9rem; margin-top: .5rem; }
  .regua { width: 2.4rem; height: .1rem; margin: 1.1rem 0 0; }
  main { flex: 1; justify-content: center; }
  ol { list-style: none; border-bottom: .04rem solid var(--fio); }
  li { display: flex; gap: .8rem; align-items: baseline; padding: .62rem 0; border-top: .04rem solid var(--fio);
       font-size: .9rem; line-height: 1.3; }
  li b { flex: none; width: 1.3rem; font-family: 'Poppins', sans-serif; font-weight: 700; font-size: .58rem; color: var(--verm); letter-spacing: .04em; }
  .lembrete { margin-top: 1.3rem; background: var(--card); border-left: .12rem solid var(--verm);
              padding: .75rem .9rem; font-size: .72rem; line-height: 1.4; }
  .lembrete strong { font-weight: 700; }
  .rodape { padding-top: .5rem; } .marca { font-size: .46rem; } .apoio { font-size: .42rem; }
  ${anton ? `
  body { padding-top: 1.8rem; }
  .titulo { font-family: 'Anton', sans-serif; font-weight: 400; text-transform: uppercase; letter-spacing: .01em; font-size: 2.9rem; line-height: 1.1; margin-top: .3rem; }
  .regua { margin-top: .7rem; }
  .lembrete { margin-top: 1rem; }
  .lembrete strong { font-family: 'Anton', sans-serif; font-weight: 400; text-transform: uppercase; letter-spacing: .03em; color: var(--verm); }` : ''}
  li.ic { align-items: center; gap: .9rem; padding: .38rem 0; }
  li .ico { flex: none; width: 2.1rem; height: 2.1rem; border-radius: 50%; background: var(--card); padding: .3rem; }
  li .ico svg { width: 100%; height: 100%; display: block; }
  li .ico .v { stroke: var(--verm); } li .ico .f { fill: var(--verm); stroke: none; }`;
  const linha = (it, i) => Array.isArray(it)
    ? `<li class="ic"><span class="ico">${icone(it[1])}</span><span>${it[0]}</span></li>`
    : `<li><b>${String(i + 1).padStart(2, '0')}</b><span>${it}</span></li>`;
  return pagina(w, h, w / 21, css, `${DIAG(7, .5)}
  <header><div class="kicker">${kicker}</div><h1 class="titulo">${titulo}</h1><div class="regua"></div></header>
  <main>
    <ol>${itens.map(linha).join('')}</ol>
    ${lembrete ? `<div class="lembrete">${lembrete}</div>` : ''}
  </main>
  ${rodape()}`);
}

// Aviso de destaque: fundo vermelho da capa, título branco em serifa. Unidade = largura/10.
function destaque(w, h, { kicker, titulo, linhas }) {
  const css = `
  body { background: var(--capa); color: #fff; padding: 1rem .85rem .6rem; }
  .diag line { stroke: #fff; stroke-opacity: .22; }
  main { flex: 1; justify-content: center; }
  .kicker { color: rgba(255,255,255,.78); font-size: .27rem; letter-spacing: .3em; }
  .titulo { margin-top: .3rem; } .titulo .fit { font-size: 1.45rem; }
  .regua { background: #fff; width: 1.3rem; height: .05rem; margin: .55rem 0 .5rem; }
  .linha { font-size: .46rem; line-height: 1.45; }
  .rodape { border-top-color: rgba(255,255,255,.3); padding-top: .3rem; }
  .marca { font-size: .22rem; letter-spacing: .3em; } .apoio { display: none; }`;
  return pagina(w, h, w / 10, css, `${DIAG(4.2, .6)}
  <main>
    <div class="kicker">${kicker}</div>
    <h1 class="titulo">${titulo.map(t => `<div><span class="fit">${t}</span></div>`).join('')}</h1>
    <div class="regua"></div>
    ${linhas.map(l => `<div class="linha">${l}</div>`).join('')}
  </main>
  ${rodape()}`);
}

// Placa de porta: fio vermelho, nome em serifa, complemento em rótulo. Unidade = largura/20.
function porta(w, h, { nome, sub }) {
  const css = `
  main { flex: 1; justify-content: center; padding: 0 1.5rem; }
  .regua { width: 1.4rem; height: .08rem; margin-bottom: .55rem; }
  .titulo .fit { font-size: 1.7rem; }
  .kicker { margin-top: .4rem; font-size: .4rem; letter-spacing: .24em; }
  .marca { position: absolute; right: 1.5rem; bottom: .55rem; font-size: .26rem; letter-spacing: .3em; color: var(--cinza); }`;
  return pagina(w, h, w / 20, css, `${DIAG(3.4, .7)}
  <main>
    <div class="regua"></div>
    <div class="titulo"><span class="fit">${nome}</span></div>
    ${sub ? `<div class="kicker">${sub}</div>` : ''}
  </main>
  <span class="marca">TATSUO ACADEMY</span>`);
}

// Placa de direção: seta em traço fino, ambientes em serifa, onde fica em rótulo. Unidade = largura/20.
function direcao(w, h, { seta, nomes, onde }) {
  const css = `
  body { padding: 2.2rem 1.8rem 1.1rem; }
  main { flex: 1; justify-content: center; }
  .seta { width: 4.6rem; height: 4.6rem; margin-bottom: 1.4rem; }
  .titulo .fit { font-size: 3.5rem; }
  .e { font-family: 'Lora', serif; font-style: italic; font-weight: 500; font-size: 1.6rem; color: var(--verm); margin: .15rem 0 .2rem; }
  .regua { width: 2.6rem; height: .1rem; margin: 1.3rem 0 .9rem; }
  .kicker { font-size: .8rem; letter-spacing: .24em; }
  .rodape { padding-top: .45rem; } .marca { font-size: .5rem; } .apoio { font-size: .45rem; }`;
  const giro = { cima: 0, direita: 90, baixo: 180, esquerda: 270 }[seta];
  return pagina(w, h, w / 20, css, `${DIAG(6.5, .45)}
  <main>
    <svg class="seta" viewBox="0 0 100 100" style="transform:rotate(${giro}deg)" fill="none" stroke="#A00F0F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M50 92 V10 M18 42 L50 10 L82 42"/></svg>
    ${nomes.map((n, i) => (i ? '<div class="e">e</div>' : '') + `<div class="titulo"><span class="fit">${n}</span></div>`).join('')}
    <div class="regua"></div>
    <div class="kicker">${onde}</div>
  </main>
  ${rodape()}`);
}

const NBH = '&#8209;'; // hífen que não quebra linha
const LEMBRETE_BANHEIRO = '<strong>Lembre-se:</strong> depois de você, outras pessoas vão usar este banheiro.';

const PLACAS = [
  // Avisos em lista
  ['placa-banheiro-feminino', 210, 297, lista, {
    kicker: 'Banheiro feminino', titulo: 'Atenção', anton: true,
    itens: [['Não suba no vaso sanitário', 'nao-subir'], ['Não urine no chão', 'nao-chao'], ['Jogue o absorvente no lixo', 'absorvente'],
            ['Jogue o papel higiênico no lixo', 'papel'], ['Após o uso, dê a descarga', 'descarga']],
    lembrete: LEMBRETE_BANHEIRO }],
  ['placa-banheiro-masculino', 210, 297, lista, {
    kicker: 'Banheiro masculino', titulo: 'Atenção', anton: true,
    itens: [['Não suba no vaso sanitário', 'nao-subir'], ['Mantenha este ambiente limpo', 'limpo'], ['Levante a tampa antes de usar', 'tampa'],
            ['Jogue o papel higiênico no lixo', 'papel'], ['Após o uso, dê a descarga', 'descarga']],
    lembrete: LEMBRETE_BANHEIRO }],
  ['placa-copa', 200, 300, lista, {
    kicker: 'Área comum', titulo: 'Copa',
    itens: ['Lave, seque e guarde a sua louça', 'Identifique seus alimentos com nome e data', 'Não deixe comida vencida na geladeira', `Limpe o que sujar: pia, mesa e micro${NBH}ondas`, 'Jogue o lixo no lugar certo'],
    lembrete: '<strong>A copa é de todos.</strong> Deixe como você gostaria de encontrar.' }],
  ['placa-sala-reuniao', 200, 300, lista, {
    kicker: 'Sala de reunião', titulo: 'Ao sair',
    itens: ['Coloque as cadeiras no lugar', 'Deixe a mesa limpa', 'Apague o quadro', `Desligue luzes, TV e ar${NBH}condicionado`, 'Feche a porta'],
    lembrete: '<strong>A próxima reunião começa</strong> do jeito que você deixar a sala.' }],
  // Destaque
  ['placa-sala-aula', 150, 200, destaque, {
    kicker: 'Sala de aula', titulo: ['Silêncio,', 'em aula'],
    linhas: ['Celular no silencioso.', 'Entre sem interromper.'] }],
  ['placa-luzes-ar', 100, 150, destaque, {
    kicker: 'Ao sair', titulo: ['Desligue', 'as luzes'],
    linhas: [`e o ar${NBH}condicionado.`] }],
  // Direção
  ['placa-buffet-banheiros', 600, 800, direcao, {
    seta: 'cima', nomes: ['Buffet', 'Banheiros'], onde: 'No andar de cima' }, 150],
  // Portas
  ...[
    ['banheiro-masculino', 'Banheiro', 'Masculino'],
    ['banheiro-feminino', 'Banheiro', 'Feminino'],
    ['sala-de-aula', 'Sala de aula'],
    ['sala-de-reuniao', 'Sala de reunião'],
    ['copa', 'Copa'],
    ['recepcao', 'Recepção'],
    ['restrito', 'Restrito', 'Somente funcionários'],
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
