import { LruCache } from "./solution";

describe("LruCache", () => {
  test("пример из условия", () => {
    const cache = new LruCache<number>(2);
    cache.put("a", 1);
    cache.put("b", 2);
    expect(cache.get("a")).toBe(1);
    cache.put("c", 3);
    expect(cache.get("b")).toBeUndefined();
    expect(cache.get("a")).toBe(1);
    expect(cache.get("c")).toBe(3);
    expect(cache.size).toBe(2);
  });

  test("без обращений вытесняется самый старый", () => {
    const cache = new LruCache<string>(2);
    cache.put("a", "1");
    cache.put("b", "2");
    cache.put("c", "3");
    expect(cache.get("a")).toBeUndefined();
    expect(cache.get("b")).toBe("2");
  });

  test("перезапись ключа освежает его и не увеличивает размер", () => {
    const cache = new LruCache<number>(2);
    cache.put("a", 1);
    cache.put("b", 2);
    cache.put("a", 10);
    expect(cache.size).toBe(2);
    cache.put("c", 3);
    expect(cache.get("b")).toBeUndefined();
    expect(cache.get("a")).toBe(10);
  });

  test("нулевое и пустое значения — не промах", () => {
    const cache = new LruCache<number | string>(3);
    cache.put("zero", 0);
    cache.put("empty", "");
    expect(cache.get("zero")).toBe(0);
    expect(cache.get("empty")).toBe("");
  });

  test("вместимость 1", () => {
    const cache = new LruCache<number>(1);
    cache.put("a", 1);
    cache.put("b", 2);
    expect(cache.get("a")).toBeUndefined();
    expect(cache.get("b")).toBe(2);
    expect(cache.size).toBe(1);
  });

  test("отсутствующий ключ", () => {
    expect(new LruCache<number>(2).get("nope")).toBeUndefined();
  });
});
