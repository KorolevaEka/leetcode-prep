"""Собирает сайт: python3 scripts/build.py _site  |  python3 scripts/build.py --json"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXT = {"python": "py", "sql": "sql", "ts": "ts", "java": "java"}
LEVELS = {"easy", "medium", "hard"}
KINDS = {"code", "tests"}


class TaskFormatError(Exception):
    def __init__(self, path, message):
        super().__init__(f"{path}: {message}")
        self.path, self.message = path, message


def _read(d: Path, name: str) -> str:
    f = d / name
    if not f.is_file():
        raise TaskFormatError(d, f"нет файла {name}")
    return f.read_text()


def _load_task(d: Path, lang: str, topic: str, topic_ids: set) -> dict:
    ext = EXT[lang]
    if topic not in topic_ids:
        raise TaskFormatError(d, f"тема «{topic}» не описана в topics.json")
    num, _, slug = d.name.partition("-")
    if not num.isdigit() or not slug:
        raise TaskFormatError(d, "имя папки должно быть NN-slug")
    meta = json.loads(_read(d, "task.json"))
    for key in ("title", "level", "kind", "hints", "mutants"):
        if key not in meta:
            raise TaskFormatError(d, f"в task.json нет «{key}»")
    if meta["level"] not in LEVELS:
        raise TaskFormatError(d, f"level «{meta['level']}»: ждём easy | medium | hard")
    if meta["kind"] not in KINDS:
        raise TaskFormatError(d, f"kind «{meta['kind']}»: ждём code | tests")
    if lang == "sql" and meta["kind"] != "code":
        raise TaskFormatError(d, "у sql только kind=code")
    mutants = meta["mutants"]
    if len(mutants) < 2:
        raise TaskFormatError(d, "нужно минимум 2 мутанта")
    for name, desc in mutants.items():
        if not str(desc).strip():
            raise TaskFormatError(d, f"у мутанта «{name}» нет описания")
    rec = {
        "id": f"{lang}/{topic}/{d.name}", "lang": lang, "topic": topic, "order": int(num),
        "level": meta["level"], "kind": meta["kind"], "title": meta["title"],
        "readme": _read(d, "README.md"), "hints": meta["hints"], "starter": _read(d, f"starter.{ext}"),
    }
    _read(d, f"reference.{ext}")
    codes = {name: _read(d / "mutants", f"{name}.{ext}") for name in mutants}
    if lang == "sql":
        rec["schema"], rec["expected"] = _read(d, "schema.sql"), _read(d, "expected.csv")
    elif meta["kind"] == "code":
        rec["tests"] = _read(d, f"tests.{ext}")
    else:
        rec["subject"] = _read(d, f"subject.{ext}")
        rec["mutants"] = [{"name": n, "description": mutants[n], "code": codes[n]} for n in mutants]
    return rec


def load_tasks(root: Path = ROOT) -> list[dict]:
    topics = json.loads((root / "topics.json").read_text())
    out = []
    for lang, tlist in topics.items():
        ids = {t["id"] for t in tlist}
        base = root / "tasks" / lang
        found = sorted(base.glob("*/*/")) if base.is_dir() else []
        for d in found:
            if d.parent.name not in ids:
                raise TaskFormatError(d, f"тема «{d.parent.name}» не описана в topics.json")
        tasks = [_load_task(d, lang, d.parent.name, ids) for d in found]
        order = {t["id"]: i for i, t in enumerate(tlist)}
        out += sorted(tasks, key=lambda t: (order[t["topic"]], t["order"]))
    return out


def build_site(root: Path, out: Path) -> None:
    tasks = load_tasks(root)
    shutil.copytree(root / "web", out, dirs_exist_ok=True)
    (out / "tasks.json").write_text(json.dumps(tasks, ensure_ascii=False))
    shutil.copy(root / "topics.json", out / "topics.json")


if __name__ == "__main__":
    if sys.argv[1:] == ["--json"]:
        print(json.dumps(load_tasks(), ensure_ascii=False))
    elif len(sys.argv) == 2:
        build_site(ROOT, Path(sys.argv[1]))
    else:
        sys.exit(__doc__)
