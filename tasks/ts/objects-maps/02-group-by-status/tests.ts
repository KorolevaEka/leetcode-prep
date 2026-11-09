import { groupByStatus } from "./solution";

describe("groupByStatus", () => {
  test("пример из условия", () => {
    const grouped = groupByStatus([
      { name: "login", status: "passed" },
      { name: "cart", status: "failed" },
      { name: "pay", status: "passed" },
      { name: "login", status: "passed" },
    ]);
    expect(grouped).toEqual(new Map([["passed", ["login", "pay"]], ["failed", ["cart"]]]));
  });

  test("несколько тестов в одной группе — в порядке появления", () => {
    const grouped = groupByStatus([
      { name: "a", status: "failed" },
      { name: "b", status: "failed" },
      { name: "c", status: "failed" },
    ]);
    expect(grouped.get("failed")).toEqual(["a", "b", "c"]);
  });

  test("ключи идут в порядке первого появления статуса", () => {
    const grouped = groupByStatus([
      { name: "a", status: "skipped" },
      { name: "b", status: "failed" },
      { name: "c", status: "passed" },
    ]);
    expect([...grouped.keys()]).toEqual(["skipped", "failed", "passed"]);
  });

  test("повтор имени с тем же статусом не дублируется", () => {
    const grouped = groupByStatus([
      { name: "a", status: "passed" },
      { name: "a", status: "passed" },
    ]);
    expect(grouped.get("passed")).toEqual(["a"]);
  });

  test("пустой отчёт", () => {
    expect(groupByStatus([]).size).toBe(0);
  });
});
