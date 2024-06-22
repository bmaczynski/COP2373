# import re module to use regular expressions
import re

# Main function
def main():

    # Function to count sentences
    def count_sentences(text):
        # We can use the following regular expression to match sentences
        # Create pattern variable to store the regular expression pattern, allowing requirement for sentences to end properly, and to exclude improper sentence endings. We can also accept integers here. Sentences must start with a capital letter or integer in order to be considered.
        pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
        sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
        return sentences
    
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
    
    # Join all sentences into a single text block
    text = ' '.join(sentences)
    # Count sentences using the regular expression
    counted_sentences = count_sentences(text)
    
    # Print the sentences entered by the user
    print("\nYou entered the following sentences:")
    # Loop through the list of counted sentences and print each sentence
    for sentence in counted_sentences:
        print(sentence)
    
    # Print the total number of sentences by counting the length of the list
    print(f"\nTotal sentences: {len(counted_sentences)}")

if __name__ == "__main__":
    main()