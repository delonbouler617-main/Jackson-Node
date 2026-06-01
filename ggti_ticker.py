#!/usr/bin/env python3
import json
import time
import os

LEDGER_LOG = os.path.expanduser("~/telephony_logs/wallet_balance_ledger.json")
MARKET_LOG = os.path.expanduser("~/telephony_logs/market_metrics.json")
CRYPTO_LOG = os.path.expanduser("~/telephony_logs/crypto_outbound_manifest.json")

class GGTITickerDaemon:
    def __init__(self):
        print("[TICKER] Initializing Upgraded Ledger Analytics Monitor...")

    def process_telemetry_cycle(self):
        if not os.path.exists(LEDGER_LOG) or not os.path.exists(MARKET_LOG):
            print("[TICKER_WARN] Active ledger components missing. Standing by...")
            return

        with open(LEDGER_LOG, 'r') as f:
            ledger_data = json.load(f)
        with open(MARKET_LOG, 'r') as f:
            market_data = json.load(f)

        confirmed_balance_hac = ledger_data.get("confirmed_balance", 0.0)
        current_holdings_subunits = int(confirmed_balance_hac * 100)
        initial_allocation_subunits = 50000000
        net_delta = current_holdings_subunits - initial_allocation_subunits

        # Parse outbound crypto logs if they exist
        staged_crypto_subunits = 0
        crypto_status = "NONE"
        if os.path.exists(CRYPTO_LOG):
            with open(CRYPTO_LOG, 'r') as f:
                crypto_data = json.load(f)
            staged_crypto_subunits = crypto_data.get("amount_subunits", 0)
            crypto_status = crypto_data.get("status", "STAGED")

        print("\n" + "="*50)
        print(f"=== GGTI FINANCIAL TELEMETRY TICKER LOOP ===")
        print(f"TIMESTAMP: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"NODE TARGET METRIC ACCOUNT: {ledger_data.get('account_id')}")
        print("-"*50)
        
        if net_delta >= 0:
            print(f"[METRIC] NET EARNINGS     : +{net_delta // 100}.{net_delta % 100:02d} H.A.C")
            print(f"[METRIC] NET LOSSES       : 0.00 H.A.C")
        else:
            abs_loss = abs(net_delta)
            print(f"[METRIC] NET EARNINGS     : 0.00 H.A.C")
            print(f"[METRIC] NET LOSSES       : -{abs_loss // 100}.{abs_loss % 100:02d} H.A.C")

        print(f"[CRYPTO] Staged Outbound  : {staged_crypto_subunits // 100}.{staged_crypto_subunits % 100:02d} H.A.C [{crypto_status}]")
        print(f"[SUPPLY] Total Circ Space : {market_data['circulating_supply_subunits'] // 100} H.A.C")
        print(f"[DEMAND] Demand Index     : {market_data['demand_index_ratio']}x")
        print(f"[STATUS] Core Stature     : STABILIZED / WORKING UP")
        print("="*50)

if __name__ == "__main__":
    daemon = GGTITickerDaemon()
    try:
        while True:
            daemon.process_telemetry_cycle()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[TICKER] Analytics view terminated.")
