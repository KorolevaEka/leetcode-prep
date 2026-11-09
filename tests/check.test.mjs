import { test } from "node:test";
import assert from "node:assert/strict";
import { check, verifyTask, truncate } from "../web/check.js";

const fake = results => async (_task, subject, tests) => {
  const r = results[`${subject}|${tests}`] ?? results[subject];
  if (!r) throw new Error(`нет результата для ${subject}|${tests}`);
  return r;
};
const ok = { passed: true, output: "ok" };
const bad = { passed: false, output: "FAILED" };

const codeTask = { kind: "code", tests: "T" };
const testsTask = {
  kind: "tests", subject: "S",
  mutants: [
    { name: "a", description: "падает на пустом вводе", code: "MA" },
    { name: "b", description: "теряет последний элемент", code: "MB" },
  ],
};

test("code task passes when tests pass", async () => {
  const r = await check(codeTask, "sol", fake({ sol: ok }));
  assert.equal(r.ok, true);
});

test("code task fails with output when tests fail", async () => {
  const r = await check(codeTask, "sol", fake({ sol: { passed: false, output: "1 failed" } }));
  assert.equal(r.ok, false);
  assert.match(r.output, /1 failed/);
});

test("tests task: all mutants caught → ok", async () => {
  const r = await check(testsTask, "mytests", fake({ "S|mytests": ok, "MA|mytests": bad, "MB|mytests": bad }));
  assert.equal(r.ok, true);
  assert.deepEqual(r.caught, { total: 2, missed: [] });
});

test("tests task: one mutant survives → not ok", async () => {
  const r = await check(testsTask, "mytests", fake({ "S|mytests": ok, "MA|mytests": bad, "MB|mytests": ok }));
  assert.equal(r.ok, false);
  assert.deepEqual(r.caught, { total: 2, missed: ["теряет последний элемент"] });
  assert.match(r.output, /Поймано 1 из 2/);
  assert.match(r.output, /теряет последний элемент/);
});

test("tests task: no tests", async () => {
  const calls = [];
  const exec = async (t, s, c) => { calls.push(s); return { passed: false, output: "", noTests: true }; };
  const r = await check(testsTask, "", exec);
  assert.equal(r.ok, false);
  assert.match(r.output, /Нет ни одного теста/);
  assert.deepEqual(calls, ["S"]);
});

test("tests task: fails on subject → mutants not run", async () => {
  const calls = [];
  const exec = async (t, s) => { calls.push(s); return bad; };
  const r = await check(testsTask, "mytests", exec);
  assert.equal(r.ok, false);
  assert.ok(r.output.startsWith("Твои тесты падают на правильной реализации"));
  assert.deepEqual(calls, ["S"]);
});

test("verifyTask reports surviving mutant by name", async () => {
  const mutants = [{ name: "m1", code: "M1" }, { name: "m2", code: "M2" }];
  const p = await verifyTask(codeTask, "ref", mutants, fake({ "ref|T": ok, "M1|T": bad, "M2|T": ok }));
  assert.deepEqual(p, ["мутант m2 не пойман"]);
});

test("verifyTask reports failing reference", async () => {
  const p = await verifyTask(codeTask, "ref", [], fake({ "ref|T": { passed: false, output: "boom" } }));
  assert.equal(p.length, 1);
  assert.match(p[0], /^эталон не проходит: boom/);
});

test("verifyTask for tests kind runs reference against subject and mutants", async () => {
  const p = await verifyTask(testsTask, "ref", [{ name: "m", code: "M" }], fake({ "S|ref": ok, "M|ref": ok }));
  assert.deepEqual(p, ["мутант m не пойман"]);
});

test("truncate cuts to limit and appends marker", () => {
  const t = truncate("x".repeat(30), 10);
  assert.equal(t, "x".repeat(10) + "\n…вывод обрезан");
  assert.equal(truncate("short"), "short");
});
