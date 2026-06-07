#!/bin/bash
# GGTI Security Utils: Integrity & Verification

# Function 1: Mod10 (Luhn) Integrity Check
validate_mod10() {
    local number="$1"
    local sum=0
    local len=${#number}
    local parity=$((len % 2))
    for (( i=0; i<len; i++ )); do
        local digit=${number:$i:1}
        if [ $((i % 2)) -eq $parity ]; then
            digit=$((digit * 2))
            [ $digit -gt 9 ] && digit=$((digit - 9))
        fi
        sum=$((sum + digit))
    done
    [ $((sum % 10)) -eq 0 ] && return 0 || return 1
}

# Function 2: Cryptographic Signature Verification (Simulated HMAC)
# Compares the provided signature against a generated hash of the data
verify_signature() {
    local data="$1"
    local provided_sig="$2"
    # Create a hash of the data using sha256
    local calculated_sig=$(echo -n "$data" | sha256sum | awk '{print $1}')
    
    if [ "$provided_sig" == "$calculated_sig" ]; then
        return 0 # Signature verified
    else
        return 1 # Integrity compromised
    fi
}



