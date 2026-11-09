"""Локальный режим сайта: http://localhost:8000. Код запускается в браузере, сервер только отдаёт
задачи и сохраняет решения в файлы, чтобы агент их видел."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from build import task_list
from check import ROOT, solution_file, tasks

STATIC = {"/": "index.html", "/py-worker.js": "py-worker.js"}


class Handler(BaseHTTPRequestHandler):
    def send(self, code: int, body: bytes, ctype: str = "application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in STATIC:
            f = STATIC[path]
            return self.send(200, (ROOT / f).read_bytes(), "text/html" if f.endswith("html") else "text/javascript")
        if path == "/tasks.json":
            return self.send(200, json.dumps(task_list(), ensure_ascii=False).encode())
        self.send(404, b"{}")

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path != "/api/save" or body.get("id") not in tasks():  # заодно защита от ../
            return self.send(404, b"{}")
        solution_file(body["id"]).write_text(body["code"])
        self.send(200, b"{}")


if __name__ == "__main__":
    print("http://localhost:8000")
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
