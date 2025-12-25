def make_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be positive")
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        return balance

    return deposit, withdraw
