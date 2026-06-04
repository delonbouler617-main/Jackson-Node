#!/usr/bin/env python3
import http.server
import ssl
import os

PORT = 8443
CERT_PATH = os.path.expanduser("~/.ggti_ssl/certs/node_root.crt")
KEY_PATH = os.path.expanduser("~/Jackson-Node/security/keys/institutional_private.pem")

class GGTIDataHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/v1/ledger/broadcast':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            print(f"\n[RECEIVER] Secure Handshake Completed Successfully.")
            print(f"[RECEIVER] Payload Received: {post_data.decode('utf-8')}")
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "ACKNOWLEDGED", "sync_state": "LOCKED"}')
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    if not os.path.exists(KEY_PATH):
        print(f"[ERROR] Private key missing at {KEY_PATH}. Cannot initialize TLS.")
        return

    server_address = ('127.0.0.1', PORT)
    httpd = http.server.HTTPServer(server_address, GGTIDataHandler)
    
    # Configure the internal SSL Context structure using Python 3.13 standard layers
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)
    
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"[NODE_ENGINE] Secure listener active on https://127.0.0.1:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[NODE_ENGINE] Service paused.")

if __name__ == '__main__':
    run_server()
