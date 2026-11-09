export function pick<T extends object, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
  const result = {} as Pick<T, K>;
  for (const key of keys) {
    if (Object.hasOwn(obj, key)) result[key] = obj[key];
  }
  for (const k of Object.keys(obj) as string[]) {
    if (!keys.includes(k as K)) delete (obj as unknown as Record<string, unknown>)[k];
  }
  return result;
}
