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
# Name
first_name = input("Enter First Name:  ")
while first_name == "":
    print("   Error: Name cannot be blank.")
    first_name = input("Please enter First Name:  ")
last_name = input("Enter Last Name:  ")
while last_name == "":
    print("   Error: Name cannot be blank.")
    last_name = input("Please enter Last Name:  ")

# Chaperone
chaperone = input("Parent volunteering to chaperone? (Y/N)").upper()
while chaperone != "Y" and chaperone != "N":
    print("   Error: Please enter only Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()

# Phone Number
phone_number = input("Enter Phone Number: ########## ")
while phone_number == "":
    print("   Error: Number cannot be blank.")
    phone_number = input("Please enter Phone Number:  ")


# Ticket Count
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets?  "))
        if tickets > 0:
            break
        print("   Error: Must be at least 1 ticket.")
    except ValueError:
        print("   Error: Please enter a Number (ex. 1,2 not 'one').")

print(f"   Ordered {tickets} tickets.")
print("Registration Complete, Thank you.")