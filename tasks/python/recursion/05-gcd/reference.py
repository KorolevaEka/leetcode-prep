def common_step(a, b):
    return a if b == 0 else common_step(b, a % b)
