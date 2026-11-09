import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { execute } from "../scripts/executors/ts.mjs";
import { check } from "../web/check.js";

const dir = "tasks/ts/strings-arrays/01-count-failed-tests/";
const read = n => readFileSync(dir + n, "utf8");
const task = { kind: "code", tests: read("tests.ts") };
const run = (subject, tests = task.tests) => execute(task, subject, tests);
const tests = body => `import { f } from "./solution";\ntest("t", async () => { ${body} });`;

test("correct solution passes with ✓", async () => {
  const r = await run(read("reference.ts"));
  assert.equal(r.passed, true, r.output);
  assert.match(r.output, /✓/);
  assert.match(r.output, /Tests: \d+ passed/);
});

test("wrong solution fails with ✕ and Expected", async () => {
  const r = await run(read("mutants/off-by-one.ts"));
  assert.equal(r.passed, false);
  assert.match(r.output, /✕/);
  assert.match(r.output, /Expected/);
  assert.match(r.output, /Tests: \d+ failed/);
});

test("type error fails the run with TS code", async () => {
  const r = await run('export const x: number = "a";', 'import { x } from "./solution";\ntest("t", () => { expect(x).toBe(1); });');
  assert.equal(r.passed, false);
  assert.match(r.output, /solution\.ts\(1,\d+\): error TS2322/);
});

test("unused @ts-expect-error is an error", async () => {
  const r = await run("export const f = (): number => 1;", 'import { f } from "./solution";\n// @ts-expect-error\nconst n: number = f();\ntest("t", () => { expect(n).toBe(1); });');
  assert.equal(r.passed, false);
  assert.match(r.output, /TS2578/);
});

test("async tests with resolves", async () => {
  const r = await run("export const f = () => Promise.resolve(1);", tests("await expect(f()).resolves.toBe(1); await expect(Promise.reject(new Error('x'))).rejects.toThrow('x');"));
  assert.equal(r.passed, true, r.output);
});

test("matchers and .not", async () => {
  const r = await run("export const f = 1;", tests(`
    expect([1, { a: 2 }]).toEqual([1, { a: 2 }]);
    expect([1]).not.toEqual([2]);
    expect({ a: undefined }).toEqual({});
    expect({ a: undefined }).not.toStrictEqual({});
    expect("hello").toContain("ell"); expect([1, 2]).toContain(2);
    expect([1, 2]).toHaveLength(2); expect(0.1 + 0.2).toBeCloseTo(0.3);
    expect(3).toBeGreaterThan(2); expect(1).toBeLessThan(2);
    expect(null).toBeNull(); expect(undefined).toBeUndefined(); expect(1).toBeDefined();
    expect("abc").toMatch(/b/); expect(() => { throw new Error("boom"); }).toThrow("boom");
    expect(() => 1).not.toThrow(); expect(1).toBeTruthy(); expect(0).toBeFalsy();`));
  assert.equal(r.passed, true, r.output);
});

test("setTimeout/clearTimeout typecheck and work in async code", async () => {
  const solution = `export const delay = (ms: number) => new Promise<string>(r => { setTimeout(() => r("done"), ms); });
export const never = () => { const id = setTimeout(() => {}, 1000); clearTimeout(id); const i = setInterval(() => {}, 1000); clearInterval(i); };`;
  const r = await run(solution, 'import { delay, never } from "./solution";\ntest("t", async () => { never(); await expect(delay(20)).resolves.toBe("done"); });');
  assert.equal(r.passed, true, r.output);
});

test("infinite loop times out within 12 s", async () => {
  const t0 = Date.now();
  const r = await run("export const f = () => { while (true) {} };", tests("f();"));
  assert.equal(r.passed, false);
  assert.match(r.output, /Таймаут/);
  assert.ok(Date.now() - t0 < 12000);
});

test("1 MB of console.log is truncated", async () => {
  const r = await check(task, "export const f = 1;", () => run("export const f = 1;", tests('console.log("x".repeat(1024 * 1024));')));
  assert.ok(r.output.length <= 20000 + "\n…вывод обрезан".length);
  assert.match(r.output, /…вывод обрезан/);
});

test("empty tests file reports noTests", async () => {
  const r = await run(read("reference.ts"), "");
  assert.equal(r.passed, false);
  assert.equal(r.noTests, true);
});

test("beforeEach/afterEach run around every test, scoped to describe", async () => {
  const r = await run("export const f = 1;", `
    const log: string[] = [];
    beforeEach(() => { log.push("b"); });
    afterEach(() => { log.push("a"); });
    describe("inner", () => { beforeEach(() => { log.push("ib"); }); test("one", () => { expect(log).toEqual(["b", "ib"]); }); });
    test("two", () => { expect(log).toEqual(["b", "ib", "a", "b"]); });
    test("three", () => { expect(log).toEqual(["b", "ib", "a", "b", "a", "b"]); });`);
  assert.equal(r.passed, true, r.output);
});

test("toBeGreaterThanOrEqual, toBeLessThanOrEqual, toHaveProperty, toThrowError", async () => {
  const r = await run("export const f = 1;", tests(`
    expect(2).toBeGreaterThanOrEqual(2); expect(2).toBeLessThanOrEqual(2);
    expect(1).not.toBeGreaterThanOrEqual(2); expect(3).not.toBeLessThanOrEqual(2);
    const o = { a: { b: [1, { c: 5 }] }, u: undefined };
    expect(o).toHaveProperty("a.b"); expect(o).toHaveProperty("a.b[1].c", 5); expect(o).toHaveProperty(["a", "b", "0"], 1);
    expect(o).toHaveProperty("u"); expect(o).not.toHaveProperty("a.x"); expect(o).not.toHaveProperty("a.b[1].c", 6);
    expect(() => { throw new Error("boom"); }).toThrowError("boom");
    await expect(Promise.reject(new Error("x"))).rejects.toThrowError("x");`));
  assert.equal(r.passed, true, r.output);
});

test("failing new matchers report Expected/Received", async () => {
  const r = await run("export const f = 1;", tests('expect(1).toBeGreaterThanOrEqual(2); expect({}).toHaveProperty("a");'));
  assert.equal(r.passed, false);
  assert.match(r.output, /toBeGreaterThanOrEqual/);
});
