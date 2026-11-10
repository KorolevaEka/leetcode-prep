def endpoint_stats(calls: list[tuple[str, int]]) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {}
    for endpoint, ms in calls:
        if endpoint not in stats:
            stats[endpoint] = {"count": 0, "min": ms, "max": ms, "total": 0}
        else:
            s = stats[endpoint]
            s["count"] += 1
            s["min"] = min(s["min"], ms)
            s["max"] = max(s["max"], ms)
            s["total"] += ms
    return stats
