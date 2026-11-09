# Нестабильные тесты по перезапускам

Упавший прогон перезапускали несколько раз. Каждая попытка — список `Solution.TestRun(name, status, durationMs)` (запись уже есть в заготовке); статус — `"PASSED"`, `"FAILED"` или `"SKIPPED"`.

Напиши метод `Solution.flakyTests(List<List<TestRun>> attempts)`, который возвращает `List<String>` имён **нестабильных** тестов: тех, что в разных попытках хотя бы раз завершились `PASSED` и хотя бы раз `FAILED`. Статус `SKIPPED` в расчёт не берётся. Имена без повторов, отсортированы по алфавиту. Решай через Stream API.

```
попытка 1: (login, FAILED), (cart, PASSED), (pay, FAILED)
попытка 2: (login, PASSED), (cart, PASSED), (pay, FAILED)
flakyTests(...)  ->  ["login"]      // cart всегда проходит, pay всегда падает
```
