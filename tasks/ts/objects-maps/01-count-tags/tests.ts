import { countTags } from "./solution";

describe("countTags", () => {
  test("пример из условия", () => {
    expect(countTags(["smoke", "API", "Smoke ", "api", "  "])).toEqual({ smoke: 2, api: 2 });
  });

  test("пробелы по краям не важны", () => {
    expect(countTags([" ui", "ui ", "  ui  "])).toEqual({ ui: 3 });
  });

  test("регистр не важен", () => {
    expect(countTags(["Smoke", "SMOKE", "smoke"])).toEqual({ smoke: 3 });
  });

  test("пустые теги пропускаются", () => {
    expect(countTags(["", " ", "\t"])).toEqual({});
  });

  test("пустой список", () => {
    expect(countTags([])).toEqual({});
  });

  test("тег с именем свойства Object.prototype", () => {
    expect(countTags(["constructor", "constructor"])).toEqual({ constructor: 2 });
  });
});
