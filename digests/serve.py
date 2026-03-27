#!/usr/bin/env python3
import http.server
import threading
import webbrowser
import os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(f"Serving read-rd at http://localhost:{PORT}")
threading.Timer(0.5, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=PORT)
