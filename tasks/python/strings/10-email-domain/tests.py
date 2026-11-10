import pytest
from solution import email_domain


@pytest.mark.parametrize("email, expected", [
    ("Ann@Example.COM", "example.com"),
    ("  bob@mail.io  ", "mail.io"),
    ("a@b@c", ""),
    ("nobody", ""),
    ("user@", ""),
    ("", ""),
    ("@x.io", "x.io"),
    ("   ", ""),
    ("qa.team@sub.Corp.org", "sub.corp.org"),
])
def test_email_domain(email, expected):
    assert email_domain(email) == expected
