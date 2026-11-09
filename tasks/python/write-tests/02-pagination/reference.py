import pytest
from solution import paginate

ITEMS = [1, 2, 3, 4, 5, 6, 7]


def test_first_page():
    assert paginate(ITEMS, 1, 3) == [1, 2, 3]


def test_middle_page():
    assert paginate(ITEMS, 2, 3) == [4, 5, 6]


def test_last_page_is_partial():
    assert paginate(ITEMS, 3, 3) == [7]


def test_page_beyond_end_is_empty():
    assert paginate(ITEMS, 4, 3) == []


def test_exact_fit():
    assert paginate([1, 2, 3, 4], 2, 2) == [3, 4]


def test_empty_list():
    assert paginate([], 1, 5) == []


def test_per_page_larger_than_list():
    assert paginate([1, 2], 1, 10) == [1, 2]


@pytest.mark.parametrize("page", [0, -1])
def test_invalid_page(page):
    with pytest.raises(ValueError):
        paginate(ITEMS, page, 3)


@pytest.mark.parametrize("per_page", [0, -5])
def test_invalid_per_page(per_page):
    with pytest.raises(ValueError):
        paginate(ITEMS, 1, per_page)
