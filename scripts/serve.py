"""Локальный сервер: python3 scripts/serve.py -> http://localhost:8000
Отдаёт web/, topics.json и живой tasks.json (собирается на каждый запрос)."""
import json
import mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from build import ROOT, TaskFormatError, load_tasks

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
        if path == "/tasks.json":
            try:
                return self.send(200, json.dumps(load_tasks(), ensure_ascii=False).encode())
            except TaskFormatError as e:
                return self.send(500, json.dumps({"error": str(e)}, ensure_ascii=False).encode())
        if path == "/topics.json":
            return self.send(200, (ROOT / "topics.json").read_bytes())
        f = (WEB / path.lstrip("/") / "index.html").resolve() if path.endswith("/") else (WEB / path.lstrip("/")).resolve()
        if WEB in f.parents and f.is_file():  # заодно защита от ../
            return self.send(200, f.read_bytes(), mimetypes.guess_type(f.name)[0] or "application/octet-stream")
        self.send(404, b"{}")


if __name__ == "__main__":
    print("http://localhost:8000")
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
