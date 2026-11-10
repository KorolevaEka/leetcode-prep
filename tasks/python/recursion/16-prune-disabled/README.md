# Удалить выключенные ветви

Узел имеет name, enabled и children. Если enabled=False, удали весь узел с потомками, вернув None. В остальных узлах рекурсивно убери выключенных детей и верни новое дерево без изменения оригинала. None остаётся None.

Реализуй `prune_disabled(tree)`. Входные коллекции менять нельзя.

## Пример

```python
prune_disabled({'name': 'r', 'enabled': True, 'children': [{'name': 'x', 'enabled': False, 'children': []}]}) → {'name': 'r', 'enabled': True, 'children': []}
```
