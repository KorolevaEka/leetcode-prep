import { longestStretch } from "./solution";

const RUN = [true, true, false, true, true, true, false, true];

describe("longestStretch", () => {
  test("допуск в одно падение", () => {
    expect(longestStretch(RUN, 1)).toBe(6);
  });

  test("без допуска — самая длинная серия успехов", () => {
    expect(longestStretch(RUN, 0)).toBe(3);
  });

  test("допуск покрывает все падения", () => {
    expect(longestStretch(RUN, 2)).toBe(8);
    expect(longestStretch(RUN, 5)).toBe(8);
  });

  test("все тесты прошли", () => {
    expect(longestStretch([true, true, true], 0)).toBe(3);
  });

  test("все упали", () => {
    expect(longestStretch([false, false, false], 0)).toBe(0);
    expect(longestStretch([false, false, false], 2)).toBe(2);
  });

  test("пустой список и один элемент", () => {
    expect(longestStretch([], 3)).toBe(0);
    expect(longestStretch([true], 0)).toBe(1);
  });
});
