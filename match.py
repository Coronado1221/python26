"""
Match case

"""

# Display Menu
print("1. Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Transfer")
print("5. Exit")

Total = 1000

while True:
    choice = int(input("Please enter the number of your choice:  "))
    if choice == 5:
        print("Order complete")
        print(f"Total: ${Total:,.2f}")
        break
    elif choice == 1:
        print(f"Total: ${Total:,.2f}")
    elif choice == 2:
        deposit = int(input("Amount to deposit?  "))
        Total += deposit 
        print(f"Total: ${Total:,.2f}")
    elif choice == 3:
        withdrawal_amount = float(input("How much to withdraw?  "))
        if withdrawal_amount <= Total:
            Total -= withdrawal_amount
            print(f"Total: ${Total:,.2f}")
        else: print("insufficient funds")
    elif choice == 4:
        transfer_amount = float(input("How much to transfer?  "))
        if transfer_amount <= Total:
            Total -= transfer_amount
            print(f"Total: ${Total:,.2f}")
        else: print("insufficient funds")
    else:
        print("I'm sorry that is not a valid menu number")