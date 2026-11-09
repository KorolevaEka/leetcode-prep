import { TokenBucket } from "./solution";

describe("TokenBucket", () => {
  test("ведро создаётся полным", () => {
    const bucket = new TokenBucket(3, 1);
    expect(bucket.tryTake(0)).toBe(true);
    expect(bucket.tryTake(0)).toBe(true);
    expect(bucket.tryTake(0)).toBe(true);
    expect(bucket.tryTake(0)).toBe(false);
  });

  test("пополнение со временем", () => {
    const bucket = new TokenBucket(3, 1);
    bucket.tryTake(0, 3);
    expect(bucket.tryTake(999)).toBe(false);
    expect(bucket.tryTake(1000)).toBe(true);
  });

  test("можно забрать последний токен целиком", () => {
    const bucket = new TokenBucket(1, 1);
    expect(bucket.tryTake(0)).toBe(true);
  });

  test("дробные токены накапливаются", () => {
    const bucket = new TokenBucket(2, 1);
    bucket.tryTake(0, 2);
    expect(bucket.tryTake(500)).toBe(false);
    expect(bucket.tryTake(1000)).toBe(true);
  });

  test("накопление ограничено вместимостью", () => {
    const bucket = new TokenBucket(2, 1);
    bucket.tryTake(0, 2);
    expect(bucket.tryTake(60_000, 2)).toBe(true);
    expect(bucket.tryTake(60_000)).toBe(false);
  });

  test("неудачная попытка ничего не списывает", () => {
    const bucket = new TokenBucket(3, 1);
    expect(bucket.tryTake(0, 5)).toBe(false);
    expect(bucket.tryTake(0, 3)).toBe(true);
  });

  test("пополнение считается от предыдущего вызова", () => {
    const bucket = new TokenBucket(5, 1);
    bucket.tryTake(0, 5);
    expect(bucket.tryTake(1000)).toBe(true);
    expect(bucket.tryTake(2000)).toBe(true);
    expect(bucket.tryTake(2000)).toBe(false);
  });
});
