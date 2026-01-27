"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f).
-----------------------------------------------------------------------
"""

# Get Input
monthly_income = float(input("How much is your monthly income?  "))
car_payment = float(input("Spent on car payment?  "))
retirement = float(input("Amount towards retirement?  "))
groceries = float(input("Spent on groceries?  "))
gym_membership = float(input("Spent on gym membership?  "))
subscriptions = float(input("Spent on subscriptions?  "))

# Calculations
spent = car_payment + retirement + groceries + gym_membership + subscriptions
remaining = monthly_income - car_payment + retirement + groceries + gym_membership + subscriptions
percent = (car_payment + retirement + groceries + gym_membership + subscriptiosn)/monthly_income

# Formatted Output
print(f"You receive {monthly_income: ,.2f}")
print(f"You spend {spent: ,.2f} a month")
print(f"You have ")
print(f"")