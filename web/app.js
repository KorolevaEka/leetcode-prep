import { check } from "./check.js";
import * as python from "./runners/python.js";
import * as sql from "./runners/sql.js";
import * as ts from "./runners/ts.js";
import * as java from "./runners/java.js";
import { createEditor, renderHints } from "./editor.js";
import { loadSchema, renderSchema } from "./schema.js";
import { parseRoute, cleanAuthParams } from "./router.js";
import { createProgress } from "./progress.js";
import { createSupabase } from "./config.js";
import { taskState } from "./unlock.js";
import { LANGS, LEVELS, blocker, catalog, langCounts, nextTask } from "./catalog.js";

const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const md = s => window.marked ? marked.parse(s) : `<pre>${esc(s)}</pre>`;
const LANG_NAME = Object.fromEntries(LANGS);
const isLang = l => Object.hasOwn(LANG_NAME, l);
const LEVEL_NAME = Object.fromEntries(LEVELS);
const FILE = {
  code: { python: "solution.py", ts: "solution.ts", java: "Solution.java", sql: "solution.sql" },
  tests: { python: "test_solution.py", ts: "solution.test.ts", java: "SolutionTest.java" },
};
const IDLE = "Вывод тестов появится здесь";
const WAITING = "Идёт предыдущий запуск — кнопка включится, когда он закончится.";
const SAVE_TEXT = { saved: "сохранено", saving: "сохраняю…", error: "не сохранено" };

let tasks = [], topics = {}, supabase = null, progress = null, authNote = "", authDone = false;
let view = null;      // открытая страница задачи: { task, editor }
let running = null;   // исполнители рассчитаны на один запуск за раз — следующий ждёт
let lastLang = "python", headerLang = null;

const withTimeout = (p, ms) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), ms))]);

// ---------- Исполнители ----------
let sqlLoading = null, sqlLoaded = false, sqlQueue = Promise.resolve();
const PGLITE_URL = "https://cdn.jsdelivr.net/npm/@electric-sql/pglite@0.2.17/dist/index.js";
// лениво, один раз; при сбое сбрасываем, чтобы повторный запуск мог сработать
const sqlReady = () => sqlLoading ??= import(PGLITE_URL).then(m => { sql.init(m.PGlite); return sql.db(); })
  .then(() => { sqlLoaded = true; })
  .catch(e => { sqlLoading = null; throw e; });
// одна база на схему и запуски: операции по очереди, иначе schema.sql соседней задачи влезет посреди запуска
const sqlSerial = fn => { const p = sqlQueue.then(fn); sqlQueue = p.catch(() => {}); return p; };
const executors = {
  python: python.execute,
  ts: ts.execute,
  java: java.execute,
  sql: (...args) => sqlSerial(async () => { await sqlReady(); return sql.execute(...args); }),
};
const loadingText = lang =>
  lang === "python" && !python.isReady() ? "Загружаю Python в браузер (первый раз ~10 сек)…"
  : lang === "ts" && !ts.isReady() ? "Загружаю TypeScript в браузер (первый раз ~10 сек)…"
  : lang === "java" && !java.isReady() ? "Загружаю Java в браузер (первый раз до минуты)…"
  : lang === "sql" && !sqlLoaded ? "Загружаю Postgres в браузер (первый раз ~10 сек)…" : "Запускаю…";

// ---------- Шапка ----------
function renderHeader(lang = headerLang) {
  headerLang = lang;
  const counts = langCounts(tasks, progress.solvedIds());
  const user = progress.user();
  $("tabs").innerHTML = LANGS.map(([id, name]) =>
    `<a href="#/learn/${id}" class="${id === lang ? "active" : ""}">${name}<span class="count">${counts[id].solved}/${counts[id].total}</span></a>`).join("");
  $("auth").innerHTML = (authNote ? `<span class="note">${esc(authNote)}</span>` : "") + (user
    ? `<span class="login">@${esc(user.login)}</span><button class="btn small" id="signout">Выйти</button>`
    : `<span class="guest">Гость — прогресс не сохраняется</span><button class="btn small primary" data-signin>Войти через GitHub</button>`);
  $("signout")?.addEventListener("click", signOut);
}

