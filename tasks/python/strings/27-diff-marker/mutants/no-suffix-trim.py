def diff_marker(expected: str, actual: str) -> str:
    if expected == actual:
        return expected
    limit = min(len(expected), len(actual))
    p = 0
    while p < limit and expected[p] == actual[p]:
        p += 1
    q = 0
    exp_mid = expected[p:len(expected) - q]
    act_mid = actual[p:len(actual) - q]
    return expected[:p] + "[-" + exp_mid + "+" + act_mid + "]" + expected[len(expected) - q:]
