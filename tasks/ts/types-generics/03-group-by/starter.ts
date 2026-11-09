export function groupBy<T, K extends string>(items: readonly T[], keyOf: (item: T) => K | undefined): Partial<Record<K, T[]>> {
  throw new Error("TODO");
}
