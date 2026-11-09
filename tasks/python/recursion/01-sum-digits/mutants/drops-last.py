def sum_digits(n: int) -> int:
    if n < 10:
        return n
    return sum_digits(n // 10)
