# Самая длинная зелёная серия

По истории ночных сборок нужно узнать, сколько сборок подряд прошло успешно. Напиши функцию `longest_green_streak(builds)`, где `builds` — список строк `"green"` или `"red"`. Верни длину самой длинной непрерывной серии `"green"`. Для пустого списка ответ `0`.

## Пример

```
longest_green_streak(["green", "green", "red", "green"])  ->  2
longest_green_streak(["red", "red"])                       ->  0
longest_green_streak(["green", "green", "green"])          ->  3
```
