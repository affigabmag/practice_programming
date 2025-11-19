# ex41 - Objects and Database!

#   File name: ex41_obj_database_simple.py

#   Exercise 41 (Simple) – Objects and Database: Introduction

#   Create a simple Person class with:
#   - Attributes: name, age, city
#   - A method info() that returns a formatted string like "Gabriel, 53, Beer Sheva"
#   - A method birthday() that increases age by 1

#   Then create 3 person objects and test:
#   1. Create 3 people with different names, ages, cities
#   2. Call info() on each to display their information
#   3. Call birthday() on one person and show the updated info
#   4. Store all 3 people in a list and loop through it, printing each person's info




  # Exercise 41 – Objects and Database: Introduction
  #
  # Create a simple Person class with attributes and methods
  # Then create and manipulate person objects

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        return f"{self.name}, {self.age}, {self.city}"

    def birthday(self):
        self.age += 1

  # Create 3 person objects
person1 = Person("Gabriel", 53, "Beer Sheva")
person2 = Person("Alice", 30, "Tel Aviv")
person3 = Person("Bob", 25, "Haifa")

# Test info() method
print(person1.info())
print(person2.info())
print(person3.info())

# Test birthday() method
print("\nAfter birthday:")
person1.birthday()
print(person1.info())

# Store all in a list and loop through
people = [person1, person2, person3]
print("\nAll people:")
for person in people:
    print(person.info())

#   Key concepts:
#   - class Person: - defines the class
#   - def __init__(self, name, age, city): - constructor (initializes objects)
#   - self.name, self.age, self.city - attributes
#   - def info(self):, def birthday(self): - methods
#   - Objects are created like: Person("name", age, "city")
#   - Call methods with dot notation: person1.info(), person1.birthday()