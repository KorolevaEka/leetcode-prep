import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { execute } from "../scripts/executors/sql.mjs";
import * as sql from "../web/runners/sql.js";
import { loadSchema } from "../web/schema.js";

const dir = "tasks/sql/joins/01-never-run-cases/";
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

test("dangling BEGIN with an error does not poison the next run", async () => {
  const r1 = await execute(task, "BEGIN; SELECT 1/0;");
  assert.equal(r1.passed, false);
  const r2 = await execute(task, read("reference.sql"));
  assert.equal(r2.passed, true, r2.output);
});

test("loadSchema renders after a dangling failed transaction", async () => {
  await execute(task, "BEGIN; SELECT 1/0;");
  const s = await loadSchema(task, await sql.db());
  assert.ok(s.tables.length > 0);
});
