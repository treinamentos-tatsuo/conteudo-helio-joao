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
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Great+Vibes&family=Noto+Serif+JP:wght@600&family=Lato:ital,wght@0,400;0,700;1,400&family=Lora:ital,wght@0,600;1,500&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
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
  'higiene': `<rect x="6" y="32" width="36" height="20" rx="9"/><path d="M13 39h12"/><circle cx="44" cy="18" r="7" class="v"/><circle cx="28" cy="14" r="4" class="v"/><circle cx="55" cy="34" r="4" class="v"/>`,
  'absorvente': `<rect x="4" y="6" width="24" height="15" rx="4"/><path d="M10 13.5h12"/><path d="M14 25c1 9 9 12 17 8" class="v"/><path d="M27 30l5 3-3 5" class="v"/>${LIXEIRA}`,
};
// Estilo C (carinhas): objetos com rostinho e preenchimento rosado.
const OLHOS = (x, y, d = 5) => `<circle cx="${x - d}" cy="${y}" r="2.2" class="p"/><circle cx="${x + d}" cy="${y}" r="2.2" class="p"/>`;
const SORRI = (x, y, w = 4) => `<path d="M${x - w} ${y}q${w} ${w * .9} ${w * 2} 0"/>`;
const TRISTE = (x, y, w = 4) => `<path d="M${x - w} ${y + 3}q${w} ${-w * .9} ${w * 2} 0"/>`;
const SELO_NAO = `<circle cx="51" cy="13" r="10" class="b"/><path d="M44 6l14 14" class="bw"/>`;
const LIXO_C = `<path d="M36 34h22l-3 24H39z" class="r"/><path d="M33 34h28M43 34v-3h8v3"/>`;
const ICONES_C = {
  'nao-subir': `<rect x="12" y="8" width="16" height="20" rx="3" class="r"/><path d="M6 30h44c0 11-8 17-18 18l2 9H16l2-10C11 45 6 39 6 30z" class="r"/>${OLHOS(26, 36)}${TRISTE(26, 40)}${SELO_NAO}`,
  'limpo': `<path d="M30 4l6 18 18 6-18 6-6 18-6-18-18-6 18-6z" class="r"/>${OLHOS(30, 26, 4)}${SORRI(30, 31, 3.5)}<path d="M52 42l2 5 5 2-5 2-2 5-2-5-5-2 5-2z" class="f"/><path d="M10 48l1.5 3.5 3.5 1.5-3.5 1.5-1.5 3.5-1.5-3.5-3.5-1.5 3.5-1.5z" class="f"/>`,
  'tampa': `<rect x="5" y="14" width="12" height="18" rx="3" class="r"/><rect x="20" y="3" width="8" height="29" rx="3" class="r"/><path d="M3 33h42c0 10-7 16-17 17l2 9H14l2-10C9 47 3 41 3 33z" class="r"/>${OLHOS(24, 39)}${SORRI(24, 43)}<path d="M55 34V8M48 15l7-7 7 7" class="v"/>`,
  'papel': `<rect x="6" y="12" width="20" height="30" rx="5" class="r"/><ellipse cx="16" cy="13" rx="10" ry="4" fill="#fff"/><circle cx="16" cy="13" r="2"/>${OLHOS(16, 26, 4)}${SORRI(16, 31, 3.5)}<path d="M26 8c11-7 22-3 26 14" class="v"/><path d="M46 18l6 5 4-6" class="v"/>${LIXO_C}`,
  'descarga': `<path d="M30 5S13 24 13 36a17 17 0 0 0 34 0C47 24 30 5 30 5z" class="r"/>${OLHOS(30, 36)}${SORRI(30, 42)}<path d="M50 13a5 5 0 0 1 0 8M55 9a10 10 0 0 1 0 16" class="v"/>`,
  'nao-chao': `<path d="M28 8s-13 15-13 25a13 13 0 0 0 26 0c0-10-13-25-13-25z" class="r"/>${OLHOS(28, 32, 4)}${TRISTE(28, 35, 3.5)}<path d="M6 54h46M14 60h30"/>${SELO_NAO}`,
  'absorvente': `<rect x="38" y="3" width="20" height="12" rx="4" class="r"/><path d="M43 9h10"/><path d="M47 18c0 4-2 7-5 9" class="v"/><path d="M40 22l1 6 6-1" class="v"/><path d="M12 28h30l-4 31H16z" class="r"/><path d="M8 28h38M21 28v-4h12v4"/>${OLHOS(27, 41)}${SORRI(27, 47)}`,
};
// Estilo E (personagens): cenas divertidas e informais, nada vulgar.
const OLHO = (x, y) => `<circle cx="${x}" cy="${y}" r="2.6" class="p"/><circle cx="${x + .9}" cy="${y - .9}" r=".9" class="w"/>`;
const OLHO_FELIZ = (x, y) => `<path d="M${x - 2.6} ${y + 1}q2.6-3.6 5.2 0"/>`;
const BOCHECHA = (x, y) => `<ellipse cx="${x}" cy="${y}" rx="2.6" ry="1.6" class="bo"/>`;
const ESTRELA = (x, y, R) => `<path d="M${x} ${y - R}L${x + R * .3} ${y - R * .3}L${x + R} ${y}L${x + R * .3} ${y + R * .3}L${x} ${y + R}L${x - R * .3} ${y + R * .3}L${x - R} ${y}L${x - R * .3} ${y - R * .3}Z" class="f"/>`;
const NAO = (x, y) => `<circle cx="${x}" cy="${y}" r="9" class="b"/><path d="M${x - 6} ${y - 6}l12 12" class="bw"/>`;
const ICONES_E = {
  'nao-subir': `<rect x="10" y="8" width="18" height="18" rx="3" class="r"/><path d="M4 28h42c0 11-8 17-17 18l2 10H15l2-11C9 43 4 37 4 28z" class="r"/>
    <circle cx="19" cy="35" r="3.6" class="w" stroke="#3B3A3A"/><circle cx="31" cy="35" r="3.6" class="w" stroke="#3B3A3A"/><circle cx="19.5" cy="35.5" r="1.7" class="p"/><circle cx="30.5" cy="35.5" r="1.7" class="p"/>
    <ellipse cx="25" cy="42.5" rx="2.2" ry="2.8" class="p"/><path d="M41 9c-2 3-3 5-3 6.5a3 3 0 0 0 6 0c0-1.5-1-3.5-3-6.5z" class="w" stroke="#3B3A3A" stroke-width="2"/>
    <path d="M34 6v6M48 10l-3 4" class="v"/>${NAO(53, 49)}`,
  'limpo': `<rect x="18" y="7" width="16" height="11" rx="3" class="r"/><path d="M18 11h-6M34 11h6l-1 8h-4"/><path d="M22 18h8v4h-8z"/>
    <rect x="14" y="22" width="24" height="36" rx="7" class="r"/>${OLHO_FELIZ(21, 36)}${OLHO(31, 35)}<path d="M20 43q6 6 12 0"/>${BOCHECHA(18, 41)}${BOCHECHA(34, 41)}
    <circle cx="7" cy="8" r="1.3" class="f"/><circle cx="4" cy="13" r="1.1" class="f"/><circle cx="8" cy="17" r="1.3" class="f"/>${ESTRELA(52, 16, 7)}${ESTRELA(53, 40, 5)}${ESTRELA(47, 55, 3.5)}`,
  'tampa': `<rect x="6" y="16" width="12" height="16" rx="3" class="r"/><rect x="20" y="4" width="9" height="28" rx="4" class="r"/>
    <path d="M3 33h42c0 10-7 16-17 17l2 9H14l2-10C9 47 3 41 3 33z" class="r"/>${OLHO_FELIZ(18, 39)}${OLHO_FELIZ(30, 39)}<path d="M18 43h12q0 6-6 6t-6-6z" class="p"/>${BOCHECHA(13, 44)}${BOCHECHA(35, 44)}
    <path d="M55 38V10M48 17l7-7 7 7" class="v"/>${ESTRELA(44, 10, 4)}`,
  'papel': `<g transform="rotate(-14 18 27)"><rect x="8" y="14" width="20" height="26" rx="5" class="r"/><ellipse cx="18" cy="14" rx="10" ry="4" class="w" stroke="#3B3A3A"/><circle cx="18" cy="14" r="1.8"/>
    ${OLHO(14, 26)}${OLHO(22, 26)}<path d="M14 31q4 4 8 0"/></g><path d="M7 25l-5-7M29 21l4-8"/><path d="M4 46h8M7 51h8" class="v"/>
    <path d="M32 8c10-6 19-2 21 11" class="v"/><path d="M48 16l5 4 3-6" class="v"/><path d="M38 36h20l-3 22H41z" class="r"/><path d="M35 36h26"/>${OLHO_FELIZ(44, 45)}${OLHO_FELIZ(52, 45)}<path d="M45 50q3 3.5 6 0"/>`,
  'descarga': `<path d="M8 36a24 24 0 0 0 38 17" class="v"/><path d="M41 56l5-3-4-4" class="v"/><path d="M56 30a24 24 0 0 0-38-17" class="v"/><path d="M23 8l-5 4 4 4" class="v"/>
    <path d="M32 12S19 28 19 37a13 13 0 0 0 26 0C45 28 32 12 32 12z" class="r"/>${OLHO_FELIZ(27, 36)}${OLHO_FELIZ(37, 36)}<path d="M27 41h10q0 5-5 5t-5-5z" class="p"/>${BOCHECHA(24, 41)}${BOCHECHA(40, 41)}`,
  'nao-chao': `<path d="M28 14c-3 5-5 8-5 10a5 5 0 0 0 10 0c0-2-2-5-5-10z" class="r"/><path d="M6 46c0-6 9-9 21-9s22 3 22 9-9 9-22 9S6 52 6 46z" class="r"/>
    ${OLHO(21, 44)}${OLHO(33, 44)}<path d="M23 51q2-2 4 0t4 0"/><path d="M2 61h52"/>${NAO(52, 14)}`,
  'absorvente': `<path d="M12 32h30l-4 26H16z" class="r"/><path d="M9 31l27-12"/><path d="M20 26l4-2 1 3"/>${OLHO(22, 41)}${OLHO(32, 41)}<path d="M22 46h10q0 6-5 6t-5-6z" class="p"/>${BOCHECHA(18, 46)}${BOCHECHA(36, 46)}
    <g transform="rotate(20 49 9)"><rect x="40" y="4" width="18" height="11" rx="4" class="r"/><path d="M45 9.5h8"/></g><path d="M45 19c-2 5-5 8-9 9" class="v"/><path d="M39 24l-3 4 5 1" class="v"/>
    <path d="M55 36c-4-3-6-5-6-7a3 3 0 0 1 6-1 3 3 0 0 1 6 1c0 2-2 4-6 7z" class="f"/>`,
};
// Estilo F (bonequinhos): o boneco fazendo o errado (selo de proibido) ou o certo (selo de ok).
const CABECA = (x, y, cara = 'feliz') => `<circle cx="${x}" cy="${y}" r="5.2" class="r"/><circle cx="${x - 2}" cy="${y - 1}" r="1" class="p"/><circle cx="${x + 2}" cy="${y - 1}" r="1" class="p"/>`
  + (cara === 'susto' ? `<ellipse cx="${x}" cy="${y + 2.4}" rx="1.1" ry="1.5" class="p"/>` : `<path d="M${x - 2} ${y + 1.6}q2 2.2 4 0" stroke-width="1.6"/>`);
