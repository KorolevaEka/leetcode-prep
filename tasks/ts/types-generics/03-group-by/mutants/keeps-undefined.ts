export function groupBy<T, K extends string>(items: readonly T[], keyOf: (item: T) => K | undefined): Partial<Record<K, T[]>> {
  const groups = new Map<string, T[]>();
  for (const item of items) {
    const key = String(keyOf(item));
    const list = groups.get(key) ?? [];
    list.push(item);
    groups.set(key, list);
  }
  return Object.fromEntries(groups) as Partial<Record<K, T[]>>;
}
