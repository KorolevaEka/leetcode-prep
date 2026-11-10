def report_row(name: str, status: str, width: int) -> str:
    return f"{name:<{width}} | {status:>6}"
