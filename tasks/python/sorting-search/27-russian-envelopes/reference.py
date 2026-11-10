from bisect import bisect_left, bisect_right

def nesting_depth(sizes):
    tails = []
    for w, h in sorted(sizes, key=lambda x: (x[0], -x[1])):
        i = bisect_left(tails, h)
        if i == len(tails):
            tails.append(h)
        else:
            tails[i] = h
    return len(tails)
