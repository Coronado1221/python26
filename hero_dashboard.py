"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# Global Constants
OFFICE_NAME = "Anthony's Office"
TAX_RATE = 0.05

def process_expenses(item_name, price, quantity):
    """Calculates tax and returns TWO values (total, status)."""
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Determine a string status based on logic
    status = f"Order Processed for {item_name}"

    return total, status # Multiple Return

def main():
    print(f"--- Welcome to {OFFICE_NAME} ---")

    # Identify item
    item = input("Enter item name: ")

    try:
        user_price = float(input("Enter order price:"))
        user_quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Defaulting to 1.00 and 1 unit.")
        user_price = 1.00
        user_quantity = 1

    # UNPACKING the two returned values using KEYWORD ARGUMENTS
    final_cost, status_txt = process_expenses(item_name=item,price=user_price,quantity=user_quantity)

    print(f"\nFinal Receipt: ${final_cost:.2f}")
    print(f"Order Type: {status_txt}")

main()
