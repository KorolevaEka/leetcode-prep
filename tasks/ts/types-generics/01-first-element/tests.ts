import { first } from "./solution";

describe("first", () => {
  test("первый элемент чисел и строк", () => {
    expect(first([10, 20, 30])).toBe(10);
    expect(first(["a", "b"])).toBe("a");
  });

  test("один элемент", () => {
    expect(first([42])).toBe(42);
  });

  test("пустой массив даёт undefined", () => {
    expect(first([])).toBeUndefined();
  });

  test("нулевое значение — тоже элемент", () => {
    expect(first([0, 1])).toBe(0);
  });

  test("типы выводятся из аргумента", () => {
    const compileChecks = () => {
      const n: number | undefined = first([1, 2]);
      // @ts-expect-error результат может быть undefined, в number его класть нельзя
      const strict: number = first([1, 2]);
      // @ts-expect-error для массива чисел результат — не строка
      const wrong: string | undefined = first([1, 2]);
      return [n, strict, wrong];
    };
    void compileChecks;
  });
});
