import http.server
import socketserver
import json
import os
import hashlib
import time

PORT = 8080
DIRECTORY = os.path.expanduser("~/GGTI_NODE")

class GGTIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ledger_path = os.path.join(DIRECTORY, "global_technical_manifest.json")
            try:
                with open(ledger_path, 'r') as f:
                    ledger = json.load(f)
                last_tx = ledger[-1]
                html = f"""
                <html>
                <body style="background:#000;color:#0f0;font-family:monospace;padding:20px;">
                    <h2>══ GGTI ACTIVE FINANCIAL LINK ══</h2>
                    <p>NODE: MOTO_G_2026 | ZIP: 49203</p><hr>
                    <p>EVENT: {last_tx['event']}</p>
                    <p>ASSET: ${last_tx['asset']} USD</p>
                    <p>TARGET: {last_tx['agent_2']}</p>
                    <p>STATUS: <span style="background:#0f0;color:#000;">EMITTED_PERMANENT</span></p>
                    <p>SEAL: {hashlib.sha256(str(last_tx).encode()).hexdigest()[:32]}...</p>
                </body></html>"""
            except Exception as e:
                html = f"<html><body><h2>GGTI ERROR: {str(e)}</h2></body></html>"
            self.wfile.write(html.encode())

def execute_solve_gate():
    print("\n" + "═"*50 + "\n GGTI CRYPTO GATEWAY INITIATION\n" + "═"*50)
    difficulty, nonce = 4, 0
    while True:
        if hashlib.sha256(f"AUTH_{nonce}".encode()).hexdigest().startswith('0' * difficulty):
            print(f"PUZZLE SOLVED: NONCE {nonce}")
            return True
        nonce += 1

if __name__ == "__main__":
    if execute_solve_gate():
        with socketserver.TCPServer(("", PORT), GGTIHandler) as httpd:
            print(f"\n[!] GGTI LINK LIVE: http://127.0.0.1:{PORT}")
            httpd.serve_forever()
