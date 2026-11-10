def largest_block(heights):
    best = 0
    stack = []
    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > h:
            left, old = stack.pop()
            best = max(best, old * (i - left + 1))
            start = left
        stack.append((start, h))
    return best
