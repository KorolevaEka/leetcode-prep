def retry_delays(retries: int, base: int, cap: int) -> list[int]:
    return [min(cap, base * (i + 1)) for i in range(retries)]
