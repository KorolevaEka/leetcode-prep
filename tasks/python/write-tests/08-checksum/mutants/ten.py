def check_digit(digits):
    return 10 - sum((int(c) for c in digits)) % 10
