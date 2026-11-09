# Live Coding Trainings — план реализации

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Превратить личный тренажёр `leetcode-prep` в открытый сайт Live Coding Trainings: лендинг, 4 языка (Python, SQL, TypeScript, Java),
темы × уровни с цепочками, задачи «напиши код» и «напиши тесты» (мутанты), подсказки, вход через GitHub с синхронизацией прогресса,
~100 задач в первом релизе.

**Architecture:** Статика на GitHub Pages, весь код пользователя выполняется в браузере (Pyodide, PGlite, TypeScript-компилятор
в воркере, CheerpJ). Для каждого языка — один «исполнитель» `execute(task, subject, tests) → {passed, output}`; общая логика
проверки `check()` (код против тестов, тесты против эталона и мутантов) одна и та же в браузере и в CI. Прогресс — Supabase
(вход через GitHub), у гостя — только в памяти. CI (`scripts/verify.mjs`) проверяет каждую задачу эталоном и мутантами до деплоя.

**Tech Stack:** HTML/CSS/vanilla ES-модули без сборщика; CodeMirror 5.65.16, marked 12.0.2, Pyodide 0.27.2, PGlite 0.2.17,
TypeScript 5.6.3, CheerpJ 5.0 (Java 21), @supabase/supabase-js 2.45.4 — всё с CDN. CI: GitHub Actions (Python 3.12 + pytest,
Node 20, Temurin JDK 21). Тесты платформы: `node --test` и pytest.

**Spec:** `docs/superpowers/specs/2026-11-09-live-coding-trainings-design.md`

## Global Constraints

- Название сайта — **Live Coding Trainings**; слово «LeetCode» нигде в брендинге и интерфейсе.
- Интерфейс и условия — только на русском.
- Условия задач — своими словами и со своими примерами, без дословных текстов LeetCode; без данных TaxDome.
- Только бесплатные тарифы: GitHub Pages, GitHub Actions, Supabase Free, CheerpJ Community. Если выбор есть — более простой вариант.
- CheerpJ грузится только с `https://cjrtnc.leaningtech.com/5.0/loader.js` (не самохостить); на сайте видимый кредит «Built with CheerpJ» со ссылкой на https://cheerpj.com.
- В коде сайта из Supabase только URL `https://gmcueqiqqgtvaedwrilm.supabase.co` и publishable-ключ `sb_publishable_VRmuzMkRX8rmUU0K1OcRqw_9bD3qeHU`.
- Библиотеки — с CDN (cdnjs / jsdelivr), с пинованной версией из Tech Stack.
- Лицензия MIT на весь репозиторий, автор — Kate Koroleva (KorolevaEka).
- Публикация сразу: пушим в `main` по готовности задачи плана, сайт рабочий после каждого пуша; CI-проверка задач гейтит деплой.
- Новый адрес сайта: `https://korolevaeka.github.io/live-coding-trainings/`.
- Таймаут выполнения пользовательского кода — 10 с после загрузки рантайма; на первую загрузку рантайма — 120 с (Java — 180 с).
- Вывод теста обрезается до 20 000 символов с пометкой «…вывод обрезан».

## Review Focus

1. **Задача «напиши тесты» с пустым файлом или без единого теста** — пустой набор тестов «падает» на мутантах по ошибке (pytest exit 5 и т.п.); ожидание: «Нет ни одного теста», задача не решена. Тест — в Task 3 (`check.test.mjs`).
2. **Тесты пользователя падают на правильной реализации** — ожидание: «Твои тесты падают на правильной реализации», мутанты не считаются. Тест — Task 3.
3. **Возврат с GitHub OAuth** — параметры в URL ломают hash-роутер или сессия не подхватывается; ожидание: `flowType: 'pkce'` (`?code=` в query, не в hash), после входа URL чистый, пользователь на той же странице, гостевой прогресс перенесён. Тест — Task 7 (`router.test.mjs`) + ручная проверка в Task 12.
4. **Бесконечный цикл / огромный вывод в TS и Java** — вкладка не виснет, через 10 с «Таймаут…», следующий запуск работает; вывод обрезан. Тесты — Tasks 4, 5.
5. **Сбой сети при сохранении черновика** — ожидание: черновик не теряется, индикатор «не сохранено», повтор при следующем изменении/запуске. Тест — Task 7 (`progress.test.mjs`).

---

## Файловая структура (итог)

