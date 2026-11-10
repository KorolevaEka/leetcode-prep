def reverse_upto(items: list, stop) -> list:
    if stop not in items:
        return items[::-1]
    end = items.index(stop)
    return items[end::-1] + items[end + 1:]
