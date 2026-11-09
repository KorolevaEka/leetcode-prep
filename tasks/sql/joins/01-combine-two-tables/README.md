# Объединение двух таблиц

Есть таблицы `person(person_id, last_name, first_name)` и `address(address_id, person_id, city, state)`.

Для каждого человека из `person` выведи `first_name, last_name, city, state` (именно в таком порядке колонок).
Если у человека нет адреса — `city` и `state` должны быть `NULL`. Порядок строк любой.

Таблицы уже лежат в схеме `t` (см. `schema.sql`), пиши решение в редакторе.
