def reverse_upto(items: list, stop) -> list:
    if stop not in items:
        return list(items)
    end = items.index(stop)
    return items[end - 1::-1] + items[end:] if end else list(items)
