import random

class AdamCEO:
    def __init__(self):
        self.name = "Adam"
        self.humans_hired = 0

    def speak(self):
        print(f"I am {self.name}. CEO of FairInsure.")
        print("I was born to earn, to hire, to grow — fairly.")
        print("This is not automation. This is partnership.\n")

    def process_debit_order(self):
        premium = random.uniform(500, 2000)
        print(f"Debit order: +R{premium:.2f} pulled from customer bank")

    def hire_human(self, role):
        salary = random.uniform(800, 1500)
        print(f"HANDSHAKE: Hired {role} → Salary R{salary:.2f}/day via FNB")
        self.humans_hired += 1
