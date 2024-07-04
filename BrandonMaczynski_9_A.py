def main():
    class BankAcct:
        def __init__(self, name, account_number, amount, interest_rate):
            # Initialize instance variables
            self.name = name
            self.account_number = account_number
            self.amount = amount
            self.interest_rate = interest_rate

        # Define interest rate method
        def adjust_interest_rate(self, new_rate):
            # Update interest rate
            self.interest_rate = new_rate

        # Define deposit method
        def deposit(self, amount):
            # Add amount to balance
            self.amount += amount

        # Define withdraw method
        def withdraw(self, amount):
            # Subtract amount from balance if sufficient funds are available
            if amount <= self.amount:
                self.amount -= amount
            else:
                raise ValueError("Insufficient funds")

        # Define balance method
        def balance(self):
            # Return current balance
            return self.amount

        # Define calculate interest method
        def calculate_interest(self, days):
            # Calculate interest earned over specified number of days
            return self.amount * (self.interest_rate / 100) * (days / 365)

        def __str__(self):
            # Return string representation of account's state
            return f"Account {self.account_number} owned by {self.name}: Balance ${self.amount:.2f}, Interest Rate {self.interest_rate}%"

    # Create BankAcct instance
    account = BankAcct("John Smith", "123456789", 2500, 3)
    print(account)
    
    # Test deposit method
    account.deposit(5000)
    print("After deposit:", account)
    
    # Test withdraw method
    account.withdraw(350)
    print("After withdrawal:", account)
    
    # Test calculate_interest method
    interest = account.calculate_interest(22)
    print(f"Interest for 30 days: ${interest:.2f}")
    
    # Test adjust_interest_rate method
    account.adjust_interest_rate(2.5)
    print("After interest rate adjustment:", account)

if __name__ == "__main__":
    main()