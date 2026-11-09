export interface TestResult {
  name: string;
  status: string;
}


export function groupByStatus(results: TestResult[]): Map<string, string[]> {
  const groups = new Map<string, string[]>();
  for (const r of results) {
    const names = groups.get(r.status) ?? [];
    names.push(r.name);
    groups.set(r.status, names);
  }
  return groups;
}
