# Политики повторов

Клиент API повторяет неудачные запросы. Интерфейс `Solution.RetryPolicy` уже есть в заготовке:

- `int maxAttempts()` — сколько всего попыток (включая первую); значит, повторов `maxAttempts() - 1`;
- `long delayBeforeRetryMs(int retryNumber)` — пауза перед повтором номер `retryNumber` (повторы нумеруются с 1). Для номера вне диапазона `1 … maxAttempts() - 1` метод бросает `IllegalArgumentException`.

Реализуй:

- `FixedDelay(int maxAttempts, long delayMs)` — пауза всегда `delayMs`;
- `ExponentialBackoff(int maxAttempts, long baseMs, long capMs)` — пауза `baseMs · 2^(n-1)`, но не больше `capMs`: при `baseMs = 100` это 100, 200, 400, …;
- в обоих конструкторах `maxAttempts < 1` приводит к `IllegalArgumentException`;
- `Solution.totalWaitMs(RetryPolicy policy)` — сумма пауз всех повторов (0, если повторов нет).

Считай `maxAttempts ≤ 30`, `baseMs`, `capMs`, `delayMs` — неотрицательные и не больше миллиона.

```
new FixedDelay(4, 250).delayBeforeRetryMs(2)              ->  250
new ExponentialBackoff(6, 100, 500): паузы повторов 1..5  ->  100, 200, 400, 500, 500
totalWaitMs(new FixedDelay(4, 250))                       ->  750
```
