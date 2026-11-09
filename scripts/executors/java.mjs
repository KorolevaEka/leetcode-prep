// Настоящий javac + java во временной папке; харнесс — web/runners/java (мини-JUnit 5).
import { mkdtempSync, writeFileSync, readdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

const harness = join(dirname(fileURLToPath(import.meta.url)), "../../web/runners/java");
const harnessFiles = readdirSync(harness, { recursive: true }).filter(f => f.endsWith(".java")).map(f => join(harness, f));
const TIMEOUT = "Таймаут: решение работает слишком долго (бесконечный цикл?)";

function sh(cmd, args, cwd, ms) {
  return new Promise(resolve => {
    let out = "", timedOut = false;
    const p = spawn(cmd, args, { cwd });
    const timer = setTimeout(() => { timedOut = true; p.kill("SIGKILL"); }, ms);
    const add = d => { if (out.length < 100000) out += d; };
    p.stdout.on("data", add);
    p.stderr.on("data", add);
    p.on("error", e => { clearTimeout(timer); resolve({ code: -1, out: String(e) }); });
    p.on("close", code => { clearTimeout(timer); resolve({ code, out, timedOut }); });
  });
}

export async function execute(task, subject, tests) {
  const dir = mkdtempSync(join(tmpdir(), "java-task-"));
  try {
    writeFileSync(join(dir, "Solution.java"), subject);
    writeFileSync(join(dir, "SolutionTest.java"), tests);
    const c = await sh("javac", ["-encoding", "UTF-8", "-nowarn", "-d", "out", "Solution.java", "SolutionTest.java", ...harnessFiles], dir, 60000);
    if (c.code !== 0) return { passed: false, output: c.out.split(harness + "/").join("") };
    const r = await sh("java", ["-Dstdout.encoding=UTF-8", "-Dstderr.encoding=UTF-8", "-cp", "out", "TestRunner"], dir, 10000);
    if (r.timedOut) return { passed: false, output: r.out + "\n" + TIMEOUT };
    return { passed: r.code === 0, output: r.out, ...(r.code === 5 && { noTests: true }) };
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}
