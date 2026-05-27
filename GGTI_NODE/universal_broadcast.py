import json, time, base64, subprocess, os

def create_jwt(sa_email, private_key):
    now = int(time.time())
    header = {"alg": "RS256", "typ": "JWT"}
    payload = {
        "iss": sa_email, "sub": sa_email,
        "aud": "https://oauth2.googleapis.com/token",
        "iat": now, "exp": now + 3600,
        "scope": "https://www.googleapis.com/auth/cloud-platform"
    }
    b64 = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).decode().replace("=", "")
    unsigned_jwt = f"{b64(header)}.{b64(payload)}"
    with open("u.txt", "w") as f: f.write(unsigned_jwt)
    with open("p.pem", "w") as f: f.write(private_key)
    sig = subprocess.check_output("openssl dgst -sha256 -sign p.pem u.txt | openssl base64 -A", shell=True).decode().replace("+", "-").replace("/", "_").replace("=", "")
    for f in ["u.txt", "p.pem"]: os.remove(f)
    return f"{unsigned_jwt}.{sig}"

def run():
    try:
        key_path = os.path.expanduser("~/GGTI_NODE/key.json")
        settlement_path = os.path.expanduser("~/GGTI_NODE/settlement_0x9fd.json")
        with open(key_path, "r") as f:
            sa = json.load(f)
        jwt = create_jwt(sa["client_email"], sa["private_key"])
        token_data = subprocess.check_output(f'curl -s -X POST https://oauth2.googleapis.com/token -d "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion={jwt}"', shell=True)
        token = json.loads(token_data)["access_token"]
        print("AUTHENTICATED: Universal Token Generated.")
        cmd = f'curl -s -o /dev/null -w "%{{http_code}}" -X POST -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d @{settlement_path} "https://web3.googleapis.com/v1/projects/jackson-node-49203/locations/global/networks/blockchain/transactions:broadcast"'
        res = subprocess.check_output(cmd, shell=True).decode()
        print(f"BROADCAST STATUS: {res}")
    except Exception as e:
        print(f"SYSTEM_ERROR: {e}")

if __name__ == "__main__":
    run()
