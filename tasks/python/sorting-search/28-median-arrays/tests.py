import pytest
from solution import two_archive_median as solve

@pytest.mark.parametrize('args, expected', [(([1, 3], [2]), 2), (([1, 2], [3, 4]), 2.5), (([], [2]), 2), (([-5, -1], [-2]), -2), (([0, 0], [0, 0]), 0)])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = ([1, 3], [2])
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_median_against_sorted_union():
    import random
    rng=random.Random(21)
    for _ in range(150):
        a=sorted(rng.randint(-9,9) for _ in range(rng.randint(0,8)))
        b=sorted(rng.randint(-9,9) for _ in range(rng.randint(0,8)))
        merged=sorted(a+b)
        if merged:
            n=len(merged); expected=(merged[(n-1)//2]+merged[n//2])/2
            assert solve(a,b)==expected


def test_binary_search_does_not_merge_archives():
    class IndexedArchive(list):
        def __iter__(self):
            raise AssertionError('Архив нужно читать по индексам, а не копировать целиком')

        def __add__(self, other):
            raise AssertionError('Слияние архивов запрещено условием')

        def __getitem__(self, key):
            if isinstance(key, slice):
                raise AssertionError('Не создавай копии участков архива')
            return super().__getitem__(key)

    assert solve(IndexedArchive(range(0, 40000, 2)), IndexedArchive(range(1, 40000, 2))) == 19999.5
