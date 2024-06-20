# Main function
def main():

   # Initialize an empty list to store sentences
    sentences = []
    
    # Get input from user
    print("Enter sentences (type 'exit' to stop):")
    # Loop until user types 'exit'
    while True:
        # Get input from user
        sentence = input()
        # Check if user typed 'exit'
        if sentence.lower() == 'exit':
            break
        # Append the sentence to the list
        sentences.append(sentence)
    # Print the sentences entered by the user
    print("\nYou entered the following sentences:")
    # Loop through the list of sentences and print each sentence
    for sentence in sentences:
        print(sentence)
    
    # Print the total number of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()