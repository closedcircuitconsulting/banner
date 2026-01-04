#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import signal
import threading

BANNER = """
  ######   ######   ######  
 ##    ## ##    ## ##    ## 
 ##       ##       ##       
 ##       ##       ##       
 ##       ##       ##       
 ##    ## ##    ## ##    ## 
  ######   ######   ######  

"""

class BannerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(BANNER.encode())
    
    def log_message(self, format, *args):
        print(f"{self.client_address[0]} - {format % args}")

server = None

def signal_handler(sig, frame):
    print("Shutting down...")
    if server:
        threading.Thread(target=server.shutdown).start()

def run(port=8080):
    global server
    server = HTTPServer(("0.0.0.0", port), BannerHandler)
    
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    
    print(f"Starting banner server on port {port}...")
    server.serve_forever()
    print(f"Server stopped")

if __name__ == '__main__':
    run()
