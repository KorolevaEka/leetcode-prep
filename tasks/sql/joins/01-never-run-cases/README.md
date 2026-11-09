# Кейсы без запусков

Есть каталог тест-кейсов `test_cases` и таблица результатов `test_results`; в ней колонка `test_case_id` указывает, какому кейсу принадлежит результат.

Выведи названия (`name`) кейсов, у которых **нет ни одного результата**. Порядок строк не важен.

## Пример

```
test_cases:           test_results:         name
1 login               1 (case 1) passed  ->  reset_password
2 reset_password
```
