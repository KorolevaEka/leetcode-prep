# Медленные упавшие тесты

В таблице `test_results` лежат результаты тестов: название, набор, статус и длительность в миллисекундах.

Выведи название и длительность (`test_name`, `duration_ms`) у тестов, которые **упали** (`status = 'failed'`) и шли **дольше 2000 мс**. Ровно 2000 мс — ещё не «долго». Порядок строк не важен.

## Пример

```
test_name      status   duration_ms          test_name     duration_ms
login_ok       passed   850          ->      cart_checkout 5100
cart_checkout  failed   5100
cart_add       failed   2000
```
