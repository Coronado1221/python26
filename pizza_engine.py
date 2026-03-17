"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("Sausage","Pepperoni", "Bacon", "Cheese")

def make_pizza(customer, size, topping, is_delivery=False):
    """Processes inbound data and local logic."""
    print(f"\n--- OFFICIAL TICKET: {customer.upper()} ---")
    print(f"Recipe: Pizza with {topping} topping.")

def main():
    user = input("Duck Name: ").title()
    print(f"Options: {TOPPINGS}")
    choice = input("Select Topping: ").title()

    size_choice = input("Enter size (Small, Medium, Large): ").title()

    try:
        TOPPINGS.index(choice)
    except ValueError:
        print(f"Error: {choice} is not an option. Defaulting to cheese.")
        choice = "Cheese"

    make_pizza(customer=user, size=size_choice, topping=choice, is_delivery=True)

main()
