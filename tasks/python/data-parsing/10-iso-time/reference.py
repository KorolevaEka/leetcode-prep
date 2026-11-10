from datetime import datetime, timezone

def utc_seconds(text):
    dt = datetime.strptime(text, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    return int(dt.timestamp())
