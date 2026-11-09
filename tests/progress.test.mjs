import { test } from "node:test";
import assert from "node:assert/strict";
import { createProgress } from "../web/progress.js";

const memStorage = () => {
  const m = new Map();
  return { getItem: k => (m.has(k) ? m.get(k) : null), setItem: (k, v) => m.set(k, String(v)), removeItem: k => m.delete(k), _m: m };
};
const wait = ms => new Promise(r => setTimeout(r, ms));

function fakeSupabase({ session = null, rows = [], failUpserts = 0 } = {}) {
  const f = { upserts: [], oauth: [], signedOut: 0, selects: 0, failUpserts };
  f.auth = {
    getSession: async () => ({ data: { session } }),
    signInWithOAuth: async o => { f.oauth.push(o); return {}; },
    signOut: async () => { f.signedOut++; return {}; },
  };
  f.from = table => {
    assert.equal(table, "progress");
    return {
      select: () => { f.selects++; return Promise.resolve({ data: rows, error: null }); },
      upsert: async (payload, opts) => {
        if (f.failUpserts > 0) { f.failUpserts--; return { error: { message: "network" } }; }
        f.upserts.push({ payload, opts });
        return { error: null };
      },
    };
  };
  return f;
}
const session = { user: { id: "u1", user_metadata: { user_name: "kate" } } };
globalThis.location = { origin: "https://h.io", pathname: "/lct/", hash: "#/learn/sql" };

test("guest: solved lives in memory only", async () => {
  const st = memStorage();
  const p = createProgress({ supabase: fakeSupabase(), storage: st });
  assert.equal(await p.init(), null);
  await p.markSolved("python/a/01-x", "code");
  assert.equal(p.isSolved("python/a/01-x"), true);
  assert.equal(createProgress({ supabase: fakeSupabase(), storage: st }).isSolved("python/a/01-x"), false);
});

test("carry: signIn stores guest progress, init upserts it and clears key", async () => {
  const st = memStorage();
  const guest = fakeSupabase();
  const g = createProgress({ supabase: guest, storage: st });
  await g.init();
  await g.markSolved("a", "A");
  await g.markSolved("b", "B");
  g.saveDraft("c", "C");
  await g.signIn();
  assert.deepEqual(JSON.parse(st.getItem("lct:guest-carry")), { solved: ["a", "b"], drafts: { a: "A", b: "B", c: "C" } });
  assert.equal(guest.oauth[0].provider, "github");
  assert.equal(guest.oauth[0].options.redirectTo, "https://h.io/lct/#/learn/sql");

  const sb = fakeSupabase({ session });
  const p = createProgress({ supabase: sb, storage: st });
  assert.deepEqual(await p.init(), { login: "kate" });
  const rows = sb.upserts.flatMap(u => u.payload);
  assert.equal(rows.length, 3);
  assert.ok(rows.filter(r => r.solved_at).map(r => r.task_id).sort().join() === "a,b");
  assert.ok(sb.upserts.every(u => u.opts.onConflict === "user_id,task_id"));
  assert.ok(rows.every(r => !("user_id" in r)));
  assert.equal(st.getItem("lct:guest-carry"), null);
  assert.ok(p.isSolved("a") && p.isSolved("b") && !p.isSolved("c"));
});

test("no session: stale carry key is removed", async () => {
  const st = memStorage();
  st.setItem("lct:guest-carry", "{}");
  await createProgress({ supabase: fakeSupabase(), storage: st }).init();
  assert.equal(st.getItem("lct:guest-carry"), null);
});

test("user: init loads solved and drafts", async () => {
  const sb = fakeSupabase({ session, rows: [
    { task_id: "a", code: "A", solved_at: "2026-01-01" },
    { task_id: "b", code: "B", solved_at: null },
  ] });
  const p = createProgress({ supabase: sb, storage: memStorage() });
  await p.init();
  assert.deepEqual([...p.solvedIds()], ["a"]);
  assert.equal(p.getDraft("b"), "B");
  assert.equal(p.user().login, "kate");
});

test("saveDraft debounces to one upsert; markSolved keeps solved_at out of drafts", async () => {
  const sb = fakeSupabase({ session });
  const p = createProgress({ supabase: sb, storage: memStorage(), debounceMs: 20 });
  await p.init();
  p.saveDraft("a", "1");
  p.saveDraft("a", "12");
  assert.equal(p.saveState(), "saving");
  await wait(60);
  assert.equal(sb.upserts.length, 1);
  assert.equal(sb.upserts[0].payload.code, "12");
  assert.ok(!("solved_at" in sb.upserts[0].payload));
  assert.equal(p.saveState(), "saved");
  await p.markSolved("a", "done");
  const last = sb.upserts.at(-1).payload;
  assert.equal(last.task_id, "a");
  assert.ok(last.solved_at);
});

test("failure: error state, retry with latest code on next saveDraft", async () => {
  const sb = fakeSupabase({ session, failUpserts: 1 });
  const p = createProgress({ supabase: sb, storage: memStorage(), debounceMs: 10 });
  await p.init();
  p.saveDraft("a", "v1");
  await wait(40);
  assert.equal(p.saveState(), "error");
  assert.equal(p.getDraft("a"), "v1");
  p.saveDraft("a", "v2");
  await wait(40);
  assert.equal(sb.upserts.length, 1);
  assert.equal(sb.upserts[0].payload.code, "v2");
  assert.equal(p.saveState(), "saved");
});

test("default debounce is 1000 ms", async () => {
  const sb = fakeSupabase({ session });
  const p = createProgress({ supabase: sb, storage: memStorage() });
  await p.init();
  p.saveDraft("a", "x");
  await wait(300);
  assert.equal(sb.upserts.length, 0);
  p.saveDraft("a", "y");
});
