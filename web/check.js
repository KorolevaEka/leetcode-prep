// Общая проверка решений: одинаково работает в браузере и в CI (Node).
// execute(task, subject, tests) -> { passed, output, noTests? } — по одному на язык.

export function truncate(text, limit = 20000) {
  return text.length > limit ? text.slice(0, limit) + "\n…вывод обрезан" : text;
}

export async function check(task, code, execute) {
  if (task.kind !== "tests") {
    const r = await execute(task, code, task.tests);
    return { ok: r.passed, output: truncate(r.output) };
  }
  const base = await execute(task, task.subject, code);
  if (base.noTests) return { ok: false, output: "Нет ни одного теста: напиши хотя бы один." };
  if (!base.passed) {
    return { ok: false, output: truncate("Твои тесты падают на правильной реализации:\n\n" + base.output) };
  }
  const missed = [];
  for (const m of task.mutants) {
    const r = await execute(task, m.code, code);
    if (r.passed) missed.push(m.description);
  }
  const total = task.mutants.length;
  const caught = { total, missed };
  if (!missed.length) return { ok: true, output: `Тесты проходят на правильной реализации и ловят все ${total} сломанных версий.`, caught };
  return {
    ok: false, caught,
    output: `Поймано ${total - missed.length} из ${total} сломанных версий. Тесты не заметили:\n` + missed.map(d => `- ${d}`).join("\n"),
  };
}

export async function verifyTask(task, reference, mutants, execute) {
  const problems = [];
  const [subjectOf, testsOf] = task.kind === "tests"
    ? [() => task.subject, () => reference]
    : [() => reference, () => task.tests];
  const ref = await execute(task, subjectOf(), testsOf());
  if (!ref.passed) problems.push("эталон не проходит: " + ref.output);
  for (const m of mutants) {
    const r = task.kind === "tests" ? await execute(task, m.code, reference) : await execute(task, m.code, task.tests);
    if (r.passed) problems.push(`мутант ${m.name} не пойман`);
  }
  return problems;
}
