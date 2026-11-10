import pytest
from solution import unescape_log


@pytest.mark.parametrize("s, expected", [
    (r"a\nb", "a\nb"),
    (r"a\tb", "a\tb"),
    (r"say \"hi\"", 'say "hi"'),
    (r"C:\\tmp", "C:\\tmp"),
    (r"\\n", "\\n"),
    (r"\x41\x7a", "Az"),
    (r"\xe9", "\u00e9"),
    (r"\x4", "\\x4"),
    (r"\x4g", "\\x4g"),
    (r"\xZZ", "\\xZZ"),
    (r"\q", "\\q"),
    ("end\\", "end\\"),
    ("", ""),
    ("plain text", "plain text"),
    (r"\\\\", "\\\\"),
    (r"\\x41", "\\x41"),
    (r"\x41\q\x4", "A\\q\\x4"),
])
def test_unescape(s, expected):
    assert unescape_log(s) == expected
