def retry_delays(retries: int, base: int, cap: int) -> list[int]:
    return [base * 2 ** i for i in range(retries)]
