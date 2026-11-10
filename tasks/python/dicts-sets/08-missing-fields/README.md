# Чего не хватает в ответе API

Контрактный тест проверяет, что в JSON-ответе есть все обязательные поля. Напиши функцию `missing_fields(response, required)`, которая возвращает список обязательных полей, которых в ответе нет. Поле со значением `None` (`null` в JSON) тоже считается отсутствующим, а `0`, `False`, `""` и `[]` — нормальные значения. Порядок результата — как в `required`.

## Пример

```
missing_fields({"id": 7, "name": None, "tags": []}, ["id", "name", "email", "tags"])  ->  ["name", "email"]
missing_fields({"count": 0, "ok": False}, ["ok", "count"])                           ->  []
missing_fields({}, ["id"])                                                           ->  ["id"]
```
