#   Exercise 31 (Easy) – Functions: Basics

#   Create three simple functions:

#   1. greet() - takes no parameters, just prints "Hello, World!"
#   2. add_two_numbers(a, b) - takes two numbers as parameters, returns their sum
#   3. describe_person(name, age) - takes a name and age, prints a formatted string like "Alice is 25 years old"

#   Then call each function at least once to show they work.

def greet():
    print("Hello, World!")

def add_two_numbers(a,b):
    return a+b

def describe_person(name,age):
    print(f"{name} is {age} years old")

greet()
print(add_two_numbers(6+8,13))
describe_person('gabriel',53)