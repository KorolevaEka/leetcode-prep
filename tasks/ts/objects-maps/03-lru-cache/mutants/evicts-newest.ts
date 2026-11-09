export class LruCache<V> {
  private items = new Map<string, V>();

  constructor(private capacity: number) {}

  get(key: string): V | undefined {
    if (!this.items.has(key)) return undefined;
    const value = this.items.get(key) as V;
    this.items.delete(key);
    this.items.set(key, value);
    return value;
  }

  put(key: string, value: V): void {
    this.items.delete(key);
    this.items.set(key, value);
    if (this.items.size > this.capacity) {
      const oldest = [...this.items.keys()].pop() as string;
      this.items.delete(oldest);
    }
  }

  get size(): number {
    return this.items.size;
  }
}
