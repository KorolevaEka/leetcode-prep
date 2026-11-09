export class SlidingAverage {
  private values: number[] = [];
  private sum = 0;

  constructor(private size: number) {}

  add(value: number): number {
    this.values.push(value);
    this.sum += value;
    return this.sum / this.values.length;
  }
}
