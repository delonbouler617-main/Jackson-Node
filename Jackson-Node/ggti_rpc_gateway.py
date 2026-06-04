import os
import requests

# Hard link to the newly generated user trust store folder
CUSTOM_CERT_PATH = os.path.expanduser("~/.ggti_ssl/certs/node_root.crt")

def transmit_payload(target_node_url, payload_data):
    """
    Transmits financial or ledger payloads through the secure local user cert anchor.
    """
    try:
        print(f"[GGTI_RPC] Initiating secure handshake with: {target_node_url}")
        response = requests.post(target_node_url, json=payload_data, verify=CUSTOM_CERT_PATH)
        print(f"[GGTI_RPC] Transmission Successful. Status: {response.status_code}")
        return response.json()
    except requests.exceptions.SSLError as ssl_err:
        print(f"[CRITICAL_ERROR] Handshake rejected by User Trust Layer: {ssl_err}")
    except Exception as e:
        print(f"[ERROR] Communication exception encountered: {e}")

if __name__ == "__main__":
    print("[ENGINE] GGTI Secure Network Module verified and ready for execution loops.")
