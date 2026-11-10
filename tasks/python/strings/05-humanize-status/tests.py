import pytest
from solution import humanize_status


@pytest.mark.parametrize("code, expected", [
    ("TEST_FAILED_ON_RETRY", "Test failed on retry"),
    ("PASSED", "Passed"),
    ("SETUP__ERROR", "Setup  error"),
    ("", ""),
    ("skipped", "Skipped"),
    ("mIxEd_cAsE", "Mixed case"),
    ("A", "A"),
    ("flaky_", "Flaky "),
])
def test_humanize_status(code, expected):
    assert humanize_status(code) == expected