const OK = (x, y) => `<circle cx="${x}" cy="${y}" r="7.5" class="ok"/><path d="M${x - 3.6} ${y + .2}l2.6 2.8 4.8-5.6" class="okw"/>`;
const NAO8 = (x, y) => `<circle cx="${x}" cy="${y}" r="7.5" class="b"/><path d="M${x - 5} ${y - 5}l10 10" class="bw"/>`;
// Bonequinho fofo: cabeça grande com topete, olhinhos com brilho e bochechas; corpo arredondado; mãos e pés.
// x, y = centro da cabeça. bracos = pontas das mãos [[x, y], [x, y]]. pernas = deslocamento dos pés a partir do quadril.
// Bonequinho no estilo pictograma de placa: silhueta cheia em grafite, cabeça redonda sem rosto,
// corpo e membros grossos e arredondados. x, y = centro da cabeça; bracos = pontas das mãos; pernas = deslocamento dos pés.
const BONECO = (x, y, bracos, { pernas = [[-6, 21], [6, 21]] } = {}) => {
  const ombro = y + 11, quadril = y + 24;
  const membros = bracos.map(([ex, ey], k) => `<path d="M${x + (k ? 3.2 : -3.2)} ${ombro}L${ex} ${ey}" class="sm"/>`).join('')
    + pernas.map(([dx, dy], k) => `<path d="M${x + (k ? 2.6 : -2.6)} ${quadril - 1}l${dx - (k ? 2.6 : -2.6)} ${dy - 1}" class="sm"/>`).join('');
  return `${membros}<rect x="${x - 5.6}" y="${y + 7.6}" width="11.2" height="${quadril - y - 6.6}" rx="4.4" class="sf"/>
    <circle cx="${x}" cy="${y - .4}" r="6" class="sf"/>`;
};
const ICONES_F = {
  'nao-subir': `<rect x="36" y="32" width="10" height="16" rx="2" class="r"/><path d="M6 48h34c0 6-5 9-12 10l1 5H16l1-5C10 57 6 54 6 48z" class="r"/>
    ${BONECO(21, 13, [[11, 18], [31, 17]], { pernas: [[-7, 11], [7, 11]] })}<path d="M6 12q-3 3 0 6M36 12q3 3 0 6" class="v"/>${NAO8(54, 11)}`,
  'limpo': `<rect x="27" y="13" width="7" height="11" rx="2" class="r"/><path d="M28 13v-3h5v3M33 10h4"/>
    <circle cx="41" cy="9" r="1.2" class="f"/><circle cx="44" cy="13" r="1.2" class="f"/><circle cx="40" cy="15" r="1.1" class="f"/>
    <path d="M32 58h26"/>${ESTRELA(48, 40, 5)}${ESTRELA(56, 48, 3.2)}${ESTRELA(38, 47, 3)}
    ${BONECO(15, 12, [[27, 19], [8, 33]], { pernas: [[-5, 22], [5, 22]] })}${OK(54, 11)}`,
  'tampa': `<rect x="48" y="26" width="10" height="18" rx="2" class="r"/><rect x="42" y="12" width="5.5" height="30" rx="2.5" class="r"/>
    <path d="M24 44h34c0 6-5 9-12 10l1 6H35l1-6C29 53 24 50 24 44z" class="r"/>
    ${BONECO(12, 12, [[40, 17], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}<path d="M35 9q4-5 9-5" class="v"/><path d="M41 2l3 2-2 3" class="v"/>${OK(56, 9)}`,
  'papel': `${BONECO(12, 12, [[21, 8], [5, 31]], { pernas: [[-5, 23], [5, 23]] })}<circle cx="25" cy="7" r="3.4" class="w"/>
    <path d="M29 9q13-2 18 18" class="v" stroke-dasharray="3 3"/><path d="M43 24l4 4 3-5" class="v"/>
    <path d="M38 36h22l-3 22H41z" class="r"/><path d="M36 36h26"/>${OK(54, 10)}`,
  'descarga': `<rect x="34" y="22" width="24" height="13" rx="2" class="r"/><circle cx="46" cy="20" r="2.6" class="f"/>
    <path d="M33 37h26c0 7-5 11-12 11l1 8h-4l1-8C38 48 33 44 33 37z" class="r"/><path d="M39 41q7 5 14 0" class="v"/>
    ${BONECO(12, 12, [[43, 19], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}<path d="M44 12l2-4M49 13l3-3" class="v"/>${OK(57, 6.5)}`,
  'nao-chao': `<rect x="48" y="24" width="10" height="16" rx="2" class="r"/><path d="M30 40h28c0 6-5 9-11 10l1 6H38l1-6C34 49 30 46 30 40z" class="r"/>
    <ellipse cx="17" cy="60" rx="13" ry="3.4" class="r"/>${BONECO(16, 13, [[10, 15], [22, 15]], { pernas: [[-5, 18], [5, 18]] })}
    <path d="M4 50l-2-3M30 50l2-3" class="v"/>${NAO8(54, 11)}`,
  'absorvente': `<path d="M38 36h22l-3 22H41z" class="r"/><path d="M36 36h26"/>${BONECO(13, 12, [[36, 20], [7, 33]], { pernas: [[-5, 23], [5, 23]] })}
    <rect x="40" y="22" width="11" height="6.5" rx="2.5" class="w"/><path d="M45.5 30v3" class="v"/>${OK(55, 10)}`,
  // Copa
  'louca': `<path d="M28 40h32"/><path d="M33 40v5q0 7 7 7h10q7 0 7-7v-5" class="r"/><path d="M45 40V30h7v4"/>
    ${BONECO(12, 12, [[26, 29], [26, 32]], { pernas: [[-5, 23], [5, 23]] })}<ellipse cx="30" cy="30.5" rx="5.5" ry="2.2" class="w"/>
    <circle cx="37" cy="24" r="2" class="v"/><circle cx="42" cy="19" r="1.5" class="v"/><circle cx="35" cy="17" r="1.2" class="v"/>${OK(55, 10)}`,
  'etiqueta': `<path d="M30 32h28"/><rect x="32" y="32" width="24" height="22" rx="3" class="r"/><rect x="37" y="38" width="14" height="9" rx="1" class="w"/>
    <path d="M40 41h8M40 44h5" stroke-width="1.6"/>${BONECO(12, 12, [[31, 35], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}<path d="M32 35l5-6" class="v"/>${OK(55, 10)}`,
  'vencida': `<rect x="32" y="8" width="24" height="50" rx="3" class="r"/><path d="M32 24h24M37 14v5M37 30v8"/>
    <path d="M60 30q3-3 0-6t0-6M60 46q3-3 0-6t0-6" class="v"/>${BONECO(14, 12, [[15, 15], [7, 32]], { pernas: [[-5, 23], [5, 23]] })}
    <path d="M24 9q3-2 0-5M26 17q3-2 0-5" class="v" stroke-width="2"/>${NAO8(55, 6)}`,
  'limpar': `<path d="M26 44h34M30 44v14M56 44v14"/><rect x="44" y="30" width="14" height="14" rx="2" class="r"/><rect x="46" y="33" width="7" height="8" rx="1" class="w"/>
    <rect x="32" y="40" width="9" height="4" rx="1" class="w"/>${BONECO(12, 12, [[34, 39], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}
    ${ESTRELA(30, 30, 3.5)}${ESTRELA(38, 33, 2.5)}${OK(55, 10)}`,
  'lixo-certo': `<path d="M34 38h12l-2 18h-8zM48 38h12l-2 18h-8z" class="r"/><path d="M32 38h16M46 38h16"/><path d="M38 46h4M52 46l2 3 2-3" stroke-width="1.6"/>
    ${BONECO(12, 12, [[20, 8], [5, 31]], { pernas: [[-5, 23], [5, 23]] })}<rect x="20" y="3" width="5" height="5" rx="1" class="w"/>
    <path d="M27 7q12-4 14 22" class="v" stroke-dasharray="3 3"/><path d="M37 26l4 4 3-5" class="v"/>${OK(55, 10)}`,
  // Sala de reunião
  'cadeiras': `<path d="M40 34h22M44 34v24M58 34v24"/><path d="M24 44h12v4H24z" class="r"/><path d="M24 28v30M24 44h12M36 44v14"/>
    ${BONECO(10, 12, [[23, 30], [23, 33]], { pernas: [[-5, 23], [5, 23]] })}<path d="M28 22h9M34 19l3 3-3 3" class="v"/>${OK(55, 10)}`,
  'mesa': `<path d="M28 42h32M32 42v16M56 42v16"/>${ESTRELA(38, 34, 4)}${ESTRELA(50, 36, 3)}
    ${BONECO(12, 12, [[24, 21], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}<path d="M24 14h7l-1 9h-5z" class="w"/><path d="M31 16h2v4h-2"/>${OK(55, 10)}`,
  'quadro': `<rect x="30" y="8" width="30" height="24" rx="1" class="w"/><path d="M36 32v24M54 32v24"/>
    <path d="M34 14q3-3 6 0t6 0" class="v" stroke-width="2"/><rect x="40" y="19" width="9" height="5" rx="1" class="r"/>
    ${BONECO(12, 12, [[40, 22], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}${OK(56, 44)}`,
  'desligar': `<rect x="32" y="16" width="12" height="18" rx="2" class="w"/><path d="M38 21v4" stroke-width="2.6"/>
    <circle cx="53" cy="14" r="6" class="w"/><path d="M50 21h6M51 24h4"/>
    <rect x="44" y="40" width="18" height="8" rx="2" class="w"/><path d="M47 45h12" stroke-width="1.4"/>
    ${BONECO(12, 12, [[33, 25], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}${OK(54, 58)}`,
  'fechar-porta': `<path d="M36 6h22v52"/><path d="M38 8l14 4v42l-14 4z" class="r"/><circle cx="48" cy="34" r="1.6" class="p"/>
    ${BONECO(12, 12, [[39, 33], [6, 33]], { pernas: [[-5, 23], [5, 23]] })}<path d="M56 16q6 8 0 16" class="v"/><path d="M53 30l3 3 3-4" class="v"/>${OK(56, 52)}`,
  // Aula, luzes, portas
  'silencio': `${BONECO(30, 16, [[24, 36], [38, 34]], { pernas: [[-6, 21], [6, 21]] })}
    <path d="M3 3h16a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-6l-5 5v-5H3a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3z" class="w" stroke-width="2"/>
    <text x="11" y="12.6" font-family="Anton" font-size="7.6" fill="#8E2B2F" stroke="none" text-anchor="middle">SHH!</text>
    <rect x="44" y="26" width="12" height="22" rx="2.5" class="w"/><path d="M47 31h6" stroke-width="1.4"/>
    <path d="M47 40q0-5 3-5t3 5l1 2H46z" stroke-width="1.6"/><path d="M45 34l10 10" class="v" stroke-width="2"/>`,
  'interruptor': `<rect x="34" y="18" width="12" height="18" rx="2" class="w"/><path d="M40 23v4" stroke-width="2.6"/>
    <circle cx="54" cy="16" r="6" class="w"/><path d="M51 23h6M52 26h4"/><path d="M50 12l8 8" class="v" stroke-width="2"/>
    ${BONECO(14, 12, [[34, 25], [8, 33]], { pernas: [[-5, 23], [5, 23]] })}
    <rect x="38" y="44" width="22" height="9" rx="2" class="w"/><path d="M41 49h16" stroke-width="1.4"/><path d="M44 56l12-14" class="v" stroke-width="2"/>`,
  'homem': `${BONECO(32, 12, [[22, 36], [42, 36]], { pernas: [[-5, 26], [5, 26]] })}`,
  'mulher': `${BONECO(32, 12, [[21, 34], [43, 34]], { pernas: [[-5, 26], [5, 26]] })}<path d="M27 22h10l6 17H21z" class="corpo" stroke-width="2"/>`,
};
const icone = (k, estilo) => `<svg viewBox="0 0 64 64" fill="none" stroke="#1E1E1E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">${(estilo === 'carinha' ? ICONES_C : estilo === 'divertido' ? ICONES_E : estilo === 'bonecos' ? ICONES_F : ICONES)[k]}</svg>`;
// Variações de ícone: linha (A, padrão), selo (B: desenho branco no círculo vermelho), carinha (C).
const ESTILO_ICONE = {
  selo: `body { background: #F2ECE4; } .lembrete { background: #fff; } ol, li { border-color: #E2DBD0 !important; } .rodape { border-top-color: #E2DBD0; }
    li .ico { background: var(--verm); } li .ico svg { stroke: #fff; } li .ico .v { stroke: #F0BEBF; } li .ico .f { fill: #F0BEBF; }`,
  carinha: `li .ico { padding: .16rem; background: #FBF4F4; } li .ico .r { fill: #F7DADB; } li .ico .p { fill: #1E1E1E; stroke: none; }
    li .ico .b { fill: var(--verm); stroke: #fff; stroke-width: 2; } li .ico .bw { stroke: #fff; stroke-width: 3.4; }`,
};

