export function firstBad(isBad: (build: number) => boolean, total: number): number {
  let low = 1;
  let high = total + 1;
  while (low < high) {
    const mid = Math.floor((low + high) / 2);
    if (isBad(mid)) high = mid;
    else low = mid + 1;
  }
  return low <= total ? low : -1;
}
