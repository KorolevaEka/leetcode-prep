# Локаторы и CSS-селекторы

В page object элементы описывают локаторами. Интерфейс `Solution.Locator` с методом `String toCss()` уже есть в заготовке; осталось реализовать его классами:

- `ById(String id)` → `"#" + id`, например `#login`;
- `ByClass(String name)` → `"." + name`, например `.btn-primary`;
- `ByTag(String tag)` → само имя тега, например `input`;
- `ByAttribute(String name, String value)` → `[name="value"]`, например `[type="submit"]`.

И метод `Solution.chain(List<Locator> path)`: селектор потомка — `toCss()` каждого локатора, соединённые одним пробелом; для пустого списка — пустая строка.

```
chain([ByTag("form"), ByClass("row"), ByAttribute("type", "submit")])  ->  form .row [type="submit"]
chain([ById("login")])                                                 ->  #login
chain([])                                                              ->  ""
```
