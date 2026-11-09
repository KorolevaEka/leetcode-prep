function isPlainObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && !Array.isArray(value);
}

export function diffPaths(before: unknown, after: unknown): string[] {
  const paths: string[] = [];

  function walk(a: unknown, b: unknown, path: string): void {
    if (Array.isArray(a) && Array.isArray(b)) {
      const length = Math.max(a.length, b.length);
      for (let i = 0; i < length; i++) {
        if (i >= a.length || i >= b.length) paths.push(`${path}[${i}]`);
        else walk(a[i], b[i], `${path}[${i}]`);
      }
    } else if (isPlainObject(a) && isPlainObject(b)) {
      for (const key of new Set([...Object.keys(a), ...Object.keys(b)])) {
        const child = path === "" ? key : `${path}.${key}`;
        if (!Object.hasOwn(a, key) || !Object.hasOwn(b, key)) paths.push(child);
        else walk(a[key], b[key], child);
      }
    } else if (a !== b) {
      paths.push(path === "" ? "$" : path);
    }
  }

  walk(before, after, "");
  return paths.sort();
}
