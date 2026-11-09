export async function loadAll<T>(loaders: (() => Promise<T>)[]): Promise<T[]> {
  const results: T[] = [];
  for (const load of loaders) results.push(await load());
  return results;
}
