def count_retries(log: str) -> int:
    return log.lower().count("retry")
