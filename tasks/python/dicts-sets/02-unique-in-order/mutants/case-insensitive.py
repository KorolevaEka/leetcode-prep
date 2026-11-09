def unique_in_order(messages: list[str]) -> list[str]:
    seen: set[str] = set()
    result = []
    for message in messages:
        if message.lower() not in seen:
            seen.add(message.lower())
            result.append(message)
    return result
