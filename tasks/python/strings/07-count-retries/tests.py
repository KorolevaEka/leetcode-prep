import pytest
from solution import count_retries


@pytest.mark.parametrize("log, expected", [
    ("Retrying step 3", 1),
    ("RETRY retry", 2),
    ("step ok\nstep ok", 0),
    ("", 0),
    ("retryretry", 2),
    ("attempt 1 failed\nretry 1\nattempt 2 failed\nRetry 2\nok", 2),
    ("Retry: retrying, will retry", 3),
    ("retr y", 0),
])
def test_count_retries(log, expected):
    assert count_retries(log) == expected