```
LICENSE                         MIT
package.json                    devDeps для CI/локальной проверки: typescript@5.6.3, @electric-sql/pglite@0.2.17
topics.json                     порядок и названия тем по языкам
tasks/<lang>/<topic>/<NN>-<slug>/   одна задача (формат ниже)
web/                            всё, что уходит на сайт (кроме tasks.json)
  index.html                    оболочка: лендинг + приложение
  style.css
  config.js                     SUPABASE_URL, SUPABASE_KEY
  app.js                        роутер, рендер лендинга / каталога / задачи
  router.js                     parseRoute / cleanAuthParams (чистые функции)
  unlock.js                     правило цепочки (чистая функция)
  progress.js                   хранилище прогресса: гость / Supabase
  check.js                      check() и verifyTask() — общие для браузера и CI
  editor.js                     CodeMirror + подсказки (перенос из index.html)
  schema.js                     ER-схема SQL (перенос из index.html)
  runners/python.js + python-worker.js
  runners/sql.js                исполнитель SQL на PGlite (браузер и Node)
  runners/ts.js + ts-worker.js + ts-core.js (компиляция+запуск, общий для браузера и Node) + ts-harness.js + ts-harness.d.ts
  runners/java.js + java/       Java-харнесс: org/junit/jupiter/api/{Test,Assertions,function/Executable}.java, TestRunner.java
scripts/build.py                собирает _site/ (web/* + tasks.json), валидирует метаданные
scripts/serve.py                локальный сервер: web/ + живой tasks.json
scripts/verify.mjs              CI-проверка задач; scripts/executors/{python,sql,ts,java}.mjs — Node-исполнители
tests/                          тесты платформы: test_build.py, *.test.mjs
```

Удаляются: `check.py`, `server.py`, `build.py`, `index.html`, `py-worker.js` (корень), `python/`, `sql/` (перенос в `tasks/`), сервис `db` из compose.

## Формат задачи

`tasks/<lang>/<topic>/<NN>-<slug>/` где `<lang>` ∈ `python|sql|ts|java`, `<topic>` — id из `topics.json`, `NN` — порядок внутри темы.

`task.json`:
```json
{
  "title": "Частота слов в логе",
  "level": "easy",                  // easy | medium | hard
  "kind": "code",                   // code | tests  (sql — только code)
  "hints": ["dict", "split()", "sorted(key=)"],
  "mutants": { "off-by-one": "теряет последний элемент", "empty": "падает на пустом вводе" }
}
```
Файлы (`<ext>`: py / sql / ts / java):
- `README.md` — условие (markdown).
- `starter.<ext>` — что пользователь видит в редакторе изначально.
- `reference.<ext>` — эталон редактируемого файла: решение (kind=code) или образцовые тесты (kind=tests). На сайт не отдаётся.
- `tests.<ext>` — только kind=code (кроме sql): тесты задачи.
- `subject.<ext>` — только kind=tests: тестируемый код, показывается read-only.
- `mutants/<name>.<ext>` — сломанные версии: решения (kind=code) или `subject` (kind=tests). Имена = ключи `task.json.mutants`. Минимум 2.
- sql: `schema.sql`, `expected.csv` (как сейчас); тестов нет — проверка сравнением результата.

Имена модулей при выполнении (одинаково для обоих видов):
| lang | subject | tests |
|------|---------|-------|
| python | `solution.py` | `test_solution.py` (`from solution import …`) |
| ts | `solution.ts` | `solution.test.ts` (`import { … } from "./solution"`) |
| java | `Solution.java` (`public class Solution`) | `SolutionTest.java` (JUnit 5: `import org.junit.jupiter.api.Test; import static org.junit.jupiter.api.Assertions.*;`) |

Запись в `tasks.json` (то, что получает браузер):
`{ id, lang, topic, order, level, kind, title, readme, hints, starter, tests?, subject?, schema?, expected?, mutants? }`,
где `id = "<lang>/<topic>/<NN>-<slug>"`, `mutants` (массив `{name, description, code}`) — **только у kind=tests**.

`topics.json`: `{ "python": [{ "id": "strings", "title": "Строки", "description": "…" }, …], "sql": [...], "ts": [...], "java": [...] }`.

---

### Task 1: Спайк — Java в браузере через CheerpJ

Одноразовый прототип; результат — решение и рабочий сниппет, не продакшен-код.

**Files:**
- Create: `spikes/java/index.html` (удаляется в Task 5), `docs/superpowers/notes/java-spike.md`

**Interfaces:**
- Produces: в `java-spike.md` — какой компилятор работает (javac из рантайма CheerpJ или ECJ 3.33.0 `https://repo1.maven.org/maven2/org/eclipse/jdt/ecj/3.33.0/ecj-3.33.0.jar`, положенный в репозиторий), точные вызовы `cheerpjInit({version: 21})` / `cheerpjRunMain(...)`, пути `/str/` или `/files/` для исходников и классов, как получить вывод и код выхода, время холодного и тёплого запуска.

