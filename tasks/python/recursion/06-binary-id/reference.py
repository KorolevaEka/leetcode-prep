def binary_id(n):
    if n < 2:
        return str(n)
    return binary_id(n // 2) + str(n % 2)
