import re

# Input from user
phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")

# Regular expression patterns
phone_pattern = r'^\d{10}$'  # 10 digits only
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Basic email pattern

# Validate phone number
if re.match(phone_pattern, phone):
    print("Phone number is valid.")
else:
    print("Invalid phone number. It should be 10 digits.")

# Validate email ID
if re.match(email_pattern, email):
    print("Email ID is valid.")
else:
    print("Invalid email ID.")