- [ ] **Step 1:** Страница грузит `https://cjrtnc.leaningtech.com/5.0/loader.js`, пишет в виртуальную ФС `Solution.java` (`public class Solution { public static int add(int a,int b){return a+b;} }`) и `Main.java` с `System.out.println(Solution.add(2,3)); System.exit(Solution.add(2,3)==5?0:1);`, компилирует javac'ом (`com.sun.tools.javac.Main`), запускает `Main`.
- [ ] **Step 2:** Запустить `python3 -m http.server 8765 -d spikes/java`, открыть `http://localhost:8765` в браузерной панели. Ожидается: в выводе `5`, код выхода 0.
- [ ] **Step 3:** Если javac недоступен — то же с ECJ (`org.eclipse.jdt.internal.compiler.batch.Main`, `-21 -d /files/out`), jar из `web/runners/java/ecj-3.33.0.jar`.
- [ ] **Step 4:** Проверить бесконечный цикл: прервать можно только уничтожением iframe/воркера — записать, как именно это получилось (например, CheerpJ в отдельном `<iframe>`, `iframe.remove()` по таймауту).
- [ ] **Step 5:** Записать результат в `java-spike.md`. **Если ни один вариант не компилирует — остановиться и сообщить Кате** (Java не начинать, остальные задачи плана продолжать без Java).
- [ ] **Step 6:** Commit: `git add spikes docs/superpowers/notes && git commit -m "spike: Java in browser via CheerpJ"`

### Task 2: Переименование, лицензия, новый формат задач и сборка

**Files:**
- Create: `LICENSE`, `topics.json`, `scripts/build.py`, `scripts/serve.py`, `tests/test_build.py`, `web/` (перенос текущего `index.html` → `web/index.html`, `py-worker.js` → `web/runners/python-worker.js`)
- Modify: `.github/workflows/pages.yml`, `docker-compose.yml`, `Dockerfile`, `run`, `.gitignore`
- Delete: `build.py`, `check.py`, `server.py`, `python/`, `sql/` (перенос в `tasks/python/arrays/01-two-sum/`, `tasks/sql/joins/01-combine-two-tables/` в новом формате)

**Interfaces:**
- Produces: `scripts/build.py`: `load_tasks(root: Path) -> list[dict]` (записи `tasks.json`, порядок: язык как в `topics.json`, тема как в `topics.json`, затем `NN`); `build_site(root: Path, out: Path) -> None` (копирует `web/` в `out/`, пишет `out/tasks.json` и `out/topics.json`); при ошибке формата — `TaskFormatError(path, message)`. CLI: `python3 scripts/build.py _site`; `python3 scripts/build.py --json` печатает `load_tasks()` в stdout.
- Produces: `scripts/serve.py` — `http://localhost:8000`, отдаёт файлы `web/`, `/topics.json` и `/tasks.json` = `load_tasks()` на каждый запрос.

- [ ] **Step 1: Переименовать репозиторий** — `gh repo rename live-coding-trainings -R KorolevaEka/leetcode-prep --yes`; `git remote set-url origin https://github.com/KorolevaEka/live-coding-trainings.git`. Проверка: `gh repo view KorolevaEka/live-coding-trainings --json url`.
- [ ] **Step 2: Тесты сборки** в `tests/test_build.py` на фикстурах во временной папке:
  - `test_task_record_fields` — задача python kind=code даёт `id == "python/strings/01-x"`, `order == 1`, `tests` есть, `subject` и `mutants` отсутствуют, `reference` отсутствует.
  - `test_tests_kind_ships_mutants` — kind=tests даёт `subject` и `mutants == [{"name": "empty", "description": "…", "code": "…"}]`.
  - `test_sql_task` — есть `schema`, `expected`, нет `tests`.
  - `test_rejects_unknown_topic`, `test_rejects_bad_level`, `test_rejects_sql_tests_kind`, `test_rejects_less_than_two_mutants`, `test_rejects_mutant_without_description` — `TaskFormatError`.
  - `test_order_follows_topics_json` — две темы, порядок в выдаче как в `topics.json`.
- [ ] **Step 3:** `pytest tests/test_build.py -q` → FAIL (модуля нет).
- [ ] **Step 4:** Реализовать `scripts/build.py`, перенести две задачи в новый формат (по 2 мутанта каждой), `topics.json` с одной темой на эти два языка; `web/index.html` читает новые поля (`starter` вместо `solution`, `files` больше нет) — сайт работает как раньше.
- [ ] **Step 5:** `pytest tests/test_build.py -q` → PASS.
- [ ] **Step 6:** `LICENSE` (MIT, 2026, Kate Koroleva). `pages.yml`: `python3 scripts/build.py _site`. Compose: только сервис `py`, команда `python3 scripts/serve.py`; Dockerfile: + `nodejs npm openjdk-21-jdk-headless`, без `postgresql-client`. `run`: `./run test` (pytest + `node --test tests/`), `./run verify [путь]` (`node scripts/verify.mjs`). `.gitignore`: `_site/`, `node_modules/`.
- [ ] **Step 7:** `docker compose up -d --build`, открыть `http://localhost:8000` — обе задачи открываются и решаются.
- [ ] **Step 8:** Commit + push; дождаться зелёного Pages-деплоя; `https://korolevaeka.github.io/live-coding-trainings/` открывается.