async function signIn() {
  if (!supabase) {
    authNote = authDone ? "Вход недоступен: не удалось загрузить Supabase. Проверь сеть и обнови страницу." : "Вход ещё загружается — попробуй через секунду.";
    return renderHeader();
  }
  try { await progress.signIn(); }
  catch (e) { authNote = "Не удалось начать вход: " + (e?.message || e); renderHeader(); }
}

async function signOut() {
  try { await progress.signOut(); } catch {}
  authNote = "";
  render();
}

document.addEventListener("click", e => { if (e.target.closest("[data-signin]")) signIn(); });

// ---------- Лендинг ----------
function renderLanding() {
  const user = progress.user();
  $("main").innerHTML = `
    <section class="landing">
      <h1>Live Coding Trainings</h1>
      <p class="lead">Бесплатный тренажёр перед live coding — для QA automation и разработчиков.
        Решай короткие задачи и пиши тесты прямо в браузере.</p>
      <ul class="features">
        <li><b>4 языка</b> — Python, SQL, TypeScript, Java.</li>
        <li><b>Темы и уровни</b> — Easy, Medium, Hard; следующая задача уровня открывается, когда решена предыдущая.</li>
        <li><b>«Напиши тесты»</b> — твои тесты проверяются на мутантах: сломанных версиях кода, которые они должны поймать.</li>
        <li><b>Подсказки</b> — ключевые слова, если не знаешь, с чего начать.</li>
        <li><b>Запуск в браузере</b> — ничего не нужно устанавливать.</li>
        <li><b>Прогресс на ноутбуке и телефоне</b> — после входа через GitHub.</li>
      </ul>
      <div class="actions">${user
        ? `<a class="btn primary" href="#/learn/${lastLang}">Продолжить</a>`
        : `<button class="btn primary" data-signin>Войти через GitHub</button><button class="btn" id="guest">Начать без входа</button>`}
      </div>
      <dialog id="guest-dlg">
        <p>Без входа прогресс не сохранится: после перезагрузки страницы решённые задачи и счётчик обнулятся.</p>
        <form method="dialog" class="actions"><button class="btn primary" value="ok">Начать</button><button class="btn" value="cancel">Отмена</button></form>
      </dialog>
    </section>`;
  const dlg = $("guest-dlg");
  $("guest")?.addEventListener("click", () => { dlg.returnValue = ""; dlg.showModal(); });
  dlg.addEventListener("close", () => { if (dlg.returnValue === "ok") location.hash = `#/learn/${lastLang}`; });
}

// ---------- Каталог ----------
const STATE = { solved: ["✓", "решена"], open: ["○", "открыта"], locked: ["🔒", "закрыта"] };
const taskItem = ({ task, state }) => `
  <li class="${state}"><a href="#/task/${task.id}">
    <span class="mark" title="${STATE[state][1]}" aria-label="${STATE[state][1]}">${STATE[state][0]}</span>
    <span class="name">${esc(task.title)}${state === "locked" ? '<span class="lock-note">Сначала реши предыдущую задачу этого уровня</span>' : ""}</span>
    ${task.kind === "tests" ? '<span class="badge tests">тесты</span>' : ""}
    <span class="badge ${task.level}">${LEVEL_NAME[task.level]}</span>
  </a></li>`;

function renderCatalog(route) {
  const lang = route.lang;
  const cards = catalog(tasks, topics, progress.solvedIds(), route);
  const opt = (value, label, current) => `<option value="${esc(value)}" ${value === (current ?? "") ? "selected" : ""}>${esc(label)}</option>`;
  $("main").innerHTML = `
    <section class="catalog">
      <div class="filters">
        <h1>${LANG_NAME[lang]}</h1>
        <label>Тема <select id="f-topic">${opt("", "Все", route.topic)}${(topics[lang] || []).map(tp => opt(tp.id, tp.title, route.topic)).join("")}</select></label>
        <label>Сложность <select id="f-level">${opt("", "Все", route.level)}${LEVELS.map(([id, name]) => opt(id, name, route.level)).join("")}</select></label>
      </div>
      ${cards.length ? cards.map(c => `
        <article class="topic">
          <header><h2>${esc(c.topic.title)}</h2><span class="muted">решено ${c.solved} из ${c.items.length}</span></header>
          <p class="muted">${esc(c.topic.description || "")}</p>
          ${c.items.length ? `<ul class="tasks">${c.items.map(taskItem).join("")}</ul>` : '<p class="muted">Задачи скоро появятся.</p>'}
        </article>`).join("") : '<p class="empty">Нет задач с такими фильтрами.</p>'}
    </section>`;
  const apply = () => {
    const q = new URLSearchParams();
    if ($("f-topic").value) q.set("topic", $("f-topic").value);
    if ($("f-level").value) q.set("level", $("f-level").value);
    location.hash = `#/learn/${lang}${String(q) ? "?" + q : ""}`;
  };
  $("f-topic").onchange = $("f-level").onchange = apply;
}

