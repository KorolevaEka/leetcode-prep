import { loadAll } from "./solution";

const later = <T>(value: T, ms: number) => () => new Promise<T>(resolve => setTimeout(() => resolve(value), ms));

describe("loadAll", () => {
  test("порядок результатов совпадает с порядком загрузчиков", async () => {
    expect(await loadAll([later("A", 20), later("B", 1), later("C", 10)])).toEqual(["A", "B", "C"]);
  });

  test("все загрузчики стартуют сразу", async () => {
    const started: number[] = [];
    const loader = (n: number) => () => {
      started.push(n);
      return new Promise<number>(resolve => setTimeout(() => resolve(n), 5));
    };
    const pending = loadAll([loader(1), loader(2), loader(3)]);
    expect(started).toEqual([1, 2, 3]);
    expect(await pending).toEqual([1, 2, 3]);
  });

  test("ошибка загрузчика отклоняет результат", async () => {
    const broken = () => Promise.reject(new Error("source down"));
    await expect(loadAll([later(1, 1), broken])).rejects.toThrow("source down");
  });

  test("пустой список загрузчиков", async () => {
    expect(await loadAll([])).toEqual([]);
  });
});
