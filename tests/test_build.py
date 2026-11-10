import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from build import TaskFormatError, build_site, load_tasks  # noqa: E402

LANG_EXT = {"python": "py", "sql": "sql", "ts": "ts", "java": "java"}


def make_task(root, lang, topic, slug, kind="code", level="easy", mutants=None, **meta):
    mutants = mutants if mutants is not None else {"a": "первая", "b": "вторая"}
    d = root / "tasks" / lang / topic / slug
    ext = LANG_EXT[lang]
    (d / "mutants").mkdir(parents=True)
    (d / "task.json").write_text(json.dumps(
        {"title": "T", "level": level, "kind": kind, "hints": ["h"], "mutants": mutants, **meta}))
    (d / "README.md").write_text("# условие")
    (d / f"starter.{ext}").write_text("starter")
    (d / f"reference.{ext}").write_text("reference")
    if lang == "sql":
        (d / "schema.sql").write_text("CREATE TABLE t(x int);")
        (d / "expected.csv").write_text("x\n1\n")
    elif kind == "code":
        (d / f"tests.{ext}").write_text("tests")
    else:
        (d / f"subject.{ext}").write_text("subject")
    for name in mutants:
        (d / "mutants" / f"{name}.{ext}").write_text(f"mutant {name}")
    return d


def make_topics(root, topics=None):
    topics = topics or {"python": [{"id": "strings", "title": "Строки", "description": "d"}]}
    (root / "topics.json").write_text(json.dumps(topics))


@pytest.fixture
def root(tmp_path):
    make_topics(tmp_path)
    return tmp_path


def test_task_record_fields(root):
    make_task(root, "python", "strings", "01-x")
    (t,) = load_tasks(root)
    assert t["id"] == "python/strings/01-x"
    assert t["order"] == 1
    assert t["tests"] == "tests"
    assert t["starter"] == "starter"
    assert t["hints"] == ["h"]
    assert "subject" not in t and "mutants" not in t and "reference" not in t


def test_tests_kind_ships_mutants(root):
    make_task(root, "python", "strings", "01-x", kind="tests", mutants={"empty": "пустой", "b": "вторая"})
    (t,) = load_tasks(root)
    assert t["subject"] == "subject"
    assert "tests" not in t
    assert {"name": "empty", "description": "пустой", "code": "mutant empty"} in t["mutants"]
    assert len(t["mutants"]) == 2


def test_sql_task(root):
    make_topics(root, {"sql": [{"id": "joins", "title": "JOIN", "description": "d"}]})
    make_task(root, "sql", "joins", "01-x")
    (t,) = load_tasks(root)
    assert t["schema"] == "CREATE TABLE t(x int);"
    assert t["expected"] == "x\n1\n"
    assert "tests" not in t


def test_rejects_unknown_topic(root):
    make_task(root, "python", "nope", "01-x")
    with pytest.raises(TaskFormatError):
        load_tasks(root)


def test_rejects_bad_level(root):
    make_task(root, "python", "strings", "01-x", level="impossible")
    with pytest.raises(TaskFormatError):
        load_tasks(root)


def test_rejects_sql_tests_kind(root):
    make_topics(root, {"sql": [{"id": "joins", "title": "JOIN", "description": "d"}]})
    make_task(root, "sql", "joins", "01-x", kind="tests")
    with pytest.raises(TaskFormatError):
        load_tasks(root)


def test_rejects_less_than_two_mutants(root):
    make_task(root, "python", "strings", "01-x", mutants={"a": "одна"})
    with pytest.raises(TaskFormatError):
        load_tasks(root)


def test_rejects_mutant_without_description(root):
    make_task(root, "python", "strings", "01-x", mutants={"a": "", "b": "вторая"})
    with pytest.raises(TaskFormatError):
        load_tasks(root)


@pytest.mark.parametrize("hints", ["подсказка", ["ok", ""], ["ok", 1], [None], {"a": "b"}])
def test_rejects_malformed_hints(root, hints):
    make_task(root, "python", "strings", "01-x", hints=hints)
    with pytest.raises(TaskFormatError):
        load_tasks(root)


@pytest.mark.parametrize("mutants", [["a", "b"], "ab", {"a": "x", "b": None}, {"a": "x", "b": 5}])
def test_rejects_malformed_mutants(root, mutants):
    make_task(root, "python", "strings", "01-x", mutants={"a": "x", "b": "y"})
    d = root / "tasks/python/strings/01-x"
    meta = json.loads((d / "task.json").read_text())
    meta["mutants"] = mutants
    (d / "task.json").write_text(json.dumps(meta))
    with pytest.raises(TaskFormatError):
        load_tasks(root)


def test_order_follows_topics_json(root):
    make_topics(root, {"python": [{"id": "z", "title": "Z", "description": "d"},
                                  {"id": "a", "title": "A", "description": "d"}]})
    make_task(root, "python", "a", "01-x")
    make_task(root, "python", "z", "02-y")
    make_task(root, "python", "z", "01-x")
    assert [t["id"] for t in load_tasks(root)] == ["python/z/01-x", "python/z/02-y", "python/a/01-x"]


def test_build_site(root, tmp_path_factory):
    make_task(root, "python", "strings", "01-x")
    (root / "web").mkdir()
    (root / "web" / "index.html").write_text("hi")
    out = tmp_path_factory.mktemp("out")
    build_site(root, out)
    assert (out / "index.html").read_text() == "hi"
    assert json.loads((out / "tasks.json").read_text())[0]["id"] == "python/strings/01-x"
    assert "python" in json.loads((out / "topics.json").read_text())


def test_build_site_index_and_details(root, tmp_path_factory):
    make_task(root, "python", "strings", "02-y", level="hard")
    make_task(root, "python", "strings", "01-x", kind="tests")
    (root / "web").mkdir()
    out = tmp_path_factory.mktemp("out")
    build_site(root, out)
    index = json.loads((out / "tasks.json").read_text())
    assert [t["id"] for t in index] == ["python/strings/01-x", "python/strings/02-y"]
    for t in index:
        assert set(t) == {"id", "lang", "topic", "order", "level", "kind", "title"}
    for full in load_tasks(root):
        assert json.loads((out / "tasks" / f"{full['id']}.json").read_text()) == full
