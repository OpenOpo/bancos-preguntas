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
MAX_PORT_ATTEMPTS = 20
BANK_NAME_MARKER = "_banco"
HIERARCHY_SEPARATOR = "__"
UPPERCASE_WORDS = {"ce", "eacv", "lo", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}


def pretty_part(value: str) -> str:
    words = value.replace("_", " ").strip().split()
    pretty_words = []
    for word in words:
        lower = word.lower()
        pretty_words.append(lower.upper() if lower in UPPERCASE_WORDS else word.capitalize())
    return " ".join(pretty_words)


def bank_hierarchy(path: Path) -> list[str]:
    try:
        relative = path.relative_to(QUESTIONS_DIR)
    except ValueError:
        relative = path

    folder_parts = [pretty_part(part) for part in relative.parts[:-1]]
    stem = path.stem
    raw_title = stem.split(BANK_NAME_MARKER, 1)[0]
    file_parts = [
        pretty_part(part)
        for part in raw_title.split(HIERARCHY_SEPARATOR)
        if part.strip()
    ]
    return folder_parts + file_parts


def bank_title(path: Path) -> str:
    return " / ".join(bank_hierarchy(path))


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
                "title": bank_title(path),
                "hierarchy": bank_hierarchy(path),
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

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

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


def open_browser(port: int) -> None:
    webbrowser.open(f"http://{HOST}:{port}")


def create_server() -> tuple[ThreadingHTTPServer, int]:
    for port in range(PORT, PORT + MAX_PORT_ATTEMPTS):
        try:
            return ThreadingHTTPServer((HOST, port), Handler), port
        except OSError:
            continue
    raise OSError(f"No hay puertos libres entre {PORT} y {PORT + MAX_PORT_ATTEMPTS - 1}.")


def main() -> None:
    QUESTIONS_DIR.mkdir(exist_ok=True)
    server, port = create_server()
    print("")
    print("Visor local de bancos de preguntas")
    print(f"Carpeta escaneada: {QUESTIONS_DIR}")
    print(f"URL: http://{HOST}:{port}")
    if port != PORT:
        print(f"Nota: el puerto {PORT} estaba ocupado; se ha usado el puerto {port}.")
    print("Añade o elimina archivos CSV en preguntas/ y recarga la página.")
    print("Pulsa Ctrl+C para detener el servidor.")
    print("")
    threading.Timer(0.8, open_browser, args=(port,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
