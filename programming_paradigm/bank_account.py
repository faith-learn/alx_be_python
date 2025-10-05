class BankAccount:
    """
    A simple bank account class that encapsulates banking operations.
    """
    def __init__(self, initial_balance=0):
        # Private attribute for encapsulation
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        # Ensure the amount is positive before updating the balance
        if amount > 0:
            self._account_balance += amount
            # NOTE: Printing removed. main-0.py will handle the print statement.

    def withdraw(self, amount):
        """
        Deducts the amount from account_balance if funds are sufficient.
        Returns True on success, False otherwise.
        """
        # Check if amount is positive and if there are sufficient funds
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            # NOTE: Printing removed. main-0.py will handle the print statement.
            return True
        else:
            # NOTE: Printing removed. main-0.py will handle the "Insufficient funds." message.
            return False

    def display_balance(self):
        """Prints the current balance in the required user-friendly currency format."""
        # Corrected: Using '$' symbol and formatting to two decimal places (.2f)
        print(f"Current Balance: ${self._account_balance:.2f}")
         
       