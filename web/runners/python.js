// Python в воркере: зависший код не вешает вкладку, воркер убиваем по таймауту.
let worker = null, ready = false, pending = null;

function arm(ms) {
  clearTimeout(pending.timer);
  pending.timer = setTimeout(() => {
    const p = pending; pending = null;
    worker.terminate(); worker = null;
    p.resolve({ passed: false, output: "Таймаут: решение работает слишком долго (бесконечный цикл?)" });
  }, ms);
}

function fail(w, output) {
  w.terminate();
  if (worker === w) worker = null;
  if (pending) { clearTimeout(pending.timer); const p = pending; pending = null; p.resolve({ passed: false, output }); }
}

function get() {
  if (!worker) {
    const w = worker = new Worker(new URL("python-worker.js", import.meta.url));
    ready = false;
    w.onmessage = ({ data }) => {
      if (data.ready) { ready = true; if (pending) arm(10000); return; }
      if (data.initError) return fail(w, "Не удалось загрузить Python: " + data.initError);
      if (!pending) return;
      clearTimeout(pending.timer);
      const p = pending; pending = null;
      p.resolve(data);
    };
    w.onerror = e => fail(w, "Не удалось загрузить Python: " + (e.message || "ошибка загрузки воркера"));
  }
  return worker;
}

export const warmup = get;
export const isReady = () => ready;

export function execute(task, subject, tests) {
  const w = get();
  return new Promise(resolve => {
    pending = { resolve, timer: null };
    // первый запуск качает Pyodide и pytest (~15 МБ); 10 с отсчитываются, только когда рантайм загружен
    arm(ready ? 10000 : 120000);
    w.postMessage({ subject, tests });
  });
}
