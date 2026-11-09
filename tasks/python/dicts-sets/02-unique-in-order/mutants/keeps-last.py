def unique_in_order(messages: list[str]) -> list[str]:
    result = []
    for i, message in enumerate(messages):
        if message not in messages[i + 1:]:
            result.append(message)
    return result
