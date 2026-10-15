// Busca a posicao do bloco de texto de cada fatia (layout F). Uso, da raiz do projeto:
//   node .claude/skills/carrossel/modelos/infografico/frameworks/circulo-em-fatias_busca-posicao.js [caminho/slide-01.html]
// Sem argumento, mede o slide 1 do post 224. Caminhos achados a partir deste arquivo (sem caminho fixo de usuario).
const path = require('path'), fs = require('fs'), { pathToFileURL } = require('url');
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd(), __dirname] }));
const RAIZ = (() => { let d = __dirname; for (;;) { if (fs.existsSync(path.join(d, '.claude/skills/carrossel'))) return d; const up = path.dirname(d); if (up === d) return process.cwd(); d = up; } })();
const ALVO = path.resolve(process.argv[2] || path.join(RAIZ, 'conteudo/carrosseis/224_tres-pilares/instagram/slide-01.html'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto(pathToFileURL(ALVO).href);
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
const res=await p.evaluate(()=>{const CX=540,CY=770,R=430,RIN=105;const SECT=[[150,270],[270,390],[30,150]];
 const badges=[...document.querySelectorAll('.badge')].map(e=>{const r=e.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2,r.width/2]});
 // alvo: mesma distancia ao centro que o bloco da Cultura ocupa hoje
 const fc=document.querySelector('.fat[data-sec="2"]').getBoundingClientRect(); const rc=Math.hypot(fc.left+fc.width/2-CX, fc.top+fc.height/2-CY);
 const out={rc:Math.round(rc)};
 for(const s of [0,1]){const f=document.querySelector(`.fat[data-sec="${s}"]`);f.style.transform='none';const [a0,a1]=SECT[s];const am=(a0+a1)/2*Math.PI/180;
  const tx=CX+rc*Math.cos(am), ty=CY+rc*Math.sin(am);let best=null;
  for(let wd=240;wd<=380;wd+=10){f.style.maxWidth=wd+'px';f.style.left='0px';f.style.top='0px';const fr=f.getBoundingClientRect();
   const rects=[];for(const el of f.querySelectorAll('.t,.d')){const rg=document.createRange();rg.selectNodeContents(el);for(const l of rg.getClientRects())rects.push([l.left-fr.left,l.top-fr.top,l.right-fr.left,l.bottom-fr.top])}
   for(let x=90;x<=990-fr.width;x+=4)for(let y=340;y<=1150;y+=4){const cxb=x+fr.width/2, cyb=y+fr.height/2;const dist=Math.hypot(cxb-tx,cyb-ty);if(best&&dist>best.dist+40)continue;
    let worst=1e9,ok=true;
    for(const [l,tp,r,bt] of rects){for(let k=0;k<=8&&ok;k++){const pts=[[x+l+(r-l)*k/8,y+tp],[x+l+(r-l)*k/8,y+bt],[x+l,y+tp+(bt-tp)*k/8],[x+r,y+tp+(bt-tp)*k/8]];
      for(const [px,py] of pts){const dx=px-CX,dy=py-CY,d=Math.hypot(dx,dy);let ang=Math.atan2(dy,dx)*180/Math.PI;while(ang<a0)ang+=360;if(ang>a1){ok=false;break}
       const dl=Math.min(d*Math.sin((ang-a0)*Math.PI/180),d*Math.sin((a1-ang)*Math.PI/180));
       const m=Math.min(R-24-d,d-RIN-20,dl-20,...badges.map(([bx,by,br])=>Math.hypot(px-bx,py-by)-br-12));if(m<0){ok=false;break}worst=Math.min(worst,m)}}if(!ok)break}
    if(!ok||worst<8)continue;const sc=dist-worst*0.3-wd*0.05;if(!best||sc<best.sc)best={sc,dist:Math.round(dist),wd,x,y,w:Math.round(fr.width),h:Math.round(fr.height),worst:Math.round(worst)}}}
  out[s]=best}
 return out});
console.log(JSON.stringify(res));await b.close();})();
