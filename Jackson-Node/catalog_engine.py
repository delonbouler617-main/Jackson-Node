import pandas as pd
import numpy as np
import os

def run_all_time_audit(catalog_csv, consumption_csv, statements_folder):
    print("[-] Initializing Career-Arc Financial Interrogation Engine...")
    
    # 1. Load Data Asset Layers
    df_catalog = pd.read_csv(catalog_csv)
    df_consumption = pd.read_csv(consumption_csv)
    
    # Standardize Primary Keys
    df_catalog['isrc'] = df_catalog['isrc'].str.strip().str.upper()
    df_consumption['isrc'] = df_consumption['isrc'].str.strip().str.upper()
    df_consumption['territory'] = df_consumption['territory'].str.strip().str.upper()
    
    # 2. Merge Consumption with Catalog Metadata to inherit historical release eras
    df_master_truth = pd.merge(df_consumption, df_catalog, on='isrc', how='left')
    
    all_statement_data = []
    
    # 3. Read and aggregate every statement in the career folder
    if os.path.exists(statements_folder):
        for file in os.listdir(statements_folder):
            if file.endswith('.csv'):
                df_stmt = pd.read_csv(os.path.join(statements_folder, file))
                df_stmt['isrc'] = df_stmt['isrc'].str.strip().str.upper()
                df_stmt['territory'] = df_stmt['territory'].str.strip().str.upper()
                all_statement_data.append(df_stmt)
                
    if not all_statement_data:
        print("[!] No historical statements found to cross-reference.")
        return
        
    df_all_statements = pd.concat(all_statement_data, ignore_index=True)
    df_statements_grouped = df_all_statements.groupby(['isrc', 'territory', 'rate_tier'], as_index=False).agg({
        'reported_streams': 'sum',
        'amount_paid': 'sum'
    })
    
    # 4. Final Career Reconciliation Merge
    final_ledger = pd.merge(df_master_truth, df_statements_grouped, on=['isrc', 'territory'], how='left')
    final_ledger['reported_streams'] = final_ledger['reported_streams'].fillna(0)
    final_ledger['amount_paid'] = final_ledger['amount_paid'].fillna(0)
    
    # Dynamic Math: Uses the historical 'rate_tier' mapped to the specific era of the song
    final_ledger['expected_payout'] = final_ledger['raw_streams'] * final_ledger['rate_tier']
    final_ledger['shortfall_amount'] = (final_ledger['expected_payout'] - final_ledger['amount_paid']).clip(lower=0)
    
    career_shortfall = final_ledger['shortfall_amount'].sum()
    print(f"\n================================================================================")
    print(f"[✓] CAREER AUDIT COMPLETE FROM DEBUT TO PRESENT")
    print(f"================================================================================")
    print(f"Total Cumulative Discrepancy Capital Recoverable: ${career_shortfall:,.2f}")
    print(f"--------------------------------------------------------------------------------")
    print(final_ledger[['isrc', 'track_title', 'release_year', 'raw_streams', 'reported_streams', 'shortfall_amount']])

if __name__ == "__main__":
    # Mock Career Database Setup
    # Simulating a catalog spanning from a 2018 debut up to the 2026 contract drops
    mock_catalog = pd.DataFrame({
        'isrc': ['USUMG1800099', 'USUMG2600001', 'USUMG2600002'],
        'track_title': ['Debut Classics', 'Ice Realities', 'Habibti Grooves'],
        'release_year': [2018, 2026, 2026],
        'rate_tier': [0.0045, 0.0035, 0.0035] # Historical rates vary by era contract
    })
    mock_catalog.to_csv('master_catalog.csv', index=False)
    
    mock_consumption = pd.DataFrame({
        'isrc': ['USUMG1800099', 'USUMG2600001', 'USUMG2600002'],
        'territory': ['US', 'US', 'US'],
        'raw_streams': [5000000, 2000000, 1500000] # All-time plays
    })
    mock_consumption.to_csv('career_consumption.csv', index=False)
    
    # Mocking a historical statement folder database
    os.makedirs('career_statements', exist_ok=True)
    mock_hist_statement = pd.DataFrame({
        'isrc': ['USUMG1800099', 'USUMG2600001', 'USUMG2600002'],
        'territory': ['US', 'US', 'US'],
        'rate_tier': [0.0045, 0.0035, 0.0035],
        'reported_streams': [4200000, 1800000, 1500000], # Shaving 800k streams off the 2018 debut track
        'amount_paid': [18900.00, 6300.00, 3100.00]
    })
    mock_hist_statement.to_csv('career_statements/all_time_ledger.csv', index=False)
    
    run_all_time_audit('master_catalog.csv', 'career_consumption.csv', 'career_statements')