### Task 3: Общая проверка `check.js`, Python- и SQL-исполнители, CI-гейт

**Files:**
- Create: `web/check.js`, `web/runners/python.js`, `web/runners/sql.js`, `scripts/verify.mjs`, `scripts/executors/python.mjs`, `scripts/executors/sql.mjs`, `package.json`, `tests/check.test.mjs`, `tests/sql.test.mjs`
- Modify: `web/runners/python-worker.js` (принимает `{subject, tests}`, пишет `solution.py`/`test_solution.py`), `.github/workflows/pages.yml`

**Interfaces:**
- Consumes: формат записи `tasks.json` из Task 2.
- Produces (`web/check.js`):
  - `type ExecResult = { passed: boolean, output: string, noTests?: boolean }`
  - `type Execute = (task, subject: string, tests: string) => Promise<ExecResult>`
  - `check(task, code: string, execute: Execute) → Promise<{ ok: boolean, output: string, caught?: { total: number, missed: string[] } }>` —
    kind=code: `execute(task, code, task.tests)`; kind=tests: `execute(task, task.subject, code)` должен пройти, затем каждый мутант `execute(task, m.code, code)` должен упасть; `missed` — `description` непойманных; `ok` = прошло и `missed` пуст.
  - `verifyTask(task, reference: string, mutants: {name, code}[], execute) → Promise<string[]>` — список проблем (пустой = ок). kind=code: `execute(task, reference, task.tests)` проходит, каждый `execute(task, m.code, task.tests)` падает. kind=tests: `execute(task, task.subject, reference)` проходит, каждый `execute(task, m.code, reference)` падает. sql: `reference` совпадает с `expected`, каждый мутант — нет. Сообщения: «эталон не проходит: …», «мутант <name> не пойман».
  - `truncate(text: string, limit = 20000) → string`.
- Produces: `web/runners/python.js` `execute` (Pyodide-воркер, таймауты из Global Constraints, перезапуск воркера по таймауту); `web/runners/sql.js` `execute` (PGlite; принимает класс `PGlite` через `init(PGlite)` — один код для браузера и Node; сравнение как сейчас в `index.html`).
- Produces: `node scripts/verify.mjs [путь-к-задаче-или-папке]` — проверяет задачи (эталон + мутанты), печатает проблемы, exit 1 при любой. Читает `reference.*` и `mutants/*` с диска, использует `load_tasks` через `python3 scripts/build.py --json`.

- [ ] **Step 1: Тесты `tests/check.test.mjs`** с фейковым `execute` (возвращает заранее заданные результаты по `subject`):
  - `code task passes when tests pass` / `fails with output when tests fail`.
  - `tests task: all mutants caught → ok, caught {total: 2, missed: []}`.
  - `tests task: one mutant survives → ok false, missed ["падает на пустом вводе"], output содержит "Поймано 1 из 2"`.
  - `tests task: no tests → ok false, output "Нет ни одного теста"` (execute отдаёт `noTests: true`; мутанты не запускаются).
  - `tests task: fails on subject → ok false, output начинается с "Твои тесты падают на правильной реализации"`, мутанты не запускаются.
  - `verifyTask reports surviving mutant by name` и `reports failing reference`.
  - `truncate cuts to limit and appends "…вывод обрезан"`.
- [ ] **Step 2: Тесты `tests/sql.test.mjs`** (PGlite из npm): правильный запрос по задаче combine-two-tables → `passed`; INNER JOIN → не `passed`, вывод содержит `--- expected`; синтаксическая ошибка → не `passed`, текст ошибки Postgres.
- [ ] **Step 3:** `npm ci && node --test tests/` → FAIL.
- [ ] **Step 4:** Реализовать `check.js`, `runners/sql.js`, `runners/python.js` (+ воркер), Node-исполнители (`python.mjs`: временная папка, `python3 -m pytest -q -p no:cacheprovider`, таймаут 10 с, exit 5 → `noTests: true`; в воркере Pyodide то же по коду возврата `pytest.main`), `verify.mjs`.
- [ ] **Step 5:** `node --test tests/` → PASS; `node scripts/verify.mjs tasks` → 0 проблем.
- [ ] **Step 6:** `pages.yml`: перед сборкой — `setup-python 3.12` + `pip install pytest`, `setup-node 20` + `npm ci`, `setup-java 21 temurin`, шаги `pytest tests -q`, `node --test tests/`, `node scripts/verify.mjs tasks`; деплой только после них.
- [ ] **Step 7:** `web/index.html` использует `check()` с новыми исполнителями — обе задачи решаются в браузере (проверка в панели на `localhost:8000`).
- [ ] **Step 8:** Commit + push; CI зелёный.

### Task 4: TypeScript-исполнитель

