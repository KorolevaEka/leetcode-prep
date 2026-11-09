export function loadAll<T>(loaders: (() => Promise<T>)[]): Promise<T[]> {
  return Promise.all(loaders.map(load => load().catch(() => undefined as T)));
}
