"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later", "Probably", "Probably not", "Very doubtful", "Without a doubt", "I don't know")

print("Welcome to the Magic 8 Ball!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop
while True:
    user_input = input("Ask your question: ")
    if "quit" in user_input.strip().lower():
        print("Bye!")
        break
    else:
        answer = random.choice(RESPONSES)
        print(F"Magic 8 Ball says: {answer}")
    



