curl -X POST -v -H "Content-Type: application/json" \
-d @$HOME/GGTI_NODE/settlement_0x9fd.json \
"https://web3.googleapis.com/v1/projects/jackson-node-49203/locations/global/networks/blockchain/transactions:broadcast"
