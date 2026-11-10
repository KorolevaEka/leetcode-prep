# Строки отчёта из XML

XML имеет корень report с непосредственными элементами case. Верни список (name,status,message), где name обязателен, status по умолчанию unknown, message — весь текст внутри дочернего message или пустая строка. Остальные элементы игнорируй; неверный XML или case без name вызывает ValueError.

Реализуй `xml_cases(text)`. Входные коллекции менять нельзя.

## Пример

```python
xml_cases('<report><case name="a" status="fail"><message>x<b>y</b>z</message></case></report>') → [('a', 'fail', 'xyz')]
```
