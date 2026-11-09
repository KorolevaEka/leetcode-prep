import { test } from "node:test";
import assert from "node:assert/strict";
import { taskState } from "../web/unlock.js";

const t = (id, level, order, extra = {}) => ({ id, lang: "python", topic: "arrays", order, level, kind: "code", title: id, ...extra });

const e1 = t("python/arrays/01-a", "easy", 1);
const e2 = t("python/arrays/02-b", "easy", 2);
const e3 = t("python/arrays/03-c", "easy", 3);
const h1 = t("python/arrays/04-d", "hard", 4);
const all = [e2, h1, e1, e3]; // намеренно не по порядку

test("first easy task is open", () => {
  assert.equal(taskState(e1, all, new Set()), "open");
});

test("second easy task is locked until the first is solved", () => {
  assert.equal(taskState(e2, all, new Set()), "locked");
  assert.equal(taskState(e2, all, new Set([e1.id])), "open");
});

test("first hard task is open without any solved easy tasks", () => {
  assert.equal(taskState(h1, all, new Set()), "open");
});

test("a solved task reports solved", () => {
  assert.equal(taskState(e1, all, new Set([e1.id])), "solved");
  assert.equal(taskState(e2, all, new Set([e2.id])), "solved");
});

test("a task in another topic does not affect the chain", () => {
  const other = t("python/loops/01-x", "easy", 1, { topic: "loops" });
  assert.equal(taskState(e2, [other, e1, e2], new Set([other.id])), "locked");
  assert.equal(taskState(e2, [other, e1, e2], new Set([e1.id])), "open");
});

test("a task in another language does not affect the chain", () => {
  const sql = t("sql/arrays/01-y", "easy", 1, { lang: "sql" });
  assert.equal(taskState(e2, [sql, e1, e2], new Set([sql.id])), "locked");
});

test("order is by the order field, not array position", () => {
  assert.equal(taskState(e3, all, new Set([e1.id])), "locked");
  assert.equal(taskState(e3, all, new Set([e2.id])), "open");
});
