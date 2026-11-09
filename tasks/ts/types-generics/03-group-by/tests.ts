import { groupBy } from "./solution";

type Status = "passed" | "failed";
interface Row {
  id: number;
  status: Status;
}

const rows: Row[] = [
  { id: 1, status: "passed" },
  { id: 2, status: "failed" },
  { id: 3, status: "passed" },
];

describe("groupBy", () => {
  test("раскладывает по группам в исходном порядке", () => {
    expect(groupBy(rows, r => r.status)).toEqual({
      passed: [rows[0], rows[2]],
      failed: [rows[1]],
    });
  });

  test("группа без элементов не создаётся", () => {
    expect(groupBy([rows[0]], r => r.status)).toEqual({ passed: [rows[0]] });
  });

  test("пустой вход", () => {
    expect(groupBy([], (r: Row) => r.status)).toEqual({});
  });

  test("ключ — любая строка, в том числе «constructor»", () => {
    expect(groupBy(["a", "bb", "cc"], s => (s.length === 1 ? "constructor" : "long"))).toEqual({
      constructor: ["a"],
      long: ["bb", "cc"],
    });
  });

  test("ключи результата ограничены типом ключа", () => {
    const compileChecks = () => {
      const grouped = groupBy(rows, r => r.status);
      const passed: Row[] | undefined = grouped.passed;
      // @ts-expect-error статуса «skipped» нет среди возможных ключей
      const skipped = grouped.skipped;
      return [passed, skipped];
    };
    void compileChecks;
  });
});
