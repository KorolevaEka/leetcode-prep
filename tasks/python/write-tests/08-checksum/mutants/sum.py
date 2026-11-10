def check_digit(digits):
    return sum((int(c) for c in digits)) % 10
