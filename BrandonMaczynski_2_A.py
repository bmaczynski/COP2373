# List of spam keywords and phrases
spam_keywords = [
    "buy now", "click here", "congratulations", "unsubscribe", "winner", 
    "free", "offer", "limited time", "risk-free", "urgent", 
    "guaranteed", "act now", "special promotion", "money-back", "cash bonus", 
    "prize", "save big", "exclusive deal", "earn money", "lowest price", 
    "miracle", "no cost", "best price", "instant", "deal", 
    "promotion", "no obligation", "trial", "order now", "promise"
]

# Create function to check spam
def check_spam(email_message):
    # Init variables for spam count
    spam_count = 0
    # Init a variable for user's matched words we find in the email
    matched_keywords = []

   # Loop through 
    for keyword in spam_keywords:
        # Conditional to check if the keyword is in the email message
        # .lower() will ensure we scan the email properly and don't miss any characters due to case sensitivity
        if keyword in email_message.lower():
            # Add 1 to spam_count if a keyword is found
            spam_count += 1
            # Append the keyword to the matched_keywords list
            matched_keywords.append(keyword)

   # Conditional to determine likelihood of spam based on spam_count
    if spam_count <= 3:
        likelihood = "Unlikely to be spam"
    elif spam_count <= 7:
        likelihood = "Possibly spam"
    else:
        likelihood = "Most likely spam"

   # Return the spam count, likelihood, and matched keywords
    return spam_count, likelihood, matched_keywords

# Get user input for email message
email_message = input("Enter your email message: ")
# Call the check_spam function and unpack the returned values
spam_count, likelihood, matched_keywords = check_spam(email_message)

# Display the spam count, likelihood, and matched keywords
print(f"Spam Count: {spam_count}")
print(f"Likelihood of being spam: {likelihood}")
if spam_count > 0:   
   print("Matched Keywords/Phrases:", ", ".join(matched_keywords))
else:
    print("There are no matched keywords/phrases in the email message.")