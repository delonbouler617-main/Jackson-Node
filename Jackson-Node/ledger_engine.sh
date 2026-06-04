#!/data/data/com.termux/files/usr/bin/bash

# --- GGTI TRANSACTION ENGINE: V1.1 ---
# Node: Jackson, MI (49203)
# Protocol: AR/AP Automated Reconciliation

LEDGER_FILE="transaction_history.log"

function calculate_balance() {
    echo "--- CALCULATING INSTITUTIONAL LIQUIDITY ---"
    
    # Extract and sum Accounts Receivable (Incoming)
    AR_TOTAL=$(grep "| TYPE:AR |" $LEDGER_FILE | awk -F'| AMT:' '{print $2}' | awk -F' |' '{print $1}' | sed 's/,//g' | awk '{sum+=$1} END {print sum}')
    
    # Extract and sum Accounts Payable (Outgoing)
    AP_TOTAL=$(grep "| TYPE:AP |" $LEDGER_FILE | awk -F'| AMT:' '{print $2}' | awk -F' |' '{print $1}' | sed 's/,//g' | awk '{sum+=$1} END {print sum}')
    
    # Calculate Net Balance
    NET_BALANCE=$(($AR_TOTAL - $AP_TOTAL))
    
    echo "Total Accounts Receivable : \$${AR_TOTAL:-0}"
    echo "Total Accounts Payable    : \$${AP_TOTAL:-0}"
    echo "--------------------------------------------"
    echo "NET INSTITUTIONAL BALANCE : \$${NET_BALANCE:-0}"
    echo "--------------------------------------------"
}

function log_transaction() {
    TYPE=$1 ENTITY=$2 AMOUNT=$3 DESC=$4
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    TX_ID=$(echo "$TIMESTAMP$ENTITY$AMOUNT" | sha256sum | cut -c1-12)

    echo "[$TIMESTAMP] TXID:$TX_ID | TYPE:$TYPE | ENTITY:$ENTITY | AMT:$AMOUNT | DESC:$DESC" >> $LEDGER_FILE
    echo "--- TRANSACTION SEALED: $TX_ID ---"
}

echo "--- JACKSON NODE FINANCIAL GATEWAY ---"
echo "1) Record Accounts Receivable (Incoming)"
echo "2) Record Accounts Payable (Outgoing)"
echo "3) View Balance & Reconciliation"
read -p "Select Operation: " OP

case $OP in
    1) read -p "Source Entity: " ENT; read -p "Amount (no commas): " AMT; read -p "Description: " DSC; log_transaction "AR" "$ENT" "$AMT" "$DSC" ;;
    2) read -p "Recipient Entity: " ENT; read -p "Amount (no commas): " AMT; read -p "Description: " DSC; log_transaction "AP" "$ENT" "$AMT" "$DSC" ;;
    3) calculate_balance ;;
    *) echo "Invalid Node Command." ;;
esac

