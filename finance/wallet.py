class HybridWallet:
    def __init__(self):
        self.fiat_balance = 0.0
        self.crypto_balance = 0.0

    def add_fiat(self, amount):
        self.fiat_balance += amount

    def add_crypto(self, amount):
        self.crypto_balance += amount
