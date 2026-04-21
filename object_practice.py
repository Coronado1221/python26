"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class Vehicle:
    def __init__(self, make_model, fuel_level, mileage, color):
        self.__make_model = make_model
        self.__fuel_level = fuel_level
        self.__mileage = mileage
        self.__color = color

    def get_make_model(self):
        return self.__make_model
    
    def get_fuel_level(self):
        return self.__fuel_level
    
    def get_mileage(self):
        return self.__mileage
    
    def get_color(self):
        return self.__color
    
    def get_vehicle_summary(self):
        return (f"Vehicle Summary:\n"
    f"Model: {self.__make_model}\n"
    f"Color: {self.__color}\n"
    f"Mileage: {self.__mileage} miles\n"
    f"Fuel: {self.__fuel_level}%\n")

car1 = Vehicle("Honda Civic", 100, 10000, "White")
car2 = Vehicle("Chevrolet Camaro", 50, 80000, "Red")

print(car1.get_vehicle_summary())
print(car2.get_vehicle_summary())



    
