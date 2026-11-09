export function loadAll<T>(loaders: (() => Promise<T>)[]): Promise<T[]> {
  return new Promise((resolve, reject) => {
    const results: T[] = [];
    if (loaders.length === 0) return resolve(results);
    for (const load of loaders) {
      load().then(value => {
        results.push(value);
        if (results.length === loaders.length) resolve(results);
      }, reject);
    }
  });
}
