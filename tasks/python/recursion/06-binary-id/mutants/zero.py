def binary_id(n):
    if n < 2:
        return ''
    return binary_id(n // 2) + str(n % 2)
