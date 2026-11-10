def endpoint_stats(calls: list[tuple[str, int]]) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {}
    for endpoint, ms in calls:
        s = stats.setdefault(endpoint, {"count": 0, "min": 0, "max": 0, "total": 0})
        s["count"] += 1
        s["min"] = min(s["min"], ms)
        s["max"] = max(s["max"], ms)
        s["total"] += ms
    return stats
