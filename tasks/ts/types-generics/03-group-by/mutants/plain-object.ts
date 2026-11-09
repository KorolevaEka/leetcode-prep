export function groupBy<T, K extends string>(items: readonly T[], keyOf: (item: T) => K): Partial<Record<K, T[]>> {
  const groups: Record<string, T[]> = {};
  for (const item of items) {
    const key = keyOf(item);
    groups[key] = groups[key] ?? [];
    groups[key].push(item);
  }
  return groups as Partial<Record<K, T[]>>;
}
