import { test } from "node:test";
import assert from "node:assert/strict";
import { hintUsed } from "../web/editor.js";

test("word hints match whole words only", () => {
  assert.equal(hintUsed("dict", "seen = dict()"), true);
  assert.equal(hintUsed("dict", "dictionary = {}"), false);
  assert.equal(hintUsed("LEFT JOIN", "select * from a left   join b"), true);
});

test("hints with non-word edges and regex metacharacters", () => {
  assert.equal(hintUsed("split()", "words = line.split()"), true);
  assert.equal(hintUsed("split()", "words = line.split(',')"), false);
  assert.equal(hintUsed("sorted(key=)", "sorted(key=)"), true);
  assert.equal(hintUsed("Promise.all", "await Promise.all(ps)"), true);
  assert.equal(hintUsed("Promise.all", "await PromiseXall(ps)"), false);
  assert.equal(hintUsed("String.join", 'String.join("_", parts)'), true);
  assert.equal(hintUsed("один проход", "# один проход"), true);
});
