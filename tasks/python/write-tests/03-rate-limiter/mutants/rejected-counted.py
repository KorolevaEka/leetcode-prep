class RateLimiter:
    """Не больше `limit` запросов на ключ за скользящее окно в `window` секунд."""

    def __init__(self, limit: int, window: float):
        self.limit = limit
        self.window = window
        self._hits: dict[str, list[float]] = {}

    def allow(self, key: str, now: float) -> bool:
        hits = [t for t in self._hits.get(key, []) if t > now - self.window]
        allowed = len(hits) < self.limit
        hits.append(now)
        self._hits[key] = hits
        return allowed
