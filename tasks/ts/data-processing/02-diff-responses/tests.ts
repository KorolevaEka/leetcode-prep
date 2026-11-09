import { diffResponses } from "./solution";

describe("diffResponses", () => {
  test("пример из условия", () => {
    const before = { id: 1, name: "a", tags: ["x"] };
    const after = { id: 1, name: "b", tags: ["x"], extra: true };
    expect(diffResponses(before, after)).toEqual({ added: ["extra"], removed: [], changed: ["name"] });
  });

  test("одинаковые ответы", () => {
    expect(diffResponses({ a: 1, b: { c: [1, 2] } }, { a: 1, b: { c: [1, 2] } })).toEqual({ added: [], removed: [], changed: [] });
  });

  test("пропавшие поля", () => {
    expect(diffResponses({ a: 1, b: 2 }, { a: 1 })).toEqual({ added: [], removed: ["b"], changed: [] });
  });

  test("изменение во вложенном объекте", () => {
    const result = diffResponses({ user: { role: "admin" } }, { user: { role: "guest" } });
    expect(result).toEqual({ added: [], removed: [], changed: ["user"] });
  });

  test("списки отсортированы по возрастанию", () => {
    const result = diffResponses({ z: 1, a: 1, m: 1 }, { z: 2, a: 2, m: 2, y: 0, b: 0 });
    expect(result.changed).toEqual(["a", "m", "z"]);
    expect(result.added).toEqual(["b", "y"]);
  });

  test("поле со значением null — это существующее поле", () => {
    expect(diffResponses({ a: null }, { a: null })).toEqual({ added: [], removed: [], changed: [] });
    expect(diffResponses({ a: null }, { a: 1 })).toEqual({ added: [], removed: [], changed: ["a"] });
    expect(diffResponses({}, { a: null })).toEqual({ added: ["a"], removed: [], changed: [] });
  });
});
