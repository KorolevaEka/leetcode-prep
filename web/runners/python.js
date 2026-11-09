// Python + pytest в воркере (Pyodide): зависший код не вешает вкладку, воркер убиваем по таймауту.
let worker = null, ready = false;

function get() {
  if (!worker) { worker = new Worker(new URL("python-worker.js", import.meta.url)); ready = false; }
  return worker;
}

export const warmup = get;
export const isReady = () => ready;

export function execute(task, subject, tests) {
  const w = get();
  return new Promise(resolve => {
    // первый запуск качает Pyodide и pytest (~15 МБ), поэтому лимит больше
    const timer = setTimeout(() => {
      w.terminate(); worker = null;
      resolve({ passed: false, output: "Таймаут: решение работает слишком долго (бесконечный цикл?)" });
    }, ready ? 10000 : 120000);
    w.onmessage = ({ data }) => { clearTimeout(timer); ready = true; resolve(data); };
    w.postMessage({ subject, tests });
  });
}
