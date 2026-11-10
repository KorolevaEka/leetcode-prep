import pytest
from solution import file_extension


@pytest.mark.parametrize("path, expected", [
    ("logs/run.1/Trace.TAR.GZ", "gz"),
    ("dir.v2/readme", ""),
    ("cfg/.gitignore", ""),
    ("report.PDF", "pdf"),
    ("a.tar.gz", "gz"),
    ("file.", ""),
    ("noext", ""),
    (".env", ""),
    (".config.json", "json"),
    ("", ""),
    ("out/", ""),
])
def test_file_extension(path, expected):
    assert file_extension(path) == expected
