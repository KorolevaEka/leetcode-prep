// tsc из npm + запуск скомпилированного JS в дочернем node с таймаутом.
import ts from "typescript";
import { mkdtempSync, writeFileSync, readFileSync, rmSync, existsSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { spawn } from "node:child_process";
import { createRequire } from "node:module";
import { fileURLToPath, pathToFileURL } from "node:url";
import { compileAndRun } from "../../web/runners/ts-core.js";
import { truncate } from "../../web/check.js";

const runners = join(dirname(fileURLToPath(import.meta.url)), "../../web/runners");
const libDir = dirname(createRequire(import.meta.url).resolve("typescript/lib/typescript.js"));
const dts = readFileSync(join(runners, "ts-harness.d.ts"), "utf8");
const harnessUrl = pathToFileURL(join(runners, "ts-harness.js")).href;
const readLib = name => readFileSync(join(libDir, name), "utf8");

const CHILD = `
import { writeFileSync, readFileSync } from "node:fs";
const dir = process.argv[1];
const { runTests } = await import(${JSON.stringify(harnessUrl)});
const r = await runTests(JSON.parse(readFileSync(dir + "/js.json", "utf8")));
writeFileSync(dir + "/result.json", JSON.stringify(r));
process.exit(0);
`;

export async function execute(task, subject, tests) {
  const { diagnostics, js } = compileAndRun(ts, { "solution.ts": subject, "solution.test.ts": tests, "ts-harness.d.ts": dts }, readLib);
  if (diagnostics.length) return { passed: false, output: truncate(diagnostics.join("\n")) };
  const dir = mkdtempSync(join(tmpdir(), "ts-task-"));
  try {
    writeFileSync(join(dir, "js.json"), JSON.stringify(js));
    return await new Promise(resolve => {
      let err = "", timedOut = false;
      const p = spawn(process.execPath, ["--input-type=module", "-e", CHILD, dir], { cwd: dir, stdio: ["ignore", "ignore", "pipe"] });
      const timer = setTimeout(() => { timedOut = true; p.kill("SIGKILL"); }, 10000);
      p.stderr.on("data", d => { if (err.length < 100000) err += d; });
      p.on("error", e => { clearTimeout(timer); resolve({ passed: false, output: String(e) }); });
      p.on("close", () => {
        clearTimeout(timer);
        if (timedOut) return resolve({ passed: false, output: "Таймаут: решение работает слишком долго (бесконечный цикл?)" });
        const file = join(dir, "result.json");
        if (!existsSync(file)) return resolve({ passed: false, output: truncate(err || "Процесс завершился без результата") });
        const r = JSON.parse(readFileSync(file, "utf8"));
        resolve({ ...r, output: truncate(r.output) });
      });
    });
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}
