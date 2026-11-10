const CARRY_KEY = "lct:guest-carry";

export function createProgress({ supabase, storage = globalThis.sessionStorage, debounceMs = 1000, seed = null }) {
  let user = null;
  const solved = new Set();
  const drafts = new Map();
  const solvedCodes = new Map();
  for (const id of seed?.solved || []) solved.add(id);
  for (const [id, code] of Object.entries(seed?.drafts || {})) drafts.set(id, code);
  for (const [id, code] of Object.entries(seed?.solvedCodes || {})) solvedCodes.set(id, code);
  const pending = new Map(); // id -> { code, solvedAt? } — ещё не записано на сервер
  let state = "saved";
  let timer = null;
  let flushing = null;
  let carryFailed = false;

  const row = (id, p) => ({
    user_id: user.id, task_id: id, code: p.code, updated_at: new Date().toISOString(),
    ...(p.solvedAt ? { solved_at: p.solvedAt } : {}),
    ...(p.solvedCode != null ? { solved_code: p.solvedCode } : {}),
  });
  const upsert = payload => supabase.from("progress").upsert(payload, { onConflict: "user_id,task_id" });

  async function flush() {
    clearTimeout(timer);
    timer = null;
    await flushing;
    if (!pending.size) return;
    state = "saving";
    const batch = [...pending];
    flushing = (async () => {
      for (const [id, p] of batch) {
        let error;
        try { ({ error } = await upsert(row(id, p))); } catch (e) { error = e; }
        if (error) { state = "error"; return; }
        if (pending.get(id) === p) pending.delete(id);
      }
      state = pending.size ? "saving" : "saved";
    })();
    await flushing;
    if (state === "saving") await flush();
  }

  return {
    async init() {
      const { data } = await supabase.auth.getSession();
      const session = data?.session;
      let stored = null;
      try { stored = JSON.parse(storage.getItem(CARRY_KEY)); } catch { storage.removeItem(CARRY_KEY); }
      const carry = stored || seed ? {
        solved: [...new Set([...(stored?.solved || []), ...(seed?.solved || [])])],
        drafts: { ...(stored?.drafts || {}), ...(seed?.drafts || {}) },
        solvedCodes: { ...(stored?.solvedCodes || {}), ...(seed?.solvedCodes || {}) },
      } : null;
      if (!session) {
        for (const id of carry?.solved || []) solved.add(id);
        for (const [id, code] of Object.entries(carry?.drafts || {})) drafts.set(id, code);
        for (const [id, code] of Object.entries(carry?.solvedCodes || {})) solvedCodes.set(id, code);
        storage.removeItem(CARRY_KEY);
        return null;
      }
      user = { login: session.user.user_metadata?.user_name, id: session.user.id };
      const { data: rows, error: selectError } = await supabase.from("progress").select("task_id, code, solved_at, solved_code");
      if (selectError) { state = "error"; return { login: user.login }; }
      const server = new Map();
      for (const r of rows || []) {
        server.set(r.task_id, r);
        if (r.solved_at) solved.add(r.task_id);
        if (r.code != null) drafts.set(r.task_id, r.code);
        if (r.solved_code != null) solvedCodes.set(r.task_id, r.solved_code);
      }
      if (carry) {
        const now = new Date().toISOString();
        const withSolved = [];
        const codeOnly = [];
        for (const id of new Set([...carry.solved, ...Object.keys(carry.drafts)])) {
          const srv = server.get(id);
          if (srv?.solved_at) continue;
          if (carry.solved.includes(id)) {
            const passing = srv?.solved_code ?? carry.solvedCodes[id] ?? carry.drafts[id] ?? null;
            withSolved.push({
              user_id: user.id, task_id: id, code: carry.drafts[id] ?? srv?.code ?? null, updated_at: now, solved_at: now,
              solved_code: passing,
            });
          } else if (!srv) {
            codeOnly.push({ user_id: user.id, task_id: id, code: carry.drafts[id], updated_at: now });
          }
        }
        let failed = false;
        for (const group of [withSolved, codeOnly]) {
          if (!group.length) continue;
          const { error } = await upsert(group);
          if (error) { failed = true; continue; }
          for (const r of group) {
            if (r.solved_at) solved.add(r.task_id);
            if (r.solved_code != null) solvedCodes.set(r.task_id, r.solved_code);
            if (r.code != null) drafts.set(r.task_id, r.code);
          }
        }
        if (failed) {
          state = "error";
          carryFailed = true;
          storage.setItem(CARRY_KEY, JSON.stringify(carry));
        } else storage.removeItem(CARRY_KEY);
      }
      return { login: user.login };
    },
    async signIn() {
      // неразобранный carry (прошлый вход не дошёл до upsert) не теряем: объединяем
      let old = null;
      try { old = JSON.parse(storage.getItem(CARRY_KEY)); } catch {}
      storage.setItem(CARRY_KEY, JSON.stringify({
        solved: [...new Set([...(old?.solved || []), ...solved])],
        drafts: { ...(old?.drafts || {}), ...Object.fromEntries(drafts) },
        solvedCodes: { ...(old?.solvedCodes || {}), ...Object.fromEntries(solvedCodes) },
      }));
      await supabase.auth.signInWithOAuth({
        provider: "github",
        options: {
          redirectTo: location.origin + location.pathname + location.hash,
          queryParams: { prompt: "select_account" },
        },
      });
    },
    flush,
    async signOut() {
      try { await flush(); } catch {}
      await supabase.auth.signOut();
      user = null; solved.clear(); drafts.clear(); solvedCodes.clear(); pending.clear(); clearTimeout(timer);
    },
    carryFailed: () => carryFailed,
    absorb(snap) {
      for (const id of snap.solved) if (!solved.has(id)) this.markSolved(id, snap.solvedCodes?.[id] ?? snap.drafts[id] ?? "");
      for (const [id, code] of Object.entries(snap.drafts)) if (!drafts.has(id)) this.saveDraft(id, code);
    },
    snapshot: () => ({ solved: [...solved], drafts: Object.fromEntries(drafts), solvedCodes: Object.fromEntries(solvedCodes) }),
    user: () => user,
    isSolved: id => solved.has(id),
    solvedIds: () => new Set(solved),
    getDraft: id => drafts.get(id),
    getSolvedCode: id => solvedCodes.get(id),
    saveState: () => state,
    saveDraft(id, code) {
      drafts.set(id, code);
      if (!user) return;
      pending.set(id, { code, solvedAt: pending.get(id)?.solvedAt, solvedCode: pending.get(id)?.solvedCode });
      state = "saving";
      clearTimeout(timer);
      timer = setTimeout(flush, debounceMs);
    },
    async markSolved(id, code) {
      solved.add(id);
      drafts.set(id, code);
      const first = !solvedCodes.has(id);
      if (first) solvedCodes.set(id, code);
      if (!user) return;
      pending.set(id, { code, solvedAt: new Date().toISOString(), solvedCode: first ? code : pending.get(id)?.solvedCode });
      await flush();
    },
  };
}
