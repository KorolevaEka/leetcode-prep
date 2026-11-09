import { pick } from "./solution";

interface User {
  id: number;
  name: string;
  email: string;
  nickname?: string;
}

const user: User = { id: 1, name: "Ann", email: "a@x.io" };

describe("pick", () => {
  test("берёт только указанные поля", () => {
    expect(pick(user, ["id", "name"])).toEqual({ id: 1, name: "Ann" });
  });

  test("пустой список ключей", () => {
    expect(pick(user, [])).toEqual({});
  });

  test("отсутствующее необязательное поле не появляется", () => {
    const picked = pick(user, ["id", "nickname"]);
    expect(Object.keys(picked)).toEqual(["id"]);
  });

  test("возвращает новый объект и не меняет исходный", () => {
    const picked = pick(user, ["id"]);
    expect(picked).not.toBe(user);
    expect(user).toEqual({ id: 1, name: "Ann", email: "a@x.io" });
  });

  test("типы результата и ключей проверяются компилятором", () => {
    const compileChecks = () => {
      const picked = pick(user, ["id", "name"]);
      const id: number = picked.id;
      // @ts-expect-error email не выбран, поля нет в типе результата
      const email = picked.email;
      // @ts-expect-error такого ключа нет у User
      const bad = pick(user, ["age"]);
      return [id, email, bad];
    };
    void compileChecks;
  });
});
