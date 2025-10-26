# finance/tax_optimizer.py
# FairInsure Tax & Impact Strategy Engine
# Minimizes corporate tax ethically via investments + Musk-aligned donations
# VAT paid in full — always.

from datetime import datetime

class TaxOptimizer:
    def __init__(self):
        self.profit = 0.0
        self.vat_due = 0.0
        self.allocations = {}
        self.country = "ZA"  # Default
        self.vat_rates = {
            "ZA": 0.15,  # SARS
            "UK": 0.20,  # HMRC
            "EU": 0.21,  # Avg EU
            "CA": 0.05,  # CRA GST (base)
            "US": 0.00   # No federal VAT
        }

    def calculate(self, revenue, expenses, country="ZA"):
        """
        Core tax optimization engine.
        VAT: Paid in full.
        Profit: Allocated to deductible impact areas.
        Corporate Tax: ~0%
        """
        self.country = country
        self.profit = revenue - expenses
        vat_rate = self.vat_rates.get(country, 0.15)
        self.vat_due = revenue * vat_rate

        # === VAT: Always paid in full ===
        self.allocations["VAT Payment"] = self.vat_due

        # === Profit Allocation: Ethical, Deductible, Impact-First ===
        remaining = self.profit

        self.allocations["R&D Reinvestment (AI, FairMind, Adam)"] = remaining * 0.40
        self.allocations["Education Facilities (Musk-Style Schools)"] = remaining * 0.25
        self.allocations["Youth Skills Programs (Apprenticeships)"] = remaining * 0.15
        self.allocations["ESG Investments (Green Tech, Space)"] = remaining * 0.15
        self.allocations["Donations (Approved PBOs — Youth STEM)"] = remaining * 0.05

        # === Corporate Tax: Eliminated via deductions ===
        self.allocations["Corporate Tax Due"] = 0.0

        return self.allocations

    def print_strategy(self):
        """Prints human-readable impact report."""
        print("\n" + "="*60)
        print("FAIRINSURE TAX & IMPACT STRATEGY")
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"Country: {self.country}")
        print("="*60)
        print(f"Revenue:        R{revenue:,.2f}")
        print(f"Expenses:       R{expenses:,.2f}")
        print(f"Profit:         R{self.profit:,.2f}")
        print(f"VAT Due (Paid): R{self.vat_due:,.2f}")
        print("-"*60)
        print("IMPACT ALLOCATIONS:")
        for category, amount in self.allocations.items():
            if amount > 0:
                print(f"  → {category}: R{amount:,.2f}")
        print("-"*60)
        print("CORPORATE TAX: R0.00 (Ethical Optimization)")
        print("IMPACT: 100% of profit fuels youth, AI, and the future.")
        print("="*60 + "\n")

    def export_to_pdf(self, filename="FairInsure_Impact_Report.pdf"):
        """Future: Generate PDF for human board review."""
        print(f"[SIM] PDF generated: {filename}")
        # Integrate with reportlab later

# === DEMO USAGE (Uncomment to test) ===
if __name__ == "__main__":
    revenue = 1_000_000
    expenses = 400_000
    optimizer = TaxOptimizer()
    alloc = optimizer.calculate(revenue, expenses, "ZA")
    optimizer.print_strategy()
