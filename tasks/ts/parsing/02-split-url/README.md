# Разбор URL на части

В `URL` из браузера нельзя положиться в любой среде, поэтому разберём адрес вручную. Напиши `splitUrl(url)` для абсолютных адресов вида `протокол://хост[:порт][/путь][?query][#hash]`.

Верни объект с полями: `protocol` (без `://`), `host` (без порта), `port` (число или `null`), `path` (если пути нет — `"/"`), `query` (без `?`, если нет — `""`), `hash` (без `#`, если нет — `""`). Знак `?` внутри фрагмента (после `#`) — часть фрагмента, а не query.

```
splitUrl("https://shop.io:8443/cart/items?id=7&x=1#top")
->  { protocol: "https", host: "shop.io", port: 8443, path: "/cart/items", query: "id=7&x=1", hash: "top" }
splitUrl("http://localhost")  ->  { protocol: "http", host: "localhost", port: null, path: "/", query: "", hash: "" }
```
