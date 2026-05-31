#!/usr/bin/env python3
import json
import time
import os

LEDGER_LOG = os.path.expanduser("~/telephony_logs/wallet_balance_ledger.json")
MARKET_LOG = os.path.expanduser("~/telephony_logs/market_metrics.json")

class GGTITickerDaemon:
    def __init__(self):
        print("[TICKER] Initializing 60-Second Ledger Analytics Monitor...")
        self.initialize_market_stats()

    def initialize_market_stats(self):
        """Initializes tracking metrics for system supply and demand parameters."""
        if not os.path.exists(MARKET_LOG):
            initial_market = {
                "system_supply_cap_subunits": 5000000000, # 5,000,000.00 Base
                "circulating_supply_subunits": 500000000, # Allocated Base
                "demand_index_ratio": 1.25,
                "total_losses_subunits": 0
            }
            with open(MARKET_LOG, 'w') as f:
                json.dump(initial_market, f, indent=4)

    def process_telemetry_cycle(self):
        """Calculates earnings, losses, and active allocations over the ledger layer."""
        if not os.path.exists(LEDGER_LOG):
            print("[TICKER_WARN] Active wallet balance ledger not found. Standing by...")
            return

        # Read active account metrics
        with open(LEDGER_LOG, 'r') as f:
            ledger_data = json.load(f)

        # Read market metric matrices
        with open(MARKET_LOG, 'r') as f:
            market_data = json.load(f)

        # Safe tracking parameters (fixed-point scaling)
        confirmed_balance_hac = ledger_data.get("confirmed_balance", 0.0)
        current_holdings_subunits = int(confirmed_balance_hac * 100)
        
        # Calculate losses vs earnings relative to initial target allocations
        initial_allocation_subunits = 50000000  # Initial 500,000.00 allocation base in subunits
        net_delta = current_holdings_subunits - initial_allocation_subunits

        print("\n" + "="*50)
        print(f"=== GGTI FINANCIAL TELEMETRY TICKER LOOP ===")
        print(f"TIMESTAMP: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"NODE TARGET METRIC ACCOUNT: {ledger_data.get('account_id')}")
        print("-"*50)
        
        if net_delta >= 0:
            print(f"[METRIC] NET EARNINGS  : +{net_delta // 100}.{net_delta % 100:02d} H.A.C")
            print(f"[METRIC] NET LOSSES    : 0.00 H.A.C")
        else:
            abs_loss = abs(net_delta)
            print(f"[METRIC] NET EARNINGS  : 0.00 H.A.C")
            print(f"[METRIC] NET LOSSES    : -{abs_loss // 100}.{abs_loss % 100:02d} H.A.C")

        # Supply / Demand Stature tracking
        print(f"[SUPPLY] Total Circulating Space : {market_data['circulating_supply_subunits'] // 100} H.A.C")
        print(f"[DEMAND] System Demand Index     : {market_data['demand_index_ratio']}x")
        print(f"[STATUS] Operational Stature     : STABILIZED")
        print("="*50)

    def start_loop(self):
        try:
            while True:
                self.process_telemetry_cycle()
                print("[INFO] Staging next telemetry analysis loop in 60 seconds... (Ctrl+C to stop)")
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n[TICKER] Background telemetry stream paused.")

if __name__ == "__main__":
    daemon = GGTITickerDaemon()
    daemon.start_loop()
