#!/bin/bash

log_transaction() {
    local TYPE="$1"
    local ENTITY="$2"
    local AMOUNT="$3"
    local DESC="$4"

    echo "$(date '+%Y-%m-%d %H:%M:%S') | $TYPE | $ENTITY | $AMOUNT | $DESC" >> ledger_db.txt

    curl -s -X POST http://localhost:5000/api/endpoint \
         -H "Content-Type: application/json" \
         -d "{
           \"type\": \"$TYPE\",
           \"entity\": \"$ENTITY\",
           \"amount\": \"$AMOUNT\",
           \"description\": \"$DESC\"
         }" > /dev/null

    echo -e "\n[+] Recorded locally and posted to API."
}

calculate_balance() {
    echo -e "\n--- FETCHING BALANCES & RECONCILIATION ---"
    response=$(curl -s http://localhost:5000/api/balance)
    echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"
    echo -e "\n----------------------------------------"
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
