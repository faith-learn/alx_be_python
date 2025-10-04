class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute for encapsulation
        self._account_balance = initial_balance

    def deposit(self, amount):
    
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: &{amount: .1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        
        if amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: &{amount}")
            return True
        else:
            print("Insufficient funds!")
            return False

    def display_balance(self):
        
        print(f"Current Balance: {self._account_balance:.2f}")
         
       