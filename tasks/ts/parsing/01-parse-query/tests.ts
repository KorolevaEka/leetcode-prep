import { parseQuery } from "./solution";

describe("parseQuery", () => {
  test("со знаком вопроса и без него", () => {
    expect(parseQuery("?page=2&sort=name")).toEqual({ page: "2", sort: "name" });
    expect(parseQuery("page=2&sort=name")).toEqual({ page: "2", sort: "name" });
  });

  test("декодирование, параметр без значения и «=» внутри значения", () => {
    expect(parseQuery("q=a%20b&flag&token=x=y")).toEqual({ q: "a b", flag: "", token: "x=y" });
  });

  test("декодируется и имя параметра", () => {
    expect(parseQuery("a%5Bb%5D=1")).toEqual({ "a[b]": "1" });
  });

  test("повторный параметр — побеждает последний", () => {
    expect(parseQuery("a=1&a=2&a=3")).toEqual({ a: "3" });
  });

  test("пустые части пропускаются", () => {
    expect(parseQuery("a=1&&b=2&")).toEqual({ a: "1", b: "2" });
  });

  test("пустая строка и один вопросительный знак", () => {
    expect(parseQuery("")).toEqual({});
    expect(parseQuery("?")).toEqual({});
  });
});