**Files:**
- Create: `web/runners/ts-core.js`, `web/runners/ts.js`, `web/runners/ts-worker.js`, `web/runners/ts-harness.js`, `web/runners/ts-harness.d.ts`, `scripts/executors/ts.mjs`, `tests/ts.test.mjs`, тестовая задача `tasks/ts/<первая тема>/01-<slug>/` (kind=code, 2 мутанта)

**Interfaces:**
- Consumes: `Execute` из Task 3.
- Produces: `ts-core.js`: `compileAndRun(ts, files: Record<string,string>, readLib: (name) => string) → { diagnostics: string[], js: Record<string,string> }` — in-memory CompilerHost, опции `{ strict: true, target: ES2022, module: CommonJS, lib: ["lib.es2022.d.ts"], noEmitOnError: true }`, файлы `solution.ts`, `solution.test.ts`, `ts-harness.d.ts`. Ошибки типов → `passed: false`, вывод `solution.ts(3,5): error TS2322: …`.
- Produces: харнесс (глобальные `describe`, `test`, `it`, `expect`): матчеры `toBe, toEqual, toStrictEqual, toBeTruthy, toBeFalsy, toBeNull, toBeUndefined, toBeDefined, toContain, toHaveLength, toBeGreaterThan, toBeLessThan, toBeCloseTo, toThrow, toMatch`, `.not.*`, `.resolves.*`/`.rejects.*`; `async` тесты; вывод в стиле Jest (`✓ name`, `✕ name` + diff, `Tests: 1 failed, 3 passed`); 0 тестов → `noTests`.
- Браузер: TypeScript `https://cdn.jsdelivr.net/npm/typescript@5.6.3/lib/typescript.js` через `importScripts` в воркере; lib-файлы с того же CDN-пути синхронным XHR в воркере (лениво, с кэшем). Node: `typescript` из npm, lib с диска; запуск JS в дочернем `node`-процессе с таймаутом.

- [ ] **Step 1: Тесты `tests/ts.test.mjs`** (Node-исполнитель):
  - правильное решение тестовой задачи → `passed`, вывод содержит `✓`;
  - неверное → не `passed`, вывод содержит `✕` и `Expected`;
  - ошибка типов (`const x: number = "a"`) → не `passed`, вывод содержит `TS2322`;
  - `async` тест с `await expect(p).resolves.toBe(1)` → `passed`;
  - `while (true) {}` → не `passed`, «Таймаут» не дольше 12 с;
  - `console.log` 1 МБ → вывод ≤ 20 000 символов + «…вывод обрезан»;
  - пустой файл тестов → `noTests: true`.
- [ ] **Step 2:** `node --test tests/ts.test.mjs` → FAIL.
- [ ] **Step 3:** Реализовать `ts-core.js`, харнесс, Node- и браузерный исполнитель.
- [ ] **Step 4:** `node --test tests/ts.test.mjs` → PASS; `node scripts/verify.mjs tasks/ts` → 0 проблем.
- [ ] **Step 5:** В браузерной панели: тестовая TS-задача решается, ошибка типов показывается, зацикливание обрывается, следующий запуск работает.
- [ ] **Step 6:** Commit + push.

### Task 5: Java-исполнитель

**Files:**
- Create: `web/runners/java.js`, `web/runners/java/org/junit/jupiter/api/{Test,Assertions,DisplayName}.java`, `web/runners/java/org/junit/jupiter/api/function/Executable.java`, `web/runners/java/TestRunner.java`, `scripts/executors/java.mjs`, `tests/java.test.mjs`, тестовая задача `tasks/java/<первая тема>/01-<slug>/`
- Delete: `spikes/`

**Interfaces:**
- Consumes: `Execute` из Task 3; способ компиляции и прерывания из `docs/superpowers/notes/java-spike.md`.
- Produces: харнесс в стиле JUnit 5 — `@Test`, `@DisplayName`, `Assertions.{assertEquals (Object/long/double+delta/с сообщением), assertNotEquals, assertTrue, assertFalse, assertNull, assertNotNull, assertArrayEquals (int[]/long[]/Object[]), assertThrows(Class<T>, Executable) → T, assertDoesNotThrow, fail}`; `TestRunner.main` рефлексией запускает методы `@Test` класса `SolutionTest`, печатает `✓ / ✕ name` + сообщение, итог `Tests: N failed, M passed`, `System.exit(0|1|5)` (5 = нет тестов).
- Node: `javac -d out *.java` (+ харнесс), `java -cp out TestRunner`, таймаут 10 с. Браузер: компиляция и запуск по рецепту спайка, CheerpJ в отдельном iframe, по таймауту iframe пересоздаётся.

