"""Проверка задачи. Работает внутри контейнера py: python check.py python/0001-two-sum"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def tasks() -> list[str]:
    return sorted(f"{p.parent.parent.name}/{p.parent.name}"
                  for kind in ("python", "sql") for p in ROOT.glob(f"{kind}/*/README.md"))


def solution_file(task: str) -> Path:
    return ROOT / task / ("solution.py" if task.startswith("python/") else "solution.sql")


def check(task: str) -> tuple[bool, str]:
    d = ROOT / task
    if task.startswith("python/"):
        r = subprocess.run(["pytest", "-q", "-p", "no:cacheprovider", str(d)],
                           capture_output=True, text=True)
        return r.returncode == 0, r.stdout + r.stderr

    # schema.sql пересоздаёт схему t, оба файла идут в одной сессии.
    # Порядок строк не важен (сортируем), для задач с ORDER BY — смотреть глазами.
    r = subprocess.run(
        ["psql", "-X", "-q", "-v", "ON_ERROR_STOP=1", "--csv",
         "-f", str(d / "schema.sql"), "-f", str(d / "solution.sql")],
        capture_output=True, text=True,
        env={**os.environ, "PGOPTIONS": "-c client_min_messages=warning"},
    )
    if r.returncode:
        return False, r.stderr
    actual = r.stdout.strip().splitlines()
    expected = (d / "expected.csv").read_text().strip().splitlines()
    if sorted(actual) == sorted(expected):
        return True, "OK\n\n" + r.stdout
    return False, "--- expected\n" + "\n".join(expected) + "\n\n--- actual\n" + r.stdout


if __name__ == "__main__":
    ok, out = check(sys.argv[1].rstrip("/"))
    print(out)
    sys.exit(0 if ok else 1)
