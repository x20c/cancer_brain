#Task 1
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, number_acc: int, name: str, balance: float):
        self.number_acc = number_acc
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount} to {self.name}, current balance is {self.balance}")
        else:
            raise ValueError("Deposit can't be negative")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw must be a positive number")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw successful. Balance is {self.balance}")
        else:
            raise ValueError(f"Withdraw must be lower than balance, current balance is {self.balance}")

    @abstractmethod
    def __str__(self):
        pass
#Task 2
class CurrentAccount(Account):
    def __str__(self):
        return f"Current Account - {self.name} (#{self.number_acc}), Balance: {self.balance}"
#Task 3
class SavingsAccount(Account):
    def __init__(self, number_acc: int, name: str, balance: float, interest_rate: float):
        super().__init__(number_acc, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest: {interest:.2f}, new balance is {self.balance:.2f}")

    def __str__(self):
        return f"Savings Account - {self.name} (#{self.number_acc}), Interest Rate: {self.interest_rate * 100:.2f}%, Balance: {self.balance:.2f}"
#Task 4
accounts = [
    CurrentAccount(12345, "Adolf Gitler", 9999999999.0),
    SavingsAccount(67890, "Alice Luftwaffe", 1410.0, 0.05),
    CurrentAccount(11122, "Gucci Mucci", 1442.2),
    SavingsAccount(33344, "Emma Haizenberg", 2210.0, 0.05)
]


accounts[0].deposit(200)
accounts[1].withdraw(150)
accounts[2].withdraw(300)
accounts[3].add_interest()

print("\n--- Account Details ---")
for account in accounts:
    print(account)