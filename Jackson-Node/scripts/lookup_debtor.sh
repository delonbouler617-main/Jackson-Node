#!/bin/bash
# GGTI Lookup Debtor & Statement Linker

STATEMENT_FILE=$1
MANIFEST="../servicing_manifest.md"

echo "Ingesting statement: $STATEMENT_FILE..."

# Logic to find "HUPP" or "3150.00" in the raw CSV data
grep -E "HUPP|3150.00|13exxw5" $STATEMENT_FILE | while read -r line; do
    echo "[$(date -u)] BANK_IMPORT | DATA: $line | STATUS: LINKED_TO_DEBTOR" >> $MANIFEST
    echo "Transaction Matched and Indexed."
done
