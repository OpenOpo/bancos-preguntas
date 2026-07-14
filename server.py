#!/usr/bin/env python3
from __future__ import annotations

import json
import mimetypes
import os
import threading
import webbrowser
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

APP_DIR = Path(__file__).resolve().parent
QUESTIONS_DIR = APP_DIR / "preguntas"
HOST = "127.0.0.1"
PORT = 8000


def discover_csv_files() -> list[dict]:
    QUESTIONS_DIR.mkdir(exist_ok=True)
    files = []
    for path in sorted(QUESTIONS_DIR.rglob("*.csv"), key=lambda p: str(p).lower()):
        if not path.is_file():
            continue
        relative = path.relative_to(QUESTIONS_DIR).as_posix()
        files.append(
            {
                "path": relative,
                "name": path.name,
                "size_bytes": path.stat().st_size,
            }
        )
    return files


def safe_question_path(relative_path: str) -> Path | None:
    try:
        candidate = (QUESTIONS_DIR / unquote(relative_path)).resolve()
        root = QUESTIONS_DIR.resolve()
        candidate.relative_to(root)
    except (ValueError, OSError):
        return None
    if candidate.suffix.lower() != ".csv" or not candidate.is_file():
        return None
    return candidate


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def log_message(self, format: str, *args) -> None:
        print(f"[visor] {self.address_string()} - {format % args}")

    def send_json(self, payload: object, status: int = 200) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path in {"/preguntas/manifest.json", "/api/files"}:
            self.send_json({"files": discover_csv_files()})
            return

        if parsed.path == "/api/csv":
            query = parse_qs(parsed.query)
            requested = query.get("path", [""])[0]
            path = safe_question_path(requested)
            if path is None:
                self.send_json({"error": "CSV no encontrado o ruta no permitida."}, HTTPStatus.NOT_FOUND)
                return

            data = path.read_bytes()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Content-Disposition", f'inline; filename="{path.name}"')
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)
            return

        if parsed.path == "/":
            self.path = "/index.html"

        super().do_GET()


def open_browser() -> None:
    webbrowser.open(f"http://{HOST}:{PORT}")


def main() -> None:
    QUESTIONS_DIR.mkdir(exist_ok=True)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("")
    print("Visor local de preguntas GVA C1")
    print(f"Carpeta escaneada: {QUESTIONS_DIR}")
    print(f"URL: http://{HOST}:{PORT}")
    print("Añade o elimina archivos CSV en preguntas/ y pulsa «Volver a escanear» en la web.")
    print("Pulsa Ctrl+C para detener el servidor.")
    print("")
    threading.Timer(0.8, open_browser).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
