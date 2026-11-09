import { summarize } from "./solution";

const slowFail = () => new Promise<never>((_, reject) => setTimeout(() => reject(new Error("late")), 10));

describe("summarize", () => {
  test("смесь успехов и ошибок", async () => {
    const result = await summarize([Promise.resolve(1), Promise.reject(new Error("x")), Promise.resolve(2)]);
    expect(result).toEqual({ fulfilled: 2, rejected: 1 });
  });

  test("все успешны", async () => {
    expect(await summarize([Promise.resolve("a"), Promise.resolve("b")])).toEqual({ fulfilled: 2, rejected: 0 });
  });

  test("все с ошибкой", async () => {
    const result = await summarize([Promise.reject(new Error("1")), Promise.reject(new Error("2"))]);
    expect(result).toEqual({ fulfilled: 0, rejected: 2 });
  });

  test("ждёт и позднюю ошибку", async () => {
    expect(await summarize([Promise.resolve(1), slowFail(), Promise.resolve(2)])).toEqual({ fulfilled: 2, rejected: 1 });
  });

  test("пустой список", async () => {
    expect(await summarize([])).toEqual({ fulfilled: 0, rejected: 0 });
  });
});
