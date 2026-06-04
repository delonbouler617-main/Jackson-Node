import pandas as pd
import numpy as np
import os
import datetime

def build_master_asset_files():
    print("[-] Compiling All-Time Master Catalog & Historical Rate Assets...")
    catalog_data = {
        'isrc': ['USUMG1800099', 'USUMG2200054', 'USUMG2600001', 'USUMG2600002'],
        'track_title': ['Debut Classics', 'Mid-Career Anthem', 'Ice Realities', 'Habibti Grooves'],
        'release_year': [2018, 2022, 2026, 2026],
        'album': ['First Impressions', 'The Turning Point', 'Iceman', 'Habibti']
    }
    pd.DataFrame(catalog_data).to_csv('master_catalog.csv', index=False)

    rate_matrix_data = {
        'consumption_year': [2018, 2019, 2022, 2023, 2026],
        'platform': ['SPOTIFY', 'SPOTIFY', 'SPOTIFY', 'SPOTIFY', 'SPOTIFY'],
        'base_rate': [0.0052, 0.0048, 0.0040, 0.0038, 0.0035]
    }
    pd.DataFrame(rate_matrix_data).to_csv('historical_rate_matrix.csv', index=False)

    consumption_data = {
        'isrc': ['USUMG1800099', 'USUMG1800099', 'USUMG2200054', 'USUMG2600001'],
        'consumption_year': [2018, 2019, 2022, 2026],
        'platform': ['SPOTIFY', 'SPOTIFY', 'SPOTIFY', 'SPOTIFY'],
        'territory': ['US', 'US', 'US', 'US'],
        'raw_streams': [5000000, 4000000, 8000000, 2000000]
    }
    pd.DataFrame(consumption_data).to_csv('career_consumption.csv', index=False)
    print("[✓] All baseline database files written safely.")

def run_fluctuating_rate_audit(catalog_csv, consumption_csv, rate_matrix_csv, statements_folder):
    print("\n[-] Initializing Advanced Fluctuating Math Reconciliation...")
    df_catalog = pd.read_csv(catalog_csv)
    df_consumption = pd.read_csv(consumption_csv)
    df_rates = pd.read_csv(rate_matrix_csv)
    
    for df in [df_catalog, df_consumption, df_rates]:
        if 'isrc' in df.columns: df['isrc'] = df['isrc'].str.strip().str.upper()
        if 'platform' in df.columns: df['platform'] = df['platform'].str.strip().str.upper()
        if 'territory' in df.columns: df['territory'] = df['territory'].str.strip().str.upper()

    df_truth = pd.merge(df_consumption, df_catalog, on='isrc', how='left')
    df_truth = pd.merge(df_truth, df_rates, on=['consumption_year', 'platform'], how='left')
    
    all_statements = []
    if os.path.exists(statements_folder):
        for file in os.listdir(statements_folder):
            if file.endswith('.csv'):
                all_statements.append(pd.read_csv(os.path.join(statements_folder, file)))
                
    if not all_statements:
        print("[!] Missing settlement statement folder dependencies.")
        return
        
    df_statements = pd.concat(all_statements, ignore_index=True)
    for col in ['isrc', 'platform', 'territory']:
        df_statements[col] = df_statements[col].astype(str).str.strip().str.upper()
        
    df_statements_grouped = df_statements.groupby(
        ['isrc', 'consumption_year', 'platform', 'territory'], as_index=False
    ).agg({'reported_streams': 'sum', 'amount_paid': 'sum'})
    
    final_ledger = pd.merge(
        df_truth, df_statements_grouped, 
        on=['isrc', 'consumption_year', 'platform', 'territory'], 
        how='left'
    ).fillna(0)
    
    final_ledger['expected_payout'] = final_ledger['raw_streams'] * final_ledger['base_rate']
    final_ledger['shortfall_amount'] = (final_ledger['expected_payout'] - final_ledger['amount_paid']).clip(lower=0)
    final_ledger['stream_deficit'] = (final_ledger['raw_streams'] - final_ledger['reported_streams']).clip(lower=0)
    
    # [NEW PROPERTY] Auto-export forensic CSV exhibit
    final_ledger.to_csv('career_audit_exhibit.csv', index=False)
    print("[✓] Local Forensic Exhibit Exported: career_audit_exhibit.csv")
    
    total_recovered_capital = final_ledger['shortfall_amount'].sum()
    print("================================================================================")
    print(f"[✓] FORENSIC CAREER RECONCILIATION COMPLETE")
    print(f"================================================================================")
    print(f"Total Recoverable Shortfall Capital: ${total_recovered_capital:,.2f}\n")

if __name__ == "__main__":
    build_master_asset_files()
    os.makedirs('career_history_statements', exist_ok=True)
    mock_statements = pd.DataFrame({
        'isrc': ['USUMG1800099', 'USUMG1800099', 'USUMG2200054', 'USUMG2600001'],
        'consumption_year': [2018, 2019, 2022, 2026],
        'platform': ['SPOTIFY', 'SPOTIFY', 'SPOTIFY', 'SPOTIFY'],
        'territory': ['US', 'US', 'US', 'US'],
        'reported_streams': [4500000, 3800000, 8000000, 1800000],
        'amount_paid': [23400.00, 18240.00, 32000.00, 6300.00]
    })
    mock_statements.to_csv('career_history_statements/all_time_settlements.csv', index=False)
    
    run_fluctuating_rate_audit('master_catalog.csv', 'career_consumption.csv', 'historical_rate_matrix.csv', 'career_history_statements')