- [ ] **Step 1: Тесты `tests/java.test.mjs`** (Node-исполнитель): правильное → `passed`; неверное → вывод содержит `expected: <5> but was: <4>`; ошибка компиляции → не `passed`, текст ошибки javac; `assertThrows` работает; `while(true){}` → «Таймаут»; нет `@Test` → `noTests`.
- [ ] **Step 2:** `node --test tests/java.test.mjs` → FAIL.
- [ ] **Step 3:** Реализовать харнесс и оба исполнителя.
- [ ] **Step 4:** `node --test tests/java.test.mjs` → PASS; `node scripts/verify.mjs tasks/java` → 0 проблем.
- [ ] **Step 5:** В браузерной панели: Java-задача решается, ошибка компиляции видна, зацикливание прерывается, показывается прогресс первой загрузки.
- [ ] **Step 6:** Commit + push.

### Task 6: Цепочки (`unlock.js`)

**Files:**
- Create: `web/unlock.js`, `tests/unlock.test.mjs`

**Interfaces:**
- Produces: `taskState(task, allTasks, solved: Set<string>) → "solved" | "open" | "locked"` — задачи той же `lang`+`topic`+`level`, по `order`; первая открыта; остальные открыты, если решена предыдущая этого же уровня.

- [ ] **Step 1: Тесты:** первая easy открыта; вторая easy закрыта, пока первая не решена; первая hard открыта без решённых easy; решённая → `"solved"`; другая тема не влияет.
- [ ] **Step 2:** FAIL → реализовать → PASS (`node --test tests/unlock.test.mjs`).
- [ ] **Step 3:** Commit.

### Task 7: Прогресс, вход через GitHub, роутер

**Files:**
- Create: `web/config.js`, `web/progress.js`, `web/router.js`, `tests/progress.test.mjs`, `tests/router.test.mjs`

**Interfaces:**
- Produces (`router.js`): `parseRoute(hash: string) → { page: "landing" } | { page: "catalog", lang, topic?: string, level?: string } | { page: "task", id }`. Хэши: `#/`, `#/learn/<lang>?topic=<id>&level=<easy|medium|hard>`, `#/task/<lang>/<topic>/<NN-slug>`. `cleanAuthParams(url: URL) → URL | null` — убирает `code`, `error`, `error_description` из query; `null`, если чистить нечего.
- Produces (`progress.js`): `createProgress({ supabase, storage = sessionStorage }) →`
  `{ init(): Promise<{login: string} | null>, signIn(): Promise<void>, signOut(): Promise<void>, user(), isSolved(id), solvedIds(): Set<string>, markSolved(id, code): Promise<void>, getDraft(id): string | undefined, saveDraft(id, code): void, saveState(): "saved" | "saving" | "error" }`.
  Гость — `Map` в памяти. `signIn()` перед редиректом кладёт гостевые `{solved, drafts}` в `storage['lct:guest-carry']`; `init()` после входа делает upsert в `progress` и удаляет ключ. Пользователь: на `init()` — `select task_id, code, solved_at`; `saveDraft` — debounce 1 с, upsert `{task_id, code, updated_at}`; при ошибке `saveState() === "error"`, повтор при следующем `saveDraft`/`markSolved` с последним кодом; `markSolved` — upsert `{task_id, code, solved_at: now}`.
  Клиент Supabase: `createClient(SUPABASE_URL, SUPABASE_KEY, { auth: { flowType: "pkce", detectSessionInUrl: true, persistSession: true } })`; `signInWithOAuth({ provider: "github", options: { redirectTo: location.origin + location.pathname + location.hash } })`. `login` = `user.user_metadata.user_name`.

- [ ] **Step 1: Тесты `router.test.mjs`:** разбор всех трёх видов хэшей; пустой хэш → landing; неизвестный → landing; `cleanAuthParams` убирает `code` и сохраняет прочее; на URL без auth-параметров → `null`.
- [ ] **Step 2: Тесты `progress.test.mjs`** с фейковым supabase-клиентом:
  гость: `markSolved` → `isSolved` true, новый `createProgress` → false;
  перенос: гость решил 2 задачи → `signIn` пишет carry; `init` с сессией делает upsert 2 строк и чистит ключ;
  пользователь: `init` грузит решённые и черновики; `saveDraft` дважды за 1 с → один upsert;
  сбой: upsert бросает → `saveState() === "error"`, следующий `saveDraft` повторяет с последним кодом, после успеха `"saved"`.
- [ ] **Step 3:** FAIL → реализовать → PASS (`node --test tests/`).
- [ ] **Step 4:** Commit.

### Task 8: Интерфейс — лендинг, каталог, страница задачи

**Files:**
- Create: `web/app.js`, `web/editor.js`, `web/schema.js`, `web/style.css`
- Modify: `web/index.html` (оболочка: шапка, `<main>`, подвал с кредитом CheerpJ; стили и скрипты — вынесены)

**Interfaces:**
- Consumes: `parseRoute`, `cleanAuthParams` (Task 7), `createProgress` (Task 7), `taskState` (Task 6), `check` + исполнители по `task.lang` (Tasks 3–5), `tasks.json`, `topics.json` (оба отдаёт сборка, Task 2).

