import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Subclass of BaseHTTPRequestHandler to handle API requests.
    """

    def do_GET(self):
        """
        Handles GET requests and routes them to specific endpoints.
        """
        if self.path == '/':
            # Hello message endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # JSON Data endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))

        elif self.path == '/status':
            # API status check endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Additional info endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        else:
            # Error handling: 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Starts the HTTP server on port 8000.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
