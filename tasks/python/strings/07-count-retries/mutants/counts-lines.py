def count_retries(log: str) -> int:
    return sum(1 for line in log.lower().splitlines() if "retry" in line)
