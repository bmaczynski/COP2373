from decimal import Decimal

# Define the Money class inheriting from Decimal
class Money(Decimal):
    # Override the new method to handle initialization
    def __new__(cls, value, units='USD'):
        instance = super(Money, cls).__new__(cls, value.replace(',', ''))  # Remove commas from value
        instance.units = units
        return instance

    # Override the string representation method
    def __str__(self):
        # Return the string representation of the amount and units
        return f"{super().__str__()} {self.units}"

    # Define the addition method
    def __add__(self, other):
        # Check if other is an instance of Money and has the same units
        if isinstance(other, Money) and self.units == other.units:
            result = super(Money, self).__add__(other)
            return Money(str(result), self.units)
        else:
            raise ValueError("Cannot add amounts with different units")

    # Define the subtraction method
    def __sub__(self, other):
        if isinstance(other, Money) and self.units == other.units:
            result = super(Money, self).__sub__(other)
            return Money(str(result), self.units)
        else:
            raise ValueError("Cannot subtract amounts with different units")

    # Define the multiplication method
    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            result = super(Money, self).__mul__(Decimal(other))
            return Money(str(result), self.units)
        else:
            raise ValueError("Can only multiply Money by a number")

def main():
    # Define the BankAcct class inheriting from Money class
    class BankAcct:
        # Initialize instance variables
        def __init__(self, name, account_number, amount, interest_rate):
            self.name = name
            self.account_number = account_number
            self.amount = Money(amount)
            self.interest_rate = interest_rate

        # Define interest rate method
        def adjust_interest_rate(self, new_rate):
            self.interest_rate = new_rate

        # Use Money class's add method as deposit
        def deposit(self, amount):
            self.amount += Money(amount)

        # Use Money class's sub method as withdraw
        def withdraw(self, amount):
            try:
                self.amount -= Money(amount)
            except ValueError:
                raise ValueError("Insufficient funds")

        # Define balance method
        def balance(self):
            return self.amount

        # Define calculate interest method
        def calculate_interest(self, days):
            return self.amount * (self.interest_rate / 100) * (days / 365)

        # Override string representation method
        def __str__(self):
            return f"Account Number: {self.account_number} Name: {self.name}: Balance: {self.amount}, Interest Rate: {self.interest_rate}%"

    # Create BankAcct instance
    account = BankAcct("John Smith", "123456789", '2500', 3)
    print(account)
    
    # Test deposit method
    account.deposit('5000')
    print("After deposit:", account)
    
    # Test withdraw method
    account.withdraw('350')
    print("After withdrawal:", account)
    
    # Test calculate interest method
    interest = account.calculate_interest(22)
    print(f"Interest for 30 days: {interest:.2f}")
    
    # Test adjust interest rate method
    account.adjust_interest_rate(3)
    print("After interest rate adjustment:", account)

if __name__ == "__main__":
    main()