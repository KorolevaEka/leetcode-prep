"""Веб-интерфейс тренажёра: http://localhost:8000"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from check import ROOT, check, solution_file, tasks


def task_info(t: str) -> dict:
    return {
        "id": t,
        "kind": t.split("/")[0],
        "readme": (ROOT / t / "README.md").read_text(),
        "solution": solution_file(t).read_text(),
    }


class Handler(BaseHTTPRequestHandler):
    def send(self, code: int, body: bytes, ctype: str = "application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            return self.send(200, (ROOT / "index.html").read_bytes(), "text/html")
        if self.path == "/api/tasks":
            return self.send(200, json.dumps([task_info(t) for t in tasks()]).encode())
        self.send(404, b"{}")

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        t = body.get("id")
        if t not in tasks():  # заодно защита от ../
            return self.send(404, b'{"error": "unknown task"}')
        solution_file(t).write_text(body["code"])
        if self.path == "/api/save":
            return self.send(200, b"{}")
        if self.path == "/api/run":
            ok, out = check(t)
            return self.send(200, json.dumps({"ok": ok, "output": out}).encode())
        self.send(404, b"{}")


if __name__ == "__main__":
    print("http://localhost:8000")
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
