import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { execute } from "../scripts/executors/sql.mjs";

const dir = "tasks/sql/joins/01-combine-two-tables/";
const read = n => readFileSync(dir + n, "utf8");
const task = { kind: "code", schema: read("schema.sql"), expected: read("expected.csv") };

test("correct query passes", async () => {
  const r = await execute(task, read("reference.sql"));
  assert.equal(r.passed, true, r.output);
});

test("wrong result fails with expected/actual diff", async () => {
  const r = await execute(task, read("mutants/inner-join.sql"));
  assert.equal(r.passed, false);
  assert.match(r.output, /--- expected/);
});

test("syntax error returns postgres message", async () => {
  const r = await execute(task, "SELEKT 1");
  assert.equal(r.passed, false);
  assert.match(r.output, /syntax error/);
});
