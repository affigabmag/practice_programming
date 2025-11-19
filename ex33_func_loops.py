#   Exercise 33 (Harder) – Functions with Loops

#   File name: ex33_func_loops.py

#   Create four functions that use loops:

#   1. sum_numbers(n) - takes a number n, returns the sum of all integers from 1 to n (inclusive). Example: sum_numbers(5) should return 1+2+3+4+5 = 15. Test with 5, 10, and 100.
#   2. count_vowels(text) - takes a string, returns the count of vowels (a, e, i, o, u). Test with at least 2 different strings.
#   3. print_multiplication_table(num) - takes a number, prints its multiplication table from 1 to 10. Example: if num=3, print "3 x 1 = 3", "3 x 2 = 6", etc. Test with 5 and 7.
#   4. find_largest(numbers) - takes a list of numbers, returns the largest one WITHOUT using the max() function. Use a loop instead. Test with at least 2 different lists.

def sum_numbers(n):
    sum=0
    for c in range(1,n+1):
        sum+=c
    return sum

def count_vowels(text):
    counter=0
    for c in text:
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            counter+=1
    return counter

def print_multiplication_table(num):
    for x in range(1,num+1):
        for y in range(1,num+1):
            print(f"{x} x {y} = {x*y}")

def find_largest(numbers):
    max=0
    for i in numbers:
        print(i)
        if i>max:
            max=i
    print( max)

print(sum_numbers(5))
print(sum_numbers(10))
print(sum_numbers(100))

print(count_vowels('Gabriel Magen'))

print_multiplication_table(5)
print_multiplication_table(7)

numbers=[12,45,2,45,666,7,55,4,55,4,5,6778,644,3]
find_largest(numbers)