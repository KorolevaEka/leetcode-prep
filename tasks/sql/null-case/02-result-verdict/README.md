# Вердикт по результату

Для отчёта по каждому результату в `test_results` нужен текстовый `verdict`:

- `passed` и были повторные запуски (`retries > 0`) — `flaky`;
- `passed` без повторов (в том числе `retries` не заполнен) — `stable`;
- `failed` — `broken`;
- `skipped` — `skipped`;
- всё остальное, в том числе статус не указан — `unknown`.

Выведи `test_result_id, verdict`. Порядок строк не важен.

## Пример

```
status  retries   verdict
passed  2         flaky
passed  NULL      stable
failed  3         broken
NULL    NULL      unknown
```
