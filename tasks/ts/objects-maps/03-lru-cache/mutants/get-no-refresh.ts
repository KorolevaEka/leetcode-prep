export class LruCache<V> {
  private items = new Map<string, V>();

  constructor(private capacity: number) {}

  get(key: string): V | undefined {
    if (!this.items.has(key)) return undefined;
    return this.items.get(key);
  }

  put(key: string, value: V): void {
    this.items.delete(key);
    this.items.set(key, value);
    if (this.items.size > this.capacity) {
      const oldest = this.items.keys().next().value as string;
      this.items.delete(oldest);
    }
  }

  get size(): number {
    return this.items.size;
  }
}
