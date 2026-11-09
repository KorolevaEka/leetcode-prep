const CARRY_KEY = "lct:guest-carry";

export function createProgress({ supabase, storage = globalThis.sessionStorage, debounceMs = 1000 }) {
  let user = null;
  const solved = new Set();
  const drafts = new Map();
  const pending = new Map(); // id -> { code, solvedAt? } — ещё не записано на сервер
  let state = "saved";
  let timer = null;
  let flushing = null;

  const row = (id, p) => ({
    task_id: id, code: p.code, updated_at: new Date().toISOString(),
    ...(p.solvedAt ? { solved_at: p.solvedAt } : {}),
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
      const carryRaw = storage.getItem(CARRY_KEY);
      if (!session) {
        storage.removeItem(CARRY_KEY);
        return null;
      }
      user = { login: session.user.user_metadata?.user_name, id: session.user.id };
      const { data: rows, error: selectError } = await supabase.from("progress").select("task_id, code, solved_at");
      if (selectError) { state = "error"; return { login: user.login }; }
      const server = new Map();
      for (const r of rows || []) {
        server.set(r.task_id, r);
        if (r.solved_at) solved.add(r.task_id);
        if (r.code != null) drafts.set(r.task_id, r.code);
      }
      if (carryRaw) {
        let carry = null;
        try { carry = JSON.parse(carryRaw); } catch { storage.removeItem(CARRY_KEY); }
        if (carry) {
          const now = new Date().toISOString();
          const withSolved = [];
          const codeOnly = [];
          for (const id of new Set([...carry.solved, ...Object.keys(carry.drafts)])) {
            const srv = server.get(id);
            if (srv?.solved_at) continue;
            if (carry.solved.includes(id)) {
              withSolved.push({ task_id: id, code: carry.drafts[id] ?? srv?.code ?? null, updated_at: now, solved_at: now });
            } else if (!srv) {
              codeOnly.push({ task_id: id, code: carry.drafts[id], updated_at: now });
            }
          }
          let failed = false;
          for (const group of [withSolved, codeOnly]) {
            if (!group.length) continue;
            const { error } = await upsert(group);
            if (error) { failed = true; continue; }
            for (const r of group) {
              if (r.solved_at) solved.add(r.task_id);
              if (r.code != null) drafts.set(r.task_id, r.code);
            }
          }
          if (failed) state = "error";
          else storage.removeItem(CARRY_KEY);
        }
      }
      return { login: user.login };
    },
    async signIn() {
      storage.setItem(CARRY_KEY, JSON.stringify({ solved: [...solved], drafts: Object.fromEntries(drafts) }));
      await supabase.auth.signInWithOAuth({
        provider: "github",
        options: { redirectTo: location.origin + location.pathname + location.hash },
      });
    },
    async signOut() {
      await supabase.auth.signOut();
      user = null; solved.clear(); drafts.clear(); pending.clear(); clearTimeout(timer);
    },
    user: () => user,
    isSolved: id => solved.has(id),
    solvedIds: () => new Set(solved),
    getDraft: id => drafts.get(id),
    saveState: () => state,
    saveDraft(id, code) {
      drafts.set(id, code);
      if (!user) return;
      pending.set(id, { code, solvedAt: pending.get(id)?.solvedAt });
      state = "saving";
      clearTimeout(timer);
      timer = setTimeout(flush, debounceMs);
    },
    async markSolved(id, code) {
      solved.add(id);
      drafts.set(id, code);
      if (!user) return;
      pending.set(id, { code, solvedAt: new Date().toISOString() });
      await flush();
    },
  };
}
