"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
EXTRAS = ("Protein Powder", "Yogurt", "Chia Seeds")

def get_price(size):
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00

def blend(size, base, fruit, extra): 
    print("Blending Smoothie")
    print(f"Size: {size}")
    print(f"Base: Smoothie with {base} base.")
    print(f"Flavor: Smoothie with {fruit} flavor.")
    print(f"Extras: Smoothie with {extra} additions.")

def main():
    print("Welcome to the Smoothie Shop")

    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_base = input("Select base: ")
    choice_fruit = input("Select fruit: ")
    choice_extra = input("Select extra: ")
    
    try:
        packets = int(input("How many scoops of protein? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1.")
        packets = 1

    cost = get_base_price(choice_size)

    blend_smoothie(choice_size, choice_base, choice_fruit, choice extra)

    print(f"Total Bill: ${cost:.2f}")