Экраны и обязательный текст:
- **Шапка**: «Live Coding Trainings», вкладки языков (Python, SQL, TypeScript, Java) со счётчиком `N/M`, справа «Войти через GitHub» или `@login` + «Выйти». У гостя рядом метка «Гость — прогресс не сохраняется».
- **Лендинг** (`#/`): для кого — QA automation и разработчикам перед live coding; что умеет — 4 языка, темы и уровни, задачи «напиши тесты» с проверкой на мутантах, подсказки, запуск в браузере без установки, прогресс на ноутбуке и телефоне. Кнопки «Войти через GitHub» и «Начать без входа»; по второй — подтверждение: «Без входа прогресс не сохранится: после перезагрузки страницы решённые задачи и счётчик обнулятся.» с кнопками «Начать» / «Отмена». Залогиненный пользователь видит на лендинге «Продолжить» → каталог.
- **Каталог** (`#/learn/<lang>`): фильтры «Тема» (все + темы из `topics.json`) и «Сложность» (все / Easy / Medium / Hard) — в URL. Темы карточками: название, описание, `решено k из n`, список задач со статусом из `taskState` (✓ решена / открыта / 🔒 «Сначала реши предыдущую задачу этого уровня»), бейдж уровня, бейдж «тесты» для kind=tests.
- **Задача** (`#/task/...`): как сейчас (условие, схема SQL, редактор CodeMirror, ⌘↵). Подсказки с подписью «Подсказки — необязательно использовать все, это только наводка». Для kind=tests — блок «Тестируемый код» (read-only CodeMirror) над редактором; результат «Поймано N из M багов» + список пропущенных. После решения — кнопка «Следующая задача →» (следующая открытая в теме). Закрытая задача по прямой ссылке — заглушка с ссылкой на ту, что надо решить. Индикатор черновика «сохранено / сохраняю… / не сохранено» (из `saveState`, только у вошедшего).
- **Подвал**: «Java работает на CheerpJ — Built with CheerpJ» (ссылка https://cheerpj.com), ссылка на GitHub-репозиторий, «MIT».
- При загрузке: `cleanAuthParams(location)` → `history.replaceState`.
- Мобильная вёрстка (≤ 900px): одна колонка, шапка с горизонтальной прокруткой вкладок, без горизонтального скролла страницы.

- [ ] **Step 1:** Перенести редактор/подсказки и ER-схему в `editor.js` / `schema.js` без изменения поведения; страница задачи работает на `localhost:8000`.
- [ ] **Step 2:** Реализовать роутинг, лендинг, каталог, шапку, подвал, состояние гостя и входа.
- [ ] **Step 3: Ручная проверка в браузерной панели (localhost:8000):** лендинг → «Начать без входа» → подтверждение → каталог; фильтр Hard показывает открытые hard-задачи; решить задачу → ✓, счётчик +1, «Следующая задача →» ведёт на следующую; перезагрузка → счётчик 0; kind=tests показывает «Поймано N из M»; мобильный вид (`resize_window` mobile) без горизонтального скролла.
- [ ] **Step 4:** Commit + push; на живом сайте вход через GitHub делает Катя (вход — её действие): после входа URL без `?code=`, задача, решённая гостем до входа, остаётся решённой; на телефоне видна после входа.

### Task 9: Документация и локальный режим

**Files:**
- Modify: `CLAUDE.md`, `README.md` (создать: что это, ссылка на сайт, как запустить локально, как добавить задачу, лицензия)

- [ ] **Step 1:** `CLAUDE.md` — новый формат задач (раздел «Формат задачи» этого плана), правила авторинга (Task 10), команды `./run test`, `./run verify <путь>`, `docker compose up -d --build` → `http://localhost:8000`. Агент «дай задачу» теперь добавляет задачу в банк; «проверь» не используется (код пользователя не пишется в файлы).
- [ ] **Step 2:** `./run test` и `./run verify tasks` зелёные в контейнере.
- [ ] **Step 3:** Commit + push.

### Task 10: Банк задач — правила авторинга (общие для Tasks 11–14)

Не отдельная поставка — правила, которым подчиняется каждая задача контента. Проверяет ревьюер Tasks 11–14.

- Условие — своими словами на русском, свои имена/данные/примеры; где возможно — сюжет из работы автоматизатора (логи, прогоны тестов, ответы API, ретраи, ожидания, тестовые данные, даты, дедупликация, отчёты).
- Структура README: заголовок, 2–4 предложения условия, «Пример» (вход → выход), «Ограничения» при необходимости. Без ссылок на LeetCode.
- `starter` — сигнатура + пустое тело (kind=code) или заготовка тестового файла с одним импортом (kind=tests).
- Тесты (kind=code): примеры из условия + граничные случаи (пустой ввод, один элемент, дубликаты, отрицательные — по смыслу); ≥ 4 проверки.
- Мутанты: ≥ 2, каждый — правдоподобная ошибка (на единицу, пропущенная граница, не тот порядок, забыли пустой ввод), описание — короткое по-русски («теряет последний элемент»).
- Подсказки: 2–5, только то, что ведёт к решению эталона; не подсказывать всё решение; ничего лишнего.
- В каждой теме 3 задачи: `01` easy, `02` medium, `03` hard — кроме тем, где явно указано 2 задачи одного уровня (для цепочки). В теме `write-tests` все задачи kind=tests (easy, medium, hard); в остальных темах — kind=code.
- `node scripts/verify.mjs tasks/<lang>` → 0 проблем — обязательное условие коммита.

### Task 11: Python — 8 тем

**Files:** `topics.json` (python), `tasks/python/**` (заменяет перенесённую Two Sum)

Темы (id — название): `strings` — Строки; `lists-loops` — Списки и циклы; `dicts-sets` — Словари и множества; `sorting-search` — Сортировка и поиск;
`two-pointers` — Два указателя и окно; `recursion` — Рекурсия; `data-parsing` — Разбор данных: логи, JSON, CSV; `write-tests` — Напиши тесты (kind=tests).
В `lists-loops` и `dicts-sets` — по 2 easy (`01`, `02` easy, `03` medium, `04` hard).

- [ ] **Step 1:** Написать задачи по правилам Task 10.
- [ ] **Step 2:** `node scripts/verify.mjs tasks/python` → 0 проблем; `pytest tests -q` → PASS.
- [ ] **Step 3:** В браузерной панели решить по одной задаче каждого вида (code и tests) эталоном — засчитано.
- [ ] **Step 4:** Commit + push.

### Task 12: SQL — 8 тем

**Files:** `topics.json` (sql), `tasks/sql/**` (заменяет Combine Two Tables)

Темы: `select-where` — SELECT и фильтрация; `joins` — JOIN; `group-by` — Агрегаты и GROUP BY / HAVING; `subqueries` — Подзапросы и CTE;
`window` — Оконные функции; `dates` — Даты и время; `null-case` — NULL и CASE; `data-quality` — Проверка данных: дубликаты, пропуски, аномалии.
В `joins` — 2 easy. В `schema.sql` объявлены `PRIMARY KEY` и, где данные позволяют, `REFERENCES`; ссылочные колонки — `<таблица>_id`. Подсказки в `task.json.hints` (`hints.txt` больше нет).

- [ ] **Step 1–4:** как в Task 11 для `tasks/sql` (вместо pytest — `node --test tests/`), схема таблиц рисуется у каждой задачи.

### Task 13: TypeScript — 8 тем

**Files:** `topics.json` (ts), `tasks/ts/**`

Темы: `strings-arrays` — Строки и массивы; `objects-maps` — Объекты, Map и Set; `types-generics` — Типы и generics (часть проверок — `// @ts-expect-error` в тестах);
`async` — Промисы и async: ретраи, таймауты, ожидание условия (без реальных задержек > 1 с суммарно на задачу); `data-processing` — Обработка данных и сравнение JSON-ответов;
`algorithms` — Стек, очередь, поиск; `parsing` — Парсинг URL, query-строк, селекторов; `write-tests` — Напиши тесты (kind=tests). В `async` — 2 easy.

- [ ] **Step 1–4:** как в Task 11 для `tasks/ts`.

### Task 14: Java — 8 тем

**Files:** `topics.json` (java), `tasks/java/**`

Темы: `strings` — Строки и StringBuilder; `arrays-loops` — Массивы и циклы; `collections` — Коллекции: List, Map, Set; `streams` — Stream API;
`oop` — ООП и интерфейсы; `exceptions` — Исключения и валидация; `algorithms` — Алгоритмы; `write-tests` — Напиши тесты (kind=tests). В `collections` — 2 easy.

- [ ] **Step 1–4:** как в Task 11 для `tasks/java`.

### Task 15: Финальная проверка релиза

- [ ] **Step 1:** CI зелёный, Pages задеплоен, `tasks.json` содержит 4 языка × 8 тем, ≥ 96 задач.
- [ ] **Step 2:** На `https://korolevaeka.github.io/live-coding-trainings/` в браузерной панели (desktop и `resize_window` mobile): лендинг; гость решает по одной задаче каждого языка; фильтр Hard; цепочка в теме с двумя easy; задача «напиши тесты» с непойманным мутантом показывает его описание; кредит CheerpJ виден.
- [ ] **Step 3:** Попросить Катю войти через GitHub на ноутбуке и телефоне и подтвердить синхронизацию прогресса.
- [ ] **Step 4:** Отдельный ревьюер (свежий агент) проверяет всю ветку против спеки и Review Focus.
