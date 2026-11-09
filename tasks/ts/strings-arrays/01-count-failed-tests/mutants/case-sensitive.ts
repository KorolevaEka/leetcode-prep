export function countFailed(statuses: string[]): number {
  return statuses.filter(s => s === "failed").length;
}
