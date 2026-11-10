# Статус для отчёта

Внутренние коды статусов вроде `TEST_FAILED_ON_RETRY` нужно показывать в отчёте читаемо. Каждое подчёркивание `_` заменяется на пробел (каждое, подряд идущие не схлопываются), первый символ строки становится заглавным, все остальные буквы строчными.

Напиши функцию `humanize_status(code)`. Пустая строка остаётся пустой.

## Пример

```
humanize_status("TEST_FAILED_ON_RETRY")  ->  "Test failed on retry"
humanize_status("PASSED")                ->  "Passed"
humanize_status("SETUP__ERROR")          ->  "Setup  error"
```
