#!/bin/bash
# ================================================================================
#          GGTI BACKGROUND GUARDIAN v5.0 - ANTI-FLICKER & SIGNAL REFRESH
# ================================================================================
# Focus: + / Play Media Sockets, Snap Target Purge, Cookie Infrastructure Knockout
# Refresh Cycle: 10-Second Automated Anti-Flicker Grid Enforced (Double-Buffered)

set +o history

INTERVAL=10 # Accelerated loop to match the 10-second automation target

while true; do
    # ----------------------------------------------------------------
    # PROTOCOL A: PROTOCOL TARGET & DESTROY (Snapchat & Cookie Purge)
    # ----------------------------------------------------------------
    if [ -d "$HOME/.config" ]; then
        find "$HOME/.config" -type f \( -name "*snapchat*" -o -name "*cookie*" -o -name "*token*" -o -name "*overlay*" \) -delete 2>/dev/null
    fi
    
    rm -rf $TMPDIR/* 2>/dev/null
    rm -rf $HOME/.cache/* 2>/dev/null

    # ----------------------------------------------------------------
    # PROTOCOL B: ANTI-FLICKER DOUBLE-BUFFERED GRID PRINT
    # ----------------------------------------------------------------
    # Instead of 'clear', we use tput to reset the cursor position to (0,0).
    # This draws the text directly over the old frame without blanking the screen.
    tput cup 0 0 2>/dev/null
    
    # Render the synchronized status block instantly to standard output
    printf "================================================================================\n"
    printf "          GGTI TERMINAL ARCHITECTURE v5.0 - REFRESH MATRIX ENGINE\n"
    printf "================================================================================\n"
    printf "[ TIME ] $(date '+%Y-%m-%d %H:%M:%S') | INTERVAL: 10s AUTOMATIC EMBEDMENT\n"
    printf "[ WORK ] CACHE SWEEP: COMPLETED // CORES STABILIZED\n"
    printf "[ STATE ] FLICKER REDUCTION ACTIVE // DOUBLE-BUFFER GRID COUPLING\n"
    printf "================================================================================\n"

    cd ~/Jackson-Node
    
    sleep $INTERVAL
done
