import time
import random
from agents.adam_ceo import AdamCEO
from finance.wallet import HybridWallet

# === FAIRINSURE LAUNCH ===
adam = AdamCEO()
wallet = HybridWallet()

print("FairInsure ONLINE. AI CEO activated.\n")
adam.speak()

# Daily operations
adam.process_debit_order()
adam.earn_crypto_premium()
adam.invest_in_esg()
adam.hire_human("Empathy Specialist")
adam.process_claim(75)
adam.pay_salary_via_bank()

print(f"\nCompany Status:")
print(f"  Fiat: R{wallet.fiat_balance:.2f}")
print(f"  Crypto: {wallet.crypto_balance:.4f} ETH")
print(f"  Humans Hired: {adam.humans_hired}")
