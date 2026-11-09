# Самое длинное стабильное окно

Ночной прогон выдал список результатов: `true` — тест прошёл, `false` — упал. Команда готова простить до `maxFailures` падений (считай их флаками), если вокруг них идёт длинная серия подряд.

Напиши функцию `longestStretch(results, maxFailures)`: длина самого длинного **непрерывного** отрезка списка, в котором не больше `maxFailures` значений `false`.

```
longestStretch([true, true, false, true, true, true, false, true], 1)  ->  6
longestStretch([true, true, false, true, true, true, false, true], 0)  ->  3
longestStretch([false, false], 1)                                      ->  1
```

## Ограничения

`maxFailures >= 0`. Список может быть пустым — ответ `0`.
