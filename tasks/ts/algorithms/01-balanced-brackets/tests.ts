import { isBalanced } from "./solution";

describe("isBalanced", () => {
  test("правильная вложенность", () => {
    expect(isBalanced('{"ids": [1, 2, (3)]}')).toBe(true);
    expect(isBalanced("()[]{}")).toBe(true);
  });

  test("неправильный порядок", () => {
    expect(isBalanced("([)]")).toBe(false);
    expect(isBalanced(")(")).toBe(false);
  });

  test("не закрыта открывающая", () => {
    expect(isBalanced("(()")).toBe(false);
    expect(isBalanced("{")).toBe(false);
  });

  test("лишняя закрывающая", () => {
    expect(isBalanced("())")).toBe(false);
    expect(isBalanced("]")).toBe(false);
    expect(isBalanced("}{")).toBe(false);
  });

  test("пустая строка и строка без скобок", () => {
    expect(isBalanced("")).toBe(true);
    expect(isBalanced("plain text")).toBe(true);
  });
});
