// Редактор CodeMirror 5 (глобальный, со скриптов CDN в index.html) и подсказки-чипы.
const esc = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const MODES = { python: "python", ts: "text/typescript", java: "text/x-java", sql: "text/x-pgsql" };
const store = {
  get(k, d) { try { return JSON.parse(localStorage[k]) ?? d; } catch { return d; } },
  set(k, v) { try { localStorage[k] = JSON.stringify(v); } catch {} },
};

export function createEditor(el, { value, lang, readOnly = false, onRun, onSave }) {
  const ts = lang === "ts";
  const mod = /Mac/.test(navigator.platform) ? "Cmd" : "Ctrl";
  return CodeMirror(el, {
    value, mode: MODES[lang], readOnly,
    lineNumbers: true, indentUnit: ts ? 2 : 4, tabSize: ts ? 2 : 4, indentWithTabs: false,
    matchBrackets: true, autoCloseBrackets: !readOnly,
    extraKeys: readOnly ? {} : {
      Tab: cm => cm.somethingSelected() ? cm.indentSelection("add") : cm.replaceSelection(" ".repeat(cm.getOption("indentUnit"))),
      "Shift-Tab": cm => cm.indentSelection("subtract"),
      ...(onRun && { [`${mod}-Enter`]: onRun }),
      ...(onSave && { [`${mod}-S`]: onSave }),
    },
  });
}

// Подсказки: ключевые слова из task.json. Ничего не проверяют и не обязательны —
// клик вставляет слово в редактор, × убирает подсказку, уже использованные помечены ✓.
export function renderHints(el, editor, task, label = "Подсказка:") {
  const key = "hints-hidden:" + task.id, hidden = store.get(key, []);
  const shown = task.hints.filter(h => !hidden.includes(h));
  const code = editor.getValue();
  const used = h => new RegExp(`\\b${h.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/\s+/g, "\\s+")}\\b`, "i").test(code);
  el.innerHTML = (shown.length ? `<span class="muted">${esc(label)}</span>` : "") +
    shown.map(h => `<span class="chip ${used(h) ? "used" : ""}"><button data-h="${esc(h)}" title="Вставить в редактор">${esc(h)}</button><button class="x" data-x="${esc(h)}" title="Убрать подсказку">×</button></span>`).join("") +
    (hidden.length && task.hints.length ? `<button class="reset">вернуть подсказки (${hidden.length})</button>` : "");
  el.onclick = e => {
    const b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.h) {
      const { line, ch } = editor.getCursor(), before = editor.getLine(line).slice(0, ch);
      editor.replaceSelection((before && !/\s$/.test(before) ? " " : "") + b.dataset.h + " ");
      editor.focus();
    } else if (b.dataset.x) {
      store.set(key, [...hidden, b.dataset.x]); renderHints(el, editor, task, label);
    } else {
      store.set(key, []); renderHints(el, editor, task, label);
    }
  };
}
