#!/usr/bin/env bash
echo "================================================================================"
echo "          GGTI CERTIFICATE TRUST SYSTEM MAPPING (v3.1-FIXED)"
echo "================================================================================"

TARGET_DIR="$HOME/.ggti_ssl/certs"
mkdir -p "$TARGET_DIR"

PRIVATE_KEY="$HOME/Jackson-Node/security/keys/institutional_private.pem"

if [ -f "$PRIVATE_KEY" ]; then
    echo "[INFO] Found private cryptographic key node. Generating X.509 Certificate..."
    
    # Sign a formal X.509 certificate using your master private key node
    openssl req -x509 -new -nodes -key "$PRIVATE_KEY" -days 3650 \
      -out "$TARGET_DIR/node_root.crt" \
      -subj "/C=US/ST=MI/L=Jackson/O=Global Database/CN=GGTI-Sovereign-Node"
      
    echo "[SUCCESS] Formatted X.509 Certificate securely deployed to -> $TARGET_DIR/node_root.crt"
else
    echo "[ERROR] Private anchor key not found at $PRIVATE_KEY"
    echo "[WORK] Creating completely standalone isolated credential node..."
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
      -keyout "$HOME/.ggti_ssl/node_private.key" \
      -out "$TARGET_DIR/node_root.crt" \
      -subj "/C=US/ST=MI/L=Jackson/O=Global Database/CN=GGTI-Node"
fi

# 2. Re-hash the trust store using proper OpenSSL cryptographic hashes
echo "[STATUS] Reindexing trust layers..."
rm -f "$TARGET_DIR"/*.0 2>/dev/null  # Purge the invalid .0 blank link

if command -v c_rehash &> /dev/null; then
    c_rehash "$TARGET_DIR"
else
    # Extract the exact cryptographic hash from the newly compiled X.509 structure
    HASH=$(openssl x509 -noout -hash -in "$TARGET_DIR/node_root.crt")
    if [ ! -z "$HASH" ]; then
        ln -sf "node_root.crt" "$TARGET_DIR/${HASH}.0"
        echo "[SUCCESS] Generated symbolic certificate link hash: ${HASH}.0"
    else
        echo "[CRITICAL] OpenSSL structure mapping failed."
    fi
fi

echo "----------------------------------------------------------------"
echo "[RESULT] User Certificate Architecture Successfully Locked."
echo "=================================================================="
