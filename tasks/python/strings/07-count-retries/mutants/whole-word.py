def count_retries(log: str) -> int:
    return log.lower().split().count("retry")
