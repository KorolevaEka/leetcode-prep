export function groupBy<T>(items: readonly T[], keyOf: (item: T) => string): Record<string, T[]> {
  const groups = new Map<string, T[]>();
  for (const item of items) {
    const key = keyOf(item);
    const list = groups.get(key) ?? [];
    list.push(item);
    groups.set(key, list);
  }
  return Object.fromEntries(groups);
}
