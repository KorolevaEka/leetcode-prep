import { formatDuration } from "./solution";

describe("formatDuration", () => {
  test("меньше минуты", () => {
    expect(formatDuration(0)).toBe("0s");
    expect(formatDuration(45)).toBe("45s");
    expect(formatDuration(59)).toBe("59s");
  });

  test("минуты с ведущим нулём в секундах", () => {
    expect(formatDuration(60)).toBe("1m 00s");
    expect(formatDuration(125)).toBe("2m 05s");
    expect(formatDuration(3599)).toBe("59m 59s");
  });

  test("часы с ведущими нулями", () => {
    expect(formatDuration(3600)).toBe("1h 00m 00s");
    expect(formatDuration(3725)).toBe("1h 02m 05s");
    expect(formatDuration(36000)).toBe("10h 00m 00s");
  });

  test("отрицательное число", () => {
    expect(() => formatDuration(-1)).toThrow(RangeError);
  });

  test("дробное число", () => {
    expect(() => formatDuration(1.5)).toThrow(RangeError);
  });
});