// ---------- Задача ----------
function renderTask(id) {
  const t = tasks.find(x => x.id === id);
  const main = $("main");
  if (!t) {
    main.innerHTML = `<p class="empty">Такой задачи нет. <a href="#/learn/${lastLang}">К каталогу</a></p>`;
    return;
  }
  const solved = progress.solvedIds();
  const topic = (topics[t.lang] || []).find(tp => tp.id === t.topic);
  const back = `<a class="back" href="#/learn/${t.lang}?topic=${t.topic}">← ${esc(topic?.title || t.topic)}</a>`;
  if (taskState(t, tasks, solved) === "locked") {
    const b = blocker(t, tasks, solved);
    main.innerHTML = `<section class="stub">${back}<h1>🔒 ${esc(t.title)}</h1>
      <p>Сначала реши предыдущую задачу этого уровня${b ? `: <a href="#/task/${b.id}">${esc(b.title)}</a>` : ""}.</p></section>`;
    return;
  }
  const tests = t.kind === "tests";
  main.innerHTML = `
    <div class="task">
      <section class="readme">
        ${back}
        <div class="badges"><span class="badge ${t.level}">${LEVEL_NAME[t.level]}</span>${tests ? '<span class="badge tests">тесты</span>' : ""}</div>
        ${md(t.readme)}<div id="schema"></div>
      </section>
      <section class="work">
        ${tests ? `<div class="subject"><div class="bar"><span class="file">Тестируемый код · ${FILE.code[t.lang]}</span></div><div class="editor ro" id="subject"></div></div>` : ""}
        <div class="bar">
          <span class="file">${FILE[t.kind][t.lang]}</span>
          <span class="save muted" id="save"></span>
          <a class="btn" id="next" hidden></a>
          <button class="btn primary" id="run">Запустить ⌘↵</button>
        </div>
        <div class="hints" id="hints"></div>
        <div class="editor" id="editor"></div>
        <pre class="out" id="out">${running ? WAITING : IDLE}</pre>
      </section>
    </div>`;
  if (tests) createEditor($("subject"), { value: t.subject, lang: t.lang, readOnly: true });
  const editor = createEditor($("editor"), {
    value: progress.getDraft(t.id) ?? t.starter, lang: t.lang,
    onRun: run, onSave: cm => progress.saveDraft(t.id, cm.getValue()),
  });
  const v = view = { task: t, editor };
  const hints = () => renderHints($("hints"), editor, t, "Подсказки — необязательно использовать все, это только наводка:");
  editor.on("change", () => { progress.saveDraft(t.id, editor.getValue()); hints(); updateSave(); });
  hints();
  if (!matchMedia("(pointer: coarse)").matches) editor.focus();
  $("run").onclick = run;
  $("run").disabled = !!running;
  if (solved.has(t.id)) showNext(v);
  updateSave();
  if (t.lang === "python") return python.warmup(); // начинаем грузить рантайм заранее
  if (t.lang === "ts") return ts.warmup();
  if (t.lang === "java") return java.warmup();
  const el = $("schema");
  el.innerHTML = '<h2>Схема</h2><p class="muted">Загружаю Postgres в браузер…</p>';
  sqlSerial(async () => { await sqlReady(); return loadSchema(t, await sql.db()); })
    .then(s => view === v && renderSchema(el, s))
    .catch(e => { if (view === v) el.innerHTML = `<h2>Схема</h2><pre>${esc(e?.message || e)}</pre>`; });
}

function updateSave() {
  const el = $("save");
  if (el) el.textContent = view && progress.user() ? SAVE_TEXT[progress.saveState()] : "";
}

