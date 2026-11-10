def common_step(a, b):
    return b if b == 0 else common_step(b, a % b)
