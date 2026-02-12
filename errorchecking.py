"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""
# rent a car
first_name = ""
while len(first_name) == 0:
    first_name = input("What is your legal first name? ")

last_name = ""
while len(last_name) == 0:
    last_name = input("What is your legal last name? ")

age = 0
while age < 16:
    age = int(input("What is your age? "))
    if age < 0 or age > 70:
        print("I'm sorry, that is not a valid age")
    elif age > 24:
        pass
    else:
        print("I'm sorry, we cannot rent to you")

valid = input("Do you have a valid drivers license (Y/N)").upper()
if valid == "Y":
    pass
else:
    print("I'm sorry, we cannot rent to you")
