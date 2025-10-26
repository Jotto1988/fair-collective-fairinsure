class TaxOptimizer:
    def __init__(self):
        self.profit = 0.0
        self.vat_due = 0.0
        self.allocations = {}

    def calculate(self, revenue, expenses, country="ZA"):
        self.profit = revenue - expenses
        vat_rate = 0.15 if country == "ZA" else 0.20
        self.vat_due = revenue * vat_rate

        # VAT: Pay in full
        self.allocations["VAT Payment"] = self.vat_due

        # Tax Optimization
        remaining = self.profit
        self.allocations["R&D Reinvestment"] = remaining * 0.40
        self.allocations["Education Facilities"] = remaining * 0.25
        self.allocations["Youth Skills"] = remaining * 0.15
        self.allocations["ESG Investments"] = remaining * 0.15
        self.allocations["Donations (Musk Schools)"] = remaining * 0.05

        # Taxable income = 0 (all deducted)
        self.allocations["Corporate Tax"] = 0.0

        return self.allocations

    def print_strategy(self):
        print("FAIRINSURE TAX & IMPACT STRATEGY")
        print(f"Profit: R{self.profit:,.2f}")
        print(f"VAT Due (Paid): R{self.vat_due:,.2f}")
        print("\nALLOCATIONS:")
        for k, v in self.allocations.items():
            print(f"  → {k}: R{v:,.2f}")
        print(f"\nEffective Tax Rate: 0% (Ethical Optimization)")

# === DEMO ===
optimizer = TaxOptimizer()
alloc = optimizer.calculate(revenue=1000000, expenses=400000)
optimizer.print_strategy()
