"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
# List 
seats = list(range(1, 21))
# Loop
while True:
    print("Available seats:  ", seats)
    seat_choice = int(input("Pick an available seat:  "))
    if seat_choice == 0:
        break
    elif seat_choice in seats:
        seats.remove(seat_choice)
        print("Seat is now taken.")
    else:
        print("Seat already taken or invalid.")
