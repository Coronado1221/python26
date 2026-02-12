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
        print(f"Total: ${Total+deposit:,.2f}")
    elif choice == 3:
        withdraw = int(input("Amount to withdraw?"))
        if withdraw > 1000:
            else print ("Insufficient funds")
            print(f"Total: ${Total-withdraw:,.2f}")
             
             


    

    
          





