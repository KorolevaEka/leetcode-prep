export class TokenBucket {
  private tokens: number;
  private last: number | null = null;

  constructor(private capacity: number, private refillPerSecond: number) {
    this.tokens = capacity;
  }

  tryTake(nowMs: number, count = 1): boolean {
    if (this.last !== null) {
      const elapsedSeconds = (nowMs - this.last) / 1000;
      this.tokens = Math.min(this.capacity, this.tokens + elapsedSeconds * this.refillPerSecond);
    }
    this.last = nowMs;
    if (this.tokens <= count) return false;
    this.tokens -= count;
    return true;
  }
}
