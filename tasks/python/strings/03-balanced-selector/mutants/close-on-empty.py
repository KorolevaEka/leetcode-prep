def is_balanced(selector: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in selector:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs and stack:
            if stack.pop() != pairs[ch]:
                return False
    return not stack
