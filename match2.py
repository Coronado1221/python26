"""
Match case

"""

# Display menu

print("1.  Coffee - $2.00")
print("2.  Tea    - $1.00")
print("3.  Water  - $1.00")
print("4.  Soda   - $1.50")
print("5.  Done")

total = 0  # total amount sold

while True:
    choice = int(input("Please enter the number of your choice:  "))
    if choice == 5:
        print("Order complete")
        print(f"Total: ${total:,.2f}")
        break
    elif choice == 4:
        total += 1.5  # total = total + 1.5
        print("Soda added")
        print(f"Total: ${total:,.2f}")
    elif choice == 3:
        total += 1
        print("Water added")
        print(f"Total: ${total:,.2f}")
    elif choice == 2:
        total += 1
        print("Tea added")
        print(f"Total: ${total:,.2f}")
    elif choice == 1:
        total += 1
        print("Coffee added")
        print(f"Total: ${total:,.2f}")
    else:
        print("I'm sorry that is not a valid menu number")

print(f"That will be: {total:,.2f}")