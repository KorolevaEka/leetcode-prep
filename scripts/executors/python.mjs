// Настоящий CPython + pytest во временной папке.
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawn } from "node:child_process";

export async function execute(task, subject, tests) {
  const dir = mkdtempSync(join(tmpdir(), "py-task-"));
  try {
    writeFileSync(join(dir, "solution.py"), subject);
    writeFileSync(join(dir, "test_solution.py"), tests);
    return await new Promise(resolve => {
      let out = "", timedOut = false;
      const p = spawn("python3", ["-m", "pytest", "-q", "-p", "no:cacheprovider"], {
        cwd: dir, env: { ...process.env, PYTHONDONTWRITEBYTECODE: "1" },
      });
      const timer = setTimeout(() => { timedOut = true; p.kill("SIGKILL"); }, 10000);
      p.stdout.on("data", d => out += d);
      p.stderr.on("data", d => out += d);
      p.on("error", e => { clearTimeout(timer); resolve({ passed: false, output: String(e) }); });
      p.on("close", code => {
        clearTimeout(timer);
        if (timedOut) return resolve({ passed: false, output: "Таймаут: решение работает слишком долго (бесконечный цикл?)" });
        resolve({ passed: code === 0, output: out, ...(code === 5 && { noTests: true }) });
      });
    });
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}
