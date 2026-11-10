def power(base, exponent):
    if exponent == 0:
        return 1
    half = power(base, exponent // 2)
    return half * half * (base if exponent % 2 else 1)
