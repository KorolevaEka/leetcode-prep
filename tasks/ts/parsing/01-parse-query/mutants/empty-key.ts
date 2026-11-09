export function parseQuery(query: string): Record<string, string> {
  const result: Record<string, string> = {};
  const text = query.startsWith("?") ? query.slice(1) : query;
  for (const pair of text.split("&")) {
    const eq = pair.indexOf("=");
    const key = eq === -1 ? pair : pair.slice(0, eq);
    const value = eq === -1 ? "" : pair.slice(eq + 1);
    result[decodeURIComponent(key)] = decodeURIComponent(value);
  }
  return result;
}
