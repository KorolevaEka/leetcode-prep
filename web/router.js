// Хэш-роутер: чистые функции, без DOM.
export function parseRoute(hash) {
  const [path, query = ""] = String(hash || "").replace(/^#/, "").split("?");
  const seg = path.split("/").filter(Boolean);
  if (seg[0] === "learn" && seg[1]) {
    const q = new URLSearchParams(query);
    const route = { page: "catalog", lang: seg[1] };
    if (q.get("topic")) route.topic = q.get("topic");
    if (q.get("level")) route.level = q.get("level");
    return route;
  }
  if (seg[0] === "task" && seg.length === 4) return { page: "task", id: seg.slice(1).join("/") };
  return { page: "landing" };
}

// PKCE-возврат с GitHub кладёт ?code= в query; после обмена URL нужно почистить.
export function cleanAuthParams(url) {
  const u = new URL(url);
  const keys = ["code", "error", "error_code", "error_description"].filter(k => u.searchParams.has(k));
  if (!keys.length) return null;
  keys.forEach(k => u.searchParams.delete(k));
  return u;
}
