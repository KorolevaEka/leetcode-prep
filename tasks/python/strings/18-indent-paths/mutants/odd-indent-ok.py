def suite_paths(text: str) -> list[str]:
    stack = []
    result = []
    for line in text.split("\n"):
        if not line.strip(" "):
            continue
        lead = len(line) - len(line.lstrip(" "))
        if line[lead] == "\t":
            raise ValueError("tab in indentation")
        level = lead // 2
        if level > len(stack):
            raise ValueError("too deep")
        del stack[level:]
        stack.append(line[lead:].rstrip())
        result.append("/".join(stack))
    return result
