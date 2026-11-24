// Uso:
//   node render.js previa 0.5,2,4,...   -> previa/grid.jpg (quadros soltos + grade)
//   node render.js video saida.mp4      -> MP4 1080x1920, 30 fps
// Rodar da raiz do repositório (usa o playwright de node_modules).
const path = require('path');
const fs = require('fs');
const { spawn, spawnSync } = require('child_process');
const { chromium } = require(path.resolve('node_modules/playwright'));

const FF = 'C:/Users/DELL/AppData/Local/Programs/Python/Python312/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v9.0.2.exe';
const DIR = __dirname;
const URL = 'file:///' + path.join(DIR, 'cena.html').replace(/\\/g, '/');
const FPS = 30;

(async () => {
  const [mode, arg] = process.argv.slice(2);
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto(URL);
  await page.evaluate(() => document.fonts.ready);
  const stage = await page.$('#stage');

  if (mode === 'previa') {
    const out = path.join(DIR, 'previa');
    fs.mkdirSync(out, { recursive: true });
    const ts = arg.split(',').map(Number);
    for (let i = 0; i < ts.length; i++) {
      await page.evaluate(t => renderAt(t), ts[i]);
      await stage.screenshot({ path: path.join(out, `q${String(i).padStart(2, '0')}.png`) });
    }
    const cols = Math.min(ts.length, 6), rows = Math.ceil(ts.length / cols);
    spawnSync(FF, ['-y', '-loglevel', 'error', '-i', path.join(out, 'q%02d.png'),
      '-vf', `scale=300:-1,tile=${cols}x${rows}:padding=6`, '-frames:v', '1', path.join(out, 'grid.jpg')], { stdio: 'inherit' });
    console.log('ok', path.join(out, 'grid.jpg'));
  } else {
    const total = await page.evaluate(() => window.TOTAL);
    const n = Math.round(total * FPS);
    const ff = spawn(FF, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', '-preset', 'slow', '-movflags', '+faststart', arg], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let i = 0; i < n; i++) {
      await page.evaluate(t => renderAt(t), i / FPS);
      const buf = await stage.screenshot({ type: 'png' });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (i % 60 === 0) console.log(`quadro ${i}/${n}`);
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    console.log('ok', arg);
  }
  await browser.close();
})();
