import pytest
from solution import run_order


def test_examples():
    assert run_order({"login": [], "cart": ["login", "catalog"]}) == ["catalog", "login", "cart"]
    with pytest.raises(ValueError):
        run_order({"a": ["b"], "b": ["a"]})


def test_empty():
    assert run_order({}) == []


def test_alphabetical_among_ready():
    assert run_order({"b": [], "a": [], "c": ["a", "b"]}) == ["a", "b", "c"]


def test_freed_test_competes_with_others():
    deps = {"x": [], "y": ["x"], "b": ["x"], "q": []}
    assert run_order(deps) == ["q", "x", "b", "y"]


def test_prereq_only_names_are_included():
    assert run_order({"t": ["setup", "db"]}) == ["db", "setup", "t"]


def test_duplicate_prereq():
    assert run_order({"b": ["a", "a"], "a": []}) == ["a", "b"]


def test_self_dependency_is_cycle():
    with pytest.raises(ValueError):
        run_order({"a": ["a"]})


def test_cycle_hidden_behind_valid_part():
    with pytest.raises(ValueError):
        run_order({"ok": [], "a": ["ok", "c"], "b": ["a"], "c": ["b"]})


def test_input_not_mutated():
    deps = {"b": ["a"], "a": []}
    run_order(deps)
    assert deps == {"b": ["a"], "a": []}


def test_larger_chain_and_fan():
    deps = {f"t{i:03d}": [f"t{i - 1:03d}"] for i in range(1, 500)}
    deps["t000"] = []
    assert run_order(deps) == [f"t{i:03d}" for i in range(500)]
    fan = {f"z{i}": ["root"] for i in range(5)}
    assert run_order(fan) == ["root", "z0", "z1", "z2", "z3", "z4"]
