from decimal import Decimal

class Money(Decimal):
    # Define new method for the Money class
    def __new__(cls, value, units='USD'):
        # Create new instance of Money
        instance = super(Money, cls).__new__(cls, value)
        # Set currency units
        instance.units = units
        return instance

    # Define the string representation method
    def __str__(self):
        # Return the value along with currency units
        return super().__str__() + ' ' + self.units

    # Define the addition method
    def __add__(self, other):
        # Check if the units are the same for both Money objects
        if isinstance(other, Money) and self.units == other.units:
            # Add the values if the units are the same
            result = super(Money, self).__add__(other)
            return Money(result, self.units)
        else:
            # Raise an error if the units are different
            raise ValueError("Cannot add amounts with different units")

    # Define the subtraction method
    def __sub__(self, other):
        # Check if the units are the same for both Money objects
        if isinstance(other, Money) and self.units == other.units:
            # Subtract the values if the units are the same
            result = super(Money, self).__sub__(other)
            return Money(result, self.units)
        else:
            # Raise an error if the units are different
            raise ValueError("Cannot subtract amounts with different units")

    # Define the multiplication method
    def __mul__(self, other):
        # Check if the other value is a number
        if isinstance(other, (int, float, Decimal)):
            # Multiply the value by the number
            result = super(Money, self).__mul__(Decimal(other))
            return Money(result, self.units)
        else:
            # Raise an error if the other value is not a number
            raise ValueError("Can only multiply Money by a number")

def Main():
    # Initialize instances of money
    m1 = Money('10.50', 'USD')
    m2 = Money('5.25', 'USD')
    m3 = Money('7.75', 'YEN')

    # Print the Money instances
    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print(f"m3: {m3}")

    try:
        # Add 2 Money instances with the same units
        m4 = m1 + m2
        print(f"m1 + m2: {m4}")
    except ValueError as e:
        print(e)

    try:
        # Subtract 2 Money instances with the same units
        m5 = m1 - m2
        print(f"m1 - m2: {m5}")
    except ValueError as e:
        print(e)

    try:
        # Attempt to add 2 Money instances with different units
        m6 = m1 + m3
        print(f"m1 + m3: {m6}")
        # Print error message if try fails
    except ValueError as e:
        print(e)

    # Multiply a Money instance by a number
    m7 = m1 * 2
    print(f"m1 * 2: {m7}")

if __name__ == "__main__":
    Main()