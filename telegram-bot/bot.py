from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Это ответ, который игра получит вместо "Not Found"
FAKE_RESPONSE = {
    "status": "success",
    "message": "Key verification passed",
    "license": "active"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[+] Игра запросила: {self.path}")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(FAKE_RESPONSE).encode())

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode()
        print(f"[+] Игра прислала данные: {body}")
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(FAKE_RESPONSE).encode())

print("[*] Запускаем фейковый сервер на порту 9999...")
print("[*] Игра должна стучаться сюда: http://10.0.2.2:9999/api/")
HTTPServer(("0.0.0.0", 9999), Handler).serve_forever()
