export function countFailed(statuses: string[]): number {
  return statuses.filter(s => ["failed", "skipped"].includes(s.toLowerCase())).length;
}
