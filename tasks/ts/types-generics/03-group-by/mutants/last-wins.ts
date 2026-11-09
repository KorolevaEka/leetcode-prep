export function groupBy<T, K extends string>(items: readonly T[], keyOf: (item: T) => K | undefined): Partial<Record<K, T[]>> {
  const groups = new Map<K, T[]>();
  for (const item of items) {
    const key = keyOf(item);
    if (key === undefined) continue;
    const list = groups.get(key) ?? [];
    list.splice(0, list.length, item);
    groups.set(key, list);
  }
  return Object.fromEntries(groups) as Partial<Record<K, T[]>>;
}
