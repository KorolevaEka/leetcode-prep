# Неизменяемая сумма

Тесты проверяют стоимость заказов, и деньги нельзя хранить в `double`. Реализуй вложенный класс `Solution.Money` (заготовка есть): неизменяемая сумма в центах с валютой.

- `Money(long cents, String currency)` — если `cents < 0`, бросает `IllegalArgumentException`; валюта не `null`;
- `long cents()` и `String currency()` — значения;
- `Money plus(Money other)` — **новый** объект с суммой центов; у валют должен быть один код, иначе `IllegalArgumentException`; исходные объекты не меняются;
- `equals` / `hashCode` — по сумме и валюте вместе: равные объекты дают одинаковый хеш-код;
- `toString()` — рубли и копейки с двумя цифрами и код валюты через пробел: `12.50 USD`, `0.05 EUR`, `100.00 USD`.

```
new Money(1250, "USD").plus(new Money(75, "USD"))  ->  13.25 USD
new Money(5, "EUR").toString()                      ->  "0.05 EUR"
new Money(100, "USD").equals(new Money(100, "EUR"))  ->  false
```
