# Все вхождения в логе

В строке лога нужно отметить все места, где встречается шаблон.

Напиши метод `Solution.findAll(String text, String pattern)`, который возвращает `List<Integer>` — индексы начал **всех** вхождений `pattern` в `text` по возрастанию. Вхождения могут перекрываться. Сравнение с учётом регистра. Если вхождений нет, результат пустой. Если `pattern` пустой, метод бросает `IllegalArgumentException`.

```
findAll("aaaa", "aa")               ->  [0, 1, 2]
findAll("ERR ok ERR", "ERR")        ->  [0, 7]
findAll("Error error", "error")     ->  [6]
findAll("abc", "x")                 ->  []
```
