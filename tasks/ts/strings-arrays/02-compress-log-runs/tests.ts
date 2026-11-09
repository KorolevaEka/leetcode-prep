import { compressRuns } from "./solution";

describe("compressRuns", () => {
  test("пример из условия", () => {
    expect(compressRuns(["start", "retry", "retry", "retry", "done"])).toEqual(["start", "retry (x3)", "done"]);
  });

  test("без повторов список не меняется", () => {
    expect(compressRuns(["a", "b", "c"])).toEqual(["a", "b", "c"]);
  });

  test("одинаковые строки не подряд — разные группы", () => {
    expect(compressRuns(["a", "b", "a"])).toEqual(["a", "b", "a"]);
  });

  test("весь лог из одной строки", () => {
    expect(compressRuns(["x", "x", "x", "x"])).toEqual(["x (x4)"]);
  });

  test("последняя группа тоже сжимается", () => {
    expect(compressRuns(["a", "b", "b"])).toEqual(["a", "b (x2)"]);
  });

  test("одна строка и пустой лог", () => {
    expect(compressRuns(["only"])).toEqual(["only"]);
    expect(compressRuns([])).toEqual([]);
  });
});
