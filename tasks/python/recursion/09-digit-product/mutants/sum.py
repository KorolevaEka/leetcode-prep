def digit_product(n):
    if n < 10:
        return n
    return n % 10 + digit_product(n // 10)
