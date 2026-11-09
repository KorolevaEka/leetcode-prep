export function groupBy<T>(items: readonly T[], keyOf: (item: T) => string | undefined): Record<string, T[]> {
  const groups = new Map<string, T[]>();
  for (const item of items) {
    const key = keyOf(item);
    if (key === undefined) continue;
    const list = groups.get(key) ?? [];
    list.push(item);
    groups.set(key, list);
  }
  return Object.fromEntries(groups);
}
