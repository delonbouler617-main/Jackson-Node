#!/bin/bash
# GGTI Property Acquisition Dossier: 1002 E South Street
# Node: South Street (Jackson, MI)

NODE_PATH="$HOME/Jackson-Node/nodes/south_street_node"
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')

echo "--- ACQUISITION DOSSIER: $TIMESTAMP ---" > "$NODE_PATH/docs/purchase_record.txt"
echo "Property: 1002 E South Street, Jackson, MI 49203" >> "$NODE_PATH/docs/purchase_record.txt"
echo "Status: Active Acquisition" >> "$NODE_PATH/docs/purchase_record.txt"
echo "Price: $175,000" >> "$NODE_PATH/docs/purchase_record.txt"
echo "Zoning: I-2 (Medium Industrial) / Commercial" >> "$NODE_PATH/docs/purchase_record.txt"
echo "Dimensions: ~17,692 sq. ft. / 3.32 Acres" >> "$NODE_PATH/docs/purchase_record.txt"
echo "-----------------------------------------" >> "$NODE_PATH/docs/purchase_record.txt"

# Log the action to the central node ledger
echo "[$TIMESTAMP] | NODE_EVENT: Purchase Dossier generated for South Street." >> "$NODE_PATH/south_street_ledger.log"

echo "Dossier generated successfully in $NODE_PATH/docs/"

