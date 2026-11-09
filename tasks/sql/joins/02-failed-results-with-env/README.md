# Упавшие результаты с версией и окружением

Результат (`test_results`) принадлежит прогону (`test_runs`), а прогон — сборке (`builds`).

Для каждого результата со статусом `failed` выведи версию сборки, окружение прогона и название теста: `version, env, test_name` (в таком порядке колонок). Порядок строк не важен.

## Пример

```
builds: 1 = 1.4.0     test_runs: 1 = сборка 1, staging     version env     test_name
test_results: прогон 1, checkout, failed                ->  1.4.0   staging checkout
```
