"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

# Define constant tuple for months
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") # defining a constant tuple locks the data in

# Loop
for month in MONTHS: # looping through months to display each month
    print(month)

# try and except block
try:
    MONTHS[0] = "Jan" # attempting a change to test the tuple 
except TypeError: # blocks to catch the resulting TypeError
    print("Tuples are locked and immutable. ")
    print("Tuples cannot be changed after they are created.")



    