// Aviso em lista: rótulo, título em serifa, itens numerados entre fios, lembrete em card. Unidade = largura/21.
function lista(w, h, { kicker, titulo, itens, lembrete, anton, estilo }) {
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
  li .ico .v { stroke: var(--verm); } li .ico .f { fill: var(--verm); stroke: none; }
  ${ESTILO_ICONE[estilo] || ''}`;
  const linha = (it, i) => Array.isArray(it)
    ? `<li class="ic"><span class="ico">${icone(it[1], estilo)}</span><span>${it[0]}</span></li>`
    : `<li><b>${String(i + 1).padStart(2, '0')}</b><span>${it}</span></li>`;
  return pagina(w, h, w / 21, css, `${DIAG(7, .5)}
  <header><div class="kicker">${kicker}</div><h1 class="titulo">${titulo}</h1><div class="regua"></div></header>
  <main>
    <ol>${itens.map(linha).join('')}</ol>
    ${lembrete ? `<div class="lembrete">${lembrete}</div>` : ''}
  </main>
  ${rodape()}`);
}

// Estilo das paredes da empresa: fundo off-white, ensō de pincel cinza atrás, texto centralizado em grafite,
// destaque vinho, palavra em letra cursiva, kanji na vertical. Unidade = largura/21.
function enso(seed = 11) {
  let x = seed; const r = () => (x = (x * 16807) % 2147483647) / 2147483647;
  const arco = (R, a0, a1) => {
    const p = a => [100 + R * Math.cos(a * Math.PI / 180), 100 + R * Math.sin(a * Math.PI / 180)].map(v => v.toFixed(1)).join(' ');
    return `M${p(a0)}A${R} ${R} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${p(a1)}`;
  };
  let tracos = '';
  for (let i = 0; i < 90; i++) {
    const R = 84 + (r() - .5) * (i < 20 ? 6 : 14), a0 = -38 + r() * 30, a1 = 250 + r() * 50;
    const dash = Array.from({ length: 6 }, () => `${(30 + r() * 220).toFixed(0)} ${(1 + r() * 9).toFixed(0)}`).join(' ');
    tracos += `<path d="${arco(R, a0, a1)}" stroke-width="${(.3 + r() * (i < 20 ? 3 : 1.3)).toFixed(2)}" stroke-opacity="${(.18 + r() * .5).toFixed(2)}" stroke-dasharray="${dash}"/>`;
  }
  return `<svg class="enso" viewBox="0 0 200 200"><defs><filter id="pincel"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="${seed}"/><feDisplacementMap in="SourceGraphic" scale="2.5"/></filter></defs>
    <g fill="none" stroke="#9E9892" stroke-linecap="round" filter="url(#pincel)">${tracos}</g></svg>`;
}

function parede(w, h, { kicker, titulo, itens, lembrete3, kanji, kanjiLegenda, estilo }) {
  const css = `
  :root { --graf: #3B3A3A; --vinho: #8E2B2F; }
  body { background: #F4F2EE; color: var(--graf); padding: 2.4rem 2rem 1.2rem; align-items: center; text-align: center; }
  .enso { position: absolute; width: 27rem; height: 27rem; left: -1.2rem; top: 3.2rem; z-index: 0; opacity: .3; }
  header, main, .rodape { position: relative; z-index: 1; }
  .ligacao { display: flex; align-items: center; justify-content: center; gap: .6rem; font-size: .7rem; letter-spacing: .02em; }
  .ligacao::before, .ligacao::after { content: ""; width: 2.6rem; height: .035rem; background: var(--graf); }
  .titulo { font-family: 'Anton', sans-serif; font-weight: 400; font-size: 3.4rem; line-height: 1.05; letter-spacing: .02em; margin-top: .9rem; text-transform: uppercase; }
  .regua { width: 2.4rem; height: .07rem; background: var(--vinho); margin: .8rem auto 0; }
  .kanji { position: absolute; right: 1.4rem; top: 2.3rem; z-index: 1; display: flex; flex-direction: column; align-items: center; }
  .kanji b { font-family: 'Noto Serif JP', serif; font-weight: 600; font-size: 2rem; line-height: 1.15; color: #6F6B67; }
  .kanji span { margin-top: .3rem; font-family: 'Anton', sans-serif; font-size: .42rem; letter-spacing: .08em; color: var(--vinho); border-bottom: .03rem solid var(--vinho); padding-bottom: .1rem; }
  main { flex: 1; width: 100%; justify-content: center; align-items: center; }
  ol { list-style: none; width: 14.6rem; text-align: left; }
  li { display: flex; align-items: center; gap: .75rem; padding: .42rem 0; border-bottom: .03rem solid rgba(59,58,58,.18); font-size: .84rem; line-height: 1.25; }
  li:last-child { border-bottom: 0; }
  .ico { flex: none; width: 1.75rem; height: 1.75rem; }
  .ico svg { width: 100%; height: 100%; display: block; stroke: var(--graf); }
  .ico .v { stroke: var(--vinho); } .ico .f { fill: var(--vinho); stroke: none; }
  ${estilo === 'selo' ? `.ico { width: 2rem; height: 2rem; border-radius: 50%; background: var(--vinho); padding: .3rem; }
    .ico svg { stroke: #fff; } .ico .v { stroke: #EBC9C9; } .ico .f { fill: #EBC9C9; }` : ''}
  ${estilo === 'bonecos' ? `ol { width: 15.6rem; } .ico { width: 2.75rem; height: 2.75rem; } .ico svg { stroke-width: 2.4; } li { padding: .08rem 0; gap: .6rem; } .lembrete { margin-top: .35rem; } .lembrete .cursiva { font-size: 1.75rem; }
    .ico .r { fill: #F1E1DE; } .ico .p { fill: var(--graf); stroke: none; } .ico .w { fill: #fff; } .ico .f { fill: var(--vinho); stroke: none; }
    .ico .b { fill: var(--vinho); stroke: #F4F2EE; stroke-width: 2; } .ico .bw { stroke: #fff; stroke-width: 3; }
    .ico .ok { fill: var(--graf); stroke: #F4F2EE; stroke-width: 2; } .ico .okw { stroke: #fff; stroke-width: 2.8; } .ico .sf { fill: var(--graf); stroke: none; } .ico .sm { stroke: var(--graf); stroke-width: 5.4; } .ico .corpo { fill: var(--graf); stroke: none; }` : ''}
  ${estilo === 'divertido' ? `.ico { width: 2.25rem; height: 2.25rem; } .ico svg { stroke-width: 2.6; } li { padding: .2rem 0; gap: .7rem; } .lembrete { margin-top: .7rem; }
    .ico .r { fill: #F1E1DE; } .ico .p { fill: var(--graf); stroke: none; } .ico .w { fill: #fff; } .ico .bo { fill: #E6A4A1; stroke: none; }
    .ico .b { fill: var(--vinho); stroke: #F4F2EE; stroke-width: 2; } .ico .bw { stroke: #fff; stroke-width: 3.2; }` : ''}
  ${estilo === 'carinha' ? `.ico { width: 2rem; height: 2rem; } .ico .r { fill: #EAD9D6; } .ico .p { fill: var(--graf); stroke: none; }
    .ico .b { fill: var(--vinho); stroke: #F4F2EE; stroke-width: 2; } .ico .bw { stroke: #fff; stroke-width: 3.4; }` : ''}
  .lembrete { margin-top: 1.1rem; font-size: .8rem; line-height: 1.2; }
  .lembrete .cursiva { display: block; font-family: 'Great Vibes', cursive; font-size: 2rem; line-height: 1.05; color: var(--vinho); margin: .05rem 0 .1rem; }
  .rodape { width: 100%; justify-content: center; border-top: 0; padding-top: .4rem; }
  .marca { font-size: .4rem; letter-spacing: .3em; color: var(--graf); } .apoio { display: none; }`;
  return pagina(w, h, w / 21, css, `${enso()}
  <header><div class="ligacao">${kicker}</div><h1 class="titulo">${titulo}</h1><div class="regua"></div></header>
  <main>
    <ol>${itens.map(([t, k]) => `<li><span class="ico">${icone(k, estilo)}</span><span>${t}</span></li>`).join('')}</ol>
    <div class="lembrete">${lembrete3[0]}<span class="cursiva">${lembrete3[1]}</span>${lembrete3[2]}</div>
  </main>
  ${rodape()}`);
}


// ---- Estilo parede para as demais placas ----
const PAREDE_CSS = `
  :root { --graf: #3B3A3A; --vinho: #8E2B2F; }
  body { background: #F4F2EE; color: var(--graf); }
  .enso { position: absolute; z-index: 0; opacity: .3; }
  header, main, .rodape, .kanji, .marca { position: relative; z-index: 1; }
  .anton { font-family: 'Anton', sans-serif; font-weight: 400; text-transform: uppercase; letter-spacing: .02em; line-height: 1.05; }
  .cursiva { font-family: 'Great Vibes', cursive; color: var(--vinho); line-height: 1; }
  .ligacao { display: flex; align-items: center; justify-content: center; letter-spacing: .02em; }
  .ligacao::before, .ligacao::after { content: ""; flex: none; background: var(--graf); }
  .kanji { position: absolute; z-index: 1; display: flex; flex-direction: column; align-items: center; }
  .kanji b { font-family: 'Noto Serif JP', serif; font-weight: 600; line-height: 1.15; color: #6F6B67; }
  .kanji span { font-family: 'Anton', sans-serif; letter-spacing: .08em; color: var(--vinho); border-bottom: .03rem solid var(--vinho); }
  .ico svg { width: 100%; height: 100%; display: block; stroke: var(--graf); stroke-width: 2.4; }
  .ico .v { stroke: var(--vinho); } .ico .f { fill: var(--vinho); stroke: none; }
  .ico .r { fill: #F1E1DE; } .ico .p { fill: var(--graf); stroke: none; } .ico .w { fill: #fff; }
  .ico .b { fill: var(--vinho); stroke: #F4F2EE; stroke-width: 2; } .ico .bw { stroke: #fff; stroke-width: 3; }
  .ico .ok { fill: var(--graf); stroke: #F4F2EE; stroke-width: 2; } .ico .okw { stroke: #fff; stroke-width: 2.8; } .ico .sf { fill: var(--graf); stroke: none; } .ico .sm { stroke: var(--graf); stroke-width: 5.4; } .ico .corpo { fill: var(--graf); stroke: none; }
  .marca { font-family: 'Poppins', sans-serif; font-weight: 700; color: var(--graf); }`;
const KANJI = (k, legenda) => `<div class="kanji">${[...k].map(c => `<b>${c}</b>`).join('')}${legenda ? `<span>${legenda}</span>` : ''}</div>`;

// Destaque (sala de aula, luzes): título Anton, palavra em cursiva, bonequinho, linhas. Unidade = largura/10.
function paredeDestaque(w, h, { kicker, titulo, cursiva, ico, linhas, kanji, legenda }) {
  const css = PAREDE_CSS + `
  body { padding: .9rem .8rem .5rem; align-items: center; text-align: center; }
  .enso { width: 12rem; height: 12rem; left: -1.5rem; top: 2rem; }
  .kanji { position: absolute; right: .45rem; top: .75rem; } .kanji b { font-size: .8rem; } .kanji span { margin-top: .12rem; font-size: .2rem; padding-bottom: .04rem; }
  main { flex: 1; width: 100%; align-items: center; justify-content: center; }
  .ligacao { gap: .25rem; font-size: .34rem; } .ligacao::before, .ligacao::after { width: 1rem; height: .02rem; }
  .titulo { font-size: 1.65rem; }
  .cursiva { font-size: 1.15rem; margin-top: -.05rem; }
  .ico { display: block; width: 2.6rem; height: 2.6rem; margin: .3rem 0 .2rem; }
  .linha { font-size: .4rem; line-height: 1.35; }
  .regua { width: 1rem; height: .04rem; background: var(--vinho); margin: .2rem auto .25rem; }
  .marca { font-size: .19rem; letter-spacing: .3em; padding-top: .2rem; }`;
  return pagina(w, h, w / 10, css, `${enso(5)}
  <main>
    <div class="ligacao">${kicker}</div>
    <div style="margin-top:.25rem"><span class="fit anton titulo">${titulo}</span></div>
    <div class="cursiva">${cursiva}</div>
    <span class="ico">${icone(ico, 'bonecos')}</span>
    <div class="regua"></div>
    ${linhas.map(l => `<div class="linha">${l}</div>`).join('')}
  </main>
  <span class="marca">TATSUO ACADEMY</span>`);
}

// Direção: seta, ambientes em Anton, "e" em cursiva, onde fica entre fios. Unidade = largura/20.
function paredeDirecao(w, h, { seta, nomes, onde, kanji, legenda }) {
  const giro = { cima: 0, direita: 90, baixo: 180, esquerda: 270 }[seta];
  const css = PAREDE_CSS + `
  body { padding: 2rem 1.6rem 1rem; align-items: center; text-align: center; }
  .enso { width: 25rem; height: 25rem; left: -2.5rem; top: 3.5rem; }
  .kanji { position: absolute; right: 1.3rem; top: 1.8rem; } .kanji b { font-size: 2rem; } .kanji span { margin-top: .3rem; font-size: .42rem; padding-bottom: .1rem; }
  main { flex: 1; width: 100%; align-items: center; justify-content: center; }
  .seta { width: 4.2rem; height: 4.2rem; margin-bottom: 1rem; }
  .nome { font-size: 3.8rem; }
  .cursiva { font-size: 2.6rem; margin: .1rem 0 .2rem; }
  .regua { width: 2.4rem; height: .08rem; background: var(--vinho); margin: 1.2rem auto .9rem; }
  .ligacao { gap: .6rem; font-size: .95rem; } .ligacao::before, .ligacao::after { width: 2.4rem; height: .04rem; }
  .marca { font-size: .42rem; letter-spacing: .3em; }`;
  return pagina(w, h, w / 20, css, `${enso(9)}
  <main>
    <svg class="seta" viewBox="0 0 100 100" style="transform:rotate(${giro}deg)" fill="none" stroke="#8E2B2F" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"><path d="M50 92 V10 M18 42 L50 10 L82 42"/></svg>
    ${nomes.map((n, i) => (i ? '<div class="cursiva">e</div>' : '') + `<div><span class="fit anton nome">${n}</span></div>`).join('')}
    <div class="regua"></div>
    <div class="ligacao">${onde}</div>
  </main>
  <span class="marca">TATSUO ACADEMY</span>`);
}

// Porta (20x8): pictograma opcional, nome em Anton, complemento em cursiva, ensō à direita. Unidade = largura/20.
function paredePorta(w, h, { nome, sub, ico }) {
  const css = PAREDE_CSS + `
  body { flex-direction: row; align-items: center; padding: 0 1.5rem; gap: 1rem; }
  .enso { width: 10rem; height: 10rem; left: auto; right: -2.6rem; top: -1rem; opacity: .28; }
  .ico { position: relative; z-index: 1; flex: none; width: 4.4rem; height: 5.4rem; }
  .ico svg { stroke-width: 3; }
  main { position: relative; z-index: 1; flex: 1; display: flex; flex-direction: column; justify-content: center; }
  .regua { width: 1.4rem; height: .07rem; background: var(--vinho); margin-bottom: .75rem; }
  .nome { font-size: 2.3rem; }
  .cursiva { font-size: 1.5rem; margin-top: .05rem; }
  .marca { position: absolute; right: 1.5rem; bottom: .5rem; font-size: .24rem; letter-spacing: .3em; }`;
  return pagina(w, h, w / 20, css, `${enso(3)}
  ${ico ? `<span class="ico">${icone(ico, 'bonecos')}</span>` : ''}
  <main>
    <div class="regua"></div>
    <div><span class="fit anton nome">${nome}</span></div>
    ${sub ? `<div class="cursiva">${sub}</div>` : ''}
  </main>
  <span class="marca">TATSUO ACADEMY</span>`);
}


// Só fundo e fonte das paredes sobre um modelo original (sem ícones, kanji ou cursiva):
// fundo off-white com ensō, títulos em Anton, grafite e vinho no lugar de preto e vermelho.
const comParede = modelo => (w, h, dados) => {
  const largo = w > h;
  const lado = largo ? h * 1.3 : w * 1.25;
  const pos = largo ? `right:${-h * .3}mm;top:${-h * .15}mm` : `left:${-w * .08}mm;top:${h * .16}mm`;
  const css = `
  :root { --verm: #8E2B2F; --capa: #F4F2EE; --tinta: #3B3A3A; --cinza: #6F6B67; --fio: rgba(59,58,58,.18); --card: #EAE5DE; --papel: #F4F2EE; }
  html, body { overflow: hidden; } body { background: #F4F2EE !important; color: #3B3A3A !important; }
  .diag { display: none; }
  .enso { position: absolute; z-index: 0; opacity: .3; width: ${lado}mm; height: ${lado}mm; ${pos}; }
  header, main, ol, .rodape, .lembrete { position: relative; z-index: 1; }
  .titulo, .titulo .fit { font-family: 'Anton', sans-serif !important; font-weight: 400 !important; text-transform: uppercase; letter-spacing: .02em; }
  .kicker { color: var(--verm) !important; }
  .regua { background: var(--verm) !important; }
  .linha { color: #3B3A3A; }
  .rodape { border-top-color: var(--fio) !important; }
  .marca { color: #3B3A3A !important; }
  li .ico, .ico { background: none !important; border-radius: 0 !important; padding: 0 !important; }
  li.ic .ico { width: 2.7rem; height: 2.7rem; } li.ic { padding: .22rem 0; gap: .7rem; }
  .ico svg { width: 100%; height: 100%; display: block; stroke: #3B3A3A; stroke-width: 2.4; }
  .ico .v { stroke: #8E2B2F; } .ico .f { fill: #8E2B2F; stroke: none; } .ico .r { fill: #F1E1DE; } .ico .p { fill: #3B3A3A; stroke: none; } .ico .w { fill: #fff; }
  .ico .b { fill: #8E2B2F; stroke: #F4F2EE; stroke-width: 2; } .ico .bw { stroke: #fff; stroke-width: 3; }
  .ico .ok { fill: #3B3A3A; stroke: #F4F2EE; stroke-width: 2; } .ico .okw { stroke: #fff; stroke-width: 2.8; }
  .ico .sf { fill: #3B3A3A; stroke: none; } .ico .sm { stroke: #3B3A3A; stroke-width: 5.4; }</style>`;
  return modelo(w, h, dados).replace('</style>', css).replace('<body>', `<body>${enso(7)}`).replace(/#A00F0F/g, '#8E2B2F');
};

// Placas de destaque em bordô: fundo bordô, ensō num bordô mais escuro, títulos em Anton branco, bonequinho branco.
const comBordo = modelo => (w, h, dados) => {
  const lado = w * 1.25;
  const css = `
  html, body { overflow: hidden; }
  body { background: #8C1C1C !important; color: #fff !important; }
  .diag { display: none; }
  .enso { position: absolute; z-index: 0; opacity: .55; width: ${lado}mm; height: ${lado}mm; left: ${-w * .08}mm; top: ${h * .16}mm; }
  header, main, .rodape { position: relative; z-index: 1; }
  .titulo, .titulo .fit { font-family: 'Anton', sans-serif !important; font-weight: 400 !important; text-transform: uppercase; letter-spacing: .02em; color: #fff; }
  .kicker { color: rgba(255,255,255,.8) !important; }
  .regua { background: #fff !important; }
  .linha, .marca { color: #fff !important; }
  .rodape { border-top-color: rgba(255,255,255,.3) !important; }
  .ico svg { width: 100%; height: 100%; display: block; stroke: #3B3A3A; stroke-width: 2.4; }
  .ico .sf { fill: #fff; stroke: none; } .ico .sm { stroke: #fff; stroke-width: 5.4; }
  .ico .w { fill: #fff; } .ico .r { fill: #F1E1DE; } .ico .v { stroke: #8E2B2F; } .ico .f { fill: #8E2B2F; stroke: none; }</style>`;
  return modelo(w, h, dados).replace('</style>', css).replace('<body>', `<body>${enso(7)}`).replace('stroke="#9E9892"', 'stroke="#5A0F10"');
};
// Aviso de destaque: fundo vermelho da capa, título branco em serifa. Unidade = largura/10.
function destaque(w, h, { kicker, titulo, linhas, ico }) {
  const css = `
  body { background: var(--capa); color: #fff; padding: 1rem .85rem .6rem; }
  .diag line { stroke: #fff; stroke-opacity: .22; }
  main { flex: 1; justify-content: center; }
  .kicker { color: rgba(255,255,255,.78); font-size: .27rem; letter-spacing: .3em; }
  .titulo { margin-top: .3rem; } .titulo .fit { font-size: 1.45rem; }
  .regua { background: #fff; width: 1.3rem; height: .05rem; margin: .55rem 0 .5rem; }
  .linha { font-size: .46rem; line-height: 1.45; }
  .rodape { border-top-color: rgba(255,255,255,.3); padding-top: .3rem; }
  .marca { font-size: .22rem; letter-spacing: .3em; } .apoio { display: none; }
  .dico { display: block; width: 3rem; height: 3rem; margin: .45rem 0 0 -.2rem; }`;
  return pagina(w, h, w / 10, css, `${DIAG(4.2, .6)}
  <main>
    <div class="kicker">${kicker}</div>
    <h1 class="titulo">${titulo.map(t => `<div><span class="fit">${t}</span></div>`).join('')}</h1>
    ${ico ? `<span class="ico dico">${icone(ico, 'bonecos')}</span>` : ''}
    <div class="regua"></div>
    ${linhas.map(l => `<div class="linha">${l}</div>`).join('')}
  </main>
  ${rodape()}`);
}

// Placa de porta: fio vermelho, nome em serifa, complemento em rótulo. Unidade = largura/20.
// Pictogramas das portas dos banheiros: executivo de terno e executiva de blazer (busto, grafite chapado).
const G = '#3B3A3A', V = '#8E2B2F', PELE = '#F4F2EE';
const PICTO = {
  executivo: `<svg viewBox="0 0 64 64" stroke-linecap="round" stroke-linejoin="round">
    <path d="M10 64c0-13 7-20 22-22 15 2 22 9 22 22z" fill="${G}"/>
    <path d="M26 42.5l6 11 6-11c-2-.6-4-.9-6-.9s-4 .3-6 .9z" fill="#fff"/>
    <path d="M32 45l-2.6 3 2.6 12 2.6-12z" fill="${V}"/><path d="M29.6 44.6h4.8l-2.4 2.6z" fill="${V}"/>
    <path d="M25.5 42.5l5 13M38.5 42.5l-5 13" stroke="#fff" stroke-width="1.4" fill="none"/>
    <path d="M28 33v8.5c2.6 1.2 5.4 1.2 8 0V33" fill="${PELE}" stroke="${G}" stroke-width="2.2"/>
    <ellipse cx="32" cy="22" rx="10.5" ry="12" fill="${PELE}" stroke="${G}" stroke-width="2.4"/>
    <path d="M21.4 21c-1.4-9 4-15 11.2-15C40 6 44 11 42.8 21c-1.2-3.4-3-5.6-5.4-6.8-5 2.2-10.8 2.4-15 .2-.6 2.2-.9 4.4-1 6.6z" fill="${G}"/>
    <circle cx="28" cy="23" r="1.4" fill="${G}"/><circle cx="36" cy="23" r="1.4" fill="${G}"/>
    <path d="M28.6 28.4q3.4 2.8 6.8 0" fill="none" stroke="${G}" stroke-width="1.8"/></svg>`,
  executiva: `<svg viewBox="0 0 64 64" stroke-linecap="round" stroke-linejoin="round">
    <path d="M10 64c0-13 7-20 22-22 15 2 22 9 22 22z" fill="${G}"/>
    <path d="M25 42.6l7 10 7-10c-2.2-.6-4.6-.9-7-.9s-4.8.3-7 .9z" fill="#fff"/>
    <path d="M25 42.6l6 14M39 42.6l-6 14" stroke="#fff" stroke-width="1.4" fill="none"/>
    <circle cx="27" cy="58" r="1.6" fill="${V}"/>
    <path d="M28 33v8.5c2.6 1.2 5.4 1.2 8 0V33" fill="${PELE}" stroke="${G}" stroke-width="2.2"/>
    <circle cx="32" cy="5.4" r="5" fill="${G}"/>
    <ellipse cx="32" cy="22" rx="10" ry="11.6" fill="${PELE}" stroke="${G}" stroke-width="2.4"/>
    <path d="M21.6 23c-2-10 3-16.4 10.4-16.4S44.4 13 42.4 23c-.8-4.6-3-7.6-6-9.2-3 2.4-8.6 3.6-12.6 3.4-1.2 1.8-1.9 3.8-2.2 5.8z" fill="${G}"/>
    <rect x="24.2" y="20.4" width="7" height="5.2" rx="2.4" fill="none" stroke="${G}" stroke-width="1.6"/>
    <rect x="32.8" y="20.4" width="7" height="5.2" rx="2.4" fill="none" stroke="${G}" stroke-width="1.6"/>
    <path d="M31.2 22.4h1.6" stroke="${G}" stroke-width="1.4"/>
    <circle cx="27.7" cy="23" r="1.1" fill="${G}"/><circle cx="36.3" cy="23" r="1.1" fill="${G}"/>
    <path d="M29.4 29q2.6 2.2 5.2 0q-2.6.6-5.2 0z" fill="${V}" stroke="${V}" stroke-width="1"/>
    <circle cx="21.6" cy="27" r="1.3" fill="${V}"/><circle cx="42.4" cy="27" r="1.3" fill="${V}"/></svg>`,
};

function porta(w, h, { nome, sub, ico }) {
  const css = `
  main { flex: 1; justify-content: center; padding: 0 1.5rem; }
  .regua { width: 1.4rem; height: .08rem; margin-bottom: .55rem; }
  .titulo .fit { font-size: 1.7rem; }
  .kicker { margin-top: .4rem; font-size: .4rem; letter-spacing: .24em; }
  .marca { position: absolute; right: 1.5rem; bottom: .55rem; font-size: .26rem; letter-spacing: .3em; color: var(--cinza); }`;
  const texto = `<div class="regua"></div>
    <div class="titulo"><span class="fit">${nome}</span></div>
    ${sub ? `<div class="kicker">${sub}</div>` : ''}`;
  return pagina(w, h, w / 20, css + (ico ? `
  main.com-ico { flex-direction: row; align-items: center; justify-content: flex-start; gap: 1.1rem; }
  .pic { flex: none; width: 5.4rem; height: 5.4rem; } .pic svg { width: 100%; height: 100%; display: block; }` : ''), `${DIAG(3.4, .7)}
  ${ico ? `<main class="com-ico"><span class="pic">${PICTO[ico]}</span><div>${texto}</div></main>` : `<main>${texto}</main>`}
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
  // Opções de ícone pra comparar: só com "node gerar.js opcoes"
  // Conjunto completo no estilo das paredes: só com "node gerar.js parede"
  if (filtro.includes('parede')) {
    const D = 'estilo-parede/';
    const P = n => PLACAS.find(p => p[0] === n);
    const lista2 = (nome, base, extra) => PLACAS.push([D + nome, base[1], base[2], parede, { ...base[4], estilo: 'bonecos', ...extra }]);
    for (const sexo of ['masculino', 'feminino']) lista2(`placa-banheiro-${sexo}`, P(`placa-banheiro-${sexo}`), {
      kicker: `banheiro ${sexo}`, kanji: '清潔', kanjiLegenda: 'ASSEIO', lembrete3: ['Lembre-se: depois de você,', 'outras pessoas', 'vão usar este banheiro.'] });
    // Demais placas: desenho original, só com fundo e fonte das paredes
    for (const nome of ['placa-copa', 'placa-sala-reuniao', 'placa-sala-aula', 'placa-luzes-ar', 'placa-buffet-banheiros',
      ...['banheiro-masculino', 'banheiro-feminino', 'sala-de-aula', 'sala-de-reuniao', 'copa', 'recepcao', 'restrito'].map(x => `placas-porta/porta-${x}`)]) {
      const [n, w, h, modelo, dados, dpi] = P(nome);
      const extra = n === 'placa-copa' ? { estilo: 'bonecos', itens: [['Lave, seque e guarde a sua louça', 'louca'], ['Identifique seus alimentos com nome e data', 'etiqueta'],
          ['Não deixe comida vencida na geladeira', 'vencida'], [`Limpe o que sujar: pia, mesa e micro${NBH}ondas`, 'limpar'], ['Jogue o lixo no lugar certo', 'lixo-certo']] }
        : null;
      if (extra) { PLACAS.push([D + n, w, h, comParede(modelo), { ...dados, ...extra }, dpi]); continue; }
      if (n === 'placa-sala-aula' || n === 'placa-luzes-ar') {
        PLACAS.push([D + n, w, h, comBordo(modelo), { ...dados, ico: n === 'placa-sala-aula' ? 'silencio' : 'interruptor' }, dpi]); continue; }
      const ico = n.endsWith('porta-banheiro-masculino') ? 'executivo' : n.endsWith('porta-banheiro-feminino') ? 'executiva' : null;
      PLACAS.push([D + n, w, h, comParede(modelo), ico ? { ...dados, ico } : dados, dpi]);
    }
  }
  if (filtro.includes('opcoes')) for (const sexo of ['masculino', 'feminino']) {
    const base = PLACAS.find(p => p[0] === `placa-banheiro-${sexo}`);
    for (const [letra, estilo] of [['A', 'linha'], ['B', 'selo'], ['C', 'carinha']])
      PLACAS.push([`opcoes-icones/banheiro-${sexo}-${letra}-${estilo}`, base[1], base[2], lista, { ...base[4], estilo }]);
    for (const [sufixo, estilo] of [['', 'linha'], ['-selo', 'selo'], ['-carinha', 'carinha'], ['-divertido', 'divertido'], ['-bonecos', 'bonecos']])
      PLACAS.push([`opcoes-icones/banheiro-${sexo}-D-parede${sufixo}`, base[1], base[2], parede, { ...base[4], estilo,
        kicker: `banheiro ${sexo}`, kanji: '清潔', kanjiLegenda: 'ASSEIO',
        lembrete3: ['Lembre-se: depois de você,', 'outras pessoas', 'vão usar este banheiro.'] }]);
  }
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
