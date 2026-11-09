import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { execute } from "../scripts/executors/java.mjs";
import { check } from "../web/check.js";

const dir = "tasks/java/strings/01-report-file-name/";
const read = n => readFileSync(dir + n, "utf8");
const task = { kind: "code", tests: read("tests.java") };
const run = (subject, tests = task.tests) => execute(task, subject, tests);
const SOL = "public class Solution { public static int f() { return 4; } }";
const tests = body => `import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class SolutionTest { @Test void t() throws Exception { ${body} } }`;

test("correct solution passes with ✓", async () => {
  const r = await run(read("reference.java"));
  assert.equal(r.passed, true, r.output);
  assert.match(r.output, /✓ простое название/);
  assert.match(r.output, /Tests: 5 passed/);
});

test("wrong solution fails with JUnit-style message", async () => {
  const r = await run(SOL, tests("assertEquals(5, Solution.f());"));
  assert.equal(r.passed, false);
  assert.match(r.output, /✕ t/);
  assert.match(r.output, /expected: <5> but was: <4>/);
  assert.match(r.output, /Tests: 1 failed, 0 passed/);
});

test("compile error is shown and fails", async () => {
  const r = await run('public class Solution { int x = "s"; }', tests(""));
  assert.equal(r.passed, false);
  assert.match(r.output, /Solution\.java:1: error: incompatible types/);
});

test("assertThrows returns the exception, other assertions work", async () => {
  const r = await run(SOL, tests(`
    IllegalArgumentException e = assertThrows(IllegalArgumentException.class, () -> { throw new IllegalArgumentException("bad"); });
    assertEquals("bad", e.getMessage());
    assertEquals(0.3, 0.1 + 0.2, 1e-9); assertEquals(4L, (long) Solution.f()); assertEquals(4, Integer.valueOf(4));
    assertEquals('a', "abc".charAt(0)); assertNotEquals(1, 2); assertTrue(true); assertFalse(false, "msg");
    assertNull(null); assertNotNull("x"); assertDoesNotThrow(() -> {});
    assertArrayEquals(new int[]{1, 2}, new int[]{1, 2}); assertArrayEquals(new long[]{1}, new long[]{1});
    assertArrayEquals(new String[]{"a"}, new String[]{"a"});`));
  assert.equal(r.passed, true, r.output);
});

test("assertion messages: custom message, arrays, assertThrows, fail", async () => {
  const r = await run(SOL, `import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class SolutionTest {
  @Test void a() { assertEquals(1, 2, "сумма"); }
  @Test void b() { assertArrayEquals(new int[]{1, 2}, new int[]{1, 3}); }
  @Test void c() { assertThrows(IllegalStateException.class, () -> {}); }
  @Test void d() { fail("стоп"); }
  @Test void e() { Object o = null; o.toString(); }
}`);
  assert.equal(r.passed, false);
  assert.match(r.output, /сумма ==> expected: <1> but was: <2>/);
  assert.match(r.output, /array contents differ at index \[1\], expected: <2> but was: <3>/);
  assert.match(r.output, /Expected java\.lang\.IllegalStateException to be thrown, but nothing was thrown/);
  assert.match(r.output, /стоп/);
  assert.match(r.output, /NullPointerException/);
  assert.match(r.output, /Tests: 5 failed, 0 passed/);
});

test("infinite loop times out within 12 s", async () => {
  const t0 = Date.now();
  const r = await run("public class Solution { public static void f() { while (true) {} } }", tests("Solution.f();"));
  assert.equal(r.passed, false);
  assert.match(r.output, /Таймаут/);
  assert.ok(Date.now() - t0 < 12000 + 5000); // + время javac
});

test("no @Test methods reports noTests", async () => {
  const r = await run(read("reference.java"), "class SolutionTest {}");
  assert.equal(r.passed, false);
  assert.equal(r.noTests, true);
});

test("empty tests file reports noTests", async () => {
  const r = await run(read("reference.java"), "");
  assert.equal(r.noTests, true);
});

test("1 MB of output is truncated", async () => {
  const r = await check(task, SOL, () => run(SOL, tests('System.out.print("x".repeat(1024 * 1024));')));
  assert.match(r.output, /…вывод обрезан/);
});
