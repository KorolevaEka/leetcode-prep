import { test } from "node:test";
import assert from "node:assert/strict";
import { guard } from "../web/runners/java-guard.js";
import { execute } from "../scripts/executors/java.mjs";

const T = "__LCT.tick()";
const g = s => guard(s).replaceAll(T, "T");

test("braced loop bodies get a tick", () => {
  assert.equal(g("while (a) { b(); }"), "while (a) { T; b(); }");
  assert.equal(g("for (int i = 0; i < n; i++) {}"), "for (int i = 0; i < n; i++) { T;}");
  assert.equal(g("for (String s : xs) {}"), "for (String s : xs) { T;}");
  assert.equal(g("do { x++; } while (x < 3);"), "do { T; x++; } while (x < 3);");
});

test("unbraced and empty loops get a tick in the condition", () => {
  assert.equal(g("while (i < n) i++;"), "while (T && (i < n)) i++;");
  assert.equal(g("while (true);"), "while (T && (true));");
  assert.equal(g("for (;;) x();"), "for (;T;) x();");
  assert.equal(g("for (int i = 0; i < n; i++) s += i;"), "for (int i = 0; T && (i < n); i++) s += i;");
  assert.equal(g("do x++; while (x < 3);"), "do x++; while (T && (x < 3));");
  assert.equal(g("for (String s : xs) f(s);"), "for (String s : xs) f(s);");
});

test("method bodies get a tick, other blocks do not", () => {
  assert.equal(g("static int f(int a) throws Exception { return a; }"), "static int f(int a) throws Exception { T; return a; }");
  assert.equal(g("List<String> f() {} int[] g() {}"), "List<String> f() { T;} int[] g() { T;}");
  const same = [
    "if (a) { b(); } else if (c) { d(); }",
    "switch (x) { case 1 -> {} }",
    "try (var r = open()) {} catch (Exception e) {} synchronized (o) {}",
    "Runnable r = new Runnable() { };",
    "public Solution(int x) { super(); }",
    "record P(int x) {}",
    "enum E { A(1) { }, B(2); E(int v) {} }",
    "Runnable r = () -> { };",
    "@DisplayName(\"x\") void",
  ];
  for (const s of same) assert.equal(g(s), s);
});

test("strings, chars, text blocks and comments are skipped", () => {
  const same = [
    'String s = "while (true) { for (;;) {";',
    "char c = '{'; char d = '\\'';",
    'String t = """\n  while (x) {\n  """;',
    "// while (true) {}\n/* for (;;) {} */",
    'String e = "\\"while (a) {";',
  ];
  for (const s of same) assert.equal(g(s), s);
});

test("line numbers are preserved", () => {
  const src = "public class Solution {\n  static int f() {\n    while (true)\n      return 1;\n  }\n}";
  assert.equal(guard(src).split("\n").length, src.split("\n").length);
});

const tests = body => `import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class SolutionTest { @Test void t() { ${body} } }`;

test("guarded code compiles and runs", async () => {
  const sol = `import java.util.*;
public class Solution {
  public static int sum(List<Integer> xs) {
    int s = 0;
    for (int x : xs) s += x;
    for (int i = 0; i < 2; i++) { s++; }
    int k = 0; do k++; while (k < 3);
    while (k < 5) k++;
    while (true) { if (k > 0) break; }
    return s + k;
  }
  static int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
}`;
  const r = await execute({}, guard(sol), guard(tests("assertEquals(13, Solution.sum(java.util.List.of(1, 2, 3))); assertEquals(6, Solution.fact(3));")));
  assert.equal(r.passed, true, r.output);
});

test("guarded infinite loop and runaway recursion stop at the deadline", async () => {
  const fib = "fib(90); } static long fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2);";
  for (const body of ["while (true) {}", "for (;;);", "int i = 0; do i++; while (i >= 0 || true);", fib]) {
    const sol = `public class Solution { public static void f() { ${body} } }`;
    const t0 = Date.now();
    const r = await execute({}, guard(sol), guard(tests("__LCT.deadline = System.currentTimeMillis() + 300; Solution.f();")));
    assert.equal(r.passed, false, body);
    assert.match(r.output, /Таймаут/, body);
    assert.ok(Date.now() - t0 < 6000, body);
  }
});
