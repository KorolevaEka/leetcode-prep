// ER-схема и данные для SQL-задач: читаем каталог Postgres после schema.sql, рисуем карточки и связи.
const esc = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

export async function loadSchema(t, db) {
  try { await db.exec("ROLLBACK"); } catch {}
  await db.exec(t.schema);
  const cols = (await db.query(`
    SELECT cl.relname AS tbl, a.attname AS col, format_type(a.atttypid, a.atttypmod) AS typ
    FROM pg_attribute a JOIN pg_class cl ON cl.oid = a.attrelid JOIN pg_namespace n ON n.oid = cl.relnamespace
    WHERE n.nspname = 't' AND cl.relkind = 'r' AND a.attnum > 0 AND NOT a.attisdropped
    ORDER BY cl.oid, a.attnum`)).rows;
  const keys = (await db.query(`
    SELECT con.contype AS kind, cl.relname AS tbl, a.attname AS col, fcl.relname AS ftbl, fa.attname AS fcol
    FROM pg_constraint con
    JOIN pg_class cl ON cl.oid = con.conrelid
    JOIN pg_namespace n ON n.oid = cl.relnamespace AND n.nspname = 't'
    CROSS JOIN LATERAL unnest(con.conkey) WITH ORDINALITY AS k(attnum, i)
    JOIN pg_attribute a ON a.attrelid = con.conrelid AND a.attnum = k.attnum
    LEFT JOIN pg_class fcl ON fcl.oid = con.confrelid
    LEFT JOIN pg_attribute fa ON fa.attrelid = con.confrelid AND fa.attnum = con.confkey[k.i]
    WHERE con.contype IN ('p', 'f')`)).rows;

  const tables = {};
  for (const c of cols) (tables[c.tbl] ??= { name: c.tbl, cols: [] }).cols.push({ name: c.col, type: c.typ });
  const pk = new Set(keys.filter(k => k.kind === "p").map(k => `${k.tbl}.${k.col}`));
  const links = keys.filter(k => k.kind === "f")
    .map(k => ({ from: `${k.tbl}.${k.col}`, to: `${k.ftbl}.${k.fcol}`, real: true }));

  // В учебных схемах внешних ключей обычно не объявляют (и данные им не всегда соответствуют),
  // поэтому дорисовываем пунктиром связи по имени: person_id -> person / persons / people.
  // ponytail: эвристика по именам, для нестандартных имён объявляй REFERENCES в schema.sql
  const linked = new Set(links.map(l => l.from));
  for (const tb of Object.values(tables)) {
    for (const c of tb.cols) {
      const from = `${tb.name}.${c.name}`, m = c.name.match(/^(.+)_id$/);
      if (!m || linked.has(from)) continue;
      const base = m[1];
      const target = Object.values(tables).find(o => o.name !== tb.name &&
        [base, base + "s", base + "es", base.replace(/y$/, "ies"), base === "person" ? "people" : ""].includes(o.name));
      if (!target) continue;
      if (pk.has(from) && tb.cols.filter(x => pk.has(`${tb.name}.${x.name}`)).length === 1) continue; // свой PK
      const tcol = target.cols.find(x => pk.has(`${target.name}.${x.name}`))
        ?? target.cols.find(x => x.name === c.name || x.name === "id");
      if (tcol) links.push({ from, to: `${target.name}.${tcol.name}`, real: false });
    }
  }

  const data = {};
  for (const name of Object.keys(tables)) {
    const r = await db.query(`SELECT * FROM t."${name.replace(/"/g, '""')}" LIMIT 50`, [], { rowMode: "array" });
    data[name] = { fields: r.fields.map(f => f.name), rows: r.rows };
  }
  return { tables: Object.values(tables), pk, links, data };
}

export function renderSchema(el, { tables, pk, links, data }) {
  const fks = new Set(links.map(l => l.from));
  const card = tb => `<div class="tbl"><div class="tname">${esc(tb.name)}</div>${tb.cols.map(c => {
    const id = `${tb.name}.${c.name}`, isPk = pk.has(id), isFk = fks.has(id);
    const key = isPk && isFk ? '<span class="key pk">PK·FK</span>' : isPk ? '<span class="key pk">PK</span>'
      : isFk ? '<span class="key fk">FK</span>' : '<span class="key"></span>';
    return `<div class="col" data-c="${esc(id)}">${key}<span>${esc(c.name)}</span><span class="typ">${esc(c.type)}</span></div>`;
  }).join("")}</div>`;
  const dataTable = name => {
    const d = data[name];
    return `<details class="data" open><summary>${esc(name)} <span class="muted">(${d.rows.length} строк)</span></summary>
      <div class="scroll"><table><tr>${d.fields.map(f => `<th>${esc(f)}</th>`).join("")}</tr>${d.rows.map(r =>
        `<tr>${r.map(v => v === null ? '<td class="null">NULL</td>' : `<td>${esc(String(v))}</td>`).join("")}</tr>`).join("")}</table></div></details>`;
  };
  el.innerHTML = `
    <h2>Схема</h2>
    <div class="er"><svg></svg>${tables.map(card).join("")}</div>
    <div class="legend muted">
      <span><svg width="28" height="8"><line x1="0" y1="4" x2="28" y2="4" style="stroke:var(--accent);stroke-width:1.5"/></svg>внешний ключ</span>
      <span><svg width="28" height="8"><line x1="0" y1="4" x2="28" y2="4" style="stroke:var(--muted);stroke-width:1.5;stroke-dasharray:5 4"/></svg>связь по имени колонки (не объявлена)</span>
      <span>● — сторона первичного ключа</span>
    </div>
    <h2>Данные</h2>${tables.map(tb => dataTable(tb.name)).join("")}`;
  const er = el.querySelector(".er");
  const draw = () => {
    const box = er.getBoundingClientRect(), svg = er.querySelector("svg");
    svg.setAttribute("width", box.width); svg.setAttribute("height", box.height);
    svg.innerHTML = links.map(l => {
      const a = er.querySelector(`[data-c="${CSS.escape(l.from)}"]`)?.getBoundingClientRect();
      const b = er.querySelector(`[data-c="${CSS.escape(l.to)}"]`)?.getBoundingClientRect();
      if (!a || !b) return "";
      const ay = a.top + a.height / 2 - box.top, by = b.top + b.height / 2 - box.top;
      const acx = a.left + a.width / 2, bcx = b.left + b.width / 2;
      let ax, bx, c1, c2;
      if (Math.abs(acx - bcx) < 60) {          // карточки друг под другом (или ссылка на себя): дуга справа
        ax = a.right - box.left; bx = b.right - box.left;
        const d = 36; c1 = ax + d; c2 = bx + d;
      } else if (bcx > acx) {                 // цель правее
        ax = a.right - box.left; bx = b.left - box.left;
        const d = Math.max(30, (bx - ax) / 2); c1 = ax + d; c2 = bx - d;
      } else {                                // цель левее
        ax = a.left - box.left; bx = b.right - box.left;
        const d = Math.max(30, (ax - bx) / 2); c1 = ax - d; c2 = bx + d;
      }
      const cls = l.real ? "" : "guess";
      return `<path class="${cls}" d="M${ax},${ay} C${c1},${ay} ${c2},${by} ${bx},${by}"/>
              <circle class="${cls}" cx="${bx}" cy="${by}" r="3.5"/>`;
    }).join("");
  };
  draw();
  new ResizeObserver(draw).observe(er);
}
