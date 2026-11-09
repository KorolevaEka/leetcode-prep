import { firstBad } from "./solution";

describe("firstBad", () => {
  test("пример из условия", () => {
    expect(firstBad(n => n >= 4, 10)).toBe(4);
  });

  test("сломана самая первая сборка", () => {
    expect(firstBad(() => true, 5)).toBe(1);
  });

  test("сломана только последняя сборка", () => {
    expect(firstBad(n => n >= 10, 10)).toBe(10);
  });

  test("сломанных сборок нет", () => {
    expect(firstBad(() => false, 10)).toBe(-1);
  });

  test("единственная сборка", () => {
    expect(firstBad(() => true, 1)).toBe(1);
    expect(firstBad(() => false, 1)).toBe(-1);
  });

  test("число вызовов isBad логарифмическое", () => {
    let calls = 0;
    const result = firstBad(n => {
      calls++;
      return n >= 777_777;
    }, 1_000_000);
    expect(result).toBe(777_777);
    expect(calls).toBeLessThan(25);
  });
});
