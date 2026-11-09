import { countFailed } from "./solution";

describe("countFailed", () => {
  test("считает упавшие", () => {
    expect(countFailed(["passed", "failed", "passed"])).toBe(1);
  });

  test("не учитывает регистр", () => {
    expect(countFailed(["Failed", "FAILED", "failed"])).toBe(3);
  });

  test("пропущенные не считаются упавшими", () => {
    expect(countFailed(["skipped", "failed", "skipped"])).toBe(1);
  });

  test("последний результат тоже считается", () => {
    expect(countFailed(["passed", "passed", "failed"])).toBe(1);
  });

  test("пустой список", () => {
    expect(countFailed([])).toBe(0);
  });

  test("возвращает число", () => {
    const wrongArgs = () => {
      // @ts-expect-error статусы должны быть строками
      countFailed([1, 2]);
    };
    void wrongArgs;
    expect(typeof countFailed(["failed"])).toBe("number");
  });
});
