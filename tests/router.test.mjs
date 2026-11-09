import { test } from "node:test";
import assert from "node:assert/strict";
import { parseRoute, cleanAuthParams } from "../web/router.js";

test("landing for empty and unknown hashes", () => {
  assert.deepEqual(parseRoute(""), { page: "landing" });
  assert.deepEqual(parseRoute("#"), { page: "landing" });
  assert.deepEqual(parseRoute("#/"), { page: "landing" });
  assert.deepEqual(parseRoute("#/nope/x"), { page: "landing" });
});

test("catalog with and without filters", () => {
  assert.deepEqual(parseRoute("#/learn/python"), { page: "catalog", lang: "python" });
  assert.deepEqual(parseRoute("#/learn/sql?topic=joins&level=hard"), { page: "catalog", lang: "sql", topic: "joins", level: "hard" });
  assert.deepEqual(parseRoute("#/learn/ts?level=easy"), { page: "catalog", lang: "ts", level: "easy" });
});

test("task route", () => {
  assert.deepEqual(parseRoute("#/task/python/arrays/01-two-sum"), { page: "task", id: "python/arrays/01-two-sum" });
});

test("cleanAuthParams strips code/error params and keeps the rest", () => {
  const u = new URL("https://x.github.io/live-coding-trainings/?code=abc&error=e&error_description=d&keep=1#/learn/sql");
  const c = cleanAuthParams(u);
  assert.equal(c.toString(), "https://x.github.io/live-coding-trainings/?keep=1#/learn/sql");
  assert.equal(u.searchParams.get("code"), "abc");
});

test("cleanAuthParams returns null when nothing to clean", () => {
  assert.equal(cleanAuthParams(new URL("https://x.io/?keep=1#/")), null);
  assert.equal(cleanAuthParams(new URL("https://x.io/#/")), null);
});
