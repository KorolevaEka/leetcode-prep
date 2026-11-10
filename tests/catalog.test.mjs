import { test } from "node:test";
import assert from "node:assert/strict";
import { blocker, catalog, langCounts, nextTask, prevTask } from "../web/catalog.js";

const t = (id, level, order, extra = {}) =>
  ({ id: `python/arrays/${id}`, lang: "python", topic: "arrays", order, level, kind: "code", title: id, ...extra });

const e1 = t("01-a", "easy", 1), e2 = t("02-b", "easy", 2), h1 = t("03-c", "hard", 3), h2 = t("04-d", "hard", 4);
const s1 = { id: "sql/joins/01-x", lang: "sql", topic: "joins", order: 1, level: "easy", kind: "code", title: "x" };
const tasks = [h2, e2, s1, h1, e1];
const topics = {
  python: [{ id: "arrays", title: "Массивы" }, { id: "empty", title: "Пусто" }],
  sql: [{ id: "joins", title: "JOIN" }],
};

test("langCounts counts solved and total per language", () => {
  const c = langCounts(tasks, new Set([e1.id, s1.id]));
  assert.deepEqual(c.python, { solved: 1, total: 4 });
  assert.deepEqual(c.sql, { solved: 1, total: 1 });
  assert.deepEqual(c.java, { solved: 0, total: 0 });
});

test("catalog without filters lists every topic, tasks by level then order, with states", () => {
  const c = catalog(tasks, topics, new Set([e1.id]), { lang: "python" });
  assert.deepEqual(c.map(x => x.topic.id), ["arrays", "empty"]);
  assert.deepEqual(c[0].items.map(i => [i.task.id, i.state]),
    [[e1.id, "solved"], [e2.id, "open"], [h1.id, "open"], [h2.id, "locked"]]);
  assert.equal(c[0].solved, 1);
  assert.deepEqual(c[1].items, []);
});

test("catalog level filter keeps only that level and drops topics without it", () => {
  const c = catalog(tasks, topics, new Set(), { lang: "python", level: "hard" });
  assert.deepEqual(c.map(x => x.topic.id), ["arrays"]);
  assert.deepEqual(c[0].items.map(i => [i.task.id, i.state]), [[h1.id, "open"], [h2.id, "locked"]]);
});

test("catalog topic filter keeps one topic", () => {
  assert.deepEqual(catalog(tasks, topics, new Set(), { lang: "python", topic: "empty" }).map(x => x.topic.id), ["empty"]);
});

test("nextTask picks the next open task in the topic, wrapping to earlier ones", () => {
  assert.equal(nextTask(e1, tasks, new Set([e1.id])).id, e2.id);
  assert.equal(nextTask(e2, tasks, new Set([e1.id, e2.id])).id, h1.id);
  assert.equal(nextTask(h1, tasks, new Set([h1.id])).id, h2.id);
  assert.equal(nextTask(h2, tasks, new Set([h1.id, h2.id])).id, e1.id);
  assert.equal(nextTask(s1, tasks, new Set([s1.id])), null);
});

test("blocker is the first unsolved task of the same level chain", () => {
  assert.equal(blocker(h2, tasks, new Set()).id, h1.id);
  assert.equal(blocker(e2, tasks, new Set()).id, e1.id);
});

test("prevTask is the previous task of the topic, no wrap-around", () => {
  assert.equal(prevTask(e2, tasks).id, e1.id);
  assert.equal(prevTask(h1, tasks).id, e2.id);
  assert.equal(prevTask(e1, tasks), null);
  assert.equal(prevTask(s1, tasks), null);
});
