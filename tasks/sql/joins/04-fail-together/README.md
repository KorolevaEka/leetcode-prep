# Тесты, которые падают вместе

Иногда два теста падают всегда парой — например, из-за общей зависимости. Результаты лежат в `test_results`: прогон (`test_run_id`), кейс (`test_case_id`) и статус.

Найди пары **разных** тестов, которые падали (`failed`) в одном и том же прогоне **минимум в двух прогонах**. Каждую пару выводи один раз: в паре первым идёт кейс с меньшим `test_case_id`. Колонки: `name_a, name_b, runs_together` — где `runs_together` число таких общих прогонов. Порядок строк не важен.

## Пример

```
test_case_id: 1 = login, 2 = checkout, 3 = search

прогон 1: login и checkout упали
прогон 2: login и checkout упали, search прошёл
прогон 3: checkout и search упали

  ->  name_a  name_b    runs_together
      login   checkout  2      (login: id 1 < checkout: id 2)
```
