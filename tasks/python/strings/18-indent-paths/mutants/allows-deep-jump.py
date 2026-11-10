def suite_paths(text: str) -> list[str]:
    stack = []
    result = []
    for line in text.split("\n"):
        if not line.strip(" "):
            continue
        lead = len(line) - len(line.lstrip(" "))
        if line[lead] == "\t":
            raise ValueError("tab in indentation")
        if lead % 2:
            raise ValueError("odd indentation")
        level = lead // 2
        del stack[level:]
        stack.append(line[lead:].rstrip())
        result.append("/".join(stack))
    return result
