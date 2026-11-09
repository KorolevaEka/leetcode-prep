export function longestStretch(results: boolean[], maxFailures: number): number {
  let best = 0;
  let left = 0;
  let failures = 0;
  for (let right = 0; right < results.length; right++) {
    if (!results[right]) {
      left = right + 1;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}
