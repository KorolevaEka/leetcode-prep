export function first<T>(items: readonly T[]): T | undefined {
  return items[items.length - 1];
}
