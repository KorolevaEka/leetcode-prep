def reverse_upto(items: list, stop) -> list:
    if stop not in items:
        return list(items)
    end = len(items) - 1 - items[::-1].index(stop)
    return items[end::-1] + items[end + 1:]
