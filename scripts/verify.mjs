// node scripts/verify.mjs [путь]  — путь: задача, любая папка выше или ничего (все задачи).
import { spawnSync } from "node:child_process";
import { readFileSync, readdirSync } from "node:fs";
import { resolve, join, sep, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { verifyTask } from "../web/check.js";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const EXT = { python: "py", sql: "sql", ts: "ts", java: "java" };

const r = spawnSync("python3", ["scripts/build.py", "--json"], { cwd: root, encoding: "utf8", maxBuffer: 1 << 28 });
if (r.status !== 0) { console.error(r.stderr || r.stdout); process.exit(1); }
const tasks = JSON.parse(r.stdout);

const arg = resolve(process.argv[2] ?? join(root, "tasks"));
const selected = tasks.filter(t => {
  const d = join(root, "tasks", t.id);
  return d === arg || d.startsWith(arg + sep);
});
if (!selected.length) { console.error(`Нет задач по пути ${arg}`); process.exit(1); }

let bad = 0;
for (const t of selected) {
  let execute;
  try { ({ execute } = await import(`./executors/${t.lang}.mjs`)); }
  catch (e) {
    if (e.code !== "ERR_MODULE_NOT_FOUND" || !String(e.message).includes(`executors/${t.lang}.mjs`)) throw e;
    bad++; console.log(`FAIL ${t.id}: нет исполнителя для ${t.lang}`); continue;
  }
  const dir = join(root, "tasks", t.id), ext = EXT[t.lang];
  const reference = readFileSync(join(dir, `reference.${ext}`), "utf8");
  const mutants = readdirSync(join(dir, "mutants")).filter(f => f.endsWith("." + ext)).sort()
    .map(f => ({ name: f.slice(0, -ext.length - 1), code: readFileSync(join(dir, "mutants", f), "utf8") }));
  const problems = await verifyTask(t, reference, mutants, execute);
  if (problems.length) { bad++; console.log(`FAIL ${t.id}`); problems.forEach(p => console.log("  " + p)); }
  else console.log(`ok   ${t.id}`);
}
process.exit(bad ? 1 : 0);
