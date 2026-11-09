import { diffPaths } from "./solution";

describe("diffPaths", () => {
  test("пример из условия", () => {
    const before = { user: { name: "a", roles: ["x", "y"] } };
    const after = { user: { name: "b", roles: ["x", "z", "w"] } };
    expect(diffPaths(before, after)).toEqual(["user.name", "user.roles[1]", "user.roles[2]"]);
  });

  test("одинаковые документы", () => {
    const doc = { a: [1, { b: null }], c: "x" };
    expect(diffPaths(doc, { a: [1, { b: null }], c: "x" })).toEqual([]);
  });

  test("ключ есть только с одной стороны", () => {
    expect(diffPaths({ a: 1, b: 2 }, { a: 1, c: 3 })).toEqual(["b", "c"]);
  });

  test("недостающие элементы массива", () => {
    expect(diffPaths({ ids: [1, 2, 3] }, { ids: [1] })).toEqual(["ids[1]", "ids[2]"]);
  });

  test("объект внутри массива", () => {
    expect(diffPaths([{ id: 1 }, { id: 2 }], [{ id: 1 }, { id: 3 }])).toEqual(["[1].id"]);
  });

  test("null и объект", () => {
    expect(diffPaths({ owner: null }, { owner: { id: 1 } })).toEqual(["owner"]);
    expect(diffPaths({ owner: { id: 1 } }, { owner: null })).toEqual(["owner"]);
  });

  test("разные типы: массив и объект", () => {
    expect(diffPaths({ v: [] }, { v: {} })).toEqual(["v"]);
  });

  test("различаются сами корни", () => {
    expect(diffPaths(1, 2)).toEqual(["$"]);
    expect(diffPaths("a", "a")).toEqual([]);
  });
});