function showNext(v) {
  const a = $("next"), n = nextTask(v.task, tasks, progress.solvedIds());
  a.href = n ? `#/task/${n.id}` : `#/learn/${v.task.lang}?topic=${v.task.topic}`;
  a.textContent = n ? "Следующая задача →" : "Все задачи темы решены → к каталогу";
  a.hidden = false;
}

function showResult(r) {
  const out = $("out");
  out.className = "out " + (r.ok ? "ok" : "err");
  if (!r.caught) { out.textContent = r.output; return; }
  const { total, missed } = r.caught;
  out.textContent = `Поймано ${total - missed.length} из ${total} багов` + (missed.length
    ? ". Тесты не заметили:\n" + missed.map(d => `- ${d}`).join("\n")
    : ". Тесты проходят на правильной реализации и ловят все сломанные версии.");
}

async function run() {
  const v = view;
  if (!v || running) return;
  const t = v.task, code = v.editor.getValue();
  progress.saveDraft(t.id, code); // заодно повтор сохранения, если прошлое не удалось
  $("run").disabled = true;
  $("out").className = "out";
  $("out").textContent = loadingText(t.lang);
  running = check(t, code, executors[t.lang])
    .catch(e => ({ ok: false, output: "Не удалось выполнить: " + (e?.message || e) }));
  const r = await running;
  running = null;
  if (r.ok) {
    try { await progress.markSolved(t.id, code); } catch {}
    renderHeader();
  }
  if ($("run")) $("run").disabled = false;
  if (view !== v) {
    if ($("out")?.textContent === WAITING) $("out").textContent = IDLE;
    return;
  }
  showResult(r);
  if (matchMedia("(max-width: 900px)").matches) $("out").scrollIntoView({ block: "nearest" });
  if (r.ok) showNext(v);
  updateSave();
}

// ---------- Роутинг ----------
function render() {
  const route = parseRoute(location.hash);
  if (route.page === "catalog" && !isLang(route.lang)) return location.replace("#/learn/python");
  const lang = route.page === "catalog" ? route.lang : route.page === "task" ? route.id.split("/")[0] : null;
  if (isLang(lang)) lastLang = lang;
  view = null;
  document.body.classList.toggle("fit", route.page === "task");
  renderHeader(lang);
  if (route.page === "landing") renderLanding();
  else if (route.page === "catalog") renderCatalog(route);
  else renderTask(route.id);
  scrollTo(0, 0);
}

async function authenticate(authError) {
  try { supabase = await withTimeout(createSupabase(), 15000); } catch { supabase = null; }
  let next = progress;
  if (supabase) {
    // сетевой сбой не блокирует сайт: работаем как гость и говорим об этом
    next = createProgress({ supabase });
    try {
      await withTimeout(next.init(), 15000);
      // ошибка select приходит как {error}, не исключение: иначе первая же правка затёрла бы серверный черновик
      if (next.user() && next.saveState() === "error") throw new Error("progress load failed");
    } catch {
      next = createProgress({ supabase });
      authNote = "не удалось загрузить прогресс";
    }
  }
  if (authError) authNote = "Вход не удался: " + authError;
  const clean = cleanAuthParams(location.href); // после init: Supabase сначала обменивает ?code= на сессию
  if (clean) history.replaceState(null, "", clean);
  authDone = true;
  const changed = next.user() || next.solvedIds().size || authNote;
  progress = next;
  if (changed) render();
}

async function boot() {
  $("main").innerHTML = '<p class="empty">Загружаю…</p>';
  const data = Promise.all(["tasks.json", "topics.json"].map(f => fetch(f, { cache: "no-store" }).then(r => {
    if (!r.ok) throw new Error(`${f}: ${r.status}`);
    return r.json();
  })));
  const authError = new URL(location.href).searchParams.get("error_description");
  progress = createProgress({ supabase: null }); // гость в памяти: сайт рисуется сразу, вход подтянется следом
  try { [tasks, topics] = await data; }
  catch (e) { $("main").innerHTML = `<p class="empty">Не удалось загрузить задачи: ${esc(e.message)}. Обнови страницу.</p>`; return; }
  addEventListener("hashchange", render);
  const flushNow = () => progress.flush().catch(() => {});
  addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flushNow(); });
  addEventListener("pagehide", flushNow);
  setInterval(updateSave, 500);
  render();
  await authenticate(authError);
}

boot();
