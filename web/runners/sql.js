// SQL на PGlite (Postgres в WASM). Класс PGlite передаём снаружи: в браузере с CDN, в Node из npm.
let PGliteClass = null, pg = null;

export function init(PGlite) { PGliteClass = PGlite; }

// значения отдаём текстом, как psql --csv: 1.50, t/f, 2024-01-01
const OIDS = [16, 20, 21, 23, 26, 114, 700, 701, 1082, 1083, 1114, 1184, 1186, 1700, 3802];

export function db() {
  pg ??= (async () => {
    const d = new PGliteClass({ parsers: Object.fromEntries(OIDS.map(o => [o, v => v])) });
    await d.waitReady;
    return d;
  })();
  return pg;
}

function parseCsv(text) {
  const rows = []; let row = [], cell = "", q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"' && text[i + 1] === '"') { cell += '"'; i++; } else if (c === '"') q = false; else cell += c; }
    else if (c === '"') q = true;
    else if (c === ",") { row.push(cell); cell = ""; }
    else if (c === "\n") { row.push(cell); rows.push(row); row = []; cell = ""; }
    else if (c !== "\r") cell += c;
  }
  if (cell || row.length) { row.push(cell); rows.push(row); }
  return rows;
}
const toCsv = rows => rows.map(r => r.map(v => /[",\n]/.test(v) ? `"${v.replace(/"/g, '""')}"` : v).join(",")).join("\n");

export async function execute(task, code) {
  try {
    const d = await db();
    await d.exec(task.schema);
    const results = await d.exec(code, { rowMode: "array" });
    const last = [...results].reverse().find(r => r.fields.length);
    if (!last) return { passed: false, output: "Запрос ничего не вернул" };
    const actual = [last.fields.map(f => f.name), ...last.rows.map(r => r.map(v => v === null ? "" : String(v)))];
    const expected = parseCsv(task.expected.trim());
    // порядок строк не важен (кроме заголовка); для задач с ORDER BY — смотреть глазами
    const norm = rows => [JSON.stringify(rows[0]), ...rows.slice(1).map(r => JSON.stringify(r)).sort()].join("\n");
    if (norm(actual) === norm(expected)) return { passed: true, output: "OK\n\n" + toCsv(actual) };
    return { passed: false, output: `--- expected\n${toCsv(expected)}\n\n--- actual\n${toCsv(actual)}` };
  } catch (e) {
    return { passed: false, output: String(e.message || e) };
  }
}
