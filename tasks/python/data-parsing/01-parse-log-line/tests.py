from solution import parse_line


def test_example():
    assert parse_line("2026-11-09 12:00:01 [ERROR] checkout: timeout after 30s") == {
        "time": "2026-11-09 12:00:01", "level": "ERROR", "source": "checkout", "message": "timeout after 30s"}


def test_message_with_colons():
    result = parse_line("2026-11-09 12:00:02 [INFO] api: GET /ping: ok: 200")
    assert result["source"] == "api"
    assert result["message"] == "GET /ping: ok: 200"


def test_level_without_brackets():
    assert parse_line("2026-01-01 00:00:00 [WARN] db: slow")["level"] == "WARN"


def test_time_has_date_and_clock():
    assert parse_line("2026-01-01 23:59:59 [INFO] x: y")["time"] == "2026-01-01 23:59:59"
