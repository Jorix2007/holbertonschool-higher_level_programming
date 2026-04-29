import http.server
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom handler class that subclasses BaseHTTPRequestHandler.
    We override the do_GET method to handle incoming GET requests.
    """
    def do_GET(self):
        # Endpoint: /
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            
        # Endpoint: /data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            # Convert dictionary to JSON string, then encode to bytes
            self.wfile.write(json.dumps(dataset).encode('utf-8'))
            
        # Endpoint: /status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            
        # Endpoint: /info
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode('utf-8'))
            
        # Error Handling: 404 Not Found for undefined endpoints
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    """
    Starts the HTTP server on port 8000.
    """
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server on port {PORT}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
