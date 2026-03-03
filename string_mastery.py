<<<<<<< HEAD
# setup
name_string = "MUSIC"
dog_letters = list(name_string)
count = 0

# Loop:
# String method:
current_name = " ".join(dog_letters)

print("")
=======
""""
----------------------------------------------------------------
Task 1: Basics (Length, Indexing, ASCII).
Task 2: Cleanup (Strip, Casing, Replace).
Task 3: Validation (isdigit check).
Task 4: The Ducky Loop (Using .join() and direct iteration). proced
Checklist Docstring present at the top.
---------------------------------------------------------------
"""

# Task 1
# get user input
user_string = input("Enter a string:  ")
# print lenght of string
print(f"Lenght of string: {len(user_string)}")
# print first and last character
print(f"First character: {user_string[0]}")
print(f"Last character: {user_string[-1]}")
# print ascii value of first character
print(f"ASCII value of first character: {ord(user_string[0])}")
# Task 2
# strip whitespace and print
cleaned_string = user_string.strip()
print(f"Cleaned string: '{cleaned_string}'")
# convert 
upper and print
upper_string = cleaned_string.upper()
print(f"Uppercase string: '{upper_string}")
# replace
replaced_string = upper_string.replace("A", "@")
print(f"Replaced string: '{replaced_string}'")
# Task 3
# validate
if cleaned_string.isdigit():
    print("The string is a number.")
else:
    print("The string is not a number.")
# Task 4
# create
ducky_string = "DUCKY"
# create
ducky_list = [char for char in ducky_string]
# join and print
joined_string = " ".join(ducky_list)
print(f"Ducky Loop Output: {joined_string}")






>>>>>>> 713b41a (m)
