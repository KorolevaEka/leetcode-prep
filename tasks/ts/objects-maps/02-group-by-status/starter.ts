export interface TestResult {
  name: string;
  status: string;
}

export function groupByStatus(results: TestResult[]): Map<string, string[]> {
  throw new Error("TODO");
}
