"""Собирает все задачи в один JSON для сайта: python build.py > _site/tasks.json"""
import json

from check import ROOT, solution_file, tasks

FILES = {"python": ["test_solution.py"], "sql": ["schema.sql", "expected.csv"]}


def task_list() -> list[dict]:
    out = []
    for t in tasks():
        kind = t.split("/")[0]
        out.append({
            "id": t,
            "kind": kind,
            "readme": (ROOT / t / "README.md").read_text(),
            "solution": solution_file(t).read_text(),
            "files": {f: (ROOT / t / f).read_text() for f in FILES[kind]},
        })
    return out


if __name__ == "__main__":
    print(json.dumps(task_list(), ensure_ascii=False))
