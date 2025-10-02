class BankAccount:
    def __init__(self,  str, initial_balance: float = 0.0):
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def display_balance(self) -> None:
        print(f"Current Balance: {self.balance:.2f}")

    def __str__(self) -> str:
        return f"BankAccount(account_balance={self.balance:.2f})"