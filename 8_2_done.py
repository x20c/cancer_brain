#Task 1
from abc import abstractmethod


class Account:
    def __init__(self, number_acc : int, name : str, balance : float):
        self.number_acc = number_acc
        self.name = name
        self.balance = balance

    def deposit(self, deposit : float):
        if deposit > 0:
            self.balance += deposit
            print(f"Successfully deposited {deposit} to {self.name}, current balance is {self.balance}")
        else:
            raise ValueError("Deposit can't be negative")

    def withdraw(self, withdraw : float):
        if withdraw <= 0:
            raise ValueError("Withdraw must be a positive number")
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Withdraw successful. Balance is {self.balance}")
        else:
            raise ValueError(f"Withdraw must be lower than balance, current balance is {self.balance}")

    @abstractmethod
    def __str__(self):
      raise NotImplementedError("Subclasses must implement __str__ method")
#Task 2
class CurrentAccount(Account):
    def __str__(self):
        return f"Current account is {self.number_acc}, current balance is {self.balance}"
#Task 3
class SavingsAccount(Account):
    def __init__(self, number_acc: int, name: str, balance: float, interest_rate: float):
        super().__init__(number_acc, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f"Added interest rate of {self.balance} rate is {self.interest_rate}")

    def __str__(self):
        return f"Savings Account: {self.number_acc}, Interest Rate: {self.interest_rate * 100:.2f}%, Balance: {self.balance}"
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