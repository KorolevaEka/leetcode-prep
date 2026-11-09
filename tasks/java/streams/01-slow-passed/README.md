# Медленные пройденные тесты

Результат каждого теста описан записью `Solution.TestRun(name, status, durationMs)` (она уже есть в заготовке). Статус — одна из строк `"PASSED"`, `"FAILED"`, `"SKIPPED"`.

Напиши метод `Solution.slowPassed(List<TestRun> runs, int limitMs)`, который возвращает `List<String>` имён тестов со статусом `PASSED`, длившихся **строго больше** `limitMs`. Имена отсортированы по алфавиту (обычное сравнение строк), повторы не убираются. Решай через Stream API.

```
runs: (login, PASSED, 900), (cart, PASSED, 300), (pay, FAILED, 5000), (search, PASSED, 1200)
slowPassed(runs, 500)  ->  ["login", "search"]
```
