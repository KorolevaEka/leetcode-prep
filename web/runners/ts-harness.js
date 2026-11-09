// Мини-Jest: describe/test/it/expect. Исполняет скомпилированный CommonJS и печатает отчёт в стиле Jest.
// Общий для браузера (воркер) и Node (дочерний процесс).
const CAP = 100000;

const fmt = v => {
  if (typeof v === "string") return JSON.stringify(v);
  if (typeof v === "function") return "[Function]";
  if (typeof v === "bigint") return v + "n";
  if (v instanceof Map) return `Map(${fmt([...v])})`;
  if (v instanceof Set) return `Set(${fmt([...v])})`;
  try { return JSON.stringify(v, (k, x) => typeof x === "bigint" ? x + "n" : x, 2) ?? String(v); } catch { return String(v); }
};

function eq(a, b, strict) {
  if (Object.is(a, b)) return true;
  if (typeof a !== "object" || typeof b !== "object" || !a || !b) return false;
  if (strict && Object.getPrototypeOf(a) !== Object.getPrototypeOf(b)) return false;
  if (a instanceof Date || b instanceof Date) return a instanceof Date && b instanceof Date && +a === +b;
  if (a instanceof RegExp || b instanceof RegExp) return String(a) === String(b);
  if (a instanceof Map || b instanceof Map) {
    return a instanceof Map && b instanceof Map && a.size === b.size && [...a].every(([k, v]) => b.has(k) && eq(v, b.get(k), strict));
  }
  if (a instanceof Set || b instanceof Set) {
    return a instanceof Set && b instanceof Set && a.size === b.size && [...a].every(x => [...b].some(y => eq(x, y, strict)));
  }
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  if (a instanceof Error && b instanceof Error && a.message !== b.message) return false;
  const keys = o => Object.keys(o).filter(k => strict || o[k] !== undefined);
  const ka = keys(a), kb = keys(b);
  return ka.length === kb.length && ka.every(k => Object.prototype.hasOwnProperty.call(b, k) && eq(a[k], b[k], strict));
}

const same = (pass, expected, received) => ({ pass, expected, received });

const MATCHERS = {
  toBe: (a, e) => same(Object.is(a, e), fmt(e), fmt(a)),
  toEqual: (a, e) => same(eq(a, e, false), fmt(e), fmt(a)),
  toStrictEqual: (a, e) => same(eq(a, e, true), fmt(e), fmt(a)),
  toBeTruthy: a => same(!!a, "truthy", fmt(a)),
  toBeFalsy: a => same(!a, "falsy", fmt(a)),
  toBeNull: a => same(a === null, "null", fmt(a)),
  toBeUndefined: a => same(a === undefined, "undefined", fmt(a)),
  toBeDefined: a => same(a !== undefined, "defined", fmt(a)),
  toContain: (a, item) => same(typeof a === "string" ? a.includes(item) : Array.from(a ?? []).includes(item), `item ${fmt(item)}`, fmt(a)),
  toHaveLength: (a, n) => same(a?.length === n, `length ${n}`, `length ${a?.length}: ${fmt(a)}`),
  toBeGreaterThan: (a, n) => same(a > n, `> ${fmt(n)}`, fmt(a)),
  toBeLessThan: (a, n) => same(a < n, `< ${fmt(n)}`, fmt(a)),
  toBeGreaterThanOrEqual: (a, n) => same(a >= n, `>= ${fmt(n)}`, fmt(a)),
  toBeLessThanOrEqual: (a, n) => same(a <= n, `<= ${fmt(n)}`, fmt(a)),
  toHaveProperty(a, path, ...value) {
    const keys = Array.isArray(path) ? path : String(path).replace(/\[(\w+)\]/g, ".$1").split(".").filter(Boolean);
    let cur = a, found = true;
    for (const k of keys) {
      if (cur == null || !(k in Object(cur))) { found = false; break; }
      cur = cur[k];
    }
    const what = `property ${fmt(keys.join("."))}` + (value.length ? ` with value ${fmt(value[0])}` : "");
    return same(found && (!value.length || eq(cur, value[0], false)), what, found ? `${fmt(keys.join("."))}: ${fmt(cur)}` : `no such property in ${fmt(a)}`);
  },
  toBeCloseTo: (a, n, d = 2) => same(Math.abs(a - n) < 10 ** -d / 2, `${fmt(n)} (±${10 ** -d / 2})`, fmt(a)),
  toMatch: (a, e) => same(typeof a === "string" && (typeof e === "string" ? a.includes(e) : e.test(a)), fmt(e instanceof RegExp ? String(e) : e), fmt(a)),
  toThrow(a, e) {
    if (typeof a !== "function") return same(false, "a function that throws", fmt(a));
    let thrown, did = false;
    try { a(); } catch (x) { thrown = x; did = true; }
    const msg = thrown?.message ?? String(thrown);
    const pass = did && (e === undefined || (typeof e === "string" ? msg.includes(e)
      : e instanceof RegExp ? e.test(msg)
      : e instanceof Error ? msg === e.message
      : thrown instanceof e));
    const what = e === undefined ? "a throw" : e instanceof Error ? `throw ${fmt(e.message)}` : `throw ${e instanceof RegExp || typeof e === "string" ? fmt(String(e)) : e.name}`;
    return same(pass, what, did ? `thrown: ${fmt(msg)}` : "no throw");
  },
};

