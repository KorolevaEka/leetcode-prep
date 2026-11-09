import { compareVersions } from "./solution";

describe("compareVersions", () => {
  test("равные версии", () => {
    expect(compareVersions("1.2.3", "1.2.3")).toBe(0);
  });

  test("меньше и больше", () => {
    expect(compareVersions("1.2.3", "1.2.4")).toBe(-1);
    expect(compareVersions("1.2.4", "1.2.3")).toBe(1);
    expect(compareVersions("1.0.0", "2.0.0")).toBe(-1);
    expect(compareVersions("2.0.0", "1.9.9")).toBe(1);
  });

  test("части сравниваются как числа", () => {
    expect(compareVersions("1.9.0", "1.10.0")).toBe(-1);
    expect(compareVersions("1.10.0", "1.9.0")).toBe(1);
  });

  test("недостающие части — нули", () => {
    expect(compareVersions("1.2", "1.2.0")).toBe(0);
    expect(compareVersions("1.2.0", "1.2")).toBe(0);
    expect(compareVersions("1", "1.0.1")).toBe(-1);
    expect(compareVersions("1.0.1", "1")).toBe(1);
  });

  test("решает третья часть", () => {
    expect(compareVersions("3.4.5", "3.4.50")).toBe(-1);
  });
});
