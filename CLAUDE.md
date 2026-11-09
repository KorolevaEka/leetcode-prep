# LeetCode prep

Тренажёр: агент выдаёт задачи с LeetCode по одной, Катя пишет решения, агент проверяет.
Python и Postgres живут в docker-compose, папка проекта смонтирована в оба контейнера как `/work`.

## Окружение

```bash
docker compose up -d --build   # один раз (и после правок Dockerfile/server.py)
# веб-интерфейс: http://localhost:8000 — решения сохраняются в файлы solution.*
docker compose exec py bash    # терминал внутри python-контейнера
docker compose exec db psql -U postgres   # psql
```

## Сайт

`index.html` + `py-worker.js`: код выполняется в браузере (Python — Pyodide + pytest, SQL — PGlite),
задачи берутся из `tasks.json` (`build.py`). Публичная версия: https://korolevaeka.github.io/leetcode-prep/ —
собирается GitHub Actions (`.github/workflows/pages.yml`) на каждый пуш в main, там черновики живут в localStorage.
Новая задача попадает на публичный сайт только после коммита и пуша.

## Проверка из терминала (pytest/psql в контейнерах, логика в check.py)

```bash
./run python/0001-two-sum
./run sql/0175-combine-two-tables
```

## Как выдавать задачу («дай задачу», «следующую»)

Одна задача — одна папка `<python|sql>/<4-значный номер>-<slug>/`. Смотри, какие уже есть, бери следующую
по сложности/теме (по умолчанию — из NeetCode 150 для python и SQL 50 для sql), не повторяйся.

- **python/**: `README.md` (условие своими словами на русском, ссылка, примеры, ограничения),
  `solution.py` — только сигнатура и `pass`, `test_solution.py` — pytest с примерами из условия + краевыми случаями.
- **sql/**: `README.md`, `schema.sql` (начинается с `DROP SCHEMA IF EXISTS t CASCADE; CREATE SCHEMA t; SET search_path = t;`,
  имена в snake_case), пустой `solution.sql`, `expected.csv` с заголовком (формат `psql --csv`, NULL — пустое поле).
  По `schema.sql` сайт рисует схему таблиц: объявляй `PRIMARY KEY`, а `REFERENCES` — если данные ему соответствуют.
  Колонки-ссылки называй `<таблица>_id` (`customer_id` → `customers`): тогда связь дорисуется пунктиром и без FK.
  `hints.txt` — ключевые слова твоего эталонного решения, по одному в строке, в порядке использования
  (`SELECT`, `FROM`, `LEFT JOIN`, `GROUP BY`, `HAVING`, `ROW_NUMBER() OVER` …). На сайте это необязательные
  подсказки над редактором: ничего не проверяют, решение другим способом тоже засчитывается.

Перед выдачей проверь, что тест/expected корректны: временно реши задачу сам, прогони `./run`, верни заготовку.
Решение не подсказывай, пока не попросят. Новую папку открой в редакторе: `idea <путь к solution>`.

## Когда Катя говорит «проверь»

Запусти `./run <папка>`. Упало — покажи, на каком кейсе, и намекни, без готового кода.
Прошло — коротко оцени сложность по времени/памяти и предложи следующую задачу.
