# 175. Combine Two Tables (Easy)

https://leetcode.com/problems/combine-two-tables/

`Person(personId, lastName, firstName)`, `Address(addressId, personId, city, state)`.

Для каждого человека из `Person` выведи `firstName, lastName, city, state`.
Если адреса нет — `city` и `state` должны быть `NULL`. Порядок строк любой.

Пиши решение в `solution.sql`, таблицы уже лежат в схеме `t` (см. `schema.sql`).