MATCHERS.toThrowError = MATCHERS.toThrow;

class AssertionError extends Error {}

function build(getActual, negate, isAsync, fromRejection) {
  const o = {};
  for (const [name, fn] of Object.entries(MATCHERS)) {
    o[name] = (...args) => {
      const run = actual => {
        if (fromRejection && name.startsWith("toThrow")) { const v = actual; actual = () => { throw v; }; }
        const { pass, expected, received } = fn(actual, ...args);
        if (pass === negate) {
          throw new AssertionError(`expect(received).${negate ? "not." : ""}${name}(…)\n\nExpected: ${negate ? "not " : ""}${expected}\nReceived: ${received}`);
        }
      };
      return isAsync ? getActual().then(run) : run(getActual());
    };
  }
  if (!negate) o.not = build(getActual, true, isAsync, fromRejection);
  return o;
}

function expect(actual) {
  const o = build(() => actual, false, false, false);
  o.resolves = build(() => Promise.resolve(actual), false, true, false);
  o.rejects = build(() => Promise.resolve(actual).then(
    () => { throw new AssertionError("Expected promise to reject, but it resolved"); }, e => e), false, true, true);
  return o;
}

// js: { "solution.js": …, "solution.test.js": … } -> { passed, output, noTests? }
export async function runTests(js) {
  const out = []; let size = 0;
  const push = s => { if (size < CAP) { out.push(s); size += s.length; } };
  const tests = []; let prefix = [];
  let suite = { before: [], after: [], parent: null };
  const g = globalThis, saved = {};
  const globals = {
    expect,
    describe(name, fn) {
      prefix.push(name); suite = { before: [], after: [], parent: suite };
      try { fn(); } finally { prefix.pop(); suite = suite.parent; }
    },
    test(name, fn) { tests.push({ name: [...prefix, name].join(" > "), fn, suite }); },
    beforeEach(fn) { suite.before.push(fn); },
    afterEach(fn) { suite.after.push(fn); },
  };
  globals.it = globals.test;
  const log = (...a) => push(a.map(x => typeof x === "string" ? x : fmt(x)).join(" "));
  const con = { log, info: log, warn: log, error: log, debug: log };
  for (const k of [...Object.keys(globals), "console"]) saved[k] = Object.getOwnPropertyDescriptor(g, k);
  Object.assign(g, globals);
  Object.defineProperty(g, "console", { value: { ...con }, configurable: true, writable: true });

  const cache = {};
  const load = name => {
    const key = name.replace(/^\.\//, "").replace(/\.js$/, "") + ".js";
    if (!(key in js)) throw new Error(`Cannot find module '${name}'`);
    if (!cache[key]) {
      const module = { exports: {} };
      cache[key] = module;
      new Function("exports", "require", "module", js[key])(module.exports, load, module);
    }
    return cache[key].exports;
  };
  let failed = 0, passed = 0;
  try {
    try { load("./solution.test"); }
    catch (e) { push(`Ошибка при загрузке: ${e?.name}: ${e?.message}`); failed++; }
    for (const t of tests) {
      const chain = [];
      for (let s = t.suite; s; s = s.parent) chain.unshift(s);
      let err = null;
      try {
        for (const s of chain) for (const h of s.before) await h();
        await t.fn();
      } catch (e) { err = { e }; }
      for (const s of chain.reverse()) for (const h of s.after) {
        try { await h(); } catch (e) { err ??= { e }; }
      }
      if (!err) { passed++; push(`✓ ${t.name}`); }
      else {
        const e = err.e;
        failed++;
        const body = e instanceof AssertionError ? e.message : `${e?.name ?? "Error"}: ${e?.message ?? e}`;
        push(`✕ ${t.name}\n` + body.replace(/^/gm, "    "));
      }
    }
  } finally {
    for (const [k, d] of Object.entries(saved)) d ? Object.defineProperty(g, k, d) : delete g[k];
  }
  const summary = `\nTests: ${failed ? failed + " failed, " : ""}${passed} passed`;
  if (!tests.length && !failed) return { passed: false, noTests: true, output: out.join("\n") + "\nNo tests found" };
  return { passed: !failed, output: out.join("\n") + summary };
}
