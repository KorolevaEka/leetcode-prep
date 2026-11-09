// Java в браузере: CheerpJ (javac из JDK 21) в скрытом iframe java-frame.html. Зацикливание обрывает
// сторож из java-guard.js (страница стоит до дедлайна ~10 с, потом оживает); на прочие зависания
// (sleep, wait) — таймер: iframe удаляется вместе с рантаймом, следующий запуск создаёт новый.
import { guard } from "./java-guard.js";

const HARNESS = ["TestRunner.java", "__LCT.java", "org/junit/jupiter/api/Test.java", "org/junit/jupiter/api/DisplayName.java", "org/junit/jupiter/api/BeforeEach.java",
  "org/junit/jupiter/api/Assertions.java", "org/junit/jupiter/api/function/Executable.java"];
const TIMEOUT = "Таймаут: решение работает слишком долго (бесконечный цикл?)";
let frame = null, ready = false, pending = null, harness = null;

const loadHarness = () => harness ??= Promise.all(HARNESS.map(async p => {
  const r = await fetch(new URL("java/" + p, import.meta.url));
  if (!r.ok) throw new Error(`${p}: ${r.status}`);
  return [p.split("/").pop(), await r.text()];
})).then(Object.fromEntries).catch(e => { harness = null; throw e; });

function settle(f, r) {
  if (!pending || pending.frame !== f) return;
  clearTimeout(pending.timer);
  const p = pending; pending = null;
  p.resolve(r);
}

function kill(f, output) {
  f.remove();
  if (frame === f) { frame = null; ready = false; }
  settle(f, { passed: false, output });
}

function arm(ms) {
  clearTimeout(pending.timer);
  const f = pending.frame;
  pending.timer = setTimeout(() => {
    let out = "";
    try { out = f.contentWindow.lct.output(); } catch {}
    // ponytail: CheerpJ после перезагрузки вкладки бывает очень медленным (см. java-spike.md) — лечится новой вкладкой
    kill(f, (out ? out + "\n" : "") + TIMEOUT + "\nЕсли Java зависает и на простом коде, открой сайт в новой вкладке.");
  }, ms);
}

function get() {
  if (frame) return frame;
  const f = frame = document.createElement("iframe");
  f.src = new URL("java-frame.html", import.meta.url);
  f.style.display = "none";
  ready = false;
  f.started = new Promise((res, rej) => { f.onload = res; f.onerror = rej; })
    .then(async () => {
      const [files] = await Promise.all([loadHarness(), f.contentWindow.lct.init()]);
      await f.contentWindow.lct.run(files, "/files/lct/warmup"); // прогрев: скачивает модули javac
      if (frame === f) { ready = true; if (pending?.frame === f) arm(15000); }
      return files;
    });
  f.started.catch(e => kill(f, "Не удалось загрузить Java: " + (e?.message || e)));
  document.body.append(f);
  return f;
}

addEventListener("pagehide", () => { frame?.remove(); frame = null; ready = false; });

export const warmup = get;
export const isReady = () => ready;

const clean = s => s.replaceAll("/str/", "");

async function runIn(f, files, subject, tests) {
  const dir = `/files/lct/r${Date.now()}${Math.floor(Math.random() * 1e6)}`; // своя папка: старые .class не подмешаются
  const all = (s, t) => ({ ...files, "Solution.java": s, "SolutionTest.java": t });
  let r = await f.contentWindow.lct.run(all(guard(subject), guard(tests)), dir, "TestRunner", [dir]);
  // если сторож сломал компиляцию — компилируем как есть (без защиты от зацикливания), ошибки показываем без вставок
  if (r.compile !== 0) r = await f.contentWindow.lct.run(all(subject, tests), dir, "TestRunner", [dir]);
  if (r.compile !== 0) return { passed: false, output: clean(r.compileOut) };
  return { passed: r.code === 0, output: clean(r.out), ...(r.code === 5 && { noTests: true }) };
}

export function execute(task, subject, tests) {
  const f = get();
  return new Promise(resolve => {
    pending = { resolve, timer: null, frame: f };
    // первый запуск качает JDK (десятки МБ); 15 с (сторож срабатывает раньше) — только когда рантайм готов
    arm(ready ? 15000 : 180000);
    f.started.then(files => runIn(f, files, subject, tests))
      .then(r => settle(f, r), e => settle(f, { passed: false, output: "Не удалось выполнить Java: " + (e?.message || e) }));
  });
}
