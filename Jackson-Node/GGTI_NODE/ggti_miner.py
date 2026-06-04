import hashlib, time, json, os

class GGTIMiner:
    def __init__(self, difficulty=5):
        self.difficulty = difficulty
        self.genesis_path = os.path.expanduser("~/Jackson-Node/sovereign_blockchain_genesis.json")
        self.recipient = "13exxw5Tnxg5rgUqxSc3xRZ8yy9ZzeC37t"
        self.tax_rate = 0.15 # 15% Tax Reserve Earmark

    def update_ledger(self):
        try:
            with open(self.genesis_path, 'r') as f:
                ledger = json.load(f)
            
            last_hash = ledger.get("last_block_hash", "0000xGENESIS")
            raw_value = 3150.00
            
            # Tax Calculation Logic
            tax_liability = raw_value * self.tax_rate
            spendable_funds = raw_value - tax_liability
            
            block_data = f"LIQUIDITY_RECON_SPENDABLE:${spendable_funds}_TAX_RESERVE:${tax_liability}"
            
            # Proof of Work
            nonce = 0
            while True:
                text = f"{last_hash}{block_data}{self.recipient}{nonce}"
                guess_hash = hashlib.sha256(text.encode()).hexdigest()
                if guess_hash[:self.difficulty] == "0" * self.difficulty:
                    break
                nonce += 1
            
            ledger.update({
                "last_block_hash": guess_hash,
                "gross_value": raw_value,
                "spendable_funds": spendable_funds,
                "tax_reserve": tax_liability,
                "status": "TAX_VERIFIED_LIQUID",
                "timestamp": time.time()
            })
            
            with open(self.genesis_path, 'w') as f:
                json.dump(ledger, f, indent=4)
            
            print(f"[✔] LIQUIDITY RECONCILED: Spendable ${spendable_funds} | Tax Hold ${tax_liability}")
            return guess_hash
        except Exception as e:
            print(f"[X] LEDGER ERROR: {e}")
