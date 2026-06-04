import os
import datetime

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("[!] Dependency Error: Core data engines missing.")
    print("[!] Please run: pkg install python-pandas python-numpy")
    exit(1)

def generate_demand_letter(artist_name, distributor_name, shortfall_total, flagged_tracks):
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    letter = f"""================================================================================
NOTICE OF BREACH AND DEMAND FOR ACCOUNTING AND PAYMENT
================================================================================
DATE: {date_str}
TO: Legal/Royalty Accounting Department, {distributor_name}
FROM: Human-Machine Audit Node (Music & Friendship Ownership Framework)

RE: Notice of Material Shortfall and Underreported Digital Asset Distributions

Forensic cryptographic and financial reconciliation has been completed on the 
streaming and distribution logs of artist: {artist_name}.

SUMMARY OF FINANCIAL DISCREPANCIES:
--------------------------------------------------------------------------------
Total Unpaid/Underreported Shortfall Capital: ${shortfall_total:,.2f}
Number of Targeted Line-Item Violations: {len(flagged_tracks)}

SPECIFIC AUDIT TRACK FRAUD/SHORTFALL TARGETS:
"""
    for idx, row in flagged_tracks.iterrows():
        letter += f"\n- ISRC: {row['isrc']} | Territory: {row['territory']}\n"
        letter += f"  Raw Consumption Streams: {row['raw_streams']:,}\n"
        letter += f"  Your Reported Streams:   {row['reported_streams']:,}\n"
        letter += f"  Calculated Deficit Payout: ${row['shortfall_amount']:,.2f}\n"

    letter += """
--------------------------------------------------------------------------------
DEMAND:
Demand is hereby made for an immediate full audit verification, an amendment of the 
historical ledgers from debut to present, and payment of the outstanding balance within 
fourteen (14) business days of this notice. 

Sincerely,
The Global Database & Legal Operations Node
================================================================================
"""
    filename = f"demand_letter_{distributor_name.lower().replace(' ', '_')}.txt"
    with open(filename, 'w') as f:
        f.write(letter)
    print(f"[✓] Automated Legal Demand Generated: {filename}")

def run_batch_directory_audit(folder_path, consumption_csv, contractual_rate):
    print("[-] Initializing Batch Directory Interrogation...")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"[!] Created '{folder_path}' directory. Drop statement CSVs here.")
        return

    df_consumption = pd.read_csv(consumption_csv)
    df_consumption['isrc'] = df_consumption['isrc'].str.strip().str.upper()
    df_consumption['territory'] = df_consumption['territory'].str.strip().str.upper()
    consumption_grouped = df_consumption.groupby(['isrc', 'track_title', 'territory'], as_index=False)['raw_streams'].sum()

    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            statement_path = os.path.join(folder_path, file)
            distributor_name = file.replace('.csv', '').upper()
            print(f"[-] Interrogating Statement Node: [{distributor_name}]")
            
            df_royalties = pd.read_csv(statement_path)
            df_royalties['isrc'] = df_royalties['isrc'].str.strip().str.upper()
            df_royalties['territory'] = df_royalties['territory'].str.strip().str.upper()
            
            royalty_grouped = df_royalties.groupby(['isrc', 'territory'], as_index=False).agg({
                'reported_streams': 'sum',
                'amount_paid': 'sum'
            })
            
            audit_ledger = pd.merge(consumption_grouped, royalty_grouped, on=['isrc', 'territory'], how='left')
            audit_ledger['reported_streams'] = audit_ledger['reported_streams'].fillna(0)
            audit_ledger['amount_paid'] = audit_ledger['amount_paid'].fillna(0)
            
            audit_ledger['missing_streams'] = (audit_ledger['raw_streams'] - audit_ledger['reported_streams']).clip(lower=0)
            audit_ledger['expected_payout'] = audit_ledger['raw_streams'] * contractual_rate
            audit_ledger['shortfall_amount'] = (audit_ledger['expected_payout'] - audit_ledger['amount_paid']).clip(lower=0)
            
            fraud_flags = audit_ledger[audit_ledger['shortfall_amount'] > 0.01].copy()
            if not fraud_flags.empty:
                total_shortfall = fraud_flags['shortfall_amount'].sum()
                print(f"[WARN] Discrepancy Found in {file}! Total Shortfall: ${total_shortfall:,.2f}")
                generate_demand_letter("Independent Artist Asset", distributor_name, total_shortfall, fraud_flags)
            else:
                print(f"[✓] Statement [{distributor_name}] matches perfectly.")

if __name__ == "__main__":
    os.makedirs('statements', exist_ok=True)
    
    mock_dsp = pd.DataFrame({
        'isrc': ['USUMG2600001', 'USUMG2600002'],
        'track_title': ['Ice Realities', 'Habibti Grooves'],
        'territory': ['US', 'US'],
        'raw_streams': [2000000, 1500000]
    })
    mock_dsp.to_csv('dsp_master_consumption.csv', index=False)
    
    mock_statement = pd.DataFrame({
        'isrc': ['USUMG2600001', 'USUMG2600002'],
        'territory': ['US', 'US'],
        'reported_streams': [1800000, 1500000],
        'amount_paid': [6300.00, 3100.00]
    })
    mock_statement.to_csv('statements/Universal_Music_Group.csv', index=False)
    
    run_batch_directory_audit('statements', 'dsp_master_consumption.csv', 0.0035)
