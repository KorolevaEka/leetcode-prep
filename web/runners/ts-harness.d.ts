interface Matchers<R> {
  toBe(expected: unknown): R;
  toEqual(expected: unknown): R;
  toStrictEqual(expected: unknown): R;
  toBeTruthy(): R;
  toBeFalsy(): R;
  toBeNull(): R;
  toBeUndefined(): R;
  toBeDefined(): R;
  toContain(item: unknown): R;
  toHaveLength(length: number): R;
  toBeGreaterThan(n: number): R;
  toBeLessThan(n: number): R;
  toBeGreaterThanOrEqual(n: number): R;
  toBeLessThanOrEqual(n: number): R;
  toHaveProperty(path: string | readonly string[], value?: unknown): R;
  toBeCloseTo(n: number, digits?: number): R;
  toThrow(expected?: string | RegExp | Error | (new (...args: any[]) => unknown)): R;
  toThrowError(expected?: string | RegExp | Error | (new (...args: any[]) => unknown)): R;
  toMatch(expected: string | RegExp): R;
}
interface Expectation extends Matchers<void> {
  not: Matchers<void>;
  resolves: Matchers<Promise<void>> & { not: Matchers<Promise<void>> };
  rejects: Matchers<Promise<void>> & { not: Matchers<Promise<void>> };
}
declare function expect(actual: unknown): Expectation;
declare function describe(name: string, fn: () => void): void;
declare function test(name: string, fn: () => void | Promise<void>): void;
declare function beforeEach(fn: () => void | Promise<void>): void;
declare function afterEach(fn: () => void | Promise<void>): void;
declare function it(name: string, fn: () => void | Promise<void>): void;
declare const console: {
  log(...args: unknown[]): void;
  info(...args: unknown[]): void;
  warn(...args: unknown[]): void;
  error(...args: unknown[]): void;
  debug(...args: unknown[]): void;
};
declare function setTimeout(handler: (...args: any[]) => void, ms?: number, ...args: any[]): number;
declare function clearTimeout(id?: number): void;
declare function setInterval(handler: (...args: any[]) => void, ms?: number, ...args: any[]): number;
declare function clearInterval(id?: number): void;
