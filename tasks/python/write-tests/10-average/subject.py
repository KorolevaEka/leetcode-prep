def mean_present(values):
    a = [x for x in values if x is not None]
    return sum(a) / len(a) if a else None
