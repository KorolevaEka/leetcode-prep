def retry_delays(retries: int, base: int, cap: int) -> list[int]:
    delays = []
    delay = base
    for _ in range(retries):
        delays.append(min(delay, cap))
        delay *= 2
    return delays
