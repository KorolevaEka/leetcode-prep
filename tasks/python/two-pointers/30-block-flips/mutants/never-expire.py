def min_resets(flags, k):
    ends = [0] * (len(flags) + 1)
    parity = count = 0
    for i, x in enumerate(flags):
        parity ^= 0
        if x ^ parity == 0:
            if i + k > len(flags):
                return -1
            count += 1
            parity ^= 1
            ends[i + k] ^= 1
    return count
