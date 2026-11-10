# Типы значений JSON

На входе корректный JSON-массив. Для каждого непосредственного элемента верни одно из имён null, bool, number, string, array, object. Вложенное содержимое разбирать не нужно.

Реализуй `json_types(text)`. Входные коллекции менять нельзя.

## Пример

```python
json_types('[null,true,0,"",[],{}]') → ['null', 'bool', 'number', 'string', 'array', 'object']
```
