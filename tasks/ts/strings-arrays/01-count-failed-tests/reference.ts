export function countFailed(statuses: string[]): number {
  return statuses.filter(s => s.toLowerCase() === "failed").length;
}
