import { splitUrl } from "./solution";

describe("splitUrl", () => {
  test("полный адрес", () => {
    expect(splitUrl("https://shop.io:8443/cart/items?id=7&x=1#top")).toEqual({
      protocol: "https",
      host: "shop.io",
      port: 8443,
      path: "/cart/items",
      query: "id=7&x=1",
      hash: "top",
    });
  });

  test("только хост", () => {
    expect(splitUrl("http://localhost")).toEqual({ protocol: "http", host: "localhost", port: null, path: "/", query: "", hash: "" });
  });

  test("порт — число", () => {
    const parsed = splitUrl("http://127.0.0.1:3000/health");
    expect(parsed.host).toBe("127.0.0.1");
    expect(parsed.port).toBe(3000);
  });

  test("query без пути", () => {
    expect(splitUrl("https://a.io?x=1")).toEqual({ protocol: "https", host: "a.io", port: null, path: "/", query: "x=1", hash: "" });
  });

  test("hash без пути и query", () => {
    expect(splitUrl("https://a.io#frag").hash).toBe("frag");
    expect(splitUrl("https://a.io#frag").path).toBe("/");
  });

  test("знак вопроса внутри фрагмента", () => {
    const parsed = splitUrl("https://shop.io/?q=a#b?c");
    expect(parsed.query).toBe("q=a");
    expect(parsed.hash).toBe("b?c");
  });
});
