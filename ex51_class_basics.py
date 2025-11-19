# Exercise 51 (Simple) – Classes: Basics

#   Learn what a class is with this simple example:

#   A class is a blueprint for creating objects. Think of it like a cookie cutter - the class defines the shape, and    
#    each object is a cookie.

#   Create a Car class with:
#   - Attributes: brand, color, year
#   - Method describe() that returns a string like "2020 Red Toyota"
#   - Method age() that calculates how many years old the car is (assume current year is 2025)

#   Then:
#   1. Create 3 car objects
#   2. Call describe() on each
#   3. Call age() on each and print how old they are
#   4. Store all cars in a list and loop through it

#   Example:
class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def describe(self):
        return f"{self.year} {self.color} {self.brand}"

    def age(self):
        return 2025 - self.year

# Create cars
car1 = Car("Toyota", "Red", 2020)
print(car1.describe())  # 2020 Red Toyota
print(car1.age())       # 5

car2 = Car("Skoda", "Black", 2017)
print(car2.describe())
print(car2.age())

car3 = Car("MG", "White", 2021)
print(car3.describe())
print(car3.age())