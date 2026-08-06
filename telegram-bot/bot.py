from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse

# Это ответ, который ждет игра (например, "Ключ активирован")
FAKE_RESPONSE = {
    "status": "success",
    "message": "Key is valid",
    "data": {
        "user": "hacker",
        "expires": "2099-12-31"
    }
}

class FakeRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Парсим путь, чтобы понять, что просит игра
        parsed_path = urllib.parse.urlparse(self.path)
        print(f"[+] Получен GET-запрос: {parsed_path.path}")
        
        # Отвечаем на любой запрос одинаково
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        # Отправляем фейковый JSON
        response_json = json.dumps(FAKE_RESPONSE)
        self.wfile.write(response_json.encode('utf-8'))
        
    def do_POST(self):
        # Если игра шлет данные (например, сам ключ) через POST
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print(f"[+] Получен POST-запрос: {self.path}")
        print(f"[+] Данные от игры: {post_data.decode('utf-8')}")
        
        # Всегда отвечаем успехом
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        response_json = json.dumps(FAKE_RESPONSE)
        self.wfile.write(response_json.encode('utf-8'))

def run_server():
    server_address = ('', 8080)  # Запускаем на порту 8080
    httpd = HTTPServer(server_address, FakeRequestHandler)
    print("[*] Фейковый сервер запущен на порту 8080...")
    print("[*] Игра должна стучаться на http://10.0.2.2:8080/api/")
    print("[*] Нажми Ctrl+C, чтобы остановить.")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Сервер остановлен.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
