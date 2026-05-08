#!/data/data/com.termux/files/usr/bin/bash

# --- GGTI TRANSACTION ENGINE: V1.0 ---
# Node: Jackson, MI (49203)
# Protocol: AR/AP Transactional Repetition

LEDGER_FILE="transaction_history.log"
MASTER_HASH="b658653e98ba35789fb820ab059090c67ac76a04b7309215a2"

function log_transaction() {
    TYPE=$1    # AR or AP
    ENTITY=$2  # Who is the counterparty?
    AMOUNT=$3  # Numeric Value
    DESC=$4    # What is it for?
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    
    # Generate a unique Transaction ID linked to your Master Hash
    TX_ID=$(echo "$TIMESTAMP$ENTITY$AMOUNT" | sha256sum | cut -c1-12)

    echo "[$TIMESTAMP] TXID:$TX_ID | TYPE:$TYPE | ENTITY:$ENTITY | AMT:$AMOUNT | DESC:$DESC" >> $LEDGER_FILE
    echo "--- TRANSACTION SEALED ---"
    echo "ID: $TX_ID"
    echo "Type: $TYPE"
    echo "State: COMMITTED TO GLOBAL DATABASE"
}

# Interface
echo "--- JACKSON NODE FINANCIAL GATEWAY ---"
echo "1) Record Accounts Receivable (Incoming)"
echo "2) Record Accounts Payable (Outgoing)"
echo "3) View Current Balance & Ledger"
read -p "Select Operation: " OP

case $OP in
    1)
        read -p "Source Entity: " ENT
        read -p "Amount: " AMT
        read -p "Description: " DSC
        log_transaction "AR" "$ENT" "$AMT" "$DSC"
        ;;
    2)
        read -p "Recipient Entity: " ENT
        read -p "Amount: " AMT
        read -p "Description: " DSC
        log_transaction "AP" "$ENT" "$AMT" "$DSC"
        ;;
    3)
        echo "--- RECENT REGISTER ENTRIES ---"
        tail -n 10 $LEDGER_FILE
        ;;
    *)
        echo "Invalid Node Command."
        ;;
esac

