# Create main function
def main():
    
    # Initialize variables
    total_tickets = 20
    tickets_left = total_tickets
    total_buyers = 0
    
      # We need a loop until all tickets are sold out
    while tickets_left > 0:
        # Display the number of tickets left
        print(f"Currently, there are {tickets_left} tickets available.")
        try:
            # Prompt user to enter the number of tickets they want to buy
            requested_tickets = int(input("How many tickets would you like to buy? (Max 4 per person): "))
            # Check if the input is a valid number
        except ValueError:
            # If not a valid number, reprompt the user
            print("Please enter a valid number.")
            continue

            # Check if the number of tickets requested is between 1 and 4
        if requested_tickets < 1 or requested_tickets > 4:
            # If tickets input is less than or greater than 4, reprompt the user
            print("You can only purchase between 1 and 4 tickets.")
            continue
        
         # Check if the number of tickets requested is greater than the number of tickets left
        if requested_tickets > tickets_left:
            # If tickets requested is greater than tickets left, reprompt the user
            print(f"Only {tickets_left} tickets left, please enter an amount between 1 and {tickets_left}.")
            continue
        # Update the number of tickets left if entered properly
        tickets_left -= requested_tickets
         # Increment the total buyers
        total_buyers += 1
        # Display the number of tickets left
        print(f"Purchase successful! {tickets_left} tickets remaining.")
    # Display sold out message once loop breaks
    print(f"All tickets sold out! Total buyers: {total_buyers}")

if __name__ == "__main__":
    main()
