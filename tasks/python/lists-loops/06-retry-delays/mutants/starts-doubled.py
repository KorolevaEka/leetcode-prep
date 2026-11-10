def retry_delays(retries: int, base: int, cap: int) -> list[int]:
    return [min(cap, base * 2 ** (i + 1)) for i in range(retries)]
