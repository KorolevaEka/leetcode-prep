import { parseSelector } from "./solution";

describe("parseSelector", () => {
  test("полный селектор", () => {
    expect(parseSelector('button#save.primary.big[data-test="ok"][disabled]')).toEqual({
      tag: "button",
      id: "save",
      classes: ["primary", "big"],
      attrs: { "data-test": "ok", disabled: "" },
    });
  });

  test("только тег", () => {
    expect(parseSelector("div")).toEqual({ tag: "div", id: null, classes: [], attrs: {} });
  });

  test("без тега: класс и id", () => {
    expect(parseSelector(".a.b#main")).toEqual({ tag: null, id: "main", classes: ["a", "b"], attrs: {} });
  });

  test("значение без кавычек и в одинарных кавычках", () => {
    expect(parseSelector("input[type=submit][name='go']").attrs).toEqual({ type: "submit", name: "go" });
  });

  test("спецсимволы внутри кавычек", () => {
    expect(parseSelector('[title="a.b]c#d"]')).toEqual({ tag: null, id: null, classes: [], attrs: { title: "a.b]c#d" } });
  });

  test("порядок классов сохраняется", () => {
    expect(parseSelector("span.z.a.m").classes).toEqual(["z", "a", "m"]);
  });
});
