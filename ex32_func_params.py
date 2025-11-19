#   Exercise 32 (Harder) – Functions: Parameters and Return Values

#   Create four functions:

#   1. calculate_average(num1, num2, num3) - returns the average of three numbers. Call it with 12, 18, 24 and print the result formatted to 2 decimal places.
#   2. is_even(n) - returns True if the number is even, False otherwise. Test it with at least 3 different numbers (mix of even and odd).
#   3. full_name(first, last) - takes first name and last name, returns a formatted string like "John Doe". Call it and print the result.
#   4. grade_student(score) - returns a letter grade based on score:
#     - A if score >= 90
#     - B if score >= 80
#     - C if score >= 70
#     - D if score >= 60
#     - F if score < 60

#   Test it with these scores: 95, 85, 75, 65, 55

def calculate_average(n1,n2,n3):
    return (n1+n2+n3)/3

def is_even(n):
    res=n % 2
    if res==0: return True
    else: return False

def full_name(fn,ln):
    return fn+' '+ln

def grade_student(score):
    if score>=90: return 'A'
    if score>=80: return 'B'
    if score>=70: return 'C'
    if score>=60: return 'D'
    if score<60: return 'F'

avg=calculate_average(12,18,24)
print(f"The average is: {avg:.2f}")

print(is_even(7))
print(is_even(6))
print(is_even(567))

print(full_name('gabriel','magen'))

print(grade_student(95))
print(grade_student(85))
print(grade_student(75))
print(grade_student(65))
print(grade_student(55))
