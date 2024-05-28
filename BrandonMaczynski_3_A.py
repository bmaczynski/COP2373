from functools import reduce

def main():
    # Initialize expenses list
    expenses = []
    # Loop until user is done entering expenses
    while True:
        expense_type = input("Enter the type of expense (or type 'q' to finish): ")
        if expense_type.lower() == 'q':
            break
        # Get the amount of the expense typed
        amount = float(input("Enter the cost for {}: ".format(expense_type)))
        # Add the expense to the list, as well as the amount
        expenses.append((expense_type, amount))
    # If no expenses were entered, display a message
    if not expenses:
        print("No expenses entered.")
        return

    # Calculate total expense
    total_expense = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    # Find the highest expense
    highest_expense = reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc, expenses)
    
    # Find the lowest expense
    lowest_expense = reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc, expenses)

    # Display results
    print(f"\nTotal expense: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

if __name__ == "__main__":
    main()
