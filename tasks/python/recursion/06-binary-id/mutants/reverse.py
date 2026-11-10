def binary_id(n):
    if n < 2:
        return str(n)
    return str(n % 2) + binary_id(n // 2)
