# Падения по модулям

Имя теста начинается с модуля: `"auth.login_ok"` — модуль `auth`. Модуль — часть имени до **первой** точки; если точки нет, модулем считается всё имя. Запись теста — `Solution.TestRun(name, status, durationMs)` (уже есть в заготовке).

Напиши метод `Solution.failedByModule(List<TestRun> runs)`, который возвращает `Map<String, Long>`: модуль → сколько тестов этого модуля имеют статус `"FAILED"`. Модули без падений в результат не попадают. Верни `TreeMap`, чтобы ключи шли по алфавиту. Решай через Stream API.

```
runs: (auth.login_ok, FAILED), (auth.logout, PASSED), (cart.add.item, FAILED), (cart.remove, FAILED), (smoke, FAILED)
failedByModule(runs)  ->  {auth=1, cart=2, smoke=1}
```
