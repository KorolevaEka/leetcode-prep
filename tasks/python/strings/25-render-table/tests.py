import pytest
from solution import render_table


def lines(*rows):
    return "\n".join(rows)


def test_readme_example():
    result = render_table(["test", "ms", "note"], [["login", 120, None], ["checkout", 95.5, "slow"]])
    assert result == lines(
        "| test     | ms   | note |",
        "|----------|------|------|",
        "| login    |  120 |      |",
        "| checkout | 95.5 | slow |",
    )


def test_no_rows():
    assert render_table(["a"], []) == lines("| a |", "|---|")


def test_header_wider_than_data():
    assert render_table(["status"], [["ok"]]) == lines("| status |", "|--------|", "| ok     |")


def test_numbers_right_aligned():
    assert render_table(["n"], [[5], [1000], [-3]]) == lines(
        "| n    |", "|------|", "|    5 |", "| 1000 |", "|   -3 |")


def test_none_is_blank():
    assert render_table(["a", "b"], [[None, 1]]) == lines("| a | b |", "|---|---|", "|   | 1 |")


def test_numeric_strings_stay_left():
    assert render_table(["id"], [["42"], ["7"]]) == lines("| id |", "|----|", "| 42 |", "| 7  |")


def test_float():
    assert render_table(["t"], [[2.5]]) == lines("| t   |", "|-----|", "| 2.5 |")


def test_width_comes_from_data():
    assert render_table(["a", "b"], [["long text", "x"]]) == lines(
        "| a         | b |", "|-----------|---|", "| long text | x |")
