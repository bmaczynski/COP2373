import random

# Create file with responses. We can store these values as strings within an array
responses = [
    "Yes, of course!",
    "Without a doubt, yes.",
    "You can count on it.",
    "For sure!",
    "Ask me later!",
    "I'm not sure.",
    "I can't tell you right now.",
    "I'll tell you after my nap.",
    "No way!",
    "I don't think so.",
    "Without a doubt, no.",
    "The answer is clearly NO!"
]

with open("8ball_responses.txt", "w") as file:
    for response in responses:
        file.write(response + "\n")

# Read responses from the file into a list
with open("8ball_responses.txt", "r") as file:
    responses = [line.strip() for line in file]

# Main function
def main():
    print("Welcome to the Magic 8 Ball program!")
    # Loop for user to ask question until they type quit
    while True:
        question = input("Ask a yes/no question (or type 'quit' to exit): ")
        # Conditional to check if user types quit
        if question.lower() == "quit":
            # If quit is typed, break the while loop
            break
        print("Magic 8 Ball says: " + random.choice(responses))
    print("Goodbye!")

# Run main
if __name__ == "__main__":
    main()
