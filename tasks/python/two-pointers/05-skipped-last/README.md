# Пропущенные в конец

В отчёте о прогоне хочется видеть сначала всё, что реально выполнялось, а пропущенные тесты (`"skipped"`) отодвинуть в конец. Напиши функцию `skipped_last(results)`, которая возвращает новый список: сначала все результаты, кроме `"skipped"`, в исходном порядке, затем все `"skipped"`. Исходный список менять нельзя.

## Пример

```
skipped_last(["passed", "skipped", "failed", "skipped", "passed"])
    ->  ["passed", "failed", "passed", "skipped", "skipped"]
skipped_last(["skipped"])  ->  ["skipped"]
skipped_last([])           ->  []
```
