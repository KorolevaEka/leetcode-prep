def unique_in_order(messages: list[str]) -> list[str]:
    seen: set[str] = set()
    result = []
    for message in messages:
        if message not in seen:
            seen.add(message)
            result.append(message)
    return result
