# import re module to use regular expressions
import re

# Validate phone number function
def validate_phone_number(phone_number):
   #  Validate phone number
   #  Valid format: (123) 456-7890 or 123-456-7890

    pattern = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    return bool(pattern.match(phone_number))

def validate_ssn(ssn):
   #  Validate social security number.
   #  Valid format: 123-45-6789

    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# Validate zip code function
def validate_zip_code(zip_code):
   #  Validate zip code
   #  Valid format: 12345 or 12345-6789

    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

def main():
   #  Main function to get input from user and validate phone number, SSN, and zip code

   # Get input from user
    phone_number = input("Enter phone number (123) 456-7890 | 123-456-7890: ")
    ssn = input("Enter social security number (123-45-6789): ")
    zip_code = input("Enter zip code (12345 | 12345-6789): ")
    
   # Validate phone number, SSN, and zip code via conditional
    if validate_phone_number(phone_number):
        print("Phone number: valid.")
    else:
        print("Phone number: invalid.")
    
    if validate_ssn(ssn):
        print("Social security number: valid.")
    else:
        print("Social security number: invalid.")
    
    # Validate zip code
    if validate_zip_code(zip_code):
        print("Zip code: valid.")
    else:
        print("Zip code: invalid.")

if __name__ == "__main__":
    main()