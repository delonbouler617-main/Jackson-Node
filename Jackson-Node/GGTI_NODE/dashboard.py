from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os

class GGTIDashboard(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Index all local ledger objects
            node_path = os.path.expanduser("~/GGTI_NODE")
            ledger_data = []
            for f in os.listdir(node_path):
                if f.endswith('.json'):
                    with open(os.path.join(node_path, f), 'r') as file:
                        ledger_data.append(json.load(file))

            html = f"""
            <html>
            <head><title>GGTI Node Explorer</title>
            <style>
                body {{ font-family: monospace; background: #000; color: #0f0; padding: 20px; }}
                .block {{ border: 1px solid #0f0; margin: 10px; padding: 10px; background: #111; }}
                h1 {{ border-bottom: 2px solid #0f0; }}
            </style>
            </head>
            <body>
                <h1>GGTI JACKSON-NODE-49203</h1>
                <p>STATUS: POSITIVE_STATE_INITIATED</p>
                <div>{"".join([f'<div class="block"><h3>{obj.get("txid", "CONFIG")}</h3><pre>{json.dumps(obj, indent=2)}</pre></div>' for obj in ledger_data])}</div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

print("INITIALIZING LOCAL DASHBOARD...")
print("Open your browser and go to: http://localhost:8080")
HTTPServer(('localhost', 8080), GGTIDashboard).serve_forever()
