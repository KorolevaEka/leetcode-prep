# Первый упавший тест

Список `statuses` — это результаты тестов по порядку: `"passed"`, `"failed"` или `"skipped"`. Напиши функцию `first_failure(statuses)`, которая возвращает индекс (с нуля) первого теста со статусом `"failed"`. Если упавших тестов нет, верни `-1`.

## Пример

```
first_failure(["passed", "skipped", "failed", "failed"])  ->  2
first_failure(["failed"])                                 ->  0
first_failure(["passed", "passed"])                       ->  -1
```
