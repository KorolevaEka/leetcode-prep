# Live Coding Trainings

Бесплатный тренажёр лайвкодинга на русском для QA-автоматизаторов и разработчиков. Четыре языка:
Python, SQL, TypeScript, Java. Код выполняется прямо в браузере (Pyodide, PGlite, компилятор TS, CheerpJ),
правильность задач проверяет CI. Сайт: https://korolevaeka.github.io/live-coding-trainings/
Репозиторий: https://github.com/KorolevaEka/live-coding-trainings (ветка `main`). Лицензия MIT.

## Структура

- `tasks/<lang>/<topic>/<NN>-<slug>/` — банк задач (`lang` ∈ `python|sql|ts|java`).
- `topics.json` — порядок и названия тем по языкам: `{ "python": [{ "id", "title", "description" }], "sql": [...], ... }`.
- `web/` — всё, что уходит на сайт (HTML/JS/CSS, раннеры в `web/runners/`).
- `scripts/` — `build.py` (собирает `_site/`: лёгкий индекс `tasks.json` и полные записи `tasks/<id>.json`, грузятся по требованию), `serve.py` (локальный сервер), `verify.mjs` (проверка задач, исполнители в `scripts/executors/`).
- `tests/` — тесты платформы: `test_build.py` (pytest), `*.test.mjs` (`node --test`).

## Формат задачи

Папка `tasks/<lang>/<topic>/<NN>-<slug>/`; `<topic>` — id из `topics.json`, `NN` — порядок внутри темы.

`task.json`:
```json
{
  "title": "Частота слов в логе",
  "level": "easy",
  "kind": "code",
  "hints": ["dict", "split()", "sorted(key=)"],
  "mutants": { "off-by-one": "теряет последний элемент", "empty": "падает на пустом вводе" }
}
```
`level`: `easy | medium | hard`. `kind`: `code` (пользователь пишет решение) или `tests` (пишет тесты; для sql — только `code`).

Файлы (`<ext>` = py / sql / ts / java):
- `README.md` — условие (markdown).
- `starter.<ext>` — что пользователь видит в редакторе изначально.
- `reference.<ext>` — эталон редактируемого файла: решение (kind=code) или образцовые тесты (kind=tests). На сайт не отдаётся.
- `tests.<ext>` — только kind=code (кроме sql): тесты задачи.
- `subject.<ext>` — только kind=tests: тестируемый код, показывается read-only.
- `mutants/<name>.<ext>` — сломанные версии: решения (kind=code) или `subject` (kind=tests). Имена совпадают с ключами `task.json.mutants`. Минимум 2.
- sql: `schema.sql`, `expected.csv` (заголовок как у `psql --csv`, NULL — пустое поле); тестов нет, проверка — сравнение результата.
  `schema.sql` начинается с `DROP SCHEMA IF EXISTS t CASCADE; CREATE SCHEMA t; SET search_path = t;`, имена в snake_case.
  По нему сайт рисует ER-схему: объявляй `PRIMARY KEY`, `REFERENCES` — если данные соответствуют; колонки-ссылки называй `<таблица>_id`.

Имена модулей при выполнении:

| lang | subject | tests |
|------|---------|-------|
| python | `solution.py` | `test_solution.py` (`from solution import …`) |
| ts | `solution.ts` | `solution.test.ts` (`import { … } from "./solution"`) |
| java | `Solution.java` (`public class Solution`) | `SolutionTest.java` (JUnit 5: `import org.junit.jupiter.api.Test; import static org.junit.jupiter.api.Assertions.*;`) |

## Правила авторинга

- Условие — своими словами на русском, свои имена/данные/примеры, без дословных текстов LeetCode и без данных TaxDome. Где возможно — сюжет из работы автоматизатора: логи, прогоны тестов, ответы API, ретраи, ожидания, тестовые данные, даты, дедупликация, отчёты.
- README: заголовок, 2–4 предложения условия, «Пример» (вход → выход), «Ограничения» при необходимости. Без ссылок на LeetCode.
- `starter` — сигнатура + пустое тело (kind=code) или заготовка тестового файла с одним импортом (kind=tests).
- Тесты (kind=code): примеры из условия + граничные случаи (пустой ввод, один элемент, дубликаты, отрицательные — по смыслу); не меньше 4 проверок.
- Мутанты: не меньше 2, каждый — правдоподобная ошибка (на единицу, пропущенная граница, не тот порядок, забыли пустой ввод); описание короткое по-русски («теряет последний элемент»).
- Подсказки: 2–5, только то, что ведёт к решению эталона; не подсказывать всё решение, ничего лишнего. На сайте они необязательны и ничего не проверяют.
- В каждой теме 3 задачи: `01` easy, `02` medium, `03` hard (кроме тем, где явно указано иначе). В теме `write-tests` все задачи kind=tests; в остальных — kind=code.
- Интерфейс и условия только на русском; слово «LeetCode» нигде в брендинге.
- Обязательное условие коммита: `./run verify tasks/<lang>` — 0 проблем.

## Как выдавать задачу («дай задачу», «следующую»)

Задача добавляется в банк, а не выдаётся в чат: выбери язык и тему (по просьбе или следующую по порядку в `topics.json`),
создай папку `tasks/<lang>/<topic>/<NN>-<slug>/` со всеми файлами по формату выше, при новой теме допиши её в `topics.json`.
Затем гоняй `./run verify tasks/<lang>/<topic>/<NN>-<slug>`, пока не будет ok: эталон проходит, мутанты падают.
Решение пользователю не подсказывай, пока не попросят. Код пользователя в файлы не пишется (он живёт в браузере), поэтому режима «проверь» нет.

## Команды

```bash
docker compose up -d --build   # сайт на http://localhost:8000 (живой tasks.json из tasks/)
./run test                     # тесты платформы: pytest + node --test
./run verify                   # проверить все задачи (по умолчанию)
./run verify tasks/<lang>/<topic>/<NN>-<slug>   # одну задачу; можно и папку темы/языка
```
Команды `./run` выполняются в контейнере `py` (`docker compose up -d`, если он не запущен).

## Деплой

Пуш в `main` запускает GitHub Actions (`.github/workflows/pages.yml`): `pytest tests`, `node --test tests/`,
`node scripts/verify.mjs tasks`, затем `scripts/build.py` и деплой на GitHub Pages — только если всё зелёное.
Используем только бесплатные сервисы: GitHub Pages/Actions, Supabase Free (вход и прогресс), CheerpJ Community (Java).
