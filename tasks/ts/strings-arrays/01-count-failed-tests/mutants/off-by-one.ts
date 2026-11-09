export function countFailed(statuses: string[]): number {
  return statuses.slice(0, -1).filter(s => s.toLowerCase() === "failed").length;
}
