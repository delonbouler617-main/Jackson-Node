source ~/Jackson-Node/ggti-init.sh
alias ggti_status='echo "=== [GGTI] GLOBAL LINVASION STATUS ANALYSIS ===" && for script in airspace_mitigation_lockdown.sh telecomm_accessibility_shield.sh camera_face_intercept.sh adaptive_ambient_shield.sh input_shroud_shield.sh anti_cloning_intercept.sh identity_battery_shroud.sh; do if [ -x "./$script" ]; then echo "\n[RUNNING] $script..."; ./$script | grep -E "(TIMESTAMP|State|Status|ALERT|WARNING|SECURE|Enforced|LOCKED|CLEAN)"; else echo "\n[-] $script: Not Detected / Inactive"; fi; done && echo "\n============================================="'
export PATH=$HOME/bin:$PATH

# GGTI Operational Shortcuts
alias ggti-sync='~/ggti_git_sync.sh'
alias ggti-process='~/ggti_cart_processor.sh'
alias ggti-run='~/ggti_cart_processor.sh cart_export.dat && ~/ggti_git_sync.sh'
pgrep -f "start_tunnel.sh" > /dev/null || nohup ./start_tunnel.sh > /dev/null 2>&1 &

# ==============================================================================
#  [🛰️] V6 SOVEREIGN LOG TRAIL ENGINE
# ==============================================================================
trail() {
  local log_file="${1:-$HOME/flask.log}"
  local counter=1

  if [ ! -f "$log_file" ]; then
    echo "[TRAIL ERROR] Target log file not found: $log_file"
    return 1
  fi

  echo "=============================================================================="
  echo " [🛰️] QUARTZ LOG TRAIL MONITOR ACTIVE"
  echo " [TARGET] $log_file"
  echo "=============================================================================="

  tail -fn 0 "$log_file" | while read -r line; do
    local ts=$(date +"%Y-%m-%d %H:%M:%S.%3N")
    printf "[%s] [SEQ:%05d] %s\n" "$ts" "$counter" "$line"
    ((counter++))
  done
}

# Parcel Data Helper Suite
get_pending_fields() {
    jq -r 'to_entries[] | select(.value | tostring | startswith("REQUIRES")) | "\(.key): \(.value)"' "$1"
}

load_parcel_env() {
    eval $(jq -r 'to_entries[] | "PARCEL_\(.key)=\(.value | @sh)"' "$1")
    echo "[+] Loaded Parcel: $PARCEL_Parcel_ID ($PARCEL_Address)"
}

parcels_to_csv() {
    echo '"Parcel_ID","Address","Legal_Description","HTTP_Status"'
    jq -r '[.Parcel_ID, .Address, .Legal_Description, .HTTP_Status] | @csv' "$@" | sort -u
}
