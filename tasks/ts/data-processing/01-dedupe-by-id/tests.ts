import { dedupeById } from "./solution";

describe("dedupeById", () => {
  test("пример из условия", () => {
    const result = dedupeById([
      { id: 2, name: "Ann" },
      { id: 1, name: "Bob" },
      { id: 2, name: "Ann (copy)" },
    ]);
    expect(result).toEqual([{ id: 2, name: "Ann" }, { id: 1, name: "Bob" }]);
  });

  test("остаётся первая запись, а не последняя", () => {
    const result = dedupeById([{ id: 1, name: "first" }, { id: 1, name: "second" }]);
    expect(result).toEqual([{ id: 1, name: "first" }]);
  });

  test("исходный порядок сохраняется", () => {
    const result = dedupeById([{ id: 3, name: "c" }, { id: 1, name: "a" }, { id: 2, name: "b" }]);
    expect(result.map(u => u.id)).toEqual([3, 1, 2]);
  });

  test("без дубликатов список не меняется", () => {
    const users = [{ id: 1, name: "a" }, { id: 2, name: "b" }];
    expect(dedupeById(users)).toEqual(users);
  });

  test("пустой список", () => {
    expect(dedupeById([])).toEqual([]);
  });
});
