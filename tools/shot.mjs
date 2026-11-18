// Screenshot 1280×800 di ogni pagina della lista (usa Chrome installato sul Mac).
import { chromium } from 'playwright';
import fs from 'fs';
const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const b = await chromium.launch({ channel: 'chrome' });
const ctx = await b.newContext({ viewport: { width: 1280, height: 800 } });
const run = async j => {
  const p = await ctx.newPage();
  try {
    await p.goto(j.src, { waitUntil: 'load', timeout: 25000 });
    await p.waitForTimeout(2500);
    await p.screenshot({ path: j.png });
    console.log('ok', j.id);
  } catch (e) { console.log('ERRORE', j.id, e.message.split('\n')[0]); }
  await p.close();
};
for (let i = 0; i < jobs.length; i += 5) await Promise.all(jobs.slice(i, i + 5).map(run));
await b.close();
