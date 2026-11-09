export interface TestResult {
  name: string;
  status: string;
}


export function groupByStatus(results: TestResult[]): Map<string, string[]> {
  const groups = new Map<string, Set<string>>();
  for (const r of results) {
    const names = groups.get(r.status) ?? new Set<string>();
    names.add(r.name);
    groups.set(r.status, names);
  }
  const out = new Map<string, string[]>();
  for (const [status, names] of groups) out.set(status, [...names]);
  return new Map([...out].sort(([a], [b]) => (a < b ? -1 : 1)));
}
