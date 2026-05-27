import hashlib
import sys

def validate_aba_routing(rtn: str) -> bool:
    if len(rtn) != 9 or not rtn.isdigit(): return False
    digits = [int(d) for d in rtn]
    weighted_sum = 3*(digits[0]+digits[3]+digits[6]) + 7*(digits[1]+digits[4]+digits[7]) + 1*(digits[2]+digits[5]+digits[8])
    return (weighted_sum % 10) == 0

rtn, acc, txn = "071012344", "700112345652", "TXN0001"
if validate_aba_routing(rtn):
    sig = hashlib.sha256(f"{rtn}{acc}{txn}".encode('utf-8')).hexdigest()
    print(f"[STATUS] LEDGER SIGNATURE: {sig}")
else:
    sys.exit(1)
