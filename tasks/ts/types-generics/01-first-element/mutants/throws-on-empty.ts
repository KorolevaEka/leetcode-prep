export function first<T>(items: readonly T[]): T | undefined {
  if (items.length === 0) throw new Error("empty");
  return items[0];
}
