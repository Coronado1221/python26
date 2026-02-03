"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [2/2]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""
# Variables
age = int(input("How old are you? "))

# Printed Variables 
if age < 1:
    print("You eat free.")
elif age < 12:
    print(f"Your total is ${1*age:.2f}")
elif age < 65:
    print("Your total is $16.95")
elif age > 65:
    print("Your total is $12.95")