"""Локальный сервер: python3 scripts/serve.py -> http://localhost:8000
Отдаёт web/, topics.json, живой индекс /tasks.json и /tasks/<id>.json (собираются на каждый запрос)."""
import json
import mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

from build import ROOT, TaskFormatError, index_record, load_tasks

WEB = (ROOT / "web").resolve()


class Handler(BaseHTTPRequestHandler):
    def send(self, code: int, body: bytes, ctype: str = "application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/tasks.json" or (path.startswith("/tasks/") and path.endswith(".json")):
            try:
                tasks = load_tasks()
            except TaskFormatError as e:
                return self.send(500, json.dumps({"error": str(e)}, ensure_ascii=False).encode())
            if path == "/tasks.json":
                return self.send(200, json.dumps([index_record(t) for t in tasks], ensure_ascii=False).encode())
            found = next((t for t in tasks if t["id"] == unquote(path[len("/tasks/"):-len(".json")])), None)
            if found:
                return self.send(200, json.dumps(found, ensure_ascii=False).encode())
            return self.send(404, b"{}")
        if path == "/topics.json":
            return self.send(200, (ROOT / "topics.json").read_bytes())
        f = (WEB / path.lstrip("/") / "index.html").resolve() if path.endswith("/") else (WEB / path.lstrip("/")).resolve()
        if WEB in f.parents and f.is_file():  # заодно защита от ../
            return self.send(200, f.read_bytes(), mimetypes.guess_type(f.name)[0] or "application/octet-stream")
        self.send(404, b"{}")


if __name__ == "__main__":
    print("http://localhost:8000")
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
