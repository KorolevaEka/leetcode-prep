export function pick(obj: any, keys: string[]): any {
  const result: Record<string, unknown> = {};
  for (const key of keys) {
    if (Object.hasOwn(obj, key)) result[key] = obj[key];
  }
  return result;
}
