export function longestStretch(results: boolean[], maxFailures: number): number {
  let best = 0;
  let left = 0;
  let failures = 0;
  for (let right = 0; right < results.length; right++) {
    if (!results[right]) failures++;
    while (failures >= maxFailures && failures > 0) {
      if (!results[left]) failures--;
      left++;
    }
    best = Math.max(best, right - left + 1);
  }
  return best;
}
