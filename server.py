#!/usr/bin/env python3
"""HTTP 请求 Demo：提供用户信息接口和静态页面。"""

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DemoHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/user":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"name": "simon"}).encode("utf-8"))
        else:
            super().do_GET()


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), DemoHandler)
    print(f"服务已启动: http://127.0.0.1:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
