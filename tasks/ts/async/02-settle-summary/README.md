# Итоги по промисам

Автотест запустил пачку независимых проверок, и каждая вернула промис. Напиши `summarize(tasks)`: дождись, пока **все** они завершатся (успешно или с ошибкой), и верни объект `{ fulfilled, rejected }` — сколько завершилось успешно и сколько с ошибкой. Итоговый промис сам никогда не отклоняется.

```
await summarize([Promise.resolve(1), Promise.reject(new Error("x")), Promise.resolve(2)])
->  { fulfilled: 2, rejected: 1 }
await summarize([])  ->  { fulfilled: 0, rejected: 0 }
```
