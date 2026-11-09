export class SlidingAverage {
  private values: number[] = [];
  private sum = 0;

  constructor(private size: number) {}

  add(value: number): number {
    this.values.push(value);
    this.sum += value;
    if (this.values.length > this.size) this.sum -= this.values.shift() as number;
    return this.sum / this.values.length;
  }
}
