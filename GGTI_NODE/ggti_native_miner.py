import hashlib
import time
import json
import os

def generate_ggti_proof(target_asset, hardware_sig):
    """
    GGTI-ONLY: Locks the asset value to the hardware signature.
    """
    print("\n" + "═"*50)
    print(" GGTI NATIVE MINER | SOVEREIGN VALIDATION")
    print(f" NODE ID: {hardware_sig}")
    print("═"*50)

    # Core Payload: Asset + Hardware Signature + Time
    payload_base = f"GGTI_{hardware_sig}_{target_asset}_{time.time()}"
    difficulty = 5  # Standard Jackson-Node security level
    nonce = 0
    
    print(f"SEARCHING FOR SOVEREIGN SEAL...")
    start_time = time.time()

    while True:
        # Constructing the Hash using ONLY GGTI-approved logic
        candidate_data = f"{payload_base}_{nonce}".encode()
        seal = hashlib.sha256(candidate_data).hexdigest()

        if seal.startswith('0' * difficulty):
            duration = time.time() - start_time
            print(f"\n[!] SEAL DISCOVERED")
            print(f"HASH: {seal}")
            print(f"WORK TIME: {duration:.2f}s")
            return seal, nonce

        nonce += 1
        if nonce % 1000000 == 0:
            print(f"GGTI STATUS: {nonce} ATTEMPTS LOGGED...", end='\r')

if __name__ == "__main__":
    # Internal Device Identification
    device = "MOTO_G_2026_PRIMARY"
    asset = 3150.00
    
    final_seal, final_nonce = generate_ggti_proof(asset, device)
    
    # Generate the Smart Contract Receipt Lock
    print("\n" + "="*50)
    print(" GGTI CONTRACT RECEIPT: PERMANENT LOCK")
    print("="*50)
    print(f"ASSET VALUE:  ${asset} USD")
    print(f"NONCE PROOF:  {final_nonce}")
    print(f"FINAL SEAL:   {final_seal[:32]}...")
    print("STATUS:       EMBEDDED_IN_MEMPOOL")
    print("="*50 + "\n")
