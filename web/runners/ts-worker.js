// TypeScript в отдельном потоке: компиляция (tsc из CDN) + запуск тестов; зависший код убиваем terminate().
const CDN = "https://cdn.jsdelivr.net/npm/typescript@5.6.3/lib/";
importScripts(CDN + "typescript.js");

const libs = new Map();
function get(url) {
  const x = new XMLHttpRequest();
  x.open("GET", url, false);
  x.send();
  if (x.status !== 200) throw new Error(`Не удалось загрузить ${url} (${x.status})`);
  return x.responseText;
}
const readLib = name => {
  if (!libs.has(name)) libs.set(name, get(CDN + name));
  return libs.get(name);
};

const ready = (async () => {
  const [core, harness] = await Promise.all([import("./ts-core.js"), import("./ts-harness.js")]);
  const dts = get("ts-harness.d.ts");
  const compile = (subject, tests) =>
    core.compileAndRun(self.ts, { "solution.ts": subject, "solution.test.ts": tests, "ts-harness.d.ts": dts }, readLib);
  compile("export {};", "export {};"); // прогрев: подтягивает lib-файлы в кэш
  return { compile, runTests: harness.runTests };
})();

ready.then(() => postMessage({ ready: true }), e => postMessage({ initError: String(e) }));

onmessage = async ({ data: { subject, tests } }) => {
  try {
    const { compile, runTests } = await ready;
    const { diagnostics, js } = compile(subject, tests);
    if (diagnostics.length) return postMessage({ passed: false, output: diagnostics.join("\n") });
    postMessage(await runTests(js));
  } catch (e) {
    postMessage({ passed: false, output: String(e) });
  }
};
