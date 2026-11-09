# Предохранитель запросов

Класс `Solution.CircuitBreaker(int failureThreshold, long openMs)` защищает сервис от повторных обращений к упавшей зависимости. Время всегда передаётся параметром `now` в миллисекундах.

- состояния: `"CLOSED"` (запросы идут), `"OPEN"` (запросы блокируются), `"HALF_OPEN"` (разрешён один пробный запрос);
- `recordFailure(now)` в состоянии CLOSED увеличивает счётчик подряд идущих неудач; когда он достигает `failureThreshold`, предохранитель открывается (`OPEN`) с моментом открытия `now`;
- `recordSuccess()` в любом состоянии закрывает предохранитель (`CLOSED`) и обнуляет счётчик;
- `recordFailure(now)` в состоянии OPEN или HALF_OPEN открывает предохранитель заново с моментом открытия `now`;
- `state(now)`: пока не прошло `openMs` с момента открытия — `OPEN`; когда `now - момент открытия >= openMs` — `HALF_OPEN`; без открытия — `CLOSED`;
- `allowRequest(now)`: в CLOSED всегда `true`; в OPEN — `false`; в HALF_OPEN **первый** вызов даёт `true` (пробный запрос), последующие — `false`, пока не придёт `recordSuccess` или `recordFailure`;
- `failureThreshold < 1` в конструкторе — `IllegalArgumentException`.

Напиши тесты в стиле JUnit 5 (`@Test`, `assertEquals`, `assertTrue`, `assertThrows`), которые проходят на этой версии и ловят версии с ошибками. Код показан справа, менять его нельзя; импорты уже есть в заготовке.
