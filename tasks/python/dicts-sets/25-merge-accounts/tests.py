from solution import merge_accounts


def test_examples():
    assert merge_accounts([["a@x", "b@x"], ["c@x"], ["b@x", "d@x"]]) == [["a@x", "b@x", "d@x"], ["c@x"]]
    assert merge_accounts([[], ["z@x"]]) == [["z@x"]]


def test_empty():
    assert merge_accounts([]) == []
    assert merge_accounts([[], []]) == []


def test_no_overlap():
    assert merge_accounts([["b"], ["a"]]) == [["a"], ["b"]]


def test_transitive_chain():
    accounts = [["a", "b"], ["c", "d"], ["b", "c"]]
    assert merge_accounts(accounts) == [["a", "b", "c", "d"]]


def test_late_bridge_of_three_groups():
    accounts = [["a1", "a2"], ["b1", "b2"], ["c1", "c2"], ["a2", "b2", "c2"]]
    assert merge_accounts(accounts) == [["a1", "a2", "b1", "b2", "c1", "c2"]]


def test_duplicates_within_account_and_across():
    assert merge_accounts([["a", "a", "b"], ["b", "b"]]) == [["a", "b"]]


def test_groups_sorted_not_first_seen():
    accounts = [["m", "n"], ["a"], ["z"], ["a", "q"]]
    assert merge_accounts(accounts) == [["a", "q"], ["m", "n"], ["z"]]


def test_case_sensitive_strings():
    assert merge_accounts([["A@x"], ["a@x"]]) == [["A@x"], ["a@x"]]


def test_input_not_mutated():
    accounts = [["b", "a"], ["a", "c"]]
    merge_accounts(accounts)
    assert accounts == [["b", "a"], ["a", "c"]]


def test_large_chain():
    n = 20_000
    accounts = [[f"e{i:05d}", f"e{i + 1:05d}"] for i in range(n)]
    accounts.reverse()
    result = merge_accounts(accounts)
    assert len(result) == 1
    assert result[0] == [f"e{i:05d}" for i in range(n + 1)]
